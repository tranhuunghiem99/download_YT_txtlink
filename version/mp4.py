from pytube import YouTube

def download_video(video_url, download_folder='.', format_index=None):
    """
    Download a YouTube video.

    :param video_url: YouTube video URL.
    :param download_folder: Folder to save the downloaded video. Default: current folder.
    :param format_index: Video format index. If None, the best available format will be chosen.
    """
    yt = YouTube(video_url)

    # Get the first stream with video and audio
    stream = yt.streams.filter(only_audio=False).first()

    # If format_index is provided, use it to select the format
    if format_index is not None:
        stream = yt.streams.get_by_itag(format_index)

    print(f'Downloading {stream.default_filename}...')
    stream.download(download_folder)
    print('Download complete.')

def download_audio(video_url, download_folder='.', format_index=None):
    """
    Download a YouTube video's audio as an MP3 file.

    :param video_url: YouTube video URL.
    :param download_folder: Folder to save the downloaded audio. Default: current folder.
    :param format_index: Audio format index. If None, the best available format will be chosen.
    """
    yt = YouTube(video_url)

    # Get the first stream with only audio
    stream = yt.streams.filter(only_audio=True).first()

    # If format_index is provided, use it to select the format
    if format_index is not None:
        stream = yt.streams.get_by_itag(format_index)

    # Change the file extension to .mp3
    filename = f'{stream.default_filename}.mp3'

    print(f'Downloading audio as {filename}...')
    stream.download(download_folder, filename=filename)
    print('Download complete.')

if __name__ == '__main__':
    # Example usage
    video_url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
    download_video(video_url, format_index=22)  # Download in 720p
    download_audio(video_url, format_index=140)  # Download audio in best available format