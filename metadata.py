import PyPDF2
import argparse


def print_meta(filename):
    pdf_file = PyPDF2.PdfFileReader(filename)
    doc_info = pdf_file.getDocumentInfo()
    print('[+] Metadata for: ' + str(filename))

    for meta_item in doc_info:
        print('[*] Print meta item from doc_info: ' + doc_info[meta_item])


def main():
    parser = argparse.ArgumentParser(usage='python recycle_bin.py -F <pdf filename>')
    parser.add_argument('-F', '--pdf_filename', type=str, help='specify pdf filename')

    args = parser.parse_args()

    pdf_filename = args.pdf_filename

    if pdf_filename is None:
        print(parser.usage)
        exit(0)

    else:
        print_meta(pdf_filename)