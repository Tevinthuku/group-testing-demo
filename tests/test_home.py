import unittest
from app import createapp


class RouteBasedTests(unittest.TestCase):
    def setUp(self):
        self.app = createapp()
        self.client = self.app.test_client()

    def tearDown(self):
        self.app.testing = False


class TestHome(RouteBasedTests):
    def test_base_route(self):
        res = self.client.get("/")
        print(res.status_code)
        self.assertEqual(res.status_code, 200)
