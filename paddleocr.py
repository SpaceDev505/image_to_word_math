import ocrmypdf

def ocr(file_path, save_path):
   ocrmypdf.ocr(file_path, save_path)
ocr("1.jpg","output.pdf")