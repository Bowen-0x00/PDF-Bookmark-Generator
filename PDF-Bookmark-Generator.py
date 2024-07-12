import PyPDF2
import argparse

def add_bookmarks(pdf_path, bookmarks, output_path, offset):
    reader = PyPDF2.PdfReader(pdf_path)
    writer = PyPDF2.PdfWriter()

    for i in range(len(reader.pages)):
        writer.add_page(reader.pages[i])

    def add_bookmark_recursively(bookmarks, parent=None):
        for title, page_num, children in bookmarks:
            bookmark = writer.add_outline_item(title, page_num - 1 + offset, parent)
            if children:
                add_bookmark_recursively(children, bookmark)

    add_bookmark_recursively(bookmarks)
    with open(output_path, "wb") as f_out:
        writer.write(f_out)

def parse_toc(toc_text):
    bookmarks = []
    stack = [(bookmarks, -1)]
    for line in toc_text.strip().split('\n'):
        indent = len(line) - len(line.lstrip())
        parts = line.strip().rsplit(' ', 1)
        title = parts[0].strip()
        page_num = int(parts[1].strip())

        bookmark = (title, page_num, [])
        while stack and stack[-1][1] >= indent:
            stack.pop()
        stack[-1][0].append(bookmark)
        stack.append((bookmark[2], indent))
    return bookmarks


def main():
    parser = argparse.ArgumentParser(description="Add bookmarks to a PDF based on a table of contents.")
    parser.add_argument("pdf_path", help="Path to the input PDF file")
    parser.add_argument("toc_path", help="Path to the text file containing the table of contents")
    parser.add_argument("output_path", help="Path to the output PDF file")
    parser.add_argument("--offset", type=int, default=0, help="Offset to apply to the page numbers in the table of contents")

    args = parser.parse_args()

    with open(args.toc_path, 'r', encoding='utf-8') as f:
        toc_text = f.read()

    bookmarks = parse_toc(toc_text)
    add_bookmarks(args.pdf_path, bookmarks, args.output_path, args.offset)

if __name__ == "__main__":
    main()