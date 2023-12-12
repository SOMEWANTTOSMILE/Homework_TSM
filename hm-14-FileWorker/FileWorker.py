from Handler import TxtHandler, JsonHandler


class FileWorker:
    def __init__(self, file_path):
        self.file_path = file_path
        self.file_type = {'json': JsonHandler, 'txt': TxtHandler}
        self.handler = self.get_file_type()

    def get_file_type(self):
        file_type = self.file_path.split('.')[-1]
        if file_type in self.file_type:
            return self.file_type[file_type](self.file_path)
        else:
            raise ValueError('Unsupported filetype!')

    def read(self):
        return self.handler.read

    def close(self):
        return self.handler.close()

    def append(self, user_string):
        return self.handler.append(user_string)
