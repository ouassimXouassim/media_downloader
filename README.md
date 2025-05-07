# 🎵 Media Downloader CLI

A powerful and interactive command-line Python script to download **videos and audios** from YouTube, Spotify, and other supported platforms (TikTok, Facebook, Instagram, etc.).

> ✅ Supports playlist downloads, automatic duplicate detection, folder selection, and a clean UI using [Rich].

---

## 📦 Features

- ✅ **Download YouTube videos** (high quality, audio-only, playlists)
- ✅ **Download Spotify tracks and playlists** via `spotdl`
- ✅ **Download from other platforms** supported by `yt-dlp` (Facebook, TikTok, Instagram, etc.)
- ✅ Choose your **download folder**
- ✅ Skip files if they already exist
- ✅ Interactive, colorful CLI


🛠 Requirements
Make sure Python is installed, then run:
pip install yt-dlp spotdl rich
Debian/Ubuntu ===================================
sudo apt install ffmpeg
arch linux ======================================
sudo pacman -S ffmpeg
Usage: ==========================================
python media_downloader.py
=================================================
🎵 Media Downloader CLI
Choose a source to download from:
1. YouTube
2. Spotify
3. Exit
4. Other Platforms (TikTok, Facebook, etc.)
=================================================
🌐 Supported Platforms
Thanks to yt-dlp, you can download from:
YouTube
Facebook
Instagram
TikTok
SoundCloud
Twitter/X
Vimeo
Dailymotion
Reddit
and hundreds more
======================================================
📁 Output Format
Files are saved in:
php-template
<your-selected-folder>/<title>.<ext>
Playlists will be saved in subfolders named after the playlist.

