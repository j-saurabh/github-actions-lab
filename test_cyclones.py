"""A module for testing"""

import unittest

from main import API


class CyclonesTests(unittest.TestCase):
    """Tests for the Cyclones"""

    def setUp(self):
        """Create a test client for the app"""
        self.app = API.test_client()

    def test_guid(self):
        """test_guid: a request for the guid shall return 200 OK"""
        res = self.app.get("/7d3c9c4f-1f3e-4f1d-a4c2-9d1a6c3f7b21")
        assert res.status == "200 OK"

    def test_json(self):
        """test_json: a request for the guid shall return the defined JSON"""
        res = self.app.get("/7d3c9c4f-1f3e-4f1d-a4c2-9d1a6c3f7b21")
        assert res.json == {
            "guid": "7d3c9c4f-1f3e-4f1d-a4c2-9d1a6c3f7b21",
            "latlong": "29.651634,-82.324826",
            "location": "Gainesville, FL, USA",
            "mascot": "Albert",
            "nickname": "Gators",
            "school": "University of Florida",
        }


if __name__ == "__main__":
    unittest.main()
