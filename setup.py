import sys
from cx_Freeze import setup, Executable

setup(
	name = "Xiangnan Gong",
	version = "1.0",
	description = "Trading Simulator",
	executables = [Executable("main.py", base = "Win32GUI")])