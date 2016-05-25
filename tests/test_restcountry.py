"""
This test suite test functions defined in restcountry module
"""

import unittest
import requests
from restcountry import restcountry as rc


class TestRestcountry(unittest.TestCase):


	def test_get_response(self):

		self.assertIsInstance(rc.get_response("/capital/london"), list, "Return type should be a list")

		response_for_all_countries = rc.get_response("/all/")

		for item in response_for_all_countries:
			self.assertIsInstance(item, dict, "All items of response list should be a dictionary")


	def test_find_all(self):

		all_countries = rc.find_all()
		for a_country in all_countries:
			self.assertTrue(hasattr(a_country,"callingCodes"), "Country object has attribute callingCodes")
			self.assertTrue(hasattr(a_country,"alpha2Code"), "Country object has attribute alpha2Code")


	def test_find_by_name(self):

		# Tests  when fullText is default value False
		countries_having_name_island = rc.find_by_name("island")

		has_island_in_country_name = False
		does_not_have_island_in_country_name = False

		for a_country in countries_having_name_island:
			self.assertTrue("land" in a_country.name or a_country.altSpellings, "name of all Country should have substring land")
			self.assertTrue(hasattr(a_country, 'callingCodes'), "Country object should have attribute callingCode")

			if a_country.latlng == [-8.0,159.0]:
				has_island_in_country_name = True

			if a_country.capital == "Cairo":
				does_not_have_island_in_country_name = True

		self.assertTrue(has_island_in_country_name, "Country with latlng [-8.0,159.0] is Solomon Islands")
		self.assertFalse(does_not_have_island_in_country_name, "Cairo is capital of Egypt, it doesn't have island in name")

		# Tests when fullText is True
		country_fullText = rc.find_by_name("Cayman Islands", fullText=True)

		for con in country_fullText:
			self.assertEqual("George Town", con.capital, "Country Cayman Islands should have capital George Town")
			self.assertTrue(".ky" in con.topLevelDomain, ".ky is top level domain of Cayman Islands")

			self.assertTrue("Solomon Islands" not in con.name, "Solomon Islands does not have name Cayman Islands")

		# Test that find_by_name raises HTTPError when finding country with name Islands and fullText=True
		with self.assertRaises(requests.HTTPError):
			rc.find_by_name("Islands", fullText=True)



	def test_find_by_capital(self):

		countries_having_ton_in_capital = rc.find_by_capital("ton")

		has_ton_in_capital = False
		does_not_have_ton_in_capital = False

		for a_country in countries_having_ton_in_capital:
			self.assertTrue("ton" in a_country.capital, "capital attribute of all Country should have substring ton")
			self.assertTrue(hasattr(a_country, 'timezones'), "Country object should have attribute timezones")

			if a_country.alpha2Code == "US":
				has_ton_in_capital = True
			if a_country.alpha2Code == "CN":
				does_not_have_ton_in_capital = True

		self.assertTrue(has_ton_in_capital, "Country US has substring ton in its capital")
		self.assertFalse(does_not_have_ton_in_capital, "Country CN has no substring ton in its capital")

	def test_find_by_region(self):

		asian_countries = rc.find_by_region("asia")

		is_china_in_asia = False
		is_capital_jerusalem_in_asia = False
		is_poland_in_asia = False

		for a_country in asian_countries:
			self.assertTrue("Asia" in a_country.region, "All Country should have region attribute equal to asia")
			self.assertTrue(hasattr(a_country, "languages"))

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
		does_not_have_callingcode_1 = False

		for a_country in countries_with_callingcode_1:
			self.assertTrue(hasattr(a_country, "topLevelDomain"),"Country should have topLevelDomain attribute")
			self.assertTrue("1" in a_country.callingCodes, "All Country objects should have callingCodes 1")

			if a_country.name == "Canada":
				has_callingcode_1 = True

			if a_country.capital == "Kathmandu":
				does_not_have_callingcode_1 = True

		self.assertTrue(has_callingcode_1, "Canada should be one of the country with calling code 1")
		self.assertFalse(does_not_have_callingcode_1, "Country with capital kathmandu does not have calling code 1")

	def test_find_by_currency(self):

		countries_using_usd = rc.find_by_currency("usd")

		has_usd_as_currency = False
		does_not_has_usd_as_currency = False

		for a_country in countries_using_usd:
			self.assertTrue("USD" in a_country.currencies, "all countries should have USD in currencies")
			self.assertTrue(hasattr(a_country, "topLevelDomain"), "Country should have topLevelDomain attribute")

			if a_country.name == "Guam":
				has_usd_as_currency = True

			if a_country.name == "Nepal":
				does_not_has_usd_as_currency = True

		self.assertTrue(has_usd_as_currency,"Guam uses USD")
		self.assertFalse(does_not_has_usd_as_currency, "Nepal does not use USD")


	def test_find_by_countrycodes(self):

		query_codes = ["np","co","nzl"]
		countries_with_countrycodes = rc.find_by_countrycodes(query_codes)

		for a_country in countries_with_countrycodes:
			self.assertTrue(a_country.alpha2Code or a_country.alpha3Code in query_codes,
													" one of np, co, nzl should be	 in alpha 2,3 of Country")

			self.assertTrue(hasattr(a_country,"callingCodes"), "Country object has callingCodes attribute")


	def test_find_by_lang(self):

		countries_speaking_en = rc.find_by_lang("en")

		speak_en = False
		does_not_speak_en = False

		for a_country in countries_speaking_en:

			self.assertTrue("en" in a_country.languages, "Country should have en as one of its languages")
			self.assertTrue(hasattr(a_country,"alpha2Code"), "Country object has attribute alpha2Code")

			if a_country.alpha3Code == "NZL":
				speak_en = True

			if a_country.name == "Nepal":
				does_not_speak_en = False

		self.assertTrue(speak_en, "People in New Zealand speak English")
		self.assertFalse(does_not_speak_en, "Nepalese do not speak English")


	def test_find_by_subregion(self):

		countries_in_southern_asia = rc.find_by_subregion("southern asia")

		is_in_southern_asia = False
		is_not_in_southern_asia = False

		for a_country in countries_in_southern_asia:
			self.assertTrue("Asia" in a_country.region, "Every country in sub region southern asia is in region Asia")
			self.assertTrue(hasattr(a_country,"languages"), "Country object has attribute languages")

			if a_country.name == "Pakistan":
				is_in_southern_asia = True

			if a_country.name == "Belgium":
				is_not_in_southern_asia = True

		self.assertTrue(is_in_southern_asia, "Pakistan is in Southern Asia")
		self.assertFalse(is_not_in_southern_asia, "Belgium is not in Southern Asia")



if __name__ == '__main__':
	unittest.main()


