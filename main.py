from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.add_font("DejaVu", style = "", fname = "DejaVuSansCondensed.ttf", uni = True)
pdf.set_font("DejaVu", size = 12)
pdf.cell(text="Oferta biura podróży")
pdf.output("Oferta_biura_podrozy.pdf")