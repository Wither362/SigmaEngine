'''
	DETELED ENTIRELY when in Micropython environment.\n\n
	Check out [SGE Development.md](<./docs/SGE Development.md>) and [SGE Limitations.md](<./docs/SGE Limitations.md>) for more information about why is this code here.
'''

import io

def open(file_path: str, mode: str = 'r'):
	file_path = file_path.replace('\\', '/')
	if file_path.startswith("sigma/"):
		file_path = file_path[6:]
	else:
		print('[DEV WARN]')
		print(f'  Path: {file_path} does not start with "sigma". If this is intentional, ignore this warning.')

	if len(file_path.split('/')) > 2:
		print('[DEV WARN]')
		print(f'  Path: {file_path} has more than 2 consecutive folders. Casio\'s CG50\'s file system does not accept this. Will raise an error.')

	for f in file_path.split('/'):
		if len(f) > 8:
			print('[DEV WARN]')
			print(f'  Path: {file_path} has a folder who\'s folder name is more than 8 characters long. Casio\'s CG50\'s file system does not accept this. Will raise an error.')

	return io.open(file_path, mode)