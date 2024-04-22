from pytube import YouTube
from moviepy.editor import AudioFileClip

def download_video_and_convert_to_audio(url):
    try:
        # Tải video
        youtube = YouTube(url)
        video = youtube.streams.get_highest_resolution()
        video.download('./video')  # Thay 'path_to_save_video' bằng đường dẫn thực tế trên máy của bạn

        # Chuyển đổi video thành file âm thanh
        video_clip = AudioFileClip('./' + video.default_filename)
        audio_clip = video_clip.audio
        audio_clip.write_audiofile('path_to_save_audio/audio.mp3')  # Thay 'path_to_save_audio/audio.mp3' bằng đường dẫn thực tế trên máy của bạn

        return True
    except Exception as e:
        print(f"Không thể tải video từ url: {url}. Lỗi: {str(e)}")
        return False

# Danh sách các URL video YouTube
youtube_urls = ['url1', 'url2', 'url3', 'url4', 'url5']  # Thay 'url1', 'url2', ... bằng các URL video YouTube thực tế của bạn

# Tải và đếm số lượng video đã tải thành công
count = 0
for url in youtube_urls:
    if download_video_and_convert_to_audio(url):
        count += 1

print(f"Đã tải thành công {count} trên tổng số {len(youtube_urls)} video.")
