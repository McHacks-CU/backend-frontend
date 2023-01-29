/*
  This example requires some changes to your config:
  
  ```
  // tailwind.config.js
  module.exports = {
    // ...
    plugins: [
      // ...
      require('@tailwindcss/forms'),
    ],
  };
  ```
*/
import { useState } from "react";
import "../components/type.css";
import Output from '../components/Output';

const Form = () => {
  const [output, setOutput] = useState("");
  // code into form
  // form data is sent when submit button clicked
  // return message to be inserted into html
  function onSubmit(event) {
    setOutput("");
    event.currentTarget.elements.submit.innerHTML = "Sending...";
    event.preventDefault();
    console.log(event.currentTarget.elements.usernameInput.value);
    var data = event.currentTarget.elements.usernameInput.value;
    console.log(data);
    fetch("/form", {
      method: "POST",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        text: data,
      }),
    })
      .then((response) => response.json())
      .then((data) => setOutput(data.result));
    event.currentTarget.elements.submit.innerHTML = "Send";
  }

  return (
    <div id="form" className="h-screen w-full bg-neutral-800 flex flex-row">
      <div className="mt-5 md:col-span-2 md:mt-0 w-3/4">
        <form action="" onSubmit={onSubmit} method="POST">
          <div className="shadow sm:overflow-hidden sm:rounded-md">
            <div className="space-y-6 px-4 py-5 sm:p-6">
              <div>
                <label
                  htmlFor="code"
                  className="block text-sm font-medium text-gray-700"
                ></label>
                <div className="mt-1">
                  {/* <textarea
                        id="code"
                        name="code"
                        rows={20}
                        className="mt-1 block w-full rounded-md bg-gray-600 border-indigo-400 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm text-slate-200"
                        placeholder="Paste here"
                        defaultValue={''}
                      /> */}
                  <label htmlFor="usernameInput" className="text-slate-200">
                    Input
                  </label>
                  <textarea
                    id="usernameInput"
                    rows={20}
                    defaultValue={""}
                    placeholder="Paste code here"
                    className="mt-1 block w-full rounded-md bg-neutral-800 border-slate-200 shadow-sm focus:border-red-300 focus:ring-red-300 sm:text-sm text-slate-200"
                    type="text"
                  />
                </div>
              </div>
            </div>
            <div className="px-4 py-3 text-right sm:px-6">
              <button
                type="submit"
                id="submit"
                className="inline-flex justify-center rounded-md border border-transparent bg-red-600 py-2 px-4 text-sm font-medium text-white shadow-sm hover:bg-red-500 focus:outline-none focus:ring-2 focus:ring-red-500 focus:ring-offset-2"
                >Send
              </button>
            </div>
          </div>
        </form>
      </div>
      <div className="text-white mt-5 md:col-span-2 md:mt-0 w-1/4">
        <div className="space-y-6 px-4 py-5 sm:p-6 flex flex-col break-words">
          <div>Response</div>
          {/* <div key={Math.random()} className="">
            {output.replace(/"([^"]+)":/g, "$1:")}
          </div> */}
          <Output key={Math.random()} para={output.replace(/"([^"]+)":/g, "$1:")}/>
        </div>
      </div>
    </div>
  );
};

export default Form;
