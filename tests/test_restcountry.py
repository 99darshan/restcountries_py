"""
This test suite test functions defined in restcountry module
"""

import unittest
import restcountry as rc
from restcountry import restcountry as rc


class TestRestcountry(unittest.TestCase):

	# TODO test get_response

	def test_get_by_name(self):

		countries_having_name_island = rc.get_by_name("island")

		has_island_in_country_name = False

		does_not_have_island_in_country_name = True

		for a_country in countries_having_name_island:

			if(a_country.name == "Falkland Islands"):
				self.assertEqual("Stanley", a_country.capital, "capital of Falkland Islands is Stanley")

			if(a_country.callingCodes == 64):
				self.assertEqual("Pitcairn Islands", a_country.name, "64 is calling code of Pitcairn Islands")
				self.assertNotEqual("Kathmandu", a_country.capital, "Kathmandu is not the capital country with 64 code")

			if(a_country.latlng == [-8.0,159.0]):
				# Country with latlng [-8.0,159.0] is Solomon Islands
				has_island_in_country_name = True

			if(a_country.capital == "Cairo"):
				# Cairo is capital of Egypt, it doesn't have island in its name
				does_not_have_island_in_country_name = False

		self.assertTrue(has_island_in_country_name, "Country with latlng [-8.0,159.0] is Solomon Islands")
		self.assertTrue(does_not_have_island_in_country_name, "Cairo is capital of Egypt, it doesn't have island in name")

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

		self.assertTrue(is_china_in_asia, "China is in region Asia")

		self.assertTrue(is_capital_jerusalem_in_asia, "Capital city Jerusalem is in region Asia")

		self.assertFalse(is_poland_in_asia)


if __name__ == '__main__':
	unittest.main()


