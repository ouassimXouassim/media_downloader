#!/usr/bin/env python3
# Created by: https://github.com/ouassimXouassim/

import os
import subprocess
from pathlib import Path
from rich.console import Console
from rich.prompt import Prompt, IntPrompt
from rich.panel import Panel
from rich import print
import sys

console = Console()
default_output_path = None


def ask_output_path():
    global default_output_path
    if default_output_path:
        return default_output_path

    folder = Prompt.ask("📁 Enter download folder (default is current directory)", default=".")
    path = Path(folder).resolve()
    path.mkdir(parents=True, exist_ok=True)
    default_output_path = path
    return path


def check_duplicate(output_path: Path, title: str, extensions: list[str]) -> bool:
    for ext in extensions:
        file_path = output_path / f"{title}.{ext}"
        if file_path.exists():
            console.print(f"[yellow]⚠️ Skipped: [bold]{file_path.name}[/bold] already exists.[/yellow]")
            return True
    return False


def youtube_menu():
    console.print(Panel.fit("[bold cyan]YouTube Download Options[/bold cyan]"))
    console.print("1. 🎬 High Quality Video")
    console.print("2. 🎧 Audio Only (MP3)")
    console.print("3. 📂 Playlist (Video or Audio)")
    return IntPrompt.ask("Choose an option", choices=["1", "2", "3"])


def download_youtube():
    option = youtube_menu()
    url = Prompt.ask("🔗 Enter YouTube URL")
    output_dir = ask_output_path()

    if option == 1:
        cmd = [
            "yt-dlp", "-f", "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best",
            "-o", str(output_dir / "%(title)s.%(ext)s"),
            url
        ]
        check_ext = ["mp4", "mkv", "webm"]

    elif option == 2:
        cmd = [
            "yt-dlp", "-x", "--audio-format", "mp3",
            "-o", str(output_dir / "%(title)s.%(ext)s"),
            url
        ]
        check_ext = ["mp3", "m4a", "webm"]

    elif option == 3:
        list_type = IntPrompt.ask("Download as 1) Video or 2) Audio", choices=["1", "2"])
        if list_type == 1:
            cmd = [
                "yt-dlp", "-f", "bestvideo+bestaudio/best",
                "-o", str(output_dir / "%(playlist)s/%(title)s.%(ext)s"),
                url
            ]
            check_ext = ["mp4", "mkv", "webm"]
        else:
            cmd = [
                "yt-dlp", "-x", "--audio-format", "mp3",
                "-o", str(output_dir / "%(playlist)s/%(title)s.%(ext)s"),
                url
            ]
            check_ext = ["mp3", "m4a", "webm"]
    else:
        console.print("[red]❌ Invalid option[/red]")
        return

    try:
        title = subprocess.check_output(["yt-dlp", "--get-title", url], text=True).strip()
        if check_duplicate(output_dir, title, check_ext):
            return
    except subprocess.CalledProcessError:
        console.print("[red]❌ Failed to fetch video title. Skipping duplicate check.[/red]")

    run_command(cmd)


def download_spotify():
    url = Prompt.ask("🎵 Enter Spotify track or playlist URL")
    output_dir = ask_output_path()

    cmd = ["spotdl", url, "--output", str(output_dir)]
    run_command(cmd)


def download_other_sites():
    url = Prompt.ask("🌐 Enter URL from supported platform (TikTok, Facebook, etc.)")
    output_dir = ask_output_path()

    console.print("1. 📹 Video (Best Quality)")
    console.print("2. 🎶 Audio Only (MP3)")
    option = IntPrompt.ask("Choose download type", choices=["1", "2"])

    try:
        title = subprocess.check_output(["yt-dlp", "--get-title", url], text=True).strip()
        check_ext = ["mp4", "mkv", "webm"] if option == 1 else ["mp3", "m4a", "webm"]
        if check_duplicate(output_dir, title, check_ext):
            return
    except subprocess.CalledProcessError:
        console.print("[red]❌ Failed to fetch title. Skipping duplicate check.[/red]")

    if option == 1:
        cmd = ["yt-dlp", "-f", "best", "-o", str(output_dir / "%(title)s.%(ext)s"), url]
    else:
        cmd = ["yt-dlp", "-x", "--audio-format", "mp3", "-o", str(output_dir / "%(title)s.%(ext)s"), url]

    run_command(cmd)


def run_command(cmd):
    console.print(f"[dim]🛠️ Executing:[/dim] {' '.join(cmd)}")
    try:
        subprocess.run(cmd, check=True)
        console.print("[green]✅ Download complete[/green]")
    except subprocess.CalledProcessError as e:
        console.print(f"[red]❌ Error occurred: {e}[/red]")


def main_menu():
    console.print(Panel("[bold green]🎵 Media Downloader CLI[/bold green]\nCreated by: [blue]https://github.com/ouassimXouassim[/blue]\n\nChoose a source to download from:"))
    console.print("1. YouTube")
    console.print("2. Spotify")
    console.print("3. Exit")
    console.print("4. Other Platforms (TikTok, Facebook, etc.)")
    return IntPrompt.ask("Your choice", choices=["1", "2", "3", "4"])


def main():
    while True:
        try:
            choice = main_menu()
            if choice == 1:
                download_youtube()
            elif choice == 2:
                download_spotify()
            elif choice == 3:
                console.print("[cyan]👋 Goodbye![/cyan]")
                break
            elif choice == 4:
                download_other_sites()
        except KeyboardInterrupt:
            console.print("\n[red]❌ Interrupted by user.[/red]")
            sys.exit(1)


if __name__ == "__main__":
    main()
