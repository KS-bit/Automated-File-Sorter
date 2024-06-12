📁 **New Functions and Modules I Learned:**

1. **Shutil Module in Python**
   - The `shutil` module offers a number of high-level operations on files and collections of files. In particular, functions are provided which support file copying and removal.

2. **OS Module in Python**
   - The `os` module in Python provides functions for interacting with the operating system.

3. **Usage and Difference between `os.makedirs()` and `os.mkdir()`**
   - **`os.makedirs()`**: 
     - The `os.makedirs()` function in Python is used to create directories, including any necessary parent directories.
     - *Recursive Creation*: It creates all the missing directories along the specified path. For instance, if you want to create a directory named `images/data/new_folder`, and `images/data` doesn't exist, `os.makedirs()` will create both `images/data` and `new_folder`.
   - **`os.mkdir()`**: 
     - The `os.mkdir()` function in Python can only create a single directory and will raise an error if the parent directory doesn't exist.
    
4. **Usage and Difference between `os.path.exists()` and `os.path.isdir()`**
   - **`os.path.exists()`**: 
     - This function will also return True if there's a regular file with that name.
   - **`os.path.isdir()`**: 
     - This function will only return True if that path exists and is a directory, or a symbolic link to a directory.

5. **`any()` Function in Python**
   - The `any()` function in Python returns True if any of the elements of a given iterable (List, Dictionary, Tuple, Set, etc.) are True, else it returns False.
