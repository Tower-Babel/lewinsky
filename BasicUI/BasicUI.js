document.addEventListener('DOMContentLoaded', function() {

    /* Dark Mode Toggle */
    function toggleDarkMode() {
        const body = document.body;
        body.classList.toggle('dark-mode');
    }

    /* Event listener button for Dark Mode Toggle */
    document.getElementById('dark-mode-toggle').addEventListener('click', function () {
        const body = document.body;

        if (body.style.backgroundColor === "white") {
            body.style.backgroundColor = "black";
            body.style.color = "white";
        } else {
            body.style.backgroundColor = "white";
            body.style.color = "black";
        }
    });

}); // end