"""
Initialization of a variable `storage`. 
This Variable creates a unique instance of `FileStorage`
    for the Application.

Consequently, the `__objects` class attribute of the `FileStorage`
    class is loaded with all objects currently on the `__file_path`
    class attribute of the `FileStorage` class.
"""


from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
