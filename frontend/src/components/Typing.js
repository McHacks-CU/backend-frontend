import React, { useRef, useEffect } from "react";
import Typed from "typed.js";

const Typing = () => {

  const typeTarget = useRef(null);

  useEffect(() => {
    const typed = new Typed(typeTarget.current, {
      strings: ["SELECT * FROM users WHERE username = '' OR '1'='1' AND password = 'whatever the password is';"],
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

export default Typing;