import os
from pathlib import Path
import yt_dlp

def download_and_organize():
    # 1. Pathlib se folder handling
    base_path = Path.cwd() / "downloads"
    video_path = base_path / "Videos"
    audio_path = base_path / "Audios"

    # Folder exist nahi karta to bana do
    video_path.mkdir(parents=True, exist_ok=True)
    audio_path.mkdir(parents=True, exist_ok=True)

    print(f"Files yahan save honge: {base_path}")

    # 2. User se input
    url = input("\nYouTube Video ka URL daal: ").strip()
    print("\n1. Video (Best Quality)\n2. Audio Only (mp3)")
    choice = input("Kya download karna hai? (1/2): ")

    try:
        # 3. yt-dlp options set karna
        if choice == "2":
            # Audio ke liye
            ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': str(audio_path / '%(title)s.%(ext)s'),
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            }
            print("\nAudio download ho raha hai...")
        else:
            # Video ke liye
            ydl_opts = {
                'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
                'outtmpl': str(video_path / '%(title)s.%(ext)s'),
            }
            print("\nVideo download ho raha hai...")

        # 4. Download
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            file_name = ydl.prepare_filename(info)
            print(f"\nHo gaya! Downloaded: {info['title']}")

        # 5. os se File Organizer ka demo
        print("\n--- File Organizer Status ---")
        for folder in [video_path, audio_path]:
            files = os.listdir(folder)
            print(f"{folder.name} folder me {len(files)} files hain:")
            for f in files:
                # pathlib se size nikalna
                file_path = folder / f
                size_mb = file_path.stat().st_size / (1024*1024)
                print(f"  - {f} ({size_mb:.2f} MB)")

    except Exception as e:
        print(f"\nError aaya: {e}")
        print("URL sahi hai kya check kar le.")

if __name__ == "__main__":
    download_and_organize()