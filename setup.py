from cx_Freeze import setup, Executable
import os
import sys
os.environ['TCL_LIBRARY'] = os.path.split(sys.executable)[0] + r"\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = os.path.split(sys.executable)[0] + r"\tcl\tk8.6"

__version__ = '1.0.2'

include_files = ['config', 'kragg icon.ico']
packages = ["os", 'shutil', 'tkinter',
            'functools', 'zipfile', 'sys']

setup(
    name="Rivals Replay Organizer",
    description='Organizes Rivals of Aether replays',
    version=__version__,
    options={"build_exe": {
        'packages': packages,
        'include_files': include_files,
        'include_msvcr': True,
    }},
    executables=[Executable("rivalsreplayorganizer.py",
                            base="Win32GUI", icon='kragg icon.ico')]
)
