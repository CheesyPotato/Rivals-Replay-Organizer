from cx_Freeze import setup, Executable
import os
import sys
os.environ['TCL_LIBRARY'] = os.path.split(sys.executable)[0] + r"\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = os.path.split(sys.executable)[0] + r"\tcl\tk8.6"

__version__ = '1.0.0'

include_files = ['config','kragg icon.ico', os.path.split(sys.executable)[0] + r'\DLLs\tcl86t.dll', os.path.split(sys.executable)[0] + r'\DLLs\tk86t.dll']
packages = ["os", 'shutil', 'tkinter', 'tqdm', 'requests', 'functools', 'bs4', 'zipfile', 'idna']

setup(
    name = "Rivals Replay Organizer",
    description='Organizes Rivals of Aether replays',
    version=__version__,
    options = {"build_exe": {
    'packages': packages,
    'include_files': include_files,
    'include_msvcr': True,
}},
executables = [Executable("rivalsreplayorganizer.py",base="Win32GUI"), Executable('update.py', base = None)]
)
