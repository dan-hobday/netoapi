import os
import sys

# Get the directory of the current file (__init__.py), then go up 1 level to the project root
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)

# Add the project root to the sys.path
sys.path.insert(0, f"{project_root}/netoapi")

# Now, 'netoapi' sub-package is available for import