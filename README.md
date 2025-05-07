# Media Downloader CLI

A powerful, interactive command-line tool to download videos and audios from YouTube, Spotify, TikTok, Facebook, and other platforms. Built with Python and enriched with a colorful terminal interface.

## Created by

[ouassimXouassim](https://github.com/ouassimXouassim)

---

## Features

* 📥 Download high-quality video or audio from YouTube.
* 🎵 Download Spotify tracks and playlists.
* 🌐 Support for other platforms (TikTok, Facebook, etc.).
* 🗂 Choose your download folder interactively.
* 🧠 Automatically detects existing files to avoid duplicates.
* 🎛 User-friendly command-line interface using `rich` library.

---

## Requirements

Make sure you have the following installed:

* Python 3.9+
* `yt-dlp` (for video/audio downloading)
* `spotdl` (for Spotify support)
* `rich` (for terminal UI)

You can install required Python dependencies with:

```bash
pip install rich
```

And install external tools:

```bash
pip install yt-dlp spotdl
```

---

## Usage

### 1. Run the Script

```bash
python downloader.py
```

### 2. Choose a Source

You'll be prompted with options like:

* YouTube
* Spotify
* Other platforms (TikTok, Facebook...)

### 3. Paste a URL

Paste the video or playlist URL when asked.

### 4. Select Output Folder

Choose the folder where files will be saved.

### 5. Duplicate Detection

If a file with the same name and format already exists, it will be skipped.

---

## Example

```bash
$ python downloader.py
🎵 Media Downloader CLI
Choose a source to download from:
1. YouTube
2. Spotify
3. Exit
4. Other Platforms (TikTok, Facebook, etc.)

> 1
Enter YouTube URL: https://www.youtube.com/watch?v=dQw4w9WgXcQ
Choose download type: Video or Audio
...
```

---

## License

This project is licensed under the MIT License.

---

## Contributions

Feel free to fork and improve this tool. Pull requests are welcome!
