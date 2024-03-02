document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll("a.playlist-download").forEach(function (link) {
    link.addEventListener("click", function (e) {
      e.preventDefault(); // Prevent the default link behavior
      const playlistUrl = this.getAttribute("href");
      // Show a custom message or modal to the user
      alert("Your download will start shortly.");
      // Start the download
      window.open(playlistUrl, "_blank");
    });
  });
});
