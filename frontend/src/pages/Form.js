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
const Form =() => {
  return (
    <div id="form" className="h-screen bg-gray-800 flex flex-row">
          <div className="mt-5 md:col-span-2 md:mt-0 flex-auto">
            <form action="#" method="POST">
              <div className="shadow sm:overflow-hidden sm:rounded-md">
                <div className="space-y-6 bg-gray-800 px-4 py-5 sm:p-6">
                  <div>
                    <label htmlFor="about" className="block text-sm font-medium text-gray-700">
                    </label>
                    <div className="mt-1">
                      <textarea
                        id="about"
                        name="about"
                        rows={20}
                        className="mt-1 block w-full rounded-md bg-gray-600 border-indigo-400 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm text-slate-200"
                        placeholder="Paste here"
                        defaultValue={''}
                      />
                    </div>
                    <p className="mt-2 text-sm text-gray-500">
                    </p>
                  </div>

                  
                  
                </div>
                <div className="bg-gray-800 px-4 py-3 text-right sm:px-6">
                  <button
                    type="submit"
                    className="inline-flex justify-center rounded-md border border-transparent bg-indigo-600 py-2 px-4 text-sm font-medium text-white shadow-sm hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2"
                  >
                    Analyze
                  </button>
                </div>
              </div>
            </form>
          </div>
          <div className="flex-auto">
            Response
          </div>
    </div>
  )
};

export default Form;