import { useState, useEffect } from "react";
import axios from "axios";
import CodeInstructions from "../Components/CodingComponents/codeInstructions";
import QuestionList from "../Components/CodingComponents/QuestionList";

const CodePage = () => {
  const [codeContent, setCodeContent] = useState(null); // To store coding question data
  const [acceptedInstructions, setAcceptedInstructions] = useState(false); // Track instructions acceptance
  const [loading, setLoading] = useState(false); // Track loading state
  const [error, setError] = useState(null); // Track errors

  useEffect(() => {
    if (acceptedInstructions) {
      fetchCode();
    }
  }, [acceptedInstructions]);

  const fetchCode = async () => {
    setLoading(true);
    setError(null);
    try {
      const response = await axios.get("http://localhost:5000/app/codingproblem");
      if (response.status === 200) {
        setCodeContent(response.data);
      } else {
        throw new Error(`Error: ${response.status}`);
      }
    } catch (err) {
      setError(err.message || "Something went wrong!");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="code-page">
      {acceptedInstructions ? (
        loading ? (
          <p>Loading...</p>
        ) : error ? (
          <p className="text-red-500">{error}</p>
        ) : (
          <QuestionList codeContent={codeContent} />
        )
      ) : (
        <CodeInstructions setAcceptedInstructions={setAcceptedInstructions} />
      )}
    </div>
  );
};

export default CodePage;
