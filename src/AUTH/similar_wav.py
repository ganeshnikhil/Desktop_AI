import wave
import numpy as np
import sys

def open_wav_file(file_path):
    """Open WAV file and extract left channel data."""
    with wave.open(file_path, 'r') as wav_file:
        params = wav_file.getparams()
        sample_rate = params[2]
        num_frames = params[3]
        num_channels = params[0]
        sample_width = params[1] * 8
        
        if sample_width == 16:
            audio_data = np.frombuffer(wav_file.readframes(num_frames), dtype=np.int16)
        elif sample_width == 32:
            audio_data = np.frombuffer(wav_file.readframes(num_frames), dtype=np.int32)
        elif sample_width == 8:
            audio_data = np.frombuffer(wav_file.readframes(num_frames), dtype=np.int8)
        
        # Extract left channel data
        left_channel = audio_data[::num_channels]
        return left_channel, sample_rate

def get_fft_chunks(audio_data, sample_rate, chunk_duration=0.02):
    """Split audio data into chunks and compute FFT for each chunk."""
    chunk_size = int(sample_rate * chunk_duration)
    num_chunks = len(audio_data) // chunk_size
    fft_chunks = [np.fft.rfft(audio_data[i * chunk_size:(i + 1) * chunk_size]) for i in range(num_chunks - 1)]
    return np.array(fft_chunks)

def compare_audio_chunks(fft_chunks1, fft_chunks2, min_matches=10, similarity_threshold=0.9):
    """Compare FFT chunks of two audio files and determine if they match."""
    chunk_diffs = {}
    num_chunks1 = len(fft_chunks1)
    num_chunks2 = len(fft_chunks2)
    
    for i in range(num_chunks1):
        for j in range(num_chunks2):
            correlation = np.corrcoef(fft_chunks1[i], fft_chunks2[j])[0][1]
            if correlation >= similarity_threshold:
                diff = abs(j - i)
                if diff in chunk_diffs:
                    chunk_diffs[diff] += 1
                    if chunk_diffs[diff] >= min_matches:
                        return True
                else:
                    chunk_diffs[diff] = 1
    return False

def main(file1, file2):
    audio_data1, sample_rate1 = open_wav_file(file1)
    audio_data2, sample_rate2 = open_wav_file(file2)
    
    if sample_rate1 != sample_rate2:
        print("Sample rates of the two audio files are different.")
        sys.exit(1)
    
    fft_chunks1 = get_fft_chunks(audio_data1, sample_rate1)
    fft_chunks2 = get_fft_chunks(audio_data2, sample_rate2)
    
    if compare_audio_chunks(fft_chunks1, fft_chunks2):
        print("Match")
        return True 
    else:
        print("No match")
        return False 

if __name__ == "__main__":
    file1 = ""
    file2 =""
    flag = compare_audio_chunks(file1 , file2)
    print(flag)
