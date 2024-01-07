function add_excitement() {
    element = document.getElementsByTagName("h1");
    len = element.length;
    for (i = 0; i < len; i++) {
        for (n = 0; n < 10; n++) {
            console.log("Q");
            element[i].innerText = element[i].innerText + "Q";
        }}
}

// add_excitement()
document.getElementById("mybutton").addEventListener("click", add_excitement)

