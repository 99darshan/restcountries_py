import requests
from .country import Country

BASE_API_URL = 'https://restcountries.eu/rest/v1'


def get_response(query_string):

	"""
	This function makes a request to the API, gets the response, decodes the json
	as python list.
	:param query_string:
	:return: list of dictionaries. Each dictioanry contains all info about a country
	"""
	response = requests.get(BASE_API_URL+query_string)

	if response.status_code == requests.codes.ok:
		countries_info = response.json()
		return countries_info

	else:
		return response.raise_for_status()


def find_by_name(country_name):
	"""
	find all countries having name as query substring

	:param country_name: name of the country to look for
	:return: a list of Country objects
	"""

	countries_info = get_response("/name/"+country_name)
	countries_having_queried_name = []
	[countries_having_queried_name.append(Country(a_country)) for a_country in countries_info]
	return countries_having_queried_name


def find_by_capital(capital_name):
	"""
	find all countries whose Capital contains the queried substring
	:param capital_name:
	:return: a list of Country objects
	"""

	countries_info = get_response("/capital/"+capital_name)
	countries_having_queried_capital = []
	[countries_having_queried_capital.append(Country(a_country)) for a_country in countries_info]
	return countries_having_queried_capital


def find_by_region(region_name):

	"""
	find all countries in a region (asia, africa, americas, oceania, europe)

	:param region_name:
	:return: list of country objects
	"""

	countries_info = get_response("/region/"+region_name)
	countries_in_region = []
	[countries_in_region.append(Country(a_country)) for a_country in countries_info]
	return countries_in_region


def find_by_callingcode(code_num):

	"""
	find all countries having the queried number as calling code

	:param code_num:
	:return: list of country objects
	"""
	countries_info = get_response("/callingcode/"+code_num)
	countries_with_callingcode = []
	[countries_with_callingcode.append(Country(a_country)) for a_country in countries_info]
	return countries_with_callingcode


def find_by_currency(currency):

	"""
	find all countries using the queried currency

	:param currency:
	:return: list of country objects
	"""

	countries_info = get_response("/currency/"+currency)
	countries_using_currency = []
	[countries_using_currency.append(Country(a_country)) for a_country in countries_info]
	return countries_using_currency

def find_by_countrycodes(code_list):

	"""
	find all countries for the Alpha 2 or Alpha 3 country codes in the query

	:param code_list: list containing country codes
	:return: list of Country objects
	"""

	query = "/alpha/?codes="
	for code in code_list:
		query += code+";"

	countries_info = get_response(query)
	countries_with_codes = []
	[countries_with_codes.append(Country(a_country)) for a_country in countries_info]
	return countries_with_codes