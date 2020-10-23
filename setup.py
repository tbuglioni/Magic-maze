from cx_Freeze import setup, Executable

build_exe_options = {"include_files": [["image"], ["level"]]}

setup(
    name = "projet 3 Buglioni Thomas",
    version = "1",
    description = "game with mcgyver",
    executables = [Executable("main.py")]
)
