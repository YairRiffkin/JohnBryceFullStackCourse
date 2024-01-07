"use strict";

console.log("hello");
let error = document.getElementById('passworderror');
let register_button = document.querySelector('#register input[type="submit"]')

function check_password() {    
    let password = document.getElementById("password");
    let password2 = document.getElementById("password2");
    if ( password.value == password2.value) {
        error.innerText = null;
        password2.removeAttribute("style");
        register_button.disabled = false;
    } else {
        error.innerText = "The Passwords are not the same";
        password2.style.backgroundColor = "Red";
        register_button.disabled = true;
    }
    
}

password2.addEventListener("input", check_password)