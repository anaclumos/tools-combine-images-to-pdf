imagelist = []
with open("imagesource.txt", "r") as imagesource:
    lines = imagesource.readlines()
    imagelist = map(str.strip, lines)

from fpdf import FPDF

pdf = FPDF()

for image in imagelist:
    print(image)
    pdf.add_page()
    pdf.image(image, 0, 0, 210, 297)  # for A4 pages

pdf.output("combined.pdf", "F")
