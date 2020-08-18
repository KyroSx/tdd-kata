import unittest

from client import Client
from clients_repository import ClientsRepository


class ClientsRepositoryTest(unittest.TestCase):

    CLIENT_NAME: str = "Client Name"

    def setUp(self):
        self.sut = ClientsRepository()

    def test_default_list_on_init(self):
        """ :: it should have default clients as [] on init """

        self.assertListEqual(self.sut.clients, [])

    def test_save_method(self):
        """ :: it should be able to add new Client on list """

        client = Client(self.CLIENT_NAME, 42.0)

        self.assertListEqual(self.sut.clients,
                             [])

        self.sut.save(client)

        self.assertListEqual(self.sut.clients,
                             [client])

    def test_calculate_mean(self):
        client_list = [Client(self.CLIENT_NAME, 12.21),
                       Client(self.CLIENT_NAME, 34.43),
                       Client(self.CLIENT_NAME, 42.00)]

        self.sut.clients = client_list

        mean = self.sut.calculate_mean()

        self.assertAlmostEqual(mean, 29.546666666667)

    def test_get_clients_with_purchase_over(self):
        """ :: it should be able to return a client List with client.purchase >= over value """
        OVER_VALUE = 20.0

        client_list = [Client(self.CLIENT_NAME, 20.0),
                       Client(self.CLIENT_NAME, 43.3),
                       Client(self.CLIENT_NAME, 13.3)]

        self.sut.clients = client_list

        clients_with_purchase_over = self.sut.get_clients_with_purchase_over(
            OVER_VALUE)

        for client in clients_with_purchase_over:
            self.assertGreaterEqual(client.purchase_amount,
                                    OVER_VALUE)

        self.assertListEqual(clients_with_purchase_over, [
            Client(self.CLIENT_NAME, 20.0),
            Client(self.CLIENT_NAME, 43.3),
        ])
