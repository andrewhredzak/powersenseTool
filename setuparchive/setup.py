import sys
from cx_Freeze import setup, Executable


'''
base = None
if sys.platform == "win32":
    base = "Win32GUI"  # To hide the console window on Windows
'''


setup(
    name="powersenseTool",
    version="1.0",
    description="Power Measurement GUI",
    #options={"build_exe": build_exe_options},
    executables=[{"script": "powersenseTool.py","base": "gui"}]
)