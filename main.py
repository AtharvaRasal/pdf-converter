import pyautogui
import pdf2docx
import PyPDF2
import tabula
import pdf2image


confirm = pyautogui.confirm(title="Alert", text="please choose", buttons=["word", "csv", "text", "image"])

file = pyautogui.prompt(title="alert", text="enter file name")

file_saved = pyautogui.prompt(title="alert", text="enter file name to be saved")

if confirm == "word":
    pdf2docx.parse(file, f"{file_saved}.docx", start=0, end=None)

elif confirm == "text":
    pdffileobject = open(file, "rb")
    pdffilereader = PyPDF2.PdfReader(pdffileobject)
    pageobject = pdffilereader.pages[0]
    text = pageobject.extract_text()
    pdffileobject.close()
    with open(f"{file_saved}.txt", "w") as file:
        file.writelines(text)

elif confirm == "csv":
    tabula.convert_into(file, f"{file_saved}.csv", pages="all", output_format="csv")

elif confirm == "image":
    images = pdf2image.convert_from_path(file)
    for index, image in enumerate(images):
        image.save(f"image_{index}.jpg", "JPEG")

else:
    print("wrong input")
