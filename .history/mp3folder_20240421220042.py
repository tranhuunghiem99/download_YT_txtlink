import os
from moviepy.editor import AudioFileClip

def convert_videos_to_audio(video_folder_path, audio_folder_path):
    # Lấy danh sách tất cả các file trong thư mục
    files = os.listdir(video_folder_path)

    for file in files:
        # Kiểm tra xem file có phải là file .mp4 không
        if file.endswith('.mp4'):
            # Tạo một đối tượng AudioFileClip từ file video
            video_clip = AudioFileClip(os.path.join(video_folder_path, file))

            # Tạo một đối tượng audio từ video và ghi nó ra file
            audio_clip = video_clip.audio
            audio_clip.write_audiofile(os.path.join(audio_folder_path, file.replace('.mp4', '.mp3')))

# Sử dụng hàm
convert_videos_to_audio('./video', 'path_to_save_audio_files')
