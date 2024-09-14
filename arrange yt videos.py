import os
from pytube import Playlist
import difflib
import re


def get_video_files(directory):
    """Get a list of video files in the specified directory."""
    video_extensions = (".mp4", ".mkv", ".avi", ".mov", ".flv", ".wmv")
    return [f for f in os.listdir(directory) if f.endswith(video_extensions)]


def fetch_playlist_order(playlist_url):
    """Fetch the video titles in the order they appear in the YouTube playlist."""
    playlist = Playlist(playlist_url)
    return [video.title for video in playlist.videos]


def find_closest_match(title, video_files):
    """Find the closest matching file name for a given title."""
    return difflib.get_close_matches(title, video_files, n=1, cutoff=0.4)


def sanitize_filename(filename):
    """Sanitize the filename to remove illegal characters for Windows."""
    sanitized_filename = re.sub(r'[<>:"/\\|?*]', "", filename)
    return sanitized_filename


def rename_files_in_order(directory, playlist_titles):
    """Rename local video files to match the playlist order."""
    video_files = get_video_files(directory)

    if len(video_files) != len(playlist_titles):
        print(
            "The number of local videos does not match the number of videos in the playlist."
        )
        # return

    for i, title in enumerate(playlist_titles, 1):
        closest_match = find_closest_match(title, video_files)
        if closest_match:
            matching_file = closest_match[0]
            extension = os.path.splitext(matching_file)[1]
            sanitized_title = sanitize_filename(title)
            new_name = f"{i:02d} - {sanitized_title}{extension}"
            original_path = os.path.join(directory, matching_file)
            new_path = os.path.join(directory, new_name)
            os.rename(original_path, new_path)
            print(f"Renamed '{matching_file[:20]}")
            video_files.remove(
                matching_file
            )  # Remove the file from the list to avoid duplicates
        else:
            print(f"No matching file found for '{title}' in local directory.")


if __name__ == "__main__":
    # Specify the directory containing the local video files
    directory = "trial"

    # Specify the YouTube playlist URL
    playlist_url = "https://youtube.com/playlist?list=PLDV1Zeh2NRsDGO4--qE8yH72HFL1Km93P&si=y0ywQfJFkCl3AGkR"

    # Fetch the playlist order
    playlist_titles = fetch_playlist_order(playlist_url)

    # Rename local files to match the playlist order
    rename_files_in_order(directory, playlist_titles)
