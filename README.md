<div align="center">

<img src="ui/logo.png" alt="KRONOS 4K Desktop" width="90" />

# KRONOS 4K — Desktop Application

**A high-performance standalone Windows desktop application for downloading YouTube videos in crystal-clear 4K UHD 60FPS and studio-grade 320kbps audio.**

[![Platform](https://img.shields.io/badge/Platform-Windows%2010%20%2F%2011-0078D6.svg?style=for-the-badge&logo=windows&logoColor=white)](https://microsoft.com)
[![Python](https://img.shields.io/badge/Python-3.11-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![pywebview](https://img.shields.io/badge/pywebview-5.x-teal.svg?style=for-the-badge)](https://pywebview.app)
[![FFmpeg](https://img.shields.io/badge/FFmpeg-8.1%20Embedded-green.svg?style=for-the-badge&logo=ffmpeg&logoColor=white)](https://ffmpeg.org)
[![License](https://img.shields.io/badge/License-MIT-lightgrey.svg?style=for-the-badge)](LICENSE)

[Features](#-features) • [Download EXE](#-download-standalone-exe) • [Running from Source](#-running-from-source) • [Building the EXE](#-building-the-standalone-exe) • [Author](#-author)

</div>

---

## ✨ Features

- 🚀 **Zero-Dependency Standalone**: Pre-packaged single `.exe` — runs instantly without requiring Python, Node.js, or FFmpeg to be installed on the machine.
- 🎬 **Ultra HD 4K Support**: Download videos up to **2160p @ 60FPS**, **1440p QHD**, **1080p FHD**, **720p**, and more.
- 🎵 **Studio-Grade Audio**: Extract pure **MP3 (320kbps & 192kbps)**, original **M4A AAC**, and lossless **WAV** with embedded ID3 tags.
- ⏸️ **Full Download Controls**: Live **Pause**, **Resume**, and **Stop** controls during downloads.
- ⚡ **1-Click Engine Updates**: Check and update the underlying `yt-dlp` extraction engine in-app without reinstalling.
- 🔑 **In-App YouTube Login & Cookie Sync**: Easily bypass age gates and download restricted content by signing in directly or syncing browser cookies (Chrome, Firefox, Edge, Brave).
- 📁 **Native Folder Picker**: Select custom save destinations on your PC with a single click.
- 🎨 **Obsidian Glassmorphism UI**: Frameless sleek dark-mode desktop interface with real-time speed, size, and ETA metrics.

---

## 📦 Download Standalone EXE

Get the pre-built, ready-to-use executable from GitHub Releases:

👉 **[Download Latest Kronos4K.exe](https://github.com/Bl4ke100/Kronos4k-Desktop--YT-Downloader/releases)**

*(Just double-click to launch — no installation required!)*

---

## 🛠️ Running from Source (Development Mode)

If you'd like to develop or run directly from Python:

### 1. Install Dependencies
```bash
pip install yt-dlp pywebview pythonnet curl_cffi pycryptodome mutagen
```

### 2. Launch App
Double-click **`run_desktop.bat`** or execute:
```bash
python main.py
```

---

## 🔨 Building the Standalone EXE

To package the desktop application into a single portable `.exe`:

1. Ensure **`ffmpeg.exe`** is present in the root folder.
2. Double-click **`build_exe.bat`** or run:
```bash
python build_exe.py
```
3. Your single self-contained binary will be created at:
```text
dist/Kronos4K.exe
```

---

## 📁 Project Layout

```text
Kronos4K-Desktop/
├── ui/                  # Obsidian UI interface (HTML5, CSS3, JavaScript)
│   ├── index.html
│   ├── style.css
│   └── app.js
├── pot_provider/        # Background Proof-of-Origin token generator
├── downloader_core.py   # Multi-threaded download manager & yt-dlp wrapper
├── engine_updater.py    # 1-Click in-app engine updater
├── main.py              # pywebview desktop application window & API bridge
├── build_exe.py         # PyInstaller multi-layer compilation script
├── build_exe.bat        # 1-click build batch runner
└── run_desktop.bat      # 1-click dev launcher
```

---

## 👤 Author

**Bl4ke100**
- GitHub: [@Bl4ke100](https://github.com/Bl4ke100)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
