import os
from pathlib import Path
from mutagen.mp3 import MP3


def get_mp3_length(file_path):
    """Get the length of an MP3 file in seconds."""
    try:
        audio = MP3(file_path)
        return audio.info.length
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return 0


def format_time(seconds):
    """Format seconds into hours:minutes:seconds."""
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds = int(seconds % 60)

    if hours > 0:
        return f"{hours}:{minutes:02d}:{seconds:02d}"
    else:
        return f"{minutes}:{seconds:02d}"


def calculate_folder_mp3_length(folder_path):
    """Calculate the total length of all MP3 files in a folder."""
    total_seconds = 0
    mp3_files = {}

    # Walk through the directory
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith('.mp3'):
                file_path = os.path.join(root, file)
                duration = get_mp3_length(file_path)

                if duration > 0:
                    mp3_files[file[:file.find('.')]] = duration
                    total_seconds += duration

    # Sort files by duration
    order = Path('length_order.txt').read_text().strip().split('\n')
    ordered = []
    for o in order:
        ordered.append(mp3_files[o])
    out = []
    for duration in ordered:
        d = format_time(duration)
        line = f'<span style="font-family:arial; font-size: 20px;">{d}</span>'
        out.append(line)
    Path('lengths.txt').write_text('\n'.join(out))


if __name__ == "__main__":
    path = Path('/home/drupchen/Documents/Dilkhyen Transcriptions/TSIG SUM/Sessions/Final')
    calculate_folder_mp3_length(path)