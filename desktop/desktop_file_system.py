'''
	Meant to be DETELED ENTIRELY when using Micropython.
'''

import io

def open(file_path: str, mode: str = 'r'):
	file_path = file_path.replace('\\', '/')
	if file_path.startswith("sigma/"):
		file_path = file_path[6:]
	if len(file_path.split('/')) > 2:
		print(f'[DEV] Path: {file_path.split('/')}')
		print("[DEV WARN] There cannot be more than 2 consecutive folders.")
	if len(file_path.split('/')[-2]) > 8:
		print(f'[DEV] Path: {file_path.split('/')[-2]}')
		print("[DEV WARN] Folder names cannot be more than 8 characters long.")
	return io.open(file_path, mode)