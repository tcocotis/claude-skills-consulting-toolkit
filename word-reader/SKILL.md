---
name: word-reader
description: Read and extract content from Microsoft Word (.docx) files. Use whenever the user wants to view, analyze, extract text or images from, summarize, or work with content in Word documents. Triggers include reading .docx files, extracting data from Word documents, analyzing document structure, or any task that requires accessing Word file content as input.
version: 1.0.0
tags: [word, docx, document-reading, extraction, parsing]
---

# Word Document Reader (Windows)

## Auto-Invocation Triggers

This skill should be automatically invoked when the user:
- Wants to **read a .docx file** or **open a Word document**
- Says "**extract from Word**" or "**read Word document**"
- Mentions "**parse .docx**", "**get content from Word**", or "**read specification**" (if it's a .docx)
- References a **.docx file path** and needs its content
- Wants to **analyze document**, **summarize Word doc**, or **extract text/tables/images**
- Says "**view Word file**", "**open specification**", or "**read project spec**" (if .docx)

**Keywords:** read .docx, Word document, extract from Word, parse docx, Word file, document content, specification document, read spec, Word tables, Word images

## Overview

This skill enables reading and extracting content from Microsoft Word (.docx) files on Windows using Python's python-docx library.

## When to Use This Skill

Use this skill when:
- User asks to read, view, or open a .docx file
- User wants to extract text, tables, or images from a Word document
- User needs to analyze or summarize document content
- User wants to convert Word content to another format
- User references a Word file and needs its content for any purpose

## Prerequisites

Ensure python-docx is installed:
```bash
pip install python-docx
```

## Reading Word Documents

### Basic Text Extraction

Use this Python script to extract all text from a Word document:

```python
from docx import Document

def read_docx(file_path):
    """Extract all text from a .docx file"""
    doc = Document(file_path)
    
    # Extract all paragraphs
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    
    return '\n'.join(full_text)

# Usage
text = read_docx('document.docx')
print(text)
```

### Reading with Structure (Headings, Lists, etc.)

```python
from docx import Document

def read_docx_structured(file_path):
    """Extract text while preserving structure"""
    doc = Document(file_path)
    
    content = []
    for para in doc.paragraphs:
        # Check if it's a heading
        if para.style.name.startswith('Heading'):
            level = para.style.name.replace('Heading ', '')
            content.append(f"\n{'#' * int(level)} {para.text}\n")
        else:
            content.append(para.text)
    
    return '\n'.join(content)

text = read_docx_structured('document.docx')
print(text)
```

### Extracting Tables

```python
from docx import Document

def extract_tables(file_path):
    """Extract all tables from a .docx file"""
    doc = Document(file_path)
    
    tables_data = []
    for table in doc.tables:
        table_data = []
        for row in table.rows:
            row_data = [cell.text for cell in row.cells]
            table_data.append(row_data)
        tables_data.append(table_data)
    
    return tables_data

# Usage
tables = extract_tables('document.docx')
for i, table in enumerate(tables):
    print(f"\n=== Table {i+1} ===")
    for row in table:
        print(row)
```

### Extracting Images

```python
from docx import Document
import os

def extract_images(file_path, output_dir='extracted_images'):
    """Extract all images from a .docx file"""
    doc = Document(file_path)
    
    # Create output directory
    os.makedirs(output_dir, exist_ok=True)
    
    image_count = 0
    for rel in doc.part.rels.values():
        if "image" in rel.target_ref:
            image_count += 1
            image_data = rel.target_part.blob
            
            # Determine file extension
            ext = rel.target_ref.split('.')[-1]
            image_filename = f"{output_dir}/image_{image_count}.{ext}"
            
            with open(image_filename, 'wb') as f:
                f.write(image_data)
            
            print(f"Extracted: {image_filename}")
    
    return image_count

# Usage
count = extract_images('document.docx')
print(f"Extracted {count} images")
```

### Reading Document Metadata

```python
from docx import Document

def get_metadata(file_path):
    """Extract document metadata"""
    doc = Document(file_path)
    core_props = doc.core_properties
    
    metadata = {
        'author': core_props.author,
        'title': core_props.title,
        'subject': core_props.subject,
        'created': core_props.created,
        'modified': core_props.modified,
        'last_modified_by': core_props.last_modified_by,
        'keywords': core_props.keywords,
    }
    
    return metadata

# Usage
meta = get_metadata('document.docx')
for key, value in meta.items():
    print(f"{key}: {value}")
```

## Complete Reading Script

Here's a comprehensive script that extracts everything:

```python
from docx import Document
import os

def read_full_document(file_path):
    """Comprehensive document reader"""
    doc = Document(file_path)
    
    print(f"=== Document: {file_path} ===\n")
    
    # Metadata
    print("=== METADATA ===")
    print(f"Author: {doc.core_properties.author}")
    print(f"Created: {doc.core_properties.created}")
    print(f"Modified: {doc.core_properties.modified}")
    print()
    
    # Text content
    print("=== CONTENT ===")
    for para in doc.paragraphs:
        if para.text.strip():  # Skip empty paragraphs
            if para.style.name.startswith('Heading'):
                print(f"\n{para.text}")
                print("-" * len(para.text))
            else:
                print(para.text)
    
    # Tables
    if doc.tables:
        print("\n\n=== TABLES ===")
        for i, table in enumerate(doc.tables):
            print(f"\nTable {i+1}:")
            for row in table.rows:
                print(" | ".join(cell.text for cell in row.cells))
    
    # Images
    image_count = sum(1 for rel in doc.part.rels.values() 
                     if "image" in rel.target_ref)
    if image_count:
        print(f"\n\n=== IMAGES ===")
        print(f"Document contains {image_count} images")

# Usage
read_full_document('document.docx')
```

## Common Use Cases

### Quick Summary Script

Save this as `read_word.py` for quick document reading:

```python
import sys
from docx import Document

if len(sys.argv) < 2:
    print("Usage: python read_word.py <document.docx>")
    sys.exit(1)

doc = Document(sys.argv[1])

# Print all text
for para in doc.paragraphs:
    print(para.text)
```

Then use it:
```bash
python read_word.py document.docx
```

### Search for Text

```python
from docx import Document

def search_in_docx(file_path, search_term):
    """Search for text in a Word document"""
    doc = Document(file_path)
    results = []
    
    for i, para in enumerate(doc.paragraphs):
        if search_term.lower() in para.text.lower():
            results.append(f"Paragraph {i}: {para.text}")
    
    return results

# Usage
results = search_in_docx('document.docx', 'budget')
for result in results:
    print(result)
```

## Tips for Windows

1. **File Paths**: Use raw strings or forward slashes for paths:
   ```python
   r"C:\Users\Documents\file.docx"  # Raw string
   "C:/Users/Documents/file.docx"    # Forward slashes work too
   ```

2. **Check if file exists**:
   ```python
   import os
   if os.path.exists('document.docx'):
       # Read the file
   ```

3. **Handle encoding issues**:
   ```python
   # When writing extracted text to a file
   with open('output.txt', 'w', encoding='utf-8') as f:
       f.write(text)
   ```

## Alternative: Pandoc on Windows

If you have pandoc installed on Windows (via chocolatey or from pandoc.org):

```bash
# Install pandoc
choco install pandoc

# Extract text
pandoc document.docx -t plain -o output.txt

# Extract to markdown
pandoc document.docx -t markdown -o output.md
```

## Limitations

- Cannot read password-protected documents without the password
- Some complex formatting may be simplified during extraction
- Macros and embedded objects are not accessible

## Troubleshooting

**If python-docx is not installed:**
```bash
pip install python-docx
# or
python -m pip install python-docx
```

**If you get import errors:**
Make sure you're importing from `docx` not `python-docx`:
```python
from docx import Document  # Correct
```

**For large documents:**
Consider processing in chunks to avoid memory issues.
