document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll("a.playlist-download").forEach(function (link) {
    link.addEventListener("click", function (e) {
      e.preventDefault(); // Prevent the default link behavior
      const playlistUrl = this.getAttribute("href");
      // Show a custom message or modal to the user
      alert(
        'Your download will start after pressing the "OK" button. You will be directed to a new tab.\nNote: for very large playlist this download can take a long time.\nSpotify limits playlist API calls to 50 items and there is built in measures to not make to many requests.'
      );
      // Start the download
      window.open(playlistUrl, "_blank");
    });
  });
});
