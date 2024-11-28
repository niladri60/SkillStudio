// import CodeEditor from "./CodeEditor";
import CodingQuestion from "./CodingQuestions";

const SolveCoding = () => {
    return (
        <div className="solve-coding-page">
            <h1 className="text-3xl text-white font-bold text-center mt-8">Solve the Coding Problem</h1>
            <section className="p-10">
                <div className="container flex flex-col-reverse mx-auto lg:flex-row">
                    <div className="flex flex-col px-6 py-8 space-y-6 border rounded-sm sm:p-8 lg:p-12 lg:w-1/2 xl:w-2/5  dark:text-[#00df9a]">

                        <div className="flex space-x-2 sm:space-x-4">
                            <CodingQuestion />
                        </div>
                    </div>
                    <div className="lg:w-1/2 xl:w-3/5">
                        <div className="flex items-center justify-center p-4 md:p-8 lg:p-12">
                            <img src="https://source.unsplash.com/640x480/" alt="" className="rounded-lg shadow-lg dark:bg-gray-800 aspect-video sm:min-h-96" />
                        </div>
                    </div>
                </div>
            </section>
            {/* <CodeEditor /> */}
        </div>
    );
};

export default SolveCoding;
