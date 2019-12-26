**Currently under development:** The Clapper integration with Google Home.

# The Clapper
A Python-based switch controller that uses PyAudio to detect double claps and turn a switch on/off. An extension of [this StackOverflow answer](https://stackoverflow.com/questions/4160175/detect-tap-with-pyaudio-from-live-mic) on single tap detection.

# Threshold
Change the value of ``INITIAL_TAP_THRESHOLD = 0.1`` in **clap_detector.py** depending on the ambient noise of your environment.
