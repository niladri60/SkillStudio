import React from "react";

const Categories = () => {
  return (
    <div>
      <section className="p-6  dark:text-white">
        <div className="container mx-auto">
          <span className="block mb-2 text-xs font-medium tracking-widest text-center uppercase dark:text-[#00df9a]">
            How it works
          </span>
          <h2 className="text-5xl font-bold text-center dark:text-gray-500">
            Building with Mamba is simple
          </h2>
          <div className="grid gap-6 my-16 lg:grid-cols-3">
            <div className="flex flex-col p-8 space-y-4 rounded-md border border-[#00df9a]">
              <div className="flex items-center justify-center flex-shrink-0 w-12 h-12 text-xl font-bold rounded-full dark:bg-[#00df9a] dark:text-black">
                1
              </div>
              <p className="text-2xl font-semibold">
                <b>Nulla.</b>Nostrum, corrupti blanditiis. Illum, architecto?
              </p>
            </div>
            <div className="flex flex-col p-8 space-y-4 rounded-md dark:bg-[#00df9a] text-black">
              <div className="flex items-center justify-center flex-shrink-0 w-12 h-12 text-xl font-bold rounded-full dark:bg-white dark:text-black">
                2
              </div>
              <p className="text-2xl font-semibold">
                <b>Accusantium.</b>Vitae saepe atque neque sunt eius dolor
                veniam alias debitis?
              </p>
            </div>
            <div className="flex flex-col p-8 space-y-4 rounded-md border border-[#00df9a]">
              <div className="flex items-center justify-center flex-shrink-0 w-12 h-12 text-xl font-bold rounded-full dark:bg-[#00df9a] dark:text-black">
                3
              </div>
              <p className="text-2xl font-semibold">
                <b>Maxime.</b>Expedita temporibus culpa reprehenderit doloribus
                consectetur odio!
              </p>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
};

export default Categories;
