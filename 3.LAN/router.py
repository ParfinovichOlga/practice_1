from server import Server


class Router:
    def __init__(self):
        self.buffer = []
        self.linked_servers = set()

    def link(self, server: Server):
        if isinstance(server, Server):
            self.linked_servers.add(server)
            server.router = self
        else:
            return print("Server wasn't added to the router.")

    def unlink(self, server: Server):
        try:
            self.servers.remove(server)
        except KeyError:
            return print(f'Server {server} is not linked to the router.')

    def send_data(self):
        for message in self.buffer:
            try:
                server = next(s for s in self.linked_servers if s.get_ip() == message.ip)
            except StopIteration:
                return print(f"Message to server {message.ip} wasn't sent: server doesn't link to the router.")
            server.buffer.append(message)
        self.buffer.clear()
