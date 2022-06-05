class File:
    def __init__(self,file, mode) -> None:
        self.file = file
        self.mode = mode
        
    def __enter__(self):
        if self.mode == 'r': open(self.file, 'w')
        self.file = open(self.file, self.mode)
        return self

    def __exit__(self, *args):
        self.file.close()
        return False

    def write(self, text):
        self.file.write(text)

    def read_all(self):
        return self.file.read()

    def read_lines(self):
        return self.file.readlines()

    def add(self, text):
        self.file.write(text)

    def add_new_line(self, text):
        self.file.write(f'\n{text}')

file = 'test.txt'

with File(file=file,mode='w') as f:
    f.write(text='hello')

with File(file=file,mode='a') as f:
    f.add(text=' world!')

with File(file=file,mode='a') as f:
    f.add_new_line(text='hello world!')

with File(file=file,mode='r') as f:
    print(f.read_all())

with File(file=file,mode='r') as f:
    print(f.read_lines())
