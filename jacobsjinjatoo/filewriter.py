import io
import os.path

class WriteIfChangedFile(io.StringIO):

    def __init__(self, filename):
        super().__init__()
        self.filename = filename
        self.initialData = None      
        try:  
            with open(filename, 'r') as fp:
                buf = fp.read()
                self.initialData = buf
        except FileNotFoundError:
            self.initialData = ''

    def write_if_changed(self):
        pos = self.tell()
        self.seek(0)
        currentData = self.read()
        self.seek(pos)
        if self.initialData != currentData:
            with open(self.filename, 'w') as fp:
                fp.seek(0)
                fp.write(currentData)
    
    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        self.write_if_changed()
