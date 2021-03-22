class Stream:

    def __init__(self, data=None):
        if data is not None:
            self.__data = list(data)
        else:
            self.__data = list()

    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data = list(data)

    def skip(self, start):
        """Function to skip upto a given start value"""
        self.__data = self.__data[start:]
        return self

    def map(self, func):
        """Function to apply function to each item
        returning the stream"""
        self.__data = [func(x) for x in self.__data]
        return self

    def for_each(self, func):
        """Function to apply function to each item
            terminating the stream"""
        for x in self.__data:
            func(x)

    def filter(self, func):
        """Function to apply filter out values that do not match a given function"""
        self.__data = [x for x in self.__data if func(x)]
        return self

    def count(self):
        """Return the count of the data"""
        return len(self.__data)

    def sum(self):
        """Return the sum of the data"""
        return sum(self.__data)

    def take(self, x=0):
        """Return all values up to a given value"""
        if x != 0:
            return self.__data[:x]
        return self.__data

    def reduce(self, func):
        """Applies an aggregator function on the data to provide a summary"""
        # create iterator
        iterator = iter(self.__data)
        value = next(iterator)

        for element in iterator:
            value = func(value, element)
        return value

    def average(self):
        """Return the average value of the data"""
        return self.sum() / self.count()

    def sort(self, desc=False):
        """sort the data ascending and descending"""
        return sorted(self.__data, reverse=desc)

    def min(self):
        """Return the minimum value of the data"""
        return min(self.__data)

    def max(self):
        """Return the maximum value of the data"""
        return max(self.__data)

    def distinct(self):
        """Return all distinct values in the data"""
        return set(self.__data)

    def range(self, start=0, stop=0, step=1):
        """ Function to set a range of numbers"""
        self.__data = range(start, stop, step)
        return self

    def print_all(self):
        """Print all the values of the data"""
        for x in self.__data:
            print(x)

    def item_counter(self):
        counter_dict = dict()
        for x in self.__data:
            if x in counter_dict:
                n = counter_dict[x]
                counter_dict[x] = n + 1
            else:
                counter_dict[x] = 1

        return counter_dict


# with open('../data/taxi.csv')as f:
#     lines = f.read()
#
#     for line in lines.split("\n"):
#         print(line[0:3])


# stream = Stream().range(0, 10)
#
# print(stream.map(lambda x: x * x).take())
#
# stream.print_all()
# print(stream.distinct())

# print(stream.sort())
# print(stream.sort(desc=True))


# stream.for_each(lambda x: print(x))

# print(stream.take(3))
# print(stream.skip(1).take())
#
# # print(stream.reduce(lambda x, y: x + y))
# print(stream.average())

# print(stream.filter(lambda x: x % 2 == 0).map(lambda x: x * x).take())
# print(stream.filter(lambda x: x % 2 == 0).map(lambda x: x * x).sum())


# print(squared_even)
#
# even = stream.filter(lambda x: x % 2 == 0)
# print(even)
