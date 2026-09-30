SECTION_ALIASES = {
    "education": [
        "education",
        "academic background",
        "academic qualifications",
        "qualifications"
    ],
    "skills": [
        "skills",
        "technical skills",
        "technical expertise",
        "technologies"
    ],
    "experience": [
        "experience",
        "work experience",
        "professional experience",
        "employment history",
        "internship"
    ],
    "projects": [
        "projects",
        "personal projects",
        "academic projects",
        "project experience"
    ],
    "certifications": [
        "certifications",
        "certificates",
        "licenses & certifications"
    ]
}

def detect_section(line: str):
    cleaned_line = line.strip().lower()

    for section, aliases in SECTION_ALIASES.items():

        for alias in aliases:

            if cleaned_line == alias:
                return section

    return None

def parse_sections(text: str):

    sections = {
        "education": [],
        "skills": [],
        "experience": [],
        "projects": [],
        "certifications": []
    }

    current_section = None

    lines = text.splitlines()

    for line in lines:

        line = line.strip()

        if not line:
            continue

        detected_section = detect_section(line)

        if detected_section:
            current_section = detected_section
            continue

        if current_section:
            sections[current_section].append(line)

    return sections