import PropTypes from "prop-types";
import { useNavigate } from "react-router-dom";

const QuestionList = ({ codeContent }) => {
    const navigate = useNavigate();

    const handleSolveClick = () => {
        navigate("/solve"); // Redirect to the SolveCoding page
    };
    if (!codeContent) {
        return (
            <p className="text-gray-500">
                No coding problem data is available. Please check back later.
            </p>
        );
    }

    return (
        <div>
            <section className="py-4 bg-black-100 text-white rounded-lg mt-4">
                <div className="container mx-auto flex flex-col items-center justify-center p-2 space-y-4 md:p-6 lg:space-y-0 lg:flex-row lg:justify-between">
                    <h1 className="text-2xl font-semibold leading-tight text-center lg:text-left">
                        {codeContent.Statement}
                    </h1>
                    <button className="px-6 py-2 text-lg font-semibold rounded-md bg-[#00df9a] text-gray-900" onClick={handleSolveClick}>
                        Solve
                    </button>
                </div>
            </section>
        </div>
    );
};

QuestionList.propTypes = {
    codeContent: PropTypes.object,
};

export default QuestionList;
