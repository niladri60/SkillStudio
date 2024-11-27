import PropTypes from "prop-types";

const CodingQuestion = ({ codeContent }) => {
  return (
    <div className="text-white">
      {codeContent ? (
        <div>
          <h2>Coding Problem</h2>
          <p>
            <strong>ID:</strong> {codeContent.id}
          </p>
          <p>
            <strong>Statement:</strong> {codeContent.Statement}
          </p>
          <p>
            {codeContent.Example}
          </p>
          <p>
            <strong>Constraints:</strong> {codeContent.Constraint}
          </p>
          <p>
            <strong>Topic:</strong> {codeContent.Topic}
          </p>
          <p>
            <strong>Difficulty:</strong> {codeContent.Level}
          </p>
        </div>
      ) : (
        <p>Loading...</p>
      )}
    </div>
  );
};

CodingQuestion.propTypes = {
  codeContent: PropTypes.object.isRequired,
};

export default CodingQuestion;
