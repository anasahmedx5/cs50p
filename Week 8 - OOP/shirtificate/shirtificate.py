from fpdf import FPDF

class Shirtificate(FPDF):
    def header(self):
        self.set_font("Arial", "B", 24)
        self.set_text_color(0,0,0)
        self.cell(0, 20, "CS50 Shirtificate", align="C", ln=True)

name = input("Name: ")

pdf = Shirtificate()
pdf.add_page()
pdf.set_auto_page_break(auto=False)

shirt_path = "shirtificate.png"
pdf.image(shirt_path, x=25, y=60, w=160)

pdf.set_font("Arial", "B", 24)
pdf.set_text_color(255, 255, 255)
pdf.text(x=60, y=130, txt=f"{name} took CS50")

pdf.output("shirtificate.pdf")


