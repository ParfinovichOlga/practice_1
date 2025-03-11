class ObjList:
    """Class for node object."""
    def __init__(self, data=0, prev_node=None, next_node=None):
        self.__data = data
        self.__prev = prev_node
        self.__next = next_node

    @property
    def data(self):
        """The data property"""
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

    @property
    def prev(self):
        """The prev property"""
        return self.__prev

    @prev.setter
    def prev(self, value):
        self.__prev = value

    @property
    def next(self):
        """The next property"""
        return self.__next

    @next.setter
    def next(self, value):
        self.__next = value

