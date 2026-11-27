# .\venv\Scripts\Activate.ps1
# python -c "from faster_whisper import WhisperModel; print('Faster-Whisper installed successfully!')"
# python transcribe.py

from faster_whisper import WhisperModel
import os
import subprocess

# File locations (FIXED)
AUDIO_FILE = "audio/my_audio.mp3"
OUTPUT_FOLDER = "output"
OUTPUT_FILE = os.path.join(OUTPUT_FOLDER, "transcription.txt")
TEMP_FOLDER = "temp_chunks"

# Settings
CHUNK_LENGTH = 300  # Fixed 5 minutes
MODEL_SIZE = "base"
COMPUTE_TYPE = "int8"

# Create folders
os.makedirs(OUTPUT_FOLDER, exist_ok=True)
os.makedirs(TEMP_FOLDER, exist_ok=True)

# Check audio file
if not os.path.exists(AUDIO_FILE):
    print("ERROR: Audio file not found!")
    raise SystemExit(1)

print("Loading Faster-Whisper BASE model...")

model = WhisperModel(
    MODEL_SIZE,
    device="cpu",
    compute_type=COMPUTE_TYPE,
    cpu_threads=2
)

# Get audio duration
print("Checking audio duration...")

info = subprocess.run(
    [
        "ffprobe", "-v", "error",
        "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1",
        AUDIO_FILE
    ],
    capture_output=True,
    text=True,
    check=True
)

duration = float(info.stdout.strip())

# Calculate chunks automatically
total_chunks = int((duration + CHUNK_LENGTH - 1) // CHUNK_LENGTH)

# Clear previous output
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write("HINGLISH AUDIO TRANSCRIPTION\n\n")

print(f"Audio duration: {duration / 60:.1f} minutes")
print(f"Total chunks: {total_chunks}")

for i, start in enumerate(range(0, int(duration), CHUNK_LENGTH)):

    print(f"\nProcessing part {i + 1}/{total_chunks}...")

    chunk_file = os.path.join(
        TEMP_FOLDER,
        f"part_{i + 1}.wav"
    )

    subprocess.run(
        [
            "ffmpeg", "-y",
            "-ss", str(start),
            "-i", AUDIO_FILE,
            "-t", str(CHUNK_LENGTH),
            "-vn",
            "-ac", "1",
            "-ar", "16000",
            chunk_file
        ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=True
    )

    segments, metadata = model.transcribe(
        chunk_file,
        task="transcribe",
        language="hi",
        beam_size=3,
        vad_filter=True
    )

    with open(OUTPUT_FILE, "a", encoding="utf-8") as f:
        f.write(f"\n--- Part {i + 1} ---\n")

        for segment in segments:
            f.write(segment.text.strip() + " ")

        f.write("\n")

    os.remove(chunk_file)

    print(f"Part {i + 1} completed.")

# Remove temporary folder
os.rmdir(TEMP_FOLDER)

print("\nTRANSCRIPTION COMPLETED!")
print("Saved at:", OUTPUT_FILE)
