import React, { useRef, useEffect } from "react";
import Typed from "typed.js";
// import { useState } from 'react';

const Output = (props) => {
  const typeTarget = useRef(null);

  useEffect(() => {
    const typed = new Typed(typeTarget.current, {
      strings: [props.para],
      typeSpeed: 40,
      showCursor: false,
      loop: true
    });

    return () => {
      typed.destroy();
    };
  }, []);

  return <span className="text-white text-3xl" ref={typeTarget} />;
};

export default Output;