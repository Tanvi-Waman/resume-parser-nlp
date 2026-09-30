import re


SKILLS = [
    "HTML",
    "CSS",
    "JavaScript",
    "TypeScript",
    "React",
    "Angular",
    "Vue",
    "Node.js",
    "Express",
    "MongoDB",
    "MySQL",
    "PostgreSQL",
    "SQL",
    "Python",
    "Java",
    "C",
    "C++",
    "Git",
    "GitHub",
    "Docker",
    "AWS",
    "Azure",
    "REST API",
    "REST APIs",
    "GraphQL",
    "Tailwind CSS",
    "Bootstrap",
    "Next.js",
    "FastAPI",
    "Django",
    "Spring Boot",
    "Machine Learning",
    "Deep Learning",
    "NLP",
    "TensorFlow",
    "PyTorch",
    "Pandas",
    "NumPy",
    "Socket.IO",
    "JWT",
    "Postman",
    "Cloudinary",
    "Zustand",
    "Prisma",
    "Redis",
    "FastAPI",
    "LangChain",
    "FAISS",
    "Chroma",
]


def extract_job_skills(job_description: str):

    found_skills = []

    text = job_description.lower()

    for skill in SKILLS:

        skill_lower = skill.lower()

        pattern = r"(?<!\w)" + re.escape(skill_lower) + r"(?!\w)"

        if re.search(pattern, text):

            found_skills.append(skill)

    return found_skills