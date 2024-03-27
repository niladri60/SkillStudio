import React from "react";

const Login = () => {
  return (
    <body>
      <div class="container px-6 mx-auto">
        <div class="flex flex-col text-center md:text-left md:flex-row h-screen justify-evenly md:items-center">
          <div class="w-full md:w-full lg:w-9/12 mx-auto md:mx-0">
            <div class="p-10 flex flex-col w-full shadow-xl rounded-xl border border-[#00df9a]">
              <h2 class="text-3xl font-bold text-[#00df9a] text-left mb-5">
                Login
              </h2>
              <form action="" class="w-full">
                <div id="input" class="flex flex-col w-full my-5">
                  <label for="username" class="text-gray-200 mb-2">
                    Username
                  </label>
                  <input
                    type="text"
                    id="username"
                    placeholder="Please insert your username"
                    class="appearance-none bg-[#1f201f] rounded-lg px-4 py-3 placeholder-[#879892] focus:outline-none focus:ring-2 focus:ring-[#00df9a] focus:shadow-lg text-[#00df9a]"
                  />
                </div>
                <div id="input" class="flex flex-col w-full my-5">
                  <label for="password" class="text-gray-200 mb-2">
                    Password
                  </label>
                  <input
                    type="password"
                    id="password"
                    placeholder="Please insert your password"
                    class="appearance-none bg-[#1f201f] rounded-lg px-4 py-3 placeholder-[#879892] focus:outline-none focus:ring-2 focus:ring-[#00df9a] focus:shadow-lg text-[#00df9a]"
                  />
                </div>
                <div id="button" class="flex flex-col w-full my-5">
                  <button
                    type="button"
                    class="w-full py-4 bg-[#00df9a] rounded-lg text-black hover:bg-[#0f5f47] hover:text-white"
                  >
                    <div class="flex flex-row items-center justify-center">
                      <div class="mr-2">
                        <svg
                          class="w-6 h-6"
                          fill="none"
                          stroke="currentColor"
                          viewBox="0 0 24 24"
                          xmlns="http://www.w3.org/2000/svg"
                        >
                          <path
                            stroke-linecap="round"
                            stroke-linejoin="round"
                            stroke-width="2"
                            d="M11 16l-4-4m0 0l4-4m-4 4h14m-5 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h7a3 3 0 013 3v1"
                          ></path>
                        </svg>
                      </div>
                      <div class="font-bold">Login</div>
                    </div>
                  </button>
                  <div class="flex justify-evenly mt-5">
                    <p className="text-center text-sm text-gray-500">
                      Don't have an Account?{" "}
                      <a
                        href="/signup"
                        className="font-semibold leading-6 text-[#00df9a] hover:text-[#02734f]"
                      >
                        Signup
                      </a>
                    </p>
                  </div>
                </div>
              </form>
            </div>
          </div>

          <div class="flex flex-col w-full">
            <div>
              <svg
                class="w-20 h-20 mx-auto md:float-right fill-stroke text-[#00df9a]"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M12 6V4m0 2a2 2 0 100 4m0-4a2 2 0 110 4m-6 8a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4m6 6v10m6-2a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4"
                ></path>
              </svg>
            </div>
            <h1 class="md:text-right text-5xl text-[#00df9a] font-bold">
              Client Login
            </h1>
          </div>
        </div>
      </div>
    </body>
  );
};

export default Login;
