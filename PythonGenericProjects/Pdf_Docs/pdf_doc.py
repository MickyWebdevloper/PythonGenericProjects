from pdf2docx import Converter

# pdf_file = 'doc1.pdf'  # main pdf file path.
# docx_file = 'Demo.docx'  # which doc name you want.

# # convert pdf to docx
# cv = Converter(pdf_file)
# cv.convert(docx_file)      # all pages by default
# cv.close()

# An alternative using parse method:

from pdf2docx import parse

pdf_file = 'uan.pdf'  # main pdf file path.
docx_file = 'Demo.docx'  # which doc name you want.


# convert pdf to docx
parse(pdf_file, docx_file)
