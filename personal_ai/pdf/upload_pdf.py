from fastapi import UploadFile, File, APIRouter
from fastapi.responses import FileResponse
from ai.pinecone_api import add_vector
from langchain import text_splitter
import PyPDF2
import os
import io

# class TextSplitter(text_splitter.TextSplitter):
#     def split_text(text: str) → List[str]:
#         return 

router = APIRouter(
    prefix="/api/pdf",
)

@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    contents = await file.read()
    pdf_file = io.BytesIO(contents)  # Convert bytes to BytesIO object
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    num_pages = pdf_reader.numPages
    # Process the PDF contents as needed
    # Example: Extract text from each page
    text = ""
    for page_num in range(num_pages):
        page = pdf_reader.getPage(page_num)
        text += page.extractText()
    text = text.replace('\n', '')
    splitter = text_splitter.RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    splited_text = splitter.split_text(text)
    for text in splited_text:
        add_vector(text)
    return {"filename": file.filename, "num_pages": num_pages}

@router.get("/download")
async def download_pdf():
    return FileResponse("uploaded.pdf", media_type="application/pdf", filename="downloaded.pdf")
