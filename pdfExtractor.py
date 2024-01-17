import PyPDF2

def extract_pages(input_pdf, output_pdf, start_page, end_page):
    """Extracts a specified page range from a PDF file."""

    with open(input_pdf, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        pdf_writer = PyPDF2.PdfWriter()

        for page_num in range(start_page - 1, end_page):  # Page numbers are 0-based
            page = pdf_reader.pages[page_num]
            pdf_writer.add_page(page)

        with open(output_pdf, 'wb') as output_file:
            pdf_writer.write(output_file)

# usage:
if __name__ == "__main__":
    input_pdf = input("Enter the input PDF file path: ")
    output_pdf = input("Enter the output PDF file path: ")
    start_page = int(input("Enter the start page number: "))
    end_page = int(input("Enter the end page number: "))
    # extracting
    extract_pages(input_pdf, output_pdf, start_page, end_page)
