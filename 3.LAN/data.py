class Data:
    def __init__(self, data, dest_ip):
        self.data = data
        self.ip = dest_ip

    def __str__(self):
        return f'{self.data}'

    def __repr__(self):
        return f'{self.data} --> {self.ip}'
