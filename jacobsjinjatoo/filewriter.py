import io
import os.path

class WriteIfChangedFile(io.TextIOBase):

    def __init__(self, filename):
        self.filename = filename
        self.initialData = None        
        with open(filename, 'r') as fp:
            self.initialData = fp.read()

    def write_if_changed(self):
        pos = self.tell()
        self.seek(0)
        currentData = self.read()
        self.seek(pos)
        if self.initialData != self.currentData:
            with open(self.filename, 'w') as fp:
                fp.seek(0)
                fp.write(currentData)
    

    def __enter__(self):
        return self

    def __exit__(self):
        self.write_if_changed()