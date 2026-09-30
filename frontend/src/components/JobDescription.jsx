function JobDescription({ jobDescription, setJobDescription }) {
  return (
    <div className="job-section">
      <h2>Job Description</h2>

      <textarea
        value={jobDescription}
        onChange={(event) => setJobDescription(event.target.value)}
        placeholder="Paste the job description here..."
        rows="12"
      />
    </div>
  );
}

export default JobDescription;
