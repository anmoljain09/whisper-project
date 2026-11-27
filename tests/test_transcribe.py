
"""
HINGLISH AUDIO TRANSCRIPTION - TESTING
======================================

This file contains basic unit tests for the project.
The project includes basic unit tests using Python's built-in `unittest` framework.

tests/
│
└── test_transcribe.py

CURRENT TESTS
-------------
1. Verify that the input audio file exists.
2. Verify that the output directory exists.
3. Verify that the transcription file has been generated.
4. Verify that the transcription file is not empty.

FUTURE TESTING IMPROVEMENTS
---------------------------
If the project is expanded in the future, the testing structure
can be extended as follows:

tests/
│
├── test_transcribe.py
├── test_audio.py
├── test_output.py
└── test_dependencies.py

Planned Improvements:

1. test_audio.py
   - Validate audio file existence.
   - Check supported audio formats.
   - Verify that the audio file is not empty.

2. test_output.py
   - Verify output directory creation.
   - Check transcription file generation.
   - Validate transcription content.
   - Verify output file is not empty.

3. test_dependencies.py
   - Verify Faster-Whisper installation.
   - Check FFmpeg availability.
   - Check FFprobe availability.

4. test_transcribe.py
   - Test transcription configuration.
   - Test audio chunking functionality.
   - Test error handling.
   - Verify temporary file cleanup.

EXECUTING TESTS
---------------
Activate the virtual environment:

    .\\venv\\Scripts\\Activate.ps1

Run all tests:

    python -m unittest discover -s tests -v

EXPECTED OUTPUT
---------------
test_audio_file_exists ... ok
test_output_folder_exists ... ok
test_transcription_file_exists ... ok
test_transcription_not_empty ... ok

Ran 4 tests

OK

NOTE
----
This is a small project, so the current basic tests are sufficient.

Additional tests can be introduced if new features or functionality
are added in the future.

These tests verify existing files and directories. They do not
execute the actual audio transcription process.

"""

import os
import unittest

AUDIO_FILE = "audio/my_audio.mp3"
OUTPUT_FOLDER = "output"
OUTPUT_FILE = os.path.join(OUTPUT_FOLDER, "transcription.txt")


class TestTranscription(unittest.TestCase):

    def test_audio_file_exists(self):
        self.assertTrue(
            os.path.isfile(AUDIO_FILE),
            "Audio file not found!"
        )

    def test_output_folder_exists(self):
        self.assertTrue(
            os.path.isdir(OUTPUT_FOLDER),
            "Output folder not found!"
        )

    def test_transcription_file_exists(self):
        self.assertTrue(
            os.path.isfile(OUTPUT_FILE),
            "Transcription file not generated!"
        )

    def test_transcription_not_empty(self):
        self.assertTrue(
            os.path.getsize(OUTPUT_FILE) > 0,
            "Transcription file is empty!"
        )


if __name__ == "__main__":
    unittest.main()
