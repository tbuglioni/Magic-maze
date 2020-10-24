from cx_Freeze import setup, Executable

setup(
    name = "projet 3 Buglioni Thomas",
    version = "1",
    description = "game with mcgyver",
    executables = [Executable("main.py")]
)
