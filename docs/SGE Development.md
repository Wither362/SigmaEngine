# SGE Development

So you wanna develop some games or tools with SGE, huh.

Well there are snippets of code which you will need to remove when transfering the code from python to micropython.

In total, there are snippets, files, and folders.

You can either delete the followings, or just download the latest release from the github releases page which won't have the code that's supposed to be deleted, for you. Or, you can use the github workflow build YAML file and run it yourself.

**files** to delete:

- `.gitignore`
- `docs.md`
- `gint.py`
- `README.md` (optional, but will take space if not deleted)

**folders** to delete:

- any `__pycache__` folder you encounter in whichever folder, as it can appear inside EVERY folder that has a `.py` file in it.
- `\desktop\` folder, with all of the files inside.
- `\docs\` folder, as you won't be able to read the `.md` documentation files inside the FX-CG50.
- `\.vscode\` folder
- `\.typings\` folder
- `\.gitbub\` folder

**snippets** to delete:

- Code that is between the lines of code `# NON_MICROPYTHON` and `# END`, such as this example:

  ```py
  # NON_MICROPYTHON
  import desktop.adasjdsajd
  # END
  ```

- `if (in_micropython)` lines. Example:

  ```py
  if (in_micropython):
    import time
  ```

  should look like this:

  ```py
  import time
  ```

## Desktop advantages

Of course, there's some advantages when using the desktop version.

For example:

- Ability to **pause** the `main update loop` by pressing `F2` (only if your code is using `pollevent()`, btw)
- A faster execution (which is indeed reaaally bad for developing projects)
