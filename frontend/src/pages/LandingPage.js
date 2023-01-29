/* This example requires Tailwind CSS v3.0+ */
// import { Outlet, Link } from "react-router-dom";
import Typing from "../components/Typing";
import Logo from "../images/sqlidify.png";

const LandingPage = () => {
  return (
    <div className="bg-neutral-800 h-screen">
      <div className="px-6 pt-6 lg:px-8">
        <nav className="flex items-center justify-between" aria-label="Global">
          <div className="flex lg:flex-1">
            <a href="#" className="-m-1.5 p-1.5">
              <span className="sr-only">Your Company</span>
              <img className="h-14" src={Logo} alt="" />
            </a>
          </div>
        </nav>
      </div>
      <div className="isolate h-5/6 flex flex-col justify-center">
        <div className="pointer-events-none	absolute inset-x-0 top-[-10rem] -z-10 transform-gpu overflow-hidden blur-3xl sm:top-[-20rem]">
          <svg
            className="relative left-[calc(50%-11rem)] -z-10 h-[21.1875rem] max-w-none -translate-x-1/2 rotate-[30deg] sm:left-[calc(50%-30rem)] sm:h-[42.375rem]"
            viewBox="0 0 1155 678"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              fill="url(#45de2b6b-92d5-4d68-a6a0-9b9b2abad533)"
              fillOpacity=".3"
              d="M317.219 518.975L203.852 678 0 438.341l317.219 80.634 204.172-286.402c1.307 132.337 45.083 346.658 209.733 145.248C936.936 126.058 882.053-94.234 1031.02 41.331c119.18 108.451 130.68 295.337 121.53 375.223L855 299l21.173 362.054-558.954-142.079z"
            />
            <defs>
              <linearGradient
                id="45de2b6b-92d5-4d68-a6a0-9b9b2abad533"
                x1="1155.49"
                x2="-78.208"
                y1=".177"
                y2="474.645"
                gradientUnits="userSpaceOnUse"
              >
                <stop stopColor="#7f1d1d" />
                <stop offset={1} stopColor="#b91c1c" />
              </linearGradient>
            </defs>
          </svg>
        </div>

        <div className="relative px-6 lg:px-8">
          {/* <div className="max-w-2xl py-32 sm:py-48 lg:py-56 w-full"> */}
          {/* <div className="hidden sm:mb-8 sm:flex sm:justify-center"> */}
          {/* <div className="relative rounded-full py-1 px-3 text-sm leading-6 text-gray-600 ring-1 ring-gray-900/10 hover:ring-gray-900/20">
                  Announcing our next round of funding.{' '}
                  <a href="#" className="font-semibold text-indigo-600">
                    <span className="absolute inset-0" aria-hidden="true" />
                    Read more <span aria-hidden="true">&rarr;</span>
                  </a>
                </div> */}
          {/* </div> */}
          <div className="flex flex-row gap-x-12 justify-center">
            <div className="flex flex-col">
              <h1 className="text-4xl font-bold tracking-tight text-slate-50 sm:text-7xl">
                Solidify your SQL
              </h1>
              <p className="mt-6 text-lg leading-8 text-slate-200">
                Paste your backend code into Sqlidify to determine if your login
                is safe
              </p>
              <div className="mt-10 flex items-center gap-x-6">
                <a
                  href="#form"
                  className="rounded-md bg-red-600 px-3.5 py-1.5 text-base font-semibold leading-7 text-white shadow-sm hover:bg-red-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
                >
                  Get started
                </a>
                <a
                  href="https://github.com/McHacks-CU"
                  target="_blank"
                  rel="noreferrer"
                  className="text-base font-semibold leading-7 text-slate-200"
                >
                  How we do it <span aria-hidden="true">→</span>
                </a>
              </div>
            </div>
            <div className="flex justify-center items-start w-1/2">
              <div className="grow text-left">
                <Typing />
              </div>
            </div>
          </div>
          <div className="pointer-events-none	absolute inset-x-0 top-[calc(100%-13rem)] -z-10 transform-gpu overflow-hidden blur-3xl sm:top-[calc(100%-30rem)]">
            <svg
              className="relative left-[calc(50%+3rem)] h-[21.1875rem] max-w-none -translate-x-1/2 sm:left-[calc(50%+36rem)] sm:h-[42.375rem]"
              viewBox="0 0 1155 678"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                fill="url(#ecb5b0c9-546c-4772-8c71-4d3f06d544bc)"
                fillOpacity=".3"
                d="M317.219 518.975L203.852 678 0 438.341l317.219 80.634 204.172-286.402c1.307 132.337 45.083 346.658 209.733 145.248C936.936 126.058 882.053-94.234 1031.02 41.331c119.18 108.451 130.68 295.337 121.53 375.223L855 299l21.173 362.054-558.954-142.079z"
              />
              <defs>
                <linearGradient
                  id="ecb5b0c9-546c-4772-8c71-4d3f06d544bc"
                  x1="1155.49"
                  x2="-78.208"
                  y1=".177"
                  y2="474.645"
                  gradientUnits="userSpaceOnUse"
                >
                  <stop stopColor="#7f1d1d" />
                  <stop offset={1} stopColor="#b91c1c" />
                </linearGradient>
              </defs>
            </svg>
          </div>
        </div>
      </div>
    </div>
  );
};

export default LandingPage;
