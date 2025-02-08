import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

package_name = "TextSummarizer"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{package_name}/__init__.py",
    f"src/{package_name}/components/__init__.py",
    f"src/{package_name}/utils/__init__.py",
    f"src/{package_name}/utils/common.py",
    f"src/{package_name}/logging/__init__.py",
    f"src/{package_name}/config/__init__.py",
    f"src/{package_name}/config/configuration.py",
    f"src/{package_name}/pipeline/__init__.py",
    f"src/{package_name}/entity/__init__.py",
    f"src/{package_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",

]

for filepath in list_of_files:
    # generates os based file path (whether to keep forward or backward slash based on OS)
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory:{filedir} for the file {filename}")

    
    # Check if the file does not exist or if it exists but is empty
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
    # Open the file in write mode ('w'), which creates the file if it does not exist
        with open(filepath, 'w') as f:
            pass  # No content is written, just creating an empty file
    
        # Log that an empty file has been created
        logging.info(f"Creating empty file: {filepath}")

    else:
        # If the file already exists and is not empty, log that it exists
        logging.info(f"{filename} already exists")