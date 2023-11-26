// Wait for the DOM to be fully loaded
document.addEventListener("DOMContentLoaded", function () {
  // Select the form and attach an event listener for the submit event
  var form = document.getElementById("comicForm");
  form.addEventListener("submit", function (event) {
    // Prevent the default form submission
    event.preventDefault();

    // Show the loader
    document.getElementById("loader").style.display = "block";

    // Gather form data
    var formData = new FormData(form);

    // Send the form data using fetch API
    fetch("/", {
      method: "POST",
      body: formData,
    })
      .then((response) => response.json())
      .then((data) => {
        // Hide the loader
        document.getElementById("loader").style.display = "none";

        const comicStripContainer = document.getElementById(
          "comic-strip-container"
        );
        comicStripContainer.innerHTML = "";

        // Check if data.image_data exists and is an array
        if (data.image_data && Array.isArray(data.image_data)) {
          // Append new images
          data.image_data.forEach((imageSrc) => {
            const img = new Image();
            img.src = imageSrc;
            img.classList.add("comic-img", "img-thumbnail");
            comicStripContainer.appendChild(img);
          });
        } else {
          // Handle the case where image_data is not as expected
          console.error("Received data is not in the expected format:", data);
          comicStripContainer.innerHTML =
            "<p>There was an error processing your request.</p>";
        }
      })
      .catch((error) => {
        console.error("Error:", error);
        document.getElementById("loader").style.display = "none";
        document.getElementById("comic-strip-container").innerHTML =
          "<p>There was an error processing your request.</p>";
      });
  });
});
