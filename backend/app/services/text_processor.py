import spacy

from app.services.section_extractor import extract_sections
from app.services.skill_extractor import extract_skills
from app.services.experience_parser import parse_experience
from app.services.project_parser import parse_projects
from app.services.education_parser import parse_education
from app.services.certification_parser import parse_certifications


nlp = spacy.load("en_core_web_sm")


def process_text(text: str):

    doc = nlp(text)

    # -------------------------
    # Token information
    # -------------------------

    tokens = []

    for token in doc:

        if not token.is_space:

            tokens.append({
                "text": token.text,
                "lemma": token.lemma_,
                "pos": token.pos_
            })

    # -------------------------
    # Named entities
    # -------------------------

    entities = []

    for entity in doc.ents:

        entities.append({
            "text": entity.text,
            "label": entity.label_
        })

    skills = extract_skills(text)

    sections = extract_sections(text)

    education = parse_education(
        sections["education"]
    )

    certifications = parse_certifications(
        sections["certifications"]
    )

    experience=parse_experience(
        sections["experience"]
    )

    projects = parse_projects(
        sections["projects"]
    )


    return {
        "tokens": tokens,
        "entities": entities,
        "skills": skills,
        "sections": sections,
        "education": education,
        "certifications": certifications,
        "experience": experience,
        "projects": projects
    }