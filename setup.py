from cx_Freeze import setup, Executable
import os
os.environ['TCL_LIBRARY'] = r"C:\Other Programs\Python 3.6.2\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Other Programs\Python 3.6.2\tcl\tk8.6"



__version__ = '0.1'

include_files = ['config','kragg icon.ico']
packages = ["os", 'shutil', 'tkinter']

setup(
    name = "Rivals Replay Organizer",
    description='Organizes Rivals of Aether replays',
    version=__version__,
    options = {"build_exe": {
    'packages': packages,
    'include_files': include_files,
    'include_msvcr': True,
}},
executables = [Executable("rivalsreplayorganizer.py",base="Win32GUI")]
)
