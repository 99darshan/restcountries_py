
class Country:
	def __init__(self, a_country):

		"""
		assign attributes to a instance of Country
		:param a_country: dictionary containing all info for a country
		"""
		self.country_name = a_country['name']
		self.area = a_country['area']
		self.latlng = a_country['latlng']
		self.currencies = a_country['currencies']
		self.subregion = a_country['subregion']
		self.relevance = a_country['relevance']
		self.callingCodes = a_country['callingCodes']
		self.alpha3Code = a_country['alpha3Code']
		self.timezones = a_country['timezones']
		self.languages = a_country['languages']
		self.population = a_country['population']
		self.capital = a_country['capital']
		self.borders = a_country['borders']
		self.demonym = a_country['demonym']
		self.topLevelDomain = a_country['topLevelDomain']
		self.altSpellings = a_country['altSpellings']
		self.translations = a_country['translations']
		self.gini = a_country['gini']
		self.alpha2Code = a_country['alpha2Code']
		self.region = a_country['region']
		self.nativeName = a_country['nativeName']

	def __repr__(self):
		return self.country_name

