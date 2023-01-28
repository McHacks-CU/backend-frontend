import './App.css';
// import ReactDOM from "react-dom/client";
// import { BrowserRouter, Routes, Route } from "react-router-dom";
import LandingPage from './pages/LandingPage';
import Form from './pages/Form';

// function App() {
//   return (
//     <BrowserRouter>
//       <Routes>
//         <Route path="/" element={<Layout />}>
//           <Route index element ={<LandingPage />} />
//           <Route path="getstarted" element={<GetStarted />} />
//         </Route>
//       </Routes>
//     </BrowserRouter>
//   );
// }
// export default App;
function App() {
  return (
    <>
      <LandingPage />
      <Form />
    </>
  );
}

export default App;
// import React, { useState, useEffect } from 'react';
// import './App.css';

// function App() {
//   const [currentTime, setCurrentTime] = useState(0);

//   useEffect(() => {
//     fetch('/time').then(res => res.json()).then(data => {
//       setCurrentTime(data.time);
//     });
//   }, []);

//   return (
//     <div className="App">
//       <header className="App-header">

//         ... no changes in this part ...

//         <p>The current time is {currentTime}.</p>
//       </header>
//     </div>
//   );
// }
// 
// export default App;
