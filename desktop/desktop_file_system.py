'''
	Meant to be DETELED ENTIRELY when using Micropython.
'''

import io

def open(file_path: str, mode: str = 'r'):
	if file_path.startswith("sigma/"):
		file_path = file_path[6:]
	return io.open(file_path, mode)