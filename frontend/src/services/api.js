import axios from "axios";

const API = axios.create({
  baseURL: "http://127.0.0.1:8000",
});

export const analyzeResume = async (file, jobDescription) => {
  const formData = new FormData();

  formData.append("file", file);
  formData.append("job_description", jobDescription);

  try {
    const response = await API.post("/api/job/match-resume", formData);

    return response.data;
  } catch (error) {
    console.error(
      "Resume analysis failed:",
      error.response?.data || error.message,
    );

    throw error;
  }
};
