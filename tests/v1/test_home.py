import unittest
from tests.v1 import RouteBasedTests


class TestHome(RouteBasedTests):
    def test_base_route(self):
        res = self.client.get("/api/v1")
        print(res.status_code)
        self.assertEqual(res.status_code, 301)
