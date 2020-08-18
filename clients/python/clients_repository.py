from client import Client


class ClientsRepository:
    clients: list

    def __init__(self, default_clients: list = []):
        self.clients = default_clients

    def save(self, client: Client) -> Client:
        self.clients.append(client)

        return client

    def get_clients_with_purchase_over(self,
                                       over_value: float = 0.0) -> [Client]:
        iterator = filter(lambda client: client.purchase_amount >= over_value,
                          self.clients)

        return list(iterator)

    def calculate_mean(self) -> float:
        total_clients = len(self.clients)
        total_sum = 0

        for client in self.clients:
            total_sum += client.purchase_amount

        mean = total_sum / total_clients

        return mean
