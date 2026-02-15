#!/usr/bin/env python3
"""
Jira Story Creator - Create detailed stories from implementation plans
Generates stories with User Story, Acceptance Criteria, Implementation, and Testing sections
"""

import argparse
import json
import sys
import subprocess
import re
from typing import List, Dict, Optional
from pathlib import Path


class StoryTemplate:
    """Templates for different types of stories"""

    @staticmethod
    def infrastructure(task_name: str, details: str) -> Dict[str, str]:
        """Template for infrastructure/setup stories"""
        return {
            "user_story": f"As a DevOps engineer, I want to {task_name.lower()} so that the application has the necessary infrastructure.",
            "acceptance_criteria": f"- {task_name} completed successfully\n- Configuration documented\n- Service is running and accessible\n- Health checks passing",
            "implementation": f"1. Review requirements for {task_name}\n2. {details}\n3. Verify installation\n4. Document configuration\n5. Add monitoring/health checks",
            "testing": f"1. Verify service is running\n2. Test connectivity\n3. Check configuration correctness\n4. Run health check commands\n5. Document verification steps"
        }

    @staticmethod
    def backend_api(task_name: str, endpoint: str, details: str) -> Dict[str, str]:
        """Template for backend API stories"""
        return {
            "user_story": f"As a backend developer, I want to {task_name.lower()} so that the frontend can {details}.",
            "acceptance_criteria": f"- {endpoint} endpoint created\n- Request/response validated\n- Error handling implemented\n- API documentation updated\n- Tests passing",
            "implementation": f"1. Create route: {endpoint}\n2. Implement controller logic\n3. Add input validation\n4. Add error handling\n5. Update API documentation\n6. Write unit tests",
            "testing": f"1. Test with valid payload (expect 200/201)\n2. Test with invalid data (expect 400)\n3. Test error cases (expect appropriate error codes)\n4. Verify database changes\n5. Run integration tests\n6. Test with Postman/curl"
        }

    @staticmethod
    def frontend_ui(task_name: str, component_name: str, details: str) -> Dict[str, str]:
        """Template for frontend UI stories"""
        return {
            "user_story": f"As a user, I want {task_name.lower()} so that I can {details}.",
            "acceptance_criteria": f"- {component_name} component created\n- Responsive design (mobile + desktop)\n- Accessibility compliant\n- User feedback on interactions\n- Loading states shown",
            "implementation": f"1. Create {component_name} component\n2. Implement UI design\n3. Add form validation (if applicable)\n4. Add loading/error states\n5. Style with CSS/Tailwind\n6. Add accessibility attributes\n7. Write component tests",
            "testing": f"1. Render component (should display correctly)\n2. Test user interactions\n3. Test validation (if forms)\n4. Test responsive design on mobile\n5. Test accessibility (keyboard navigation, screen reader)\n6. Verify API integration"
        }

    @staticmethod
    def generic(task_name: str, role: str, benefit: str) -> Dict[str, str]:
        """Generic template for any story"""
        return {
            "user_story": f"As a {role}, I want to {task_name.lower()} so that {benefit}.",
            "acceptance_criteria": f"- {task_name} implemented\n- Tests passing\n- Documentation updated",
            "implementation": f"1. Analyze requirements for {task_name}\n2. Design solution approach\n3. Implement functionality\n4. Add error handling\n5. Write tests\n6. Document implementation",
            "testing": f"1. Test happy path\n2. Test edge cases\n3. Test error scenarios\n4. Verify integration with other components\n5. Run full test suite"
        }


class StoryGenerator:
    """Generate story content from task descriptions"""

    def __init__(self):
        self.template = StoryTemplate()

    def detect_story_type(self, task_name: str) -> str:
        """Detect what type of story this is"""
        task_lower = task_name.lower()

        if any(word in task_lower for word in ['install', 'setup', 'configure', 'infrastructure', 'aws', 'nginx', 'postgresql', 'redis']):
            return 'infrastructure'
        elif any(word in task_lower for word in ['endpoint', 'api', 'backend', 'service', 'controller']):
            return 'backend_api'
        elif any(word in task_lower for word in ['ui', 'component', 'page', 'interface', 'display', 'form', 'button']):
            return 'frontend_ui'
        else:
            return 'generic'

    def generate_story(self, task_name: str, epic_context: str) -> Dict[str, str]:
        """Generate a complete story with all sections"""
        story_type = self.detect_story_type(task_name)

        if story_type == 'infrastructure':
            return self.template.infrastructure(task_name, epic_context)
        elif story_type == 'backend_api':
            # Extract endpoint if present
            endpoint_match = re.search(r'(/[a-z/]+)', task_name.lower())
            endpoint = endpoint_match.group(1) if endpoint_match else '/api/endpoint'
            return self.template.backend_api(task_name, endpoint, epic_context)
        elif story_type == 'frontend_ui':
            # Extract component name
            component_match = re.search(r'(Create|Build|Implement)\s+(.+?)(?:\s+UI|\s+Component|$)', task_name)
            component_name = component_match.group(2) if component_match else task_name
            return self.template.frontend_ui(task_name, component_name, epic_context)
        else:
            return self.template.generic(task_name, 'developer', 'the system functions correctly')


class JiraStoryCreator:
    """Create stories in Jira with full formatting"""

    def __init__(self, config: Dict):
        self.base_url = config["jira"]["instanceUrl"]
        self.auth = f"{config['jira']['email']}:{config['jira']['apiToken']}"
        self.project_key = config["jira"]["projectKey"]
        self.story_type_id = config["jira"].get("storyTypeId", "10006")

    def create_adf_description(self, user_story: str, acceptance_criteria: str,
                               implementation: str, testing: str) -> Dict:
        """Create Atlassian Document Format (ADF) for description"""
        return {
            "type": "doc",
            "version": 1,
            "content": [
                {
                    "type": "heading",
                    "attrs": {"level": 3},
                    "content": [{"type": "text", "text": "User Story"}]
                },
                {
                    "type": "paragraph",
                    "content": [{"type": "text", "text": user_story}]
                },
                {
                    "type": "heading",
                    "attrs": {"level": 3},
                    "content": [{"type": "text", "text": "Acceptance Criteria"}]
                },
                {
                    "type": "paragraph",
                    "content": [{"type": "text", "text": acceptance_criteria}]
                },
                {
                    "type": "heading",
                    "attrs": {"level": 3},
                    "content": [{"type": "text", "text": "Implementation Method"}]
                },
                {
                    "type": "paragraph",
                    "content": [{"type": "text", "text": implementation}]
                },
                {
                    "type": "heading",
                    "attrs": {"level": 3},
                    "content": [{"type": "text", "text": "Testing Method"}]
                },
                {
                    "type": "paragraph",
                    "content": [{"type": "text", "text": testing}]
                }
            ]
        }

    def create_story(self, epic_key: str, summary: str, user_story: str,
                     acceptance_criteria: str, implementation: str, testing: str,
                     labels: List[str] = None) -> str:
        """Create a story in Jira"""

        description = self.create_adf_description(user_story, acceptance_criteria,
                                                    implementation, testing)

        fields = {
            "project": {"key": self.project_key},
            "summary": summary,
            "description": description,
            "issuetype": {"id": self.story_type_id},
            "parent": {"key": epic_key}
        }

        if labels:
            fields["labels"] = labels

        data = json.dumps({"fields": fields})

        result = subprocess.run(
            ["curl", "-s", "-u", self.auth, "-X", "POST",
             "-H", "Content-Type: application/json",
             "-d", data,
             f"{self.base_url}/rest/api/3/issue"],
            capture_output=True,
            text=True
        )

        try:
            response = json.loads(result.stdout)
            return response.get("key", "")
        except json.JSONDecodeError:
            print(f"Error creating story: {result.stdout}")
            return ""


class ImplementationPlanParser:
    """Parse implementation plan markdown files"""

    def __init__(self, plan_path: str):
        self.plan_path = plan_path

    def parse_stages(self) -> List[Dict]:
        """Parse stages from markdown file"""
        with open(self.plan_path, 'r', encoding='utf-8') as f:
            content = f.read()

        stages = []
        # Find all stage sections
        stage_pattern = r'### Stage (\d+): (.+?) \(Week .+?\).*?\*\*Tasks:\*\*(.*?)(?=###|\Z)'
        matches = re.finditer(stage_pattern, content, re.DOTALL)

        for match in matches:
            stage_num = int(match.group(1))
            stage_name = match.group(2)
            tasks_section = match.group(3)

            # Extract tasks
            tasks = []
            task_lines = re.findall(r'- \[ \] (.+)', tasks_section)
            for task in task_lines:
                # Skip sub-items (lines that start with more spaces)
                if not task.startswith('  '):
                    tasks.append(task.strip())

            stages.append({
                "number": stage_num,
                "name": stage_name,
                "tasks": tasks
            })

        return stages


def main():
    parser = argparse.ArgumentParser(
        description="Create detailed Jira Stories from implementation plans"
    )
    parser.add_argument("--plan", required=True, help="Path to implementation plan (markdown)")
    parser.add_argument("--config", required=True, help="Path to Jira config JSON")
    parser.add_argument("--stages", help="Comma-separated stage numbers (e.g., 1,2,3)")
    parser.add_argument("--epic-prefix", default="AURA", help="Epic key prefix")
    parser.add_argument("--dry-run", action="store_true", help="Preview without creating")

    args = parser.parse_args()

    # Load config
    with open(args.config) as f:
        config = json.load(f)

    # Parse implementation plan
    print(f"Parsing implementation plan: {args.plan}")
    plan_parser = ImplementationPlanParser(args.plan)
    stages = plan_parser.parse_stages()

    # Filter stages if specified
    if args.stages:
        stage_nums = [int(s) for s in args.stages.split(',')]
        stages = [s for s in stages if s["number"] in stage_nums]

    print(f"Found {len(stages)} stages to process")
    print()

    if args.dry_run:
        print("=== DRY RUN MODE ===")
        print()

    # Initialize creators
    story_gen = StoryGenerator()
    jira_creator = JiraStoryCreator(config)

    total_stories = 0

    for stage in stages:
        epic_key = f"{args.epic_prefix}-{stage['number']}"
        stage_label = f"stage-{stage['number']:03d}"

        print(f"Stage {stage['number']}: {stage['name']} ({epic_key})")
        print(f"  Tasks: {len(stage['tasks'])}")

        for task in stage['tasks']:
            # Generate story content
            story_content = story_gen.generate_story(task, stage['name'])

            # Determine labels based on task
            labels = [stage_label]
            task_lower = task.lower()
            if 'backend' in task_lower or 'api' in task_lower:
                labels.append('backend')
            if 'frontend' in task_lower or 'ui' in task_lower:
                labels.append('frontend')
            if 'test' in task_lower:
                labels.append('testing')
            if 'database' in task_lower or 'table' in task_lower:
                labels.append('database')

            if args.dry_run:
                print(f"  [DRY RUN] Would create: {task}")
            else:
                # Create story in Jira
                story_key = jira_creator.create_story(
                    epic_key=epic_key,
                    summary=task,
                    user_story=story_content["user_story"],
                    acceptance_criteria=story_content["acceptance_criteria"],
                    implementation=story_content["implementation"],
                    testing=story_content["testing"],
                    labels=labels
                )

                if story_key:
                    print(f"  ✓ {story_key}: {task}")
                    total_stories += 1
                else:
                    print(f"  ✗ Failed: {task}")

        print()

    print(f"=== Complete ===")
    if not args.dry_run:
        print(f"Created {total_stories} stories")
    print()


if __name__ == "__main__":
    main()
