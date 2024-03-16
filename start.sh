
#!/bin/bash

# Activate the virtual environment (assuming your venv is in a folder named 'myvenv')
source myvenv/bin/activate

# Execute the Python script within the activated virtual environment
python3 ddos.py greyproject.studio 90

# Optional: Deactivate the virtual environment (if desired)
# deactivate 