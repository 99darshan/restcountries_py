import requests
from .country import Country

BASE_API_URL = 'https://restcountries.eu/rest/v1'


def get_response(query_string):
	"""
	This function makes a request to the API, gets the response, decodes the json
	as python list.
	:param query_string:
	:return: list of dictionaries. Each dictionary contains all info about a country
	"""
	response = requests.get(BASE_API_URL + query_string)

	if response.status_code == requests.codes.ok:
		countries_info = response.json()
		return countries_info

	else:
		return response.raise_for_status()


def get_country_objects(info_about_countries):
	"""
	:param info_about_countries: list of dictionaries. Each dictionary contains all info about a country
	:return: list of Country objects
	"""
	countries = []
	[countries.append(Country(a_country)) for a_country in info_about_countries]
	return countries


def find_all():
	"""
	find all countries available

	:return: list of Country objects
	"""

	countries_info = get_response("/all/")
	return get_country_objects(countries_info)


def find_by_name(country_name, full_text=False):
	"""
	find all countries having name as query

	:param country_name: name of the country to look for
	:param full_text: checks whether to find countries name using fullText or Substring
	:return: a list of Country objects

	"""

	# if fullText is True, get country whose name matches query string
	if full_text:
		countries_info = get_response("/name/" + country_name + "?fullText=true")
		return get_country_objects(countries_info)

	# return all countries having query as substring in their name
	else:
		countries_info = get_response("/name/" + country_name)
		return get_country_objects(countries_info)


def find_by_capital(capital_name):
	"""
	find all countries whose Capital contains the queried substring
	:param capital_name:
	:return: a list of Country objects
	"""

	countries_info = get_response("/capital/" + capital_name)
	return get_country_objects(countries_info)


def find_by_region(region_name):
	"""
	find all countries in a region (asia, africa, americas, oceania, europe)

	:param region_name:
	:return: list of country objects
	"""

	countries_info = get_response("/region/" + region_name)
	return get_country_objects(countries_info)


def find_by_callingcode(code_num):
	"""
	find all countries having the queried number as calling code

	:param code_num:
	:return: list of country objects
	"""
	countries_info = get_response("/callingcode/" + code_num)
	return get_country_objects(countries_info)


def find_by_currency(currency):
	"""
	find all countries using the queried currency

	:param currency:
	:return: list of country objects
	"""

	countries_info = get_response("/currency/" + currency)
	return get_country_objects(countries_info)


def find_by_countrycodes(code_list):
	"""
	find all countries for all Alpha 2 or Alpha 3 country codes in the query

	:param code_list: list containing country codes
	:return: list of Country objects
	"""

	query = "/alpha/?codes="
	for code in code_list:
		query += code + ";"

	countries_info = get_response(query)
	return get_country_objects(countries_info)


def find_by_lang(language):
	"""
	find all countries speaking the language queried

	:param language:
	:return: list of Country objects
	"""

	countries_info = get_response("/lang/" + language)
	return get_country_objects(countries_info)


def find_by_subregion(sub_region):
	"""
	find all countries in queried sub_region
	:param sub_region: String
	:return: list of Country objects
	"""

	countries_info = get_response("/subregion/" + sub_region)
	return get_country_objects(countries_info)
