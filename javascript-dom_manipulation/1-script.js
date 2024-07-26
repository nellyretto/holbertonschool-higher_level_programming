const button = document.getElementById("red_header");
button.addEventListener("click",
    () => {
        document.querySelector("header").style.color = "#FF0000";
    });