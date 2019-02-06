import unittest
import json

from tests.v1 import RouteBasedTests


class TestHome(RouteBasedTests):

    def test_get_offices(self):
        res = self.client.get("/api/v1/offices")
        result = json.loads(res.data.decode('utf-8'))
        self.assertEqual(result['data'], [])
        self.assertEqual(result["status"], 200)
        self.assertEqual(res.status_code, 200)

    def test_wrong_post_format(self):
        res = self.client.post(
            "api/v1/offices", data=json.dumps({
                "type": "erew",
                "name": "djkjweyr"
            }), content_type="application/json")
        result = json.loads(res.data.decode('utf-8'))
        self.assertEqual(result['status'], 400)
