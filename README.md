# 🎙️ Hinglish Audio Transcription

Convert Hindi + English mixed audio into text using **Faster-Whisper**.

A free, offline, API-key-free audio transcription project built with Python. It runs locally on your computer using CPU, without requiring an NVIDIA GPU.

## ✨ Features

- No OpenAI API key required.
- Runs locally on your PC.
- Hindi + English mixed audio transcription.
- CPU-based processing (no NVIDIA GPU required).
- Faster-Whisper with INT8 quantization.
- Automatic audio duration detection.
- Automatic 5-minute audio chunking.
- Saves transcription in a TXT file.
- Supports MP3, WAV and M4A through FFmpeg.
- Temporary audio chunks are automatically deleted after processing.
- No cloud-based transcription service required.

## 🛠️ Technologies Used

- Python 3.11
- Faster-Whisper
- CTranslate2
- FFmpeg
- FFprobe
- unittest

## 💻 System Requirements

- Windows 10 or later
- Python 3.11
- Minimum 4 GB RAM (8 GB or more recommended)
- Internet connection for initial model download
- FFmpeg and FFprobe installed and available in PATH

## 📁 Project Structure

```text
Whisper-project/
│
├── audio/
│   └── my_audio.mp3
│
├── output/
│   └── transcription.txt
│
├── temp_chunks/
│
├── tests/
│   └── test_transcribe.py
│
├── venv/
│
├── transcribe.py
├── pyproject.toml
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

> `venv/` and `temp_chunks/` are local folders. They are not uploaded to GitHub (they are listed in `.gitignore`). `temp_chunks/` is created automatically while the script runs and is deleted after processing.

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/anmoljain09/whisper-project.git
cd whisper-project
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

**Windows PowerShell:**

```powershell
venv\Scripts\activate
```

### 4. Install and Verify Python Dependencies

Install the required Python dependencies:

```bash
pip install -r requirements.txt
```

Verify installation (e.g., Faster-Whisper):

```powershell
python -c "from faster_whisper import WhisperModel; print('Faster-Whisper installed successfully!')"
```

If the installation is successful, you will see:

```text
Faster-Whisper installed successfully!
```

### 5. Install FFmpeg

Install FFmpeg and make sure both `ffmpeg` and `ffprobe` are available in your system PATH.

Verify installation:

```bash
ffmpeg -version
ffprobe -version
```

## 🎧 Add Audio File

Place your audio file inside the `audio` folder.

**Default audio filename:**

```text
audio/my_audio.mp3
```

The script currently uses this fixed path:

```python
AUDIO_FILE = "audio/my_audio.mp3"
```

If your audio file has a different name, update the `AUDIO_FILE` variable in `transcribe.py`.

## 🔁 How to Run Again After Closing VS Code

After completing the initial setup, you do not need to install dependencies or download the model again.

Whenever you close VS Code or restart your PC, follow these steps to run the project again.

### 1. Open the Project in VS Code

Open your `whisper-project` folder in VS Code.

### 2. Activate the Virtual Environment

Open the VS Code terminal (PowerShell) and run:

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Verify Faster-Whisper Installation (Optional)

To check whether Faster-Whisper is installed correctly, run:

```powershell
python -c "from faster_whisper import WhisperModel; print('Faster-Whisper installed successfully!')"
```

### 4. Run the Transcription Script

```powershell
python transcribe.py
```

**Important Notes:**

- Activate the virtual environment every time you open a new VS Code terminal.
- You do not need to reinstall Python dependencies every time.
- You do not need to download the Whisper model again once it has been downloaded.
- Simply activate `venv` and run `transcribe.py` to start transcription again.
- Make sure your audio file is available in the `audio` folder.

## ▶️ Run Transcription

Run the following command:

```bash
python transcribe.py
```

On the first run, Faster-Whisper automatically downloads the BASE model.

After the model is downloaded, transcription can run offline.

## ⚙️ Configuration

Current settings in `transcribe.py`:

| Setting | Value |
|---|---|
| Model Size | BASE |
| Device | CPU |
| Compute Type | INT8 |
| CPU Threads | 2 |
| Chunk Length | 300 seconds (5 minutes) |
| Beam Size | 3 |
| Language | Hindi |
| VAD Filter | Enabled |

## 🔄 How It Works

1. Checks whether the audio file exists.
2. Loads the Faster-Whisper BASE model.
3. Detects the total audio duration using FFprobe.
4. Automatically divides audio into 5-minute chunks.
5. Converts each chunk into mono 16 kHz WAV format.
6. Transcribes each chunk using Faster-Whisper.
7. Appends the transcription to a TXT file.
8. Deletes temporary WAV chunks after processing.
9. Saves the final transcription.

## 📄 Output

The transcription is automatically saved at:

```text
output/transcription.txt
```

**Example:**

```text
HINGLISH AUDIO TRANSCRIPTION

--- Part 1 ---
आपका transcription text यहां आएगा।

--- Part 2 ---
अगले audio chunk का transcription यहां आएगा।
```

## 🧪 Running Tests

The tests check for the audio file, the output folder and the generated transcription file. Because of this, run the transcription at least once before running the tests.

1. Place your audio file at `audio/my_audio.mp3`.
2. Run the transcription:

```powershell
python transcribe.py
```

3. Run the tests from the project root folder:

```powershell
python -m unittest discover -s tests -v
```

**Expected output:**

```text
test_audio_file_exists ... ok
test_output_folder_exists ... ok
test_transcription_file_exists ... ok
test_transcription_not_empty ... ok

Ran 4 tests

OK
```

**Note:** The tests only verify that the required files and folders exist. They do not run the actual audio transcription. The audio file and the transcription file are not uploaded to GitHub (they are listed in `.gitignore`), so the tests will fail on a fresh clone until you add an audio file and run `transcribe.py`.

## 🔒 Privacy

- Audio is processed locally on your computer.
- No OpenAI API key is required.
- No cloud transcription API is used.
- The Whisper model is downloaded initially from Hugging Face.
- Once the model is downloaded, transcription can run without an internet connection.

## ⚠️ Limitations

- Transcription speed depends on CPU performance.
- Systems with 4 GB RAM may experience memory limitations.
- Hinglish accuracy depends on audio quality, background noise and pronunciation.
- Hindi language selection may not perfectly recognize every English word.
- Output is written in Devanagari (Hindi) script because the language is fixed to Hindi. English words may also appear in Devanagari.
- The BASE model is fast but its Hindi accuracy is limited. For better accuracy, try `MODEL_SIZE = "small"` in `transcribe.py` (it will be slower).
- Longer audio files require more processing time.
- The first execution requires an internet connection to download the model.

## 📜 License

MIT License (project code).

See the `LICENSE` file for details.

---

**Made with ❤️ using Python and Faster-Whisper**
