# SGE Limitations

There's some limitations with making an engine for a freakin' calculator that you, dev, NEED to know.

## File System

The Casio fx-CG50 file system isn't that good. Here's a list of things you have to get in mind when developing anything with ExtraPython:

1. File paths are ABSOLUTE, NOT RELATIVE, they are used directly inside the CG50's root folder. If you want to access a file inside SGE's `sigma` folder (for example), you'll have to use `sigma\`
2. You CANNOT create new folders. (But you CAN make new files in already existing folders).
3. Folder names CANNOT BE MORE than 8 (eight) characters long. The code will just throw OSError. (Filenames can have more characters, but it's NOT RECOMMENDED, use acronyms in all ways possible)
4. There CANNOT BE more than TWO (2) CONSECUTIVE FOLDERS. (for example, `Folder1/Folder2/file.py` is correct, but `Folder1/Folder2/Folder3/file.py` will raise an error). So, all the scenes should be contained inside the `scenes/` folder.

These limitations are already in SGE `desktop_file_system.py`, which you'll have to reference inside your code if you want to access a file that is not related to SGE's normal execution. For that, just copy and paste this code right here along your import code:

```py
# NON_MICROPYTHON
from desktop.desktop_file_system import open
# END
```

As said in [SGE Development.md](SGE%20Development.md), you will need to strip out that code entirely from the file when in a micropython environment.
