import sys, os
from collections import Counter
from superwand import make_theme_splash
import pytesseract
from PIL import Image
from smart_color import SmartColor
from smart_menu import SmartMenu

"""
`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,
`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,
`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,
`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,**:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,
`:,:***:`:,:`:,:`:,:`:,:`:,*********`:,:`:,:`:,:`:,:`:,:`***`:,:`:,:`:,
`:,:***:`:,:`:,:`:,:`:,:`:************,:`:,:`:,:`:,:`:,:`***`:,:`:,:`:,
`:,:***:`:,:`:,:`:,:`:,:`*************,:`:,:`:,:`:,:`:,:`***`:,:`:,:`:,
`:,:`:,:`:,:`:,:`:,:`:,:`**************:`:,:`:,:`:,:`:,:`***`:,:`:,:`:,
`:,:`:,:`:,:`:,:`:,:`:,:*****:,**:*****:`:,:`:,:`:,:`:,:`***`:,:`:,:`:,
`:,:`:,:`:,:`:,:`:,:`:,:****`:,**:,****:`:,:`:,:`:,:`:,:`***`:,:`:,:`:,
`:,:***:`:,:`:,:`:,:`:,:****`:,**:,:`:,:`:,:`:,:`:,:`:,:`***`********:,
`:,:***:`:,:`:,:`:,:`:,:*****:,**:,:`:,:`:,:`:,:`:,:`:,:`*************,
`:,:***:`:,:`:,:`:,:`:,:`********:,:`:,:`:,:`:,:`:,:`:,:`**************
`:,:***:`:,:`:,:`:,:`:,:`*********,:`:,:`:,:`:,:`:,:`:,:`**************
`:,:***:`:,:`:,:`:,:`:,:`:**********`:,:`:,:`:,:`:,:`:,:`*****,:`:,****
`:,:***:`:,:`:,:`:,:`:,:`:,***********,:`:,:`:,:`:,:`:,:`****:,:`:,****
`:,:***:`:,:`:,:`:,:`:,:`:,:`**********:`:,:`:,:`:,:`:,:`****:,:`:,****
`:,:***:`:,:`:,:`:,:`:,:`:,:`:,********:`:,:`:,:`:,:`:,:`****:,:`:,****
`:,:***:`:,:`:,:`:,:`:,:`:,:`:,**:,*****`:,:`:,:`:,:`:,:`***`:,:`:,****
`:,:***:`:,:`:,:`:,:`:,:`:,:`:,**:,:****`:,:`:,:`:,:`:,:`***`:,:`:,****
`:,:***:`:,:`:,:`:,:`:,:****`:,**:,:****`:,:`:,:`:,:`:,:`***`:,:`:,****
`:,:***:`:,:`:,:`:,:`:,:****`:,**:,:****`:,:`:,:`:,:`:,:`***`:,:`:,****
`:,:***:`:,:`:,:`:,:`:,:*****:,**:,*****`:,:`:,:`:,:`:,:`***`:,:`:,****
`:,:***:`:,:`:,:`:,:`:,:***************:`:,:`:,:`:,:`:,:`***`:,:`:,****
`:,:***:`:,:`:,:`:,:`:,:`**************:`:,:`:,:`:,:`:,:`***`:,:`:,****
`:,:***:`:,:`:,:`:,:`:,:`:************,:`:,:`:,:`:,:`:,:`***`:,:`:,****
`:,:***:`:,:`:,:`:,:`:,:`:,**********:,:`:,:`:,:`:,:`:,:`***`:,:`:,****
`:,:***:`:,:`:,:`:,:`:,:`:,:`:,**:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,
`:,****:`:,:`:,:`:,:`:,:`:,:`:,**:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,
`:*****:`:,:`:,:`:,:`:,:`:,:`:,**:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,
*******:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,
*******:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,
******,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,
`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,
`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,
`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,'
"""
from pri import nt

print = nt


def extract_text_from_image(image_path):
    image = pytesseract.imread(image_path)
    return extracted_text


# def generate_html_css(menu_text):
#     return html_code, css_code


def save_to_file(html_code, css_code):
    print("Website generated successfully!")


def premain(roo: str):
    # Provide the path to the menu image
    x = os.listdir(roo)
    ips = ["/".join((os.getcwd(), roo, y,)) for y in x]
    return ips


def main(*a, **k):
    ips = premain("examples/sabor-catracha")
    sm = SmartMenu(ips)
    sm.get_html_body()
    sc = SmartColor(ips, colors=32)
    sc.global_colors()
    print(*sc.g_c, sep="\n>>>")


if __name__ == "__main__":
    print("hey")
