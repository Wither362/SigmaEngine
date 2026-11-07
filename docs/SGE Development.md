# SGE Development
So you wanna develop some games or tools with SGE, huh.

Well there are snippets of code which you will need to remove when transfering the code from python to micropython.

In total, there are snippets, files, and folders.

files to delete:

- `.gitignore`
- `docs.md`
- `gint.py`
- `README.md` (optional, but will take space if not deleted)

folders to delete:

- any `__pycache__` folder you encounter in whichever folder, as it can appear in EVERY folder that has a `.py` file in it.
- `\desktop\` folder, with all of the files inside.
- `\docs\` folder, as you won't be able to read the `.md` doc files from the FX-CG50.
- `\.vscode\` folder
- `\.typings` folder

snippets to delete:

## Desktop advantages

Of course, there's some advantages when using the desktop version.

For example:

- Ability to **pause** the `main update loop` by pressing `F2`
- A faster execution (which is indeed reaaally bad for developing projects)
