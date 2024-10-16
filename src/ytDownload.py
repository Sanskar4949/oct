import tkinter as tk
from tkinter import messagebox, filedialog, ttk
from yt_dlp import YoutubeDL
import os
import threading
def download_video():
    url = url_entry.get()
    if not url:
        messagebox.showerror("Error", "Please enter a YouTube URL")
        return
    save_path = filedialog.askdirectory()
    if not save_path:
        return
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': f'{save_path}/%(title)s.%(ext)s',
    }
    progress_bar = ttk.Progressbar(root, orient="horizontal", length=200, mode="indeterminate")
    progress_bar.pack(pady=10)
    progress_bar.start()
    status_label = tk.Label(root, text="Downloading...", font=("Arial", 12), bg="#f0f0f0")
    status_label.pack(pady=10)
    def download_video_thread():
        try:
            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            status_label.config(text="Download complete!")
            progress_bar.stop()
        except Exception as e:
            status_label.config(text=f"Error: {str(e)}")
            progress_bar.stop()


    download_thread = threading.Thread(target=download_video_thread)
    download_thread.start()
root = tk.Tk()
root.title("YouTube Downloader")
current_dir = os.path.dirname(_file_)
icon_path = os.path.join(current_dir, 'youtube.ico')
root.iconbitmap(icon_path)
root.resizable(False, False)  
style = ttk.Style()
style.configure('TButton', font=('Arial', 12), padding=10, relief='flat')
style.map('TButton', 
          background=[('active', '#4CAF50'), ('!active', '#4CAF50')],
          foreground=[('active', '#ffffff'), ('!active', '#ffffff')])
style.configure('Round.TButton', borderwidth=1, relief="solid", anchor="center")
style.map('Round.TButton',
          background=[('pressed', '!disabled', '#4CAF50'), ('active', '#4CAF50')],
          foreground=[('pressed', '#ffffff'), ('active', '#ffffff')],
          highlightcolor=[('focus', '#ffffff'), ('!focus', '#ffffff')],
          highlightbackground=[('focus', '#4CAF50'), ('!focus', '#4CAF50')])
header_frame = tk.Frame(root, bg="#212121")
header_frame.pack(fill="x")
header_label = tk.Label(header_frame, text="YouTube Downloader", font=("Arial", 18, "bold"), bg="#212121", fg="#ffffff")
header_label.pack(pady=10)
main_frame = tk.Frame(root, bg="#f0f0f0")
main_frame.pack(padx=20, pady=20)
url_label = tk.Label(main_frame, text="Enter YouTube URL:", font=("Arial", 12), bg="#f0f0f0")
url_label.pack()
url_entry = tk.Entry(main_frame, width=50, font=("Arial", 12))
url_entry.pack(pady=10)
download_button = ttk.Button(main_frame, text="Download", command=download_video, style='Round.TButton')
download_button.pack(pady=10)
footer_frame = tk.Frame(root, bg="#212121")
footer_frame.pack(fill="x")
footer_label = tk.Label(footer_frame, text="", font=("Arial", 12), bg="#212121", fg="#ffffff")
footer_label.pack(pady=5)
root.mainloop()