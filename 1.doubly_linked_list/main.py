from object_list import ObjList


class LinkedList:
    """Class for managing doubly linked list."""
    def __init__(self):
        self.head = None
        self.tail = None

    def _is_empty(self):
        """Check if LinkedList is empty."""
        return self.head is None and self.tail is None

    def add_obj(self, obj: ObjList):
        """Add new node to the end of the list."""
        if self._is_empty():
            self.head = obj
            self.tail = obj
        else:
            self.tail.next = obj
            obj.prev = self.tail
            self.tail = obj

    def remove_obj(self):
        """Remove the tail object."""
        if self._is_empty():
            return print("Can't be deleted: LinkedList is empty")
        if self.tail == self.head:
            self.head, self.tail = None, None
        else:
            cur = self.tail.prev
            cur.next = None
            self.tail = cur

    def get_data(self):
        """Retrieve the list of data from all objects LinkedList."""
        data = []
        cur = self.head
        while cur:
            data.append(cur.data)
            cur = cur.next
        return data



