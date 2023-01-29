import React, { useRef, useEffect } from "react";
import Typed from "typed.js";
// import { useState } from 'react';

const Output = (props) => {
  const typeTarget = useRef(null);

  useEffect(() => {
    const typed = new Typed(typeTarget.current, {
      strings: [props.para],
      typeSpeed: 20,
      showCursor: false,
      loop: false
    });

    return () => {
      typed.destroy();
    };
  }, [props.para]);

  return <span className="text-slate-200 text-lg" ref={typeTarget} />;
};

export default Output;