from data import Data


class Server:
    IP = 0

    def __init__(self):
        Server.IP = Server.IP + 1
        self._ip = self.IP
        self.buffer = []
        self.router = None

    @classmethod
    def get_total_servers_number(cls):
        return f'Total number of servers in the net is {cls.IP}.'

    def get_ip(self):
        return self._ip

    def __str__(self):
        return f'{self._ip}'

    def send_data(self, data: Data):
        if isinstance(data, Data):
            if self.router:
                self.router.buffer.append(data)
            else:
                return print('Link server to the router')
        else:
            return print('Invalid data format')

    def get_data(self):
        messages = self.buffer[:]
        self.buffer.clear()
        return messages






