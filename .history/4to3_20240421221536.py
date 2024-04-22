import subprocess

def extract_audio(input_file, output_file, format_='mp3'):
    """
    Extract audio from a video file using ffmpeg.

    :param input_file: Path to the input video file.
    :param output_file: Path to save the extracted audio file.
    :param format_: Output audio format. Supported formats: 'mp3', 'aac', 'm4a', 'wav', etc.
    """
    command = f'ffmpeg -i "{input_file}" -vn -ab 256k -ar 44100 -f {format_} "{output_file}"'
    subprocess.run(command, shell=True)

if __name__ == '__main__':
    input_file = './video/'
    output_file = 'path/to/your/audio.mp3'  # Change the file extension based on the desired output format
    extract_audio(input_file, output_file, format_='mp3')  # You can change the format to 'aac', 'm4a', 'wav', etc.