from fastapi import APIRouter, UploadFile, File, Form

import os
import tempfile

from app.services.pdf_parser import extract_text_from_pdf
from app.services.skill_extractor import extract_skills
from app.services.job_skill_extractor import extract_job_skills
from app.services.job_matcher import calculate_similarity
from app.services.personal_info import extract_personal_info
from app.services.resume_parser import parse_sections
from app.services.text_processor import process_text


router = APIRouter(
    prefix="/api/job",
    tags=["Job Matching"]
)


@router.post("/match")
async def match_job(data: dict):

    resume_text = data.get("resume_text")
    job_description = data.get("job_description")
    resume_skills = data.get("resume_skills", [])

    if not resume_text:

        return {
            "error": "resume_text is required"
        }

    if not job_description:

        return {
            "error": "job_description is required"
        }

    # ---------------------------------
    # TF-IDF similarity
    # ---------------------------------

    similarity_score = calculate_similarity(
        resume_text,
        job_description
    )

    # ---------------------------------
    # Extract required job skills
    # ---------------------------------

    job_skills = extract_job_skills(
        job_description
    )

    # ---------------------------------
    # Compare skills
    # ---------------------------------

    resume_skill_map = {
        skill.lower(): skill
        for skill in resume_skills
    }

    matched_skills = []
    missing_skills = []

    for skill in job_skills:

        if skill.lower() in resume_skill_map:

            matched_skills.append(skill)

        else:

            missing_skills.append(skill)

    # ---------------------------------
    # Skill percentage
    # ---------------------------------

    if len(job_skills) > 0:

        skill_match_percentage = round(
            (
                len(matched_skills)
                /
                len(job_skills)
            ) * 100,
            2
        )

    else:

        skill_match_percentage = 0

    return {

        "similarity_score": similarity_score,

        "job_skills": job_skills,

        "matched_skills": matched_skills,

        "missing_skills": missing_skills,

        "skill_match_percentage":
            skill_match_percentage
    }

@router.post("/match-resume")
async def match_resume(
    file: UploadFile = File(...),
    job_description: str = Form(...)
):

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

        # 1. Extract text
        resume_text = extract_text_from_pdf(
            temp_file_path
        )

        # 2. Resume skills
        resume_skills = extract_skills(
            resume_text
        )

        # 3. Job skills
        job_skills = extract_job_skills(
            job_description
        )

        # 4. Similarity
        similarity_score = calculate_similarity(
            resume_text,
            job_description
        )

        # 5. Compare skills
        resume_skill_map = {
            skill.lower(): skill
            for skill in resume_skills
        }

        matched_skills = []
        missing_skills = []

        for skill in job_skills:

            if skill.lower() in resume_skill_map:
                matched_skills.append(skill)

            else:
                missing_skills.append(skill)

        # 6. Skill percentage
        if job_skills:

            skill_match_percentage = round(
                len(matched_skills)
                / len(job_skills)
                * 100,
                2
            )

        else:

            skill_match_percentage = 0

        # 7. Complete resume information
        personal_info = extract_personal_info(
            resume_text
        )

        sections = parse_sections(
            resume_text
        )

        nlp_result = process_text(
            resume_text
        )

        # 8. Final response
        return {

            "filename": file.filename,

            "resume": {

                "personal_info":
                    personal_info,

                "skills":
                    resume_skills,

                "sections":
                    sections,

                "nlp":
                    nlp_result
            },

            "job_match": {

                "similarity_score":
                    similarity_score,

                "job_skills":
                    job_skills,

                "matched_skills":
                    matched_skills,

                "missing_skills":
                    missing_skills,

                "skill_match_percentage":
                    skill_match_percentage
            }
        }

    finally:

        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)