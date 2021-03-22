from Stream.stream import Stream
import csv


#
#
# class TextStream(Stream):
#     def __int__(self, path):
#         super().__init__(None)
#         self.path = path
#
#     def get_path(self):
#         return self.path
#
#
# textStream = TextStream('../data/taxi.csv')
#
# print(textStream.get_path())


# Use the Person class to create an object, and then execute the printname method:


def read_file(path):
    with open(path, 'r') as f:
        return f.readlines()


read_file('../data/taxi.csv')


class TextStream(Stream):
    def __init__(self, path: str):
        super().__init__(read_file(path))



print(TextStream('../data/taxi.csv')\
    .skip(1).filter(lambda x: str(x).split(",")[1] == 'wed')\
    .map(lambda x: str(x).split(",")[1]).item_counter())


print(TextStream('../data/taxi.csv')\
    .skip(1).filter(lambda x: str(x).split(",")[1] != 'wed')\
    .map(lambda x: str(x).split(",")[1]).item_counter())


