import NLPAnalysis from "./NLPAnalysis";

function ResultCard({ result }) {
  if (!result) {
    return null;
  }

  const { resume, job_match } = result;

  return (
    <div className="results">
      <h2>Analysis Results</h2>

      {/* Scores */}

      <div className="score-container">
        <div className="score-card">
          <h3>Resume Similarity</h3>

          <p>{job_match.similarity_score}%</p>
        </div>

        <div className="score-card">
          <h3>Skill Match</h3>

          <p>{job_match.skill_match_percentage}%</p>
        </div>
      </div>

      {/* Personal Information */}

      <div className="resume-section">
        <h2>Personal Information</h2>

        <p>
          <strong>Name:</strong> {resume.personal_info.name || "Not found"}
        </p>

        <p>
          <strong>Email:</strong> {resume.personal_info.email || "Not found"}
        </p>

        <p>
          <strong>Phone:</strong> {resume.personal_info.phone || "Not found"}
        </p>

        <p>
          <strong>LinkedIn:</strong>{" "}
          {resume.personal_info.linkedin || "Not found"}
        </p>

        <p>
          <strong>GitHub:</strong> {resume.personal_info.github || "Not found"}
        </p>
      </div>

      {/* Resume Skills */}

      <div className="resume-section">
        <h2>Resume Skills</h2>

        <div className="skills-list">
          {resume.skills.map((skill) => (
            <span key={skill} className="skill">
              {skill}
            </span>
          ))}
        </div>
      </div>

      {/* Matched Skills */}

      <div className="resume-section">
        <h2>Matched Skills</h2>

        <div className="skills-list">
          {job_match.matched_skills.map((skill) => (
            <span key={skill} className="skill">
              {skill}
            </span>
          ))}
        </div>
      </div>

      {/* Missing Skills */}

      <div className="resume-section">
        <h2>Missing Skills</h2>

        <div className="skills-list">
          {job_match.missing_skills.map((skill) => (
            <span key={skill} className="skill missing">
              {skill}
            </span>
          ))}
        </div>
      </div>

      {/* Education */}

      <div className="resume-section">
        <h2>Education</h2>

        {resume.sections.education.map((item, index) => (
          <p key={index}>{item}</p>
        ))}
      </div>

      {/* Projects */}

      <div className="resume-section">
        <h2>Projects</h2>

        {resume.sections.projects.map((project, index) => (
          <p key={index}>{project}</p>
        ))}
      </div>

      {/* Certifications */}

      <div className="resume-section">
        <h2>Certifications</h2>

        {resume.sections.certifications.map((certification, index) => (
          <p key={index}>{certification}</p>
        ))}
      </div>

      {/* NLP Analysis */}

      <NLPAnalysis nlp={resume.nlp} />
    </div>
  );
}

export default ResultCard;
