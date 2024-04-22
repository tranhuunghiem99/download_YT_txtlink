from moviepy.editor import AudioFileClip

def convert_video_to_audio(video_file_path, audio_file_path):
    # Tạo một đối tượng AudioFileClip từ file video
    video_clip = AudioFileClip(video_file_path)

    # Tạo một đối tượng audio từ video và ghi nó ra file
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(audio_file_path)

# Sử dụng hàm
convert_video_to_audio('path_to_your_video_file.mp4', 'path_to_save_audio_file.mp3')
