from unittest import TestCase
from app import app
from converter import Converter, all_currencies_unfiltered

class FlaskTests(TestCase):

    def setUp(self):
        """Stuff to do before every test."""
        self.conv = Converter()
        self.client = app.test_client()
        app.config['TESTING'] = True


    def test_homepage(self):
        """Make sure information is in the session and HTML is displayed"""

        with self.client:
            response = self.client.get('/')
            self.assertIn(b'<h1>Live Forex Converter</h1>', response.data)

    def test_convert_forex_post(self):
        # Send a POST request to the convert endpoint with sample data
        response = self.client.post('/convert', data={
            'base': 'USD',
            'final': 'USD',
            'amount': '10'
        })
        # Check if the response is 200 OK
        self.assertEqual(response.status_code, 200)

        self.assertIn(b"<b>10", response.data)

    def test_get_curr(self):
        # Test if the get_curr method returns the correct list of currency codes.
        result = self.conv.get_curr(all_currencies_unfiltered)
        self.assertIn('USD', result)
        self.assertIn('EUR', result)
        # You can add more currencies to check here.

    def test_check_valid_currency(self):
        # Test if the check_valid_currency method correctly identifies valid currencies.
        self.assertTrue(self.conv.check_valid_currency('USD'))
        self.assertFalse(self.conv.check_valid_currency('FAKE'))


    def test_getData(self):
        # Test if the getData method successfully gets conversion data.

        result = self.conv.getData('USD', 'EUR', 10)
        self.assertNotEqual(result, -1)  # Assuming -1 is returned for an error.

    def test_process_conversion(self):
        # Test the complete process_conversion method for valid input.
        result = self.conv.process_conversion('USD', 'EUR', 10)
        self.assertEqual(result[0], 'ok')
        # Add tests for invalid inputs as well.
        result = self.conv.process_conversion('FAKE', 'EUR', 10)
        self.assertEqual(result[0], 'err')
        result = self.conv.process_conversion('USD', 'FAKE', 10)
        self.assertEqual(result[0], 'err')
        result = self.conv.process_conversion('USD', 'EUR', 'invalid_amount')
        self.assertEqual(result[0], 'err')

