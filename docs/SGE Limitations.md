# SGE Limitations

There's some limitations with making an engine for a freakin' calculator that you, dev, NEED to know.

## File System

The Casio fx-CG50 file system isn't that good. Here's a list of things you have to get in mind when developing anything with ExtraPython:

- You CANNOT create new folders. (But you CAN make new files in already existing folders).
- Folder names CANNOT BE MORE than 8 (eight) characters long. The code will just throw OSError. (Filenames can have more characters, but it's NOT RECOMMENDED, use acronyms in all ways possible)
- There CANNOT BE more than TWO (2) CONSECUTIVE FOLDERS. (for example, `Folder1/Folder2/file.py` is correct, but `Folder1/Folder2/Folder3/file.py` will throw an error).
