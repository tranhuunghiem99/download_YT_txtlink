from pydub import AudioSegment

# Define a function to convert a video to an audio
def convert_video_to_audio(video_path, audio_path):
    video = AudioSegment.from_file(video_path, "mp4")
    video.export(audio_path, format="mp3")

# Call the function to convert "video.mp4" to an audio and save it as "audio.mp3"
convert_video_to_audio("./video/", "audio.mp3")

# Print a success message
print("video.mp4 was successfully converted to audio and saved as audio.mp3")
