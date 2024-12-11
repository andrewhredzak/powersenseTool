"""A very simple setup script to create a single executable using Tkinter.

test_tkinter.py is a very simple type of Tkinter application.

Run the build process by running the command 'python setup.py build'

If everything works well you should find a subdirectory in the build
subdirectory that contains the files needed to run the script without Python.
"""

from cx_Freeze import Executable, setup

executables = [Executable("powersenseTool.py", base="gui", icon="python")]
include_files = [("logox128.png", "share/python.png")]

setup(
    name="powersenseTool",
    version="0.2.7",
    description="powersenseTool test exe",
    options={"build_exe": {"include_files": include_files}},
    executables=executables,
)
