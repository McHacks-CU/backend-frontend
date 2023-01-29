import React, { useRef, useEffect } from "react";
import Typed from "typed.js";

const Typing = () => {
  const typeTarget = useRef(null);

  useEffect(() => {
    const typed = new Typed(typeTarget.current, {
      strings: [
        "Preventing injections before they occur",
        "'SELECT * FROM users WHERE username = ? AND password = ?', [username, password]",
      ],
      typeSpeed: 40,
      showCursor: false,
      loop: true,
    });

    return () => {
      typed.destroy();
    };
  }, []);

  return <span className="text-white text-3xl" ref={typeTarget} />;
};

export default Typing;
