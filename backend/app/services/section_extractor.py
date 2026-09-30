import re


SECTION_NAMES = {
    "education": [
        "education",
        "academic background",
        "educational background",
        "academic qualifications"
    ],

    "experience": [
        "experience",
        "work experience",
        "professional experience",
        "employment",
        "internship",
        "internships"
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
        "licenses and certifications"
    ]
}


def normalize_line(line: str):

    line = line.strip()

    line = re.sub(r"\s+", " ", line)

    return line


def identify_section(line: str):

    normalized = line.lower().strip()

    normalized = re.sub(
        r"[^a-zA-Z\s&]",
        "",
        normalized
    )

    normalized = normalized.strip()

    for section, names in SECTION_NAMES.items():

        for name in names:

            if normalized == name:
                return section

    return None


def extract_sections(text: str):

    lines = text.splitlines()

    sections = {
        "education": [],
        "experience": [],
        "projects": [],
        "certifications": []
    }

    current_section = None

    for line in lines:

        line = normalize_line(line)

        if not line:
            continue

        detected_section = identify_section(line)

        if detected_section:
            current_section = detected_section
            continue

        if current_section:
            sections[current_section].append(line)

    return sections