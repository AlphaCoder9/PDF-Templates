from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation='P', unit='mm', format='A4')

df = pd.read_csv('topics.csv')

# creating a loop to iterate each row.
for index, row in df.iterrows():
    pdf.add_page()

    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row['Topic'], align='L', ln=1)
    pdf.line(10, 22, 200, 22)

    # to iterate the number of pages of each topic
    for i in range(row['Pages'] - 1):
        pdf.add_page()
pdf.output('output.pdf')  # To create the output of PDF.
