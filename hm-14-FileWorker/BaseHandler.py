import json


class BaseHandler:
    def __init__(self, file_path):
        self.file_path = file_path
        self.content = None
        self.file = None

    def read(self):
        return NotImplemented

    def append(self, user_string):
        return NotImplemented

    def close(self):
        return NotImplemented


class JsonHandler(BaseHandler):
    def __init__(self, file_path):
        super().__init__(file_path)
        self.user_string = None

    def read(self):
        self.file = open(self.file_path, "r")
        self.content = json.load(self.file)
        if list is type(self.content):
            print(f"all ok, json file have contains")
            return self.content
        else:
            print(f"Json file ain`t have list")
            raise TypeError

    def append(self, user_string):
        self.file = open(self.file_path, "r")
        self.content = json.load(self.file)
        self.content.append(user_string)
        with open(self.file_path, "w") as j_file:
            json.dump(self.content, j_file)

    def close(self):
        self.file = open(self.file_path, "r")
        self.file.close()


class TxtHandler(BaseHandler):
    def __init__(self, file_path):
        super().__init__(file_path)
        self.user_string = None

    def read(self):
        self.file = open(self.file_path, "r")
        self.content = self.file.read()
        print(self.content)
        return self.content

    def append(self, user_string):
        self.file = open(self.file_path, 'a')
        return self.file.write(f'{user_string}\n')

    def close(self):
        self.file.close()
