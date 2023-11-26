// app/static/index.js
document.addEventListener("DOMContentLoaded", function () {
  // When the DOM is fully loaded, add event listeners or any other initialization logic here.

  // Listen for form submission to show the loader
  document.getElementById("comicForm").addEventListener("submit", function () {
    document.getElementById("loader").style.display = "block"; // Show the loader
  });
});
