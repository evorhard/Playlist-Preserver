# Playlist Preserver

## Current State

In it's current state the application is able to retrieve the user's playlists and download the playlists to disk. What still needs to be implemented is feedback for the downloading (it has to loop through calls because of the API limit) and so it just now shows a blank tab. Proper tests need to be written afterwards. As soon as this is done I will update the [Getting Started](#getting-started) section to explain how to get the initial program to run.

## Description

This little application was born out of the idea that I might one day lose all my music collection if, for some reason, Spotify went under. Or their backups did not get everything. So this application will allow you to backup your playlists.

## Tech Stack

- **Languages**: Python, JavaScript, Ajax, HTML5
- **Libraries**: Flask, Loguru, Requests, URLLib, Celery
- **APIs**: Spotify API

## Planned Features

- **Automatic Backups**: Periodic backups set to the time you want.
- **Automatic Upload of Backups**: Automatically upload your playlists to some cloud hosting.
- **Different Formats**: For now the output will be a plain-text list of your songs in a clean format.
- **Spotify Import**: A way for you to import these lists back into Spotify.

## Getting Started

_This section will be updated with installation, configuration, and usage instructions as the project develops._

## Contributing

While Disc List Scout is currently a personal project, I may consider opening it up for contributions in the future. Feel free to fork the project and experiment on your own. Any major changes proposed can be discussed through pull requests.

## License

This project is licensed under the MIT License.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Acknowledgments

Inspiration for this project comes from the vast and diverse music communities on platforms like Discogs and RateYourMusic.

## Project Status

The project is in its initial stages of development. Regular updates will be pushed to this repository as progress is made.

---

_This README is subject to change as Playlist Preserver evolves._
