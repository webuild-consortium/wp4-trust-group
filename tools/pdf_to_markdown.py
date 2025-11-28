#!/usr/bin/env python3
"""
PDF to Markdown Converter
Converts PDF files to markdown format preserving structure and formatting.
"""

import sys
import os
from pathlib import Path

try:
    import fitz  # PyMuPDF
except ImportError:
    print("Error: PyMuPDF is required. Install it with: pip install pymupdf")
    sys.exit(1)


def pdf_to_markdown(pdf_path, output_path=None):
    """
    Convert a PDF file to markdown format.
    
    Args:
        pdf_path: Path to the input PDF file
        output_path: Path to the output markdown file (optional)
    
    Returns:
        Path to the created markdown file
    """
    pdf_path = Path(pdf_path)
    
    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")
    
    # Generate output path if not provided
    if output_path is None:
        output_path = pdf_path.parent / f"{pdf_path.stem}.md"
    else:
        output_path = Path(output_path)
    
    # Open PDF
    doc = fitz.open(pdf_path)
    
    markdown_content = []
    
    # Add document header
    markdown_content.append(f"# {pdf_path.stem}\n")
    markdown_content.append(f"*Converted from: {pdf_path.name}*\n")
    markdown_content.append(f"*Total pages: {len(doc)}*\n\n")
    markdown_content.append("---\n\n")
    
    # Extract text from each page
    for page_num in range(len(doc)):
        page = doc[page_num]
        
        # Add page separator
        markdown_content.append(f"\n## Page {page_num + 1}\n\n")
        
        # Extract text blocks with formatting
        blocks = page.get_text("dict")
        
        for block in blocks["blocks"]:
            if "lines" in block:  # Text block
                paragraph = []
                for line in block["lines"]:
                    line_text = []
                    for span in line["spans"]:
                        text = span["text"]
                        # Preserve formatting
                        if span.get("flags", 0) & 16:  # Bold
                            text = f"**{text}**"
                        if span.get("flags", 0) & 2:  # Italic
                            text = f"*{text}*"
                        line_text.append(text)
                    if line_text:
                        paragraph.append("".join(line_text))
                
                if paragraph:
                    # Join lines and add to markdown
                    para_text = " ".join(paragraph).strip()
                    if para_text:
                        markdown_content.append(f"{para_text}\n\n")
            elif "image" in block:  # Image block
                markdown_content.append(f"![Image on page {page_num + 1}]\n\n")
    
    doc.close()
    
    # Write markdown file
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("".join(markdown_content))
    
    print(f"Successfully converted {pdf_path.name} to {output_path.name}")
    return output_path


def main():
    """Main function to handle command line arguments."""
    if len(sys.argv) < 2:
        print("Usage: python pdf_to_markdown.py <pdf_file> [output_file]")
        print("   or: python pdf_to_markdown.py <pdf_file1> <pdf_file2> ...")
        sys.exit(1)
    
    pdf_files = sys.argv[1:]
    
    for pdf_file in pdf_files:
        try:
            pdf_to_markdown(pdf_file)
        except Exception as e:
            print(f"Error converting {pdf_file}: {e}", file=sys.stderr)
            sys.exit(1)


if __name__ == "__main__":
    main()


