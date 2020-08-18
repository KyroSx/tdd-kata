import locale

from input_output import read_many_inputs_times
from client import create_many_clients
from clients_repository import ClientsRepository


class Main:

    OVER_VALUE: float = 20.0

    def execute(self):

        input_list = read_many_inputs_times(2)
        clients_list = create_many_clients(input_list)

        clientsRepository = ClientsRepository(clients_list)

        clients_with_purchase_over = clientsRepository.get_clients_with_purchase_over(
            self.OVER_VALUE)

        clients = clientsRepository.clients

        mean = clientsRepository.calculate_mean()

        self.print_client_list(before_text="All Clients: ",
                               client_list=clients)

        self.print_client_list(before_text=f"All Clients Over: {self.OVER_VALUE}",
                               client_list=clients_with_purchase_over,)

        print("Mean: ", end="")
        self.print_float_as_money(value=mean)

    def print_client_list(self, client_list: list, before_text="\n") -> None:
        print(before_text)

        for client in client_list:
            print(
                F"Client: {client.name}, payed: ", end="")
            self.print_float_as_money(client.purchase_amount)

    def print_float_as_money(self, value: float):
        print(f"$ {round(value, 2)}")


if __name__ == "__main__":
    Main().execute()
