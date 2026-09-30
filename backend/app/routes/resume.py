from fastapi import APIRouter, UploadFile, File

import os
import tempfile

from app.services.pdf_parser import extract_text_from_pdf
from app.services.text_processor import process_text
from app.services.personal_info import extract_personal_info


router = APIRouter(
    prefix="/api/resume",
    tags=["Resume"]
)


@router.post("/upload")
async def upload_resume(file: UploadFile = File(...)):

    if not file.filename.lower().endswith(".pdf"):
        return {
            "error": "Only PDF files are supported"
        }

    contents = await file.read()

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".pdf"
    ) as temp_file:

        temp_file.write(contents)

        temp_file_path = temp_file.name

    try:

        # Extract text from PDF
        text = extract_text_from_pdf(temp_file_path)

        # Process resume using NLP
        nlp_result = process_text(text)

        # Extract personal information
        personal_info = extract_personal_info(text)

        return {
            "filename": file.filename,

            "personal_info": personal_info,

            "skills": nlp_result["skills"],

            "education": nlp_result["education"],

            "certifications": nlp_result["certifications"],

            "sections": nlp_result["sections"],

            "experience": nlp_result["experience"],

            "projects": nlp_result["projects"],

            "text": text,

            "nlp": {
                "tokens": nlp_result["tokens"],
                "entities": nlp_result["entities"]
            }
        }

    finally:

        os.remove(temp_file_path)