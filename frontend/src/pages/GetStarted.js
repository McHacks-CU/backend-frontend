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
  }
  ```
*/
const GetStarted =() => {
  return (
    <div className="h-screen bg-gray-800 flex flex-col justify-center">
          <div className="mt-5 md:col-span-2 md:mt-0">
            <form action="/form" method="POST">
              <div className="shadow sm:overflow-hidden sm:rounded-md">
                <div className="space-y-6 bg-gray-800 px-4 py-5 sm:p-6">
                  

                  <div>
                    <label htmlFor="code" className="block text-sm font-medium text-gray-700">
                    </label>
                    <div className="mt-1">
                      <textarea
                        id="code"
                        name="code"
                        rows={20}
                        className="mt-1 block w-full rounded-md bg-gray-600 border-indigo-400 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
                        placeholder="Paste here"
                        defaultValue={''}
                      />
                    </div>
                  </div>

                  
                  
                </div>
                <div className="bg-gray-800 px-4 py-3 text-right sm:px-6">
                  <button
                    type="submit"
                    className="inline-flex justify-center rounded-md border border-transparent bg-indigo-600 py-2 px-4 text-sm font-medium text-white shadow-sm hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2"
                  >
                    Save
                  </button>
                </div>
              </div>
            </form>
          </div>
    </div>
  )
};

export default GetStarted;