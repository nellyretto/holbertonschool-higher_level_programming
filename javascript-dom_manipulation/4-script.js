const button = document.getElementById("add_item");
const ul = document.querySelector('ul');
button.addEventListener("click", function() {
    const li = document.createElement("li");
    li.appendChild(document.createTextNode("Item"));
    ul.appendChild(li);
});