from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv('topics.csv')

# creating a loop to iterate each row.
for index, row in df.iterrows():
    pdf.add_page()

    # set the header

    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row['Topic'], align='L', ln=1)
    for y in range(20, 289, 10):
        pdf.line(10, y, 200, y)

    # set the footer
    pdf.ln(265)
    pdf.set_font(family="Times", style="I", size=10)
    pdf.set_text_color(175, 175, 175)
    pdf.cell(w=0, h=12, txt=row['Topic'], align='R')

    # to iterate the number of pages of each topic
    for i in range(row['Pages'] - 1):
        pdf.add_page()
    # set the footer for following topic pages.
        pdf.ln(277)
        pdf.set_font(family='Times', style='I', size=10)
        pdf.set_text_color(175, 175, 175)
        pdf.cell(w=0, h=10, txt=row['Topic'], align='R')
        for y in range(20, 289, 10):
            pdf.line(10, y, 200, y)
pdf.output('output.pdf')  # To create the output of PDF.
