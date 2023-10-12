function toggleMenu() {
    const sidebar = document.querySelector('.sidebar');
    sidebar.classList.toggle('active');
}

function expandSidebar() {
    const sidebar = document.querySelector('.sidebar');
    sidebar.classList.add('active');
}

function collapseSidebar() {
    const sidebar = document.querySelector('.sidebar');
    sidebar.classList.remove('active');
}

$(document).ready(function () {
    $('.dropdown-toggle').dropdown();
});
function toggleFormVisibility() {
    const formContainer = document.getElementById("customer-form-container");
    if (formContainer.style.display === "none") {
        formContainer.style.display = "block";
    } else {
        formContainer.style.display = "none";
    }
}