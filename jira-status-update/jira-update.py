#!/usr/bin/env python3
"""
Jira Status Update Skill Implementation
Updates Jira stories and test cases to reflect development progress

Configure via environment variables:
  JIRA_BASE_URL - Your Jira instance URL (e.g., https://your-company.atlassian.net)
  JIRA_EMAIL - Your Jira email address
  JIRA_API_TOKEN - Your Jira API token (generate at https://id.atlassian.com/manage-profile/security/api-tokens)
"""
import json
import sys
import os
import requests
from requests.auth import HTTPBasicAuth

# Try to load .env file if python-dotenv is available
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # python-dotenv not installed, rely on environment variables

# Load configuration from environment variables
JIRA_BASE_URL = os.environ.get('JIRA_BASE_URL')
JIRA_EMAIL = os.environ.get('JIRA_EMAIL')
JIRA_TOKEN = os.environ.get('JIRA_API_TOKEN')

# Validate configuration
if not all([JIRA_BASE_URL, JIRA_EMAIL, JIRA_TOKEN]):
    print("[ERROR] Missing required environment variables")
    print("Please set the following environment variables:")
    print("  JIRA_BASE_URL - Your Jira instance URL")
    print("  JIRA_EMAIL - Your Jira email address")
    print("  JIRA_API_TOKEN - Your Jira API token")
    print("\nExample:")
    print("  export JIRA_BASE_URL='https://your-company.atlassian.net'")
    print("  export JIRA_EMAIL='your.email@company.com'")
    print("  export JIRA_API_TOKEN='your-api-token'")
    sys.exit(1)

# Status name to transition ID mapping
STATUS_TRANSITIONS = {
    "Done": 21,
    "In Progress": 11,
    "Not Needed": 2,
    "Cancelled": 2
}

def get_issue_details(issue_key):
    """Get issue details from Jira"""
    url = f"{JIRA_BASE_URL}/rest/api/3/issue/{issue_key}"
    auth = HTTPBasicAuth(JIRA_EMAIL, JIRA_TOKEN)

    response = requests.get(url, auth=auth, headers={"Content-Type": "application/json"})

    if response.status_code == 200:
        data = response.json()
        return {
            'key': data['key'],
            'summary': data['fields']['summary'],
            'status': data['fields']['status']['name'],
            'type': data['fields']['issuetype']['name']
        }
    else:
        return None

def get_issue_subtasks(issue_key):
    """Get all subtasks for an issue"""
    url = f"{JIRA_BASE_URL}/rest/api/3/issue/{issue_key}"
    auth = HTTPBasicAuth(JIRA_EMAIL, JIRA_TOKEN)

    # Request with fields parameter to get subtasks
    params = {"fields": "subtasks"}
    response = requests.get(url, auth=auth, headers={"Content-Type": "application/json"}, params=params)

    if response.status_code == 200:
        data = response.json()
        subtasks = []
        if 'subtasks' in data['fields'] and data['fields']['subtasks']:
            for subtask in data['fields']['subtasks']:
                subtasks.append({
                    'key': subtask['key'],
                    'summary': subtask['fields']['summary'],
                    'status': subtask['fields']['status']['name']
                })
        return subtasks
    else:
        return []

def get_linked_test_cases(issue_key):
    """Get all linked test cases (issues with 'tests' or 'is tested by' link)"""
    url = f"{JIRA_BASE_URL}/rest/api/3/issue/{issue_key}"
    auth = HTTPBasicAuth(JIRA_EMAIL, JIRA_TOKEN)

    # Request with fields parameter to get issue links
    params = {"fields": "issuelinks"}
    response = requests.get(url, auth=auth, headers={"Content-Type": "application/json"}, params=params)

    test_cases = []
    if response.status_code == 200:
        data = response.json()
        if 'issuelinks' in data['fields']:
            for link in data['fields']['issuelinks']:
                # Check both inward and outward links
                linked_issue = None
                if 'outwardIssue' in link:
                    linked_issue = link['outwardIssue']
                elif 'inwardIssue' in link:
                    linked_issue = link['inwardIssue']

                if linked_issue:
                    # Check if it's a test case (you can adjust this logic)
                    issue_type = linked_issue['fields']['issuetype']['name']
                    if 'Test' in issue_type or linked_issue['key'].startswith('TC-'):
                        test_cases.append({
                            'key': linked_issue['key'],
                            'summary': linked_issue['fields']['summary'],
                            'status': linked_issue['fields']['status']['name']
                        })

    return test_cases

def get_transitions(issue_key):
    """Get available transitions for an issue"""
    url = f"{JIRA_BASE_URL}/rest/api/3/issue/{issue_key}/transitions"
    auth = HTTPBasicAuth(JIRA_EMAIL, JIRA_TOKEN)

    response = requests.get(url, auth=auth, headers={"Content-Type": "application/json"})

    if response.status_code == 200:
        data = response.json()
        return {t['name']: t['id'] for t in data['transitions']}
    else:
        return {}

def transition_issue(issue_key, status_name):
    """Transition an issue to a new status"""
    # Get available transitions
    transitions = get_transitions(issue_key)

    # Map common status names to actual transition names
    status_mapping = {
        "In Progress": "Start Progress",
        "in progress": "Start Progress",
        "progress": "Start Progress",
    }

    # Try to find the transition
    transition_name = status_mapping.get(status_name, status_name)

    if transition_name not in transitions:
        print(f"[ERROR] Status '{status_name}' not available for {issue_key}")
        print(f"Available: {', '.join(transitions.keys())}")
        return False

    transition_id = transitions[transition_name]

    url = f"{JIRA_BASE_URL}/rest/api/3/issue/{issue_key}/transitions"
    auth = HTTPBasicAuth(JIRA_EMAIL, JIRA_TOKEN)

    payload = {
        "transition": {
            "id": str(transition_id)
        }
    }

    response = requests.post(
        url,
        auth=auth,
        headers={"Content-Type": "application/json"},
        data=json.dumps(payload)
    )

    if response.status_code == 204:
        return True
    else:
        print(f"[ERROR] Error transitioning {issue_key}: {response.status_code}")
        print(response.text)
        return False

def update_story(story_key, target_status):
    """Update a story and all associated test cases"""
    print(f"\n[UPDATING] {story_key} to {target_status}")
    print("=" * 50)

    # Get story details
    details = get_issue_details(story_key)
    if not details:
        print(f"[ERROR] Story {story_key} not found")
        return False

    print(f"\n[STORY DETAILS]")
    print(f"  Key: {details['key']}")
    print(f"  Summary: {details['summary']}")
    print(f"  Current Status: {details['status']}")
    print(f"  Type: {details['type']}")

    # Get all test cases (subtasks and linked issues)
    print(f"\n[FINDING TEST CASES]")
    subtasks = get_issue_subtasks(story_key)
    linked_tests = get_linked_test_cases(story_key)

    # Combine all test cases
    all_test_cases = subtasks + linked_tests

    if all_test_cases:
        print(f"  Found {len(all_test_cases)} test case(s):")
        for tc in all_test_cases:
            print(f"    - {tc['key']}: {tc['summary']} (Status: {tc['status']})")
    else:
        print(f"  No test cases found")

    # Update the story
    story_updated = False
    if details['status'] != target_status:
        print(f"\n[TRANSITION STORY] {story_key}...")
        success = transition_issue(story_key, target_status)

        if success:
            print(f"[SUCCESS] {story_key} -> {target_status}")

            # Verify the update
            new_details = get_issue_details(story_key)
            if new_details and new_details['status'] == target_status:
                print(f"[VERIFIED] Story status is now '{target_status}'")
                story_updated = True
        else:
            print(f"[FAILED] Could not update story")
            return False
    else:
        print(f"\n[OK] Story already in '{target_status}' status")
        story_updated = True

    # Update all test cases
    test_case_results = {'success': [], 'failed': [], 'skipped': []}

    if all_test_cases:
        print(f"\n[UPDATING TEST CASES]")
        for tc in all_test_cases:
            tc_key = tc['key']
            tc_status = tc['status']

            # Skip if already in target status
            if tc_status == target_status:
                print(f"  [SKIP] {tc_key} already in '{target_status}'")
                test_case_results['skipped'].append(tc_key)
                continue

            # Try to transition
            print(f"  [TRANSITION] {tc_key}...", end=" ")
            success = transition_issue(tc_key, target_status)

            if success:
                print(f"[OK]")
                test_case_results['success'].append(tc_key)
            else:
                print(f"[FAILED]")
                test_case_results['failed'].append(tc_key)

    # Print summary
    print(f"\n[SUMMARY]")
    print(f"  Story: {'Updated' if story_updated else 'Failed'}")
    if all_test_cases:
        total = len(all_test_cases)
        success_count = len(test_case_results['success'])
        failed_count = len(test_case_results['failed'])
        skipped_count = len(test_case_results['skipped'])

        print(f"  Test Cases: {total} total")
        if success_count > 0:
            print(f"    - {success_count} updated: {', '.join(test_case_results['success'])}")
        if skipped_count > 0:
            print(f"    - {skipped_count} skipped (already in status)")
        if failed_count > 0:
            print(f"    - {failed_count} failed: {', '.join(test_case_results['failed'])}")

    return story_updated and len(test_case_results['failed']) == 0

def main():
    """Main entry point"""
    if len(sys.argv) < 3:
        print("Usage: python jira-update.py <STORY-ID> <STATUS>")
        print("Example: python jira-update.py AURA-21 Done")
        print("\nSupported statuses:")
        print("  - Done")
        print("  - In Progress")
        print("  - Not Needed")
        sys.exit(1)

    story_key = sys.argv[1]
    target_status = sys.argv[2]

    # Allow status shortcuts
    status_shortcuts = {
        "done": "Done",
        "complete": "Done",
        "completed": "Done",
        "progress": "In Progress",
        "started": "In Progress",
        "start": "In Progress",
        "working": "In Progress",
        "cancel": "Not Needed",
        "cancelled": "Not Needed",
        "skip": "Not Needed"
    }

    target_status = status_shortcuts.get(target_status.lower(), target_status)

    # Update the story
    success = update_story(story_key, target_status)

    if success:
        print("\n" + "=" * 50)
        print("[COMPLETE] Update Complete!")
        print("=" * 50)
        print(f"\nView in Jira: {JIRA_BASE_URL}/browse/{story_key}")
        sys.exit(0)
    else:
        print("\n[FAILED] Update Failed")
        sys.exit(1)

if __name__ == "__main__":
    main()
