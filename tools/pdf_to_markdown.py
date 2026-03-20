#!/usr/bin/env python3
"""
PDF to Markdown Converter
Converts PDF files to markdown format preserving structure and formatting.
"""

import sys
from pathlib import Path

try:
    import fitz  # PyMuPDF
except ImportError:
    print("Error: PyMuPDF is required. Install it with: pip install pymupdf")
    sys.exit(1)


def _format_span(span):
    """Apply markdown formatting to a text span based on its flags."""
    text = span["text"]
    flags = span.get("flags", 0)
    if flags & 16:  # Bold
        text = f"**{text}**"
    if flags & 2:  # Italic
        text = f"*{text}*"
    return text


def _process_text_block(block):
    """Extract and format text from a text block. Returns paragraph or None."""
    paragraph = []
    for line in block["lines"]:
        line_text = [_format_span(span) for span in line["spans"]]
        if line_text:
            paragraph.append("".join(line_text))
    if paragraph:
        return " ".join(paragraph).strip()
    return None


def _extract_page_content(page, page_num):
    """Extract markdown content from a single page."""
    blocks = page.get_text("dict")["blocks"]
    content = [f"\n## Page {page_num}\n\n"]
    for block in blocks:
        if "lines" in block:
            para_text = _process_text_block(block)
            if para_text:
                content.append(f"{para_text}\n\n")
        elif "image" in block:
            content.append(f"![Image on page {page_num}]\n\n")
    return content


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

    if output_path is None:
        output_path = pdf_path.parent / f"{pdf_path.stem}.md"
    else:
        output_path = Path(output_path)

    doc = fitz.open(pdf_path)
    markdown_content = [
        f"# {pdf_path.stem}\n",
        f"*Converted from: {pdf_path.name}*\n",
        f"*Total pages: {len(doc)}*\n\n",
        "---\n\n",
    ]

    for page_num in range(len(doc)):
        page = doc[page_num]
        markdown_content.extend(_extract_page_content(page, page_num + 1))

    doc.close()

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
