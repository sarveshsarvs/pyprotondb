import unittest
from pyprotondb import ProtonDBClient

HOST = "127.0.0.1"
PORT = 9090
USERNAME = "admin123"
PASSWORD = "welcome"

class TestProtonDBClient(unittest.TestCase):
    def setUp(self):
        # Setup a client connection (mock server recommended for real tests)
        self.client = ProtonDBClient(HOST, PORT, USERNAME, PASSWORD)

    def tearDown(self):
        self.client.close()

    def test_create_db(self):
        response = self.client.driver.create_db("test_db")
        self.assertEqual(response["Status"].lower(), "ok")

    def test_insert_document(self):
        doc = {"name": "Sarvesh", "role": "developer"}
        response = self.client.driver.insert_document("test_db.users", doc)
        self.assertEqual(response["Status"].lower(), "ok")

if __name__ == '__main__':
    unittest.main()
