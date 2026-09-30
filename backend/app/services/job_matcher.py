from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def calculate_similarity(
    resume_text: str,
    job_description: str
):

    vectorizer = TfidfVectorizer(
        stop_words="english"
    )

    vectors = vectorizer.fit_transform([
        resume_text,
        job_description
    ])

    similarity = cosine_similarity(
        vectors[0:1],
        vectors[1:2]
    )

    score = similarity[0][0]

    return round(score * 100, 2)


def compare_skills(
    resume_skills,
    job_skills
):

    resume_skill_map = {
        skill.lower(): skill
        for skill in resume_skills
    }

    job_skill_map = {
        skill.lower(): skill
        for skill in job_skills
    }

    matched_skills = []

    missing_skills = []

    for skill_lower, original_skill in job_skill_map.items():

        if skill_lower in resume_skill_map:

            matched_skills.append(
                original_skill
            )

        else:

            missing_skills.append(
                original_skill
            )

    total_required = len(job_skills)

    if total_required > 0:

        skill_match_percentage = round(
            (len(matched_skills) / total_required) * 100,
            2
        )

    else:

        skill_match_percentage = 0

    return {
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "skill_match_percentage": skill_match_percentage
    }