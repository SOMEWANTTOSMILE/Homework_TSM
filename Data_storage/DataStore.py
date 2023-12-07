import json


class DataStorage:
    def __init__(self, file_path):
        self.status = 'disconnect'
        self.content = None
        self.__file_path = file_path
        self.file = None

    @property
    def file_path(self):
        return self.__file_path

    def _create_storage(self):
        with open(self.file_path, 'w') as file:
            json.dump([], file)
            return file

    def connect(self):
        try:
            self.file = open(self.file_path, 'r')
            self.content = json.load(self.file)
            self.status = 'connected'
            return self.file
        except FileNotFoundError:
            return self._create_storage()

    def disconnect(self):
        if self.status == 'connected':
            self.file.close()
            self.status = 'disconnected'
            print('file close')


class DataStorageWrite(DataStorage):
    def connect(self):
        super().connect()

    def _create_storage(self):
        with open(self.file_path, 'w') as file:
            json.dump([], file)
            return file

    def append(self, string_):
        if self.status == 'connected':
            self.content.append(string_)
            with open(self.file_path, 'w') as file:
                json.dump(self.content, file)
        else:
            print('You need to set a "connect" status first')


storage = DataStorageWrite("json_fi.json")
storage.connect()
storage.append('Hello, world')
storage.disconnect()
print(storage.content)
