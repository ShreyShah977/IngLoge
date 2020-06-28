try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
from GSearch import GSearch
# If you don't have tesseract executable in your PATH, include the following:
# pytesseract.pytesseract.tesseract_cmd = r'<>'
# Example tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

# Simple image to string
s = str(pytesseract.image_to_string(Image.open('table_nutella.png')));
s = s.replace("\n", "").replace("INGREDIENTS:", '').split(',');
item_list = [e for e in s if e not in ('AS', 'AN', 'INGREDIENTS:', 'CONTAINS')]
thislist = set(item_list);    
print(thislist)
for x in thislist:
    GSearch.SearchNow(str(x));
