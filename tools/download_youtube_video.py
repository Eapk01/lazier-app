import yt_dlp
from tkinter import filedialog, Tk, messagebox, simpledialog
import threading

def run_in_thread():

    root = Tk()
    root.withdraw()

    try:
        # Ask for the YouTube video URL
        url = simpledialog.askstring("YouTube URL", "Enter the YouTube video URL:")
        if not url:
            return  # User canceled

        # Ask for the output location to save the file
        output_path = filedialog.askdirectory(title="Select output directory")
        if not output_path:
            return  # User canceled

        def download_video():
            try:
                ydl_opts = {
                    'format': 'bestvideo+bestaudio/best',  # Get best video and audio quality
                    'outtmpl': f"{output_path}/%(title)s.%(ext)s",  # Save as: video_title.mp4
                    'postprocessors': [{
                        'key': 'FFmpegVideoConvertor',
                        'preferedformat': 'mp4',  # Convert to mp4 format
                    }],
                }

                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])

                messagebox.showinfo("Success", "Video downloaded successfully.")

            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")

        # Start the download in a separate thread
        download_thread = threading.Thread(target=download_video)
        download_thread.start()

    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")
    finally:
        root.destroy()