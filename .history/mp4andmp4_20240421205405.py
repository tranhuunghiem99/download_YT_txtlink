from pytube import YouTube
from moviepy.editor import AudioFileClip

def download_video_and_convert_to_audio(url):
    # Tải video
    youtube = YouTube(url)
    video = youtube.streams.get_highest_resolution()
    video.download('./video')  # Thay 'path_to_save_video' bằng đường dẫn thực tế trên máy của bạn

    # Chuyển đổi video thành file âm thanh
    video_clip = AudioFileClip('./video/' + video.default_filename)
    audio_clip = video_clip.audio
    audio_clip.write_audiofile('.//audio.mp3')  # Thay 'path_to_save_audio/audio.mp3' bằng đường dẫn thực tế trên máy của bạn

# Sử dụng hàm
download_video_and_convert_to_audio('your_youtube_url')  # Thay 'your_youtube_url' bằng URL video YouTube thực tế của bạn
