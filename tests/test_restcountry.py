"""
This test suite test functions defined in restcountry module
"""

import unittest
import restcountry as rc
from restcountry import restcountry as rc


class TestRestcountry(unittest.TestCase):

	# TODO test get_response

	def test_find_by_name(self):

		countries_having_name_island = rc.find_by_name("island")

		has_island_in_country_name = False

		does_not_have_island_in_country_name = True

		for a_country in countries_having_name_island:
			self.assertTrue("land" in a_country.name or a_country.altSpellings, "name of all Country should have substring land")
			self.assertTrue(hasattr(a_country, 'callingCodes'), "Country object should have attribute callingCode")

			if a_country.latlng == [-8.0,159.0]:
				# Country with latlng [-8.0,159.0] is Solomon Islands
				has_island_in_country_name = True

			if a_country.capital == "Cairo":
				# Cairo is capital of Egypt, it doesn't have island in its name
				does_not_have_island_in_country_name = False

		self.assertTrue(has_island_in_country_name, "Country with latlng [-8.0,159.0] is Solomon Islands")
		self.assertTrue(does_not_have_island_in_country_name, "Cairo is capital of Egypt, it doesn't have island in name")

	def test_find_by_capital(self):

		countries_having_ton_in_capital = rc.find_by_capital("ton")

		has_ton_in_capital = False
		does_not_have_ton_in_capital = True

		for a_country in countries_having_ton_in_capital:
			self.assertTrue("ton" in a_country.capital, "capital attribute of all Country should have substring ton")
			self.assertTrue(hasattr(a_country, 'timezones'), "Country object should have attribute timezones")

			if a_country.alpha2Code == "US":
				has_ton_in_capital = True
			if a_country.alpha2Code == "CN":
				does_not_have_ton_in_capital = False

		self.assertTrue(has_ton_in_capital, "Country US has substring ton in its capital")
		self.assertTrue(does_not_have_ton_in_capital, "Country CN has no substring ton in its capital")

	def test_find_by_region(self):

		asian_countries = rc.find_by_region("asia")

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


	def test_find_by_callingcode(self):

		countries_with_callingcode_1 = rc.find_by_callingcode("1")

		has_callingcode_1 = False
		does_not_have_callingcode_1 = True

		for a_country in countries_with_callingcode_1:
			self.assertTrue(hasattr(a_country, "topLevelDomain"),"Country should have topLevelDomain attribute")
			self.assertTrue("1" in a_country.callingCodes, "All Country objects should have callingCodes 1")

			if a_country.name == "Canada":
				has_callingcode_1 = True

			if a_country.capital == "Kathmandu":
				does_not_have_callingcode_1 = False

		self.assertTrue(has_callingcode_1, "Canada should be one of the country with calling code 1")
		self.assertTrue(does_not_have_callingcode_1, "Country with capital kathmandu does not have calling code 1")




if __name__ == '__main__':
	unittest.main()


