import re

from app.services.skill_extractor import extract_skills


PROJECT_START_PATTERN = re.compile(
    r"^\s*\d+\s*\.\s*(.+?)(?:\s*:\s*Code:.*)?$",
    re.IGNORECASE
)


def split_projects(lines):

    projects = []
    current_project = None

    for line in lines:

        line = line.strip()

        if not line:
            continue

        # Stop project parsing when another section begins
        if line.upper() in {
            "OTHER SKILLS",
            "SKILLS",
            "CERTIFICATIONS",
            "EDUCATION",
            "EXPERIENCE"
        }:
            break

        match = PROJECT_START_PATTERN.match(line)

        if match:

            if current_project:
                projects.append(current_project)

            project_name = match.group(1).strip()

            current_project = {
                "name": project_name,
                "lines": []
            }

        else:

            if current_project:
                current_project["lines"].append(line)

    if current_project:
        projects.append(current_project)

    return projects

def parse_single_project(project):

    name = project["name"]

    lines = project["lines"]

    project_text = " ".join(lines)

    technologies = extract_skills(project_text)

    description = []

    for line in lines:

        # Skip lines containing only the GitHub/code link
        if "Code:" in line:
            continue

        description.append(line)

    return {
        "name": name,
        "technologies": technologies,
        "description": description
    }


def parse_projects(lines):

    if not lines:
        return []

    projects = split_projects(lines)

    parsed_projects = []

    for project in projects:

        parsed_project = parse_single_project(project)

        parsed_projects.append(parsed_project)

    return parsed_projects