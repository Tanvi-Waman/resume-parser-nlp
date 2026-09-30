import { useState } from "react";

import ResumeUpload from "./components/ResumeUpload";
import JobDescription from "./components/JobDescription";
import ResultCard from "./components/ResultCard";

import { analyzeResume } from "./services/api";

import "./App.css";

function App() {
  const [file, setFile] = useState(null);

  const [jobDescription, setJobDescription] = useState("");

  const [result, setResult] = useState(null);

  const [loading, setLoading] = useState(false);

  const [error, setError] = useState("");

  const handleAnalyze = async () => {
    if (!file) {
      setError("Please upload a resume.");
      return;
    }

    if (!jobDescription.trim()) {
      setError("Please enter a job description.");
      return;
    }

    try {
      setLoading(true);
      setError("");
      setResult(null);

      const data = await analyzeResume(file, jobDescription);

      setResult(data);
    } catch (error) {
      console.error(error);

      setError("Failed to analyze resume. Make sure the backend is running.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app">
      <header>
        <h1>Resume Analyzer</h1>

        <p>Analyze your resume against a job description</p>
      </header>

      <main>
        <ResumeUpload file={file} setFile={setFile} />

        <JobDescription
          jobDescription={jobDescription}
          setJobDescription={setJobDescription}
        />

        {error && <p className="error">{error}</p>}

        <button onClick={handleAnalyze} disabled={loading}>
          {loading ? "Analyzing..." : "Analyze Resume"}
        </button>

        <ResultCard result={result} />
      </main>
    </div>
  );
}

export default App;
