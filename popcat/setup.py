from setuptools import setup

APP = ['taylor.py']  # Replace with your script name
DATA_FILES = []  # Add any additional files or directories you need to include
OPTIONS = {
    'argv_emulation': True,
    'packages': ['pygame', 'cv2'],  # Include any additional packages your script uses
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
