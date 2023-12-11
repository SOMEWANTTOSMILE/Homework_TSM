from BaseHandler import TxtHandler, JsonHandler


class FileWorker:
    def __init__(self, file_path):
        self.file_path = file_path
        self.file_type = {'json': JsonHandler, 'txt': TxtHandler}

    def get_file_type(self):
        if self.file_path.endswith('json'):
            return self.file_type.get('json')
        elif self.file_path.endswith('txt'):
            return self.file_type.get('txt')
        else:
            return 'error'

    def read(self):
        reader = self.get_file_type()
        return reader(self.file_path).read()

    def append(self, string_):
        appender = self.get_file_type()
        return appender(self.file_path).append(string_)

    def close(self):
        closer = self.get_file_type()
        return closer(self.file_path).close()


def app():
    fw = FileWorker('test.json')
    content = fw.read()
    fw.append('obj1')
    fw.append('obj2')
    fw.close()
    return content


print(app())
