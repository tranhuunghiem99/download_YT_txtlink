from pytube import YouTube

def download_video(url):
    try:
        # Tải video
        youtube = YouTube(url)
        video = youtube.streams.get_highest_resolution()
        video.download('path_to_save_video')  # Thay 'path_to_save_video' bằng đường dẫn thực tế trên máy của bạn

        return True
    except Exception as e:
        print(f"Không thể tải video từ url: {url}. Lỗi: {str(e)}")
        return False

# Đọc danh sách các URL video YouTube từ file .txt
with open(./', 'r') as f:  # Thay 'path_to_your_txt_file' bằng đường dẫn thực tế đến file .txt của bạn
    youtube_urls = [line.strip() for line in f]

# Tải và đếm số lượng video đã tải thành công
count = 0
for url in youtube_urls:
    if download_video(url):
        count += 1

print(f"Đã tải thành công {count} trên tổng số {len(youtube_urls)} video.")
