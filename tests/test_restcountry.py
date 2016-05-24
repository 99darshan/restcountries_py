"""
This test suite test functions defined in restcountry module
"""

import unittest
import restcountry as rc
from restcountry import restcountry as rc


class TestRestcountry(unittest.TestCase):

	# TODO test get_response

	def test_get_by_name(self):

		# expect Country object with name attribute Nepal
		self.assertEqual("Nepal", rc.get_by_name("Nepal").name, "The name attribute for Country object should be Nepal")

		# expect Country object with capital attribute Ottawa
		self.assertEqual("Ottawa", rc.get_by_name("Canada").capital, "capital attribute for Country object should be Ottawa")

	def test_get_by_region(self):

		asian_countries = rc.get_by_region("asia")

		is_china_in_asia = False
		is_capital_jerusalem_in_asia = False
		is_poland_in_asia = False

		for a_country in asian_countries:
			if a_country.name == "China":
				is_china_in_asia = True
			if a_country.capital == "Jerusalem":
				is_capital_jerusalem_in_asia = True
			if a_country.name == "Poland":
				is_poland_in_asia = True

		# expect Country with name China in region Asia
		self.assertTrue(is_china_in_asia, "China is in region Asia")

		# expect Country with capital jerusalem in asia
		self.assertTrue(is_capital_jerusalem_in_asia, "Capital city Jerusalem is in region Asia")

		# expect Country Poland to not be in region Asia
		self.assertFalse(is_poland_in_asia)


if __name__ == '__main__':
	unittest.main()

	
