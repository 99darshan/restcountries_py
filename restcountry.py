import requests

BASE_API_URL = 'https://restcountries.eu/rest/v1/'


def get_response(query_string):

	'''
	This function makes a request to the API, gets the response, decodes the json
	as python list.

	prams: query string to append to  BASE_API_URL
	returns: list containing dictionary of country info 
	'''

	response = requests.get(BASE_API_URL+'query_string')

	if response.status_code == requests.code.ok:
		response.encoding('utf-8')
		countries_list = response.json()
		return countries_list

	else:
		return response.raise_for_status()





		


