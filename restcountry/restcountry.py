import requests
from .country import Country

BASE_API_URL = 'https://restcountries.eu/rest/v1'


def get_response(query_string):

	"""
	This function makes a request to the API, gets the response, decodes the json
	as python list.
	:param query_string:
	:return: list containing dictionaries of country info
	"""
	response = requests.get(BASE_API_URL+query_string)

	if response.status_code == requests.codes.ok:
		countries_list = response.json()
		return countries_list

	else:
		return response.raise_for_status()


def get_by_name(country_name):
	"""
	Get all countries having name as query substring

	:param country_name: name of the country to look for
	:return: a list of Country objects
	"""

	countries_list = get_response("/name/"+country_name)
	countries_having_queried_name = []
	[countries_having_queried_name.append(Country(a_country)) for a_country in countries_list]
	return countries_having_queried_name

def get_by_capital(capital_name):
	"""
	Get all countries whose Capital contains the queried substring
	:param capital_name:
	:return: a list of Country objects
	"""

	countries_list = get_response("/capital/"+capital_name)
	countries_having_queried_capital = []
	[countries_having_queried_capital.append(Country(a_country)) for a_country in countries_list]
	return countries_having_queried_capital


def get_by_region(region_name):

	"""
	get all countries in a particular region like Asia, Africa, etc.

	:param region_name:
	:return: list of country objects
	"""
	countries_list = get_response("/region/"+region_name)
	countries_in_region = []
	[countries_in_region.append(Country(a_country)) for a_country in countries_list]
	return countries_in_region


