# Playlist Preserver

## Description

Playlist Preserver is designed to safeguard your precious Spotify playlists by allowing you to back them up to disk. This ensures that even if Spotify faces issues or if data gets lost, your music collection remains safe with you.

## Alpha Release

The application is currently in its alpha state, focusing on core functionality. Users can:

- Retrieve their Spotify playlists.
- Download these playlists in a plain-text format.

For now the app can only be run locally (and I honestly do not have plans to have it hosted. However, Spotify makes it really easy to set this up. Future updates will aim to refine the user experience, introduce feedback during the downloading process, and implement comprehensive tests.

## Tech Stack

- **Languages**: Python, JavaScript, HTML5
- **Libraries/Frameworks**: Flask, Requests, Loguru
- **APIs**: Spotify API

## Planned Features

- **Automatic Backups**: Schedule backups at your convenience.
- **Cloud Uploads**: Option to automatically upload backups to cloud storage.
- **Multiple Formats**: Support for different file formats for backups.
- **Spotify Import**: Functionality to import playlists back into Spotify.

## Getting Started

1. Clone this repository to wherever you like
2. [Install Python](https://realpython.com/installing-python/) and use a [virtual environment](https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/) or, my preferred method, a [virtual enivornment](https://conda.io/projects/conda/en/latest/user-guide/getting-started.html) using [miniconda](https://docs.anaconda.com/free/miniconda/miniconda-install/).
3. Install the required packages using ```pip install -r requirements.txt```
4. In the main folder create a ```.env``` file, we will populate this with some required keys in a bit.
5. Go to https://developer.spotify.com/dashboard and create an app, name it whatever you want.
6. Go to the settings menu and copy both the Client ID and Client Secret and populate the ```.env`` file like so:
  ```
  CLIENT_ID = {YOUR_CLIENT_ID}
  CLIENT_SECRET = {YOU_CLIENT_SECRET}
  ```
7. While still in the settings menu we also want to change the redirect uri to ```http://localhost:5000/callback```; you can set this to any port you want but than you would have to change it in the config.py file yourself.
8. We also want to add another entry to our ```.env``` file called ```SECRET_KEY```. This really can be anything you like. Base64 encode some string, do some crazy hashing or just type your favorite animal. It is just something internal having to do with Flask, but since this is all local it is of no matter what this is.
9. Now in your preferred terminal, making sure you are in the correct environment simply type ```python run.py```, hit enter and Flask should start running locally and you should see an output like this:
 ```
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
```
Ctrl+click the url the Flask server is running on and it will direct you to your browser and open up the login page. Click on the login button and it will direct you to the OAuth page where you will have to approve the application. You will only have to do this once (in the settings menu on your account you can revoke access).
10. Once logged in you will be shown all your playlists and you will be able to download them by simply clicking on them. NOTE! This application is very much still in alpha stage and the downloading is clunky to say the least; you will be directed to a blank page which seemingly does nothing but in the backend it is looping through your playlist and downloading the information (Unfortunately Spotify limits the amount of tracks in a playlist shown to 50 per page). For small playlists, like one with only a hundred songs it will only be half a second but for a playlist of, let's say 2000 songs, this will take around 10 seconds. 

## Contributing

Playlist Preserver is in its early stages and is currently a personal project. However, contributions, ideas, and feedback are welcome. Feel free to fork the project, explore the code, and suggest improvements via pull requests.

## License

This project is licensed under the MIT License.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Project Status

The project is in alpha release. It's functional with core features implemented. Further developments, including UI/UX improvements and additional functionalities, are planned and will be integrated in future updates.

---

_This README is subject to change as Playlist Preserver evolves._
