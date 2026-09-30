function ResumeUpload({ file, setFile }) {
  const handleFileChange = (event) => {
    const selectedFile = event.target.files[0];

    if (!selectedFile) {
      return;
    }

    if (selectedFile.type !== "application/pdf") {
      alert("Please select a PDF file.");
      return;
    }

    setFile(selectedFile);
  };

  return (
    <div className="upload-section">
      <h2>Upload Resume</h2>

      <input type="file" accept=".pdf" onChange={handleFileChange} />

      {file && <p className="file-name">Selected: {file.name}</p>}
    </div>
  );
}

export default ResumeUpload;
