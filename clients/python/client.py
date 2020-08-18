from dataclasses import dataclass


@dataclass
class Client:
    name: str
    purchase_amount: float


def create_client(name: str,
                  purchase_amount: float) -> Client:
    if name == '' or purchase_amount <= 0:
        raise ValueError("Invalid Input")

    client = Client(name=name,
                    purchase_amount=purchase_amount)

    return client


def create_many_clients(client_input_list: list) -> [Client]:
    client_list = [
        create_client(name=name_input,
                      purchase_amount=purchase_input)
        for name_input, purchase_input in client_input_list
    ]

    return client_list
