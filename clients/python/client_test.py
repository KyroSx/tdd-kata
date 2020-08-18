import unittest


from client import Client, create_client, create_many_clients


class ClientTest(unittest.TestCase):

    VALID_NUMBER: float = 42.00
    VALID_NAME: str = "Client Name"

    _INVALID_NUMBER_: float = -1
    _INVALID_NAME_: str = ""

    def test_is_instanciented_correctly(self):
        """:: it should create a instance of Client if input is valid"""

        client = create_client(self.VALID_NAME, self.VALID_NUMBER)

        self.assertIsInstance(client, Client)
        self.assertEqual(client.name, self.VALID_NAME)
        self.assertEqual(client.purchase_amount, self.VALID_NUMBER)

    def test_invalid_input(self):
        """ :: it should raises if data is invalid """

        with self.assertRaises(ValueError):
            create_client(self._INVALID_NAME_, self._INVALID_NUMBER_)

    def test_create_many_clients_by_list(self):
        """ :: it should create an Client list """

        client_list = create_many_clients([
            (self.VALID_NAME, self.VALID_NUMBER),
            (self.VALID_NAME, self.VALID_NUMBER),
            (self.VALID_NAME, self.VALID_NUMBER),
        ])

        for client in client_list:
            self.assertIsInstance(client, Client)
            self.assertEqual(client.name, self.VALID_NAME)
            self.assertEqual(client.purchase_amount, self.VALID_NUMBER)

    def test_create_many_clients_with_invalid_input(self):
        """ :: it should raises if Client list is invalid """

        with self.assertRaises(ValueError):
            create_many_clients([
                (self.VALID_NAME, self.VALID_NUMBER),
                (self._INVALID_NAME_, self.VALID_NUMBER),
            ])

        with self.assertRaises(ValueError):
            create_many_clients([
                (self.VALID_NAME, self.VALID_NUMBER),
                (self.VALID_NAME, self._INVALID_NUMBER_),
            ])
