// // app/static/index.js
// document.addEventListener("DOMContentLoaded", function () {
//   // When the DOM is fully loaded, add event listeners or any other initialization logic here.

//   // Listen for form submission to show the loader
//   document.getElementById("comicForm").addEventListener("submit", function () {
//     document.getElementById("loader").style.display = "block"; // Show the loader
//   });
// });
// app/static/index.js

// Wait for the DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
    // Select the form and attach an event listener for the submit event
    var form = document.getElementById('comicForm');
    form.addEventListener('submit', function(event) {
        // Prevent the default form submission
        event.preventDefault();

        // Show the loader
        document.getElementById('loader').style.display = 'block';

        // Gather form data
        var formData = new FormData(form);

        // Send the form data using fetch API
        fetch('/', {
            method: 'POST',
            body: formData
        })
        .then(response => response.text())
        .then(html => {
            // Hide the loader
            document.getElementById('loader').style.display = 'none';

            // Replace the current page content with the new one
            document.open();
            document.write(html);
            document.close();
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });
});
