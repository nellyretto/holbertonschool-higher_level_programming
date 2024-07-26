const button = document.getElementById("update_header"),
content = document.querySelector("header");

button.onclick = function () {
    content.innerHTML = "New Header!!!";
}