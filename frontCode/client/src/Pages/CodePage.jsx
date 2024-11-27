import { useState, useEffect } from "react";
import axios from "axios";
import CodeInstructions from "../Components/CodingComponents/codeInstructions";
import CodingQuestion from "../Components/CodingComponents/CodingQuestions";
import CodeEditor from "../Components/CodingComponents/CodeEditor";

const CodePage = () => {
  const [codeContent, setCodeContent] = useState(null);
  const [acceptedInstructions, setAcceptedInstructions] = useState(false); // Track instructions acceptance

  useEffect(() => {
    if (acceptedInstructions) {
      fetchCode();
    }
  }, [acceptedInstructions]);

  const fetchCode = async () => {
    try {
      const response = await axios.get("http://localhost:5000/app/codingproblem");
      if (response.status === 200) {
        setCodeContent(response.data);
      } else {
        throw new Error(`Error: ${response.status}`);
      }
    } catch (error) {
      console.error("Error fetching data:", error.message || error);
    }
  };

  return (
    <CodeEditor />
  );
};

export default CodePage;


// {acceptedInstructions ? (
//   <>
//     {/* Display Coding Problem */}
//     <CodingQuestion codeContent={codeContent} />
//   </>
// ) : (
//   <CodeInstructions setAcceptedInstructions={setAcceptedInstructions} />
// )}