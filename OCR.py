from PIL import Image
import pytesseract
tessdata_dir_config = '--tessdata-dir "F:ProgramWin7\\Tesseract-OCR\\tessdata"'


# 上面都是导包，只需要下面这一行就能实现图片文字识别
Im = Image.open('s.png')
text = pytesseract.image_to_string(Im,lang = 'chi_sim',config=tessdata_dir_config)
print(text)