from fastapi import UploadFile, File, APIRouter
from fastapi.responses import FileResponse
from ai.pinecone_api import add_vector
import PyPDF2
import os
import io

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
    extracted_text = ""
    for page_num in range(num_pages):
        page = pdf_reader.getPage(page_num)
        add_vector(page.extractText())
    return {"filename": file.filename, "num_pages": num_pages, "extracted_text": extracted_text}

@router.get("/download")
async def download_pdf():
    return FileResponse("uploaded.pdf", media_type="application/pdf", filename="downloaded.pdf")
