import unittest
from app import app
import json

class TestApp(unittest.TestCase):
	def test_index_method(self):
		response = app.test_client().get('/')
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.data, '<html ng-app="myApp">\n\t<head>\n\t\t<script src="/static/angular.min.js"></script>\n\t</head>\n\t<body>\n\t\t<h1>Test!</h1>\n\t</body>\n</html>')

	def test_data_returns_jsonified_data(self):
		response = app.test_client().get('/data')
		expected_names = ["Brain", "Jacob", "Julie", "Jennifer"]
		response_data = json.loads(response.data)
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response_data['names'], expected_names)
		

if __name__ == '__main__':
    unittest.main()