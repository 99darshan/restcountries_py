# restcountries_py
***
This is a Python wrapper library around the API provided by REST Countries v1.1.2

By calling the functions provided by *restcountries_py* you can simplify your code and access vast amount of data
about different countries. To learn more about the restcountries API, check out their website http://restcountries.eu

### Installation
***
*restcountries_py* is available on the Python Package Index(PyPi) at https://pypi.python.org/pypi/restcountries_py/0.1.3

You can install *restcountries_py* using one of the following methods:

+ Use pip

```
pip install restcountries_py
```

+ Install it yourself by downloading .zip or .tar.gz file from PyPi
+ Install it on your own by downloading [source from Github](https://github.com/99darshan/restcountries_py)

If you install it yourself, also install [requests](http://www.python-requests.org/en/latest/).

### Example Usage
***

Once you have the *restcountries_py* installed, you could start playing around.

First, import the restcountry module where all the functions for finding countries are defined.

```python
>>> import restcountries_py.restcountry as rc
```

To communicate with the REST countries API, call one of the functions provided in restcountry module. These
function return a list of Country objects. Access the instance attributes on the Country objects.

##### Find all countries

```python
>>> all_countries = rc.find_all()

>>> print(all_countries[0].country_name)
'Afghanistan'
>>> print(all_countries[0].borders)
['IRN', 'PAK', 'TKM', 'UZB', 'TJK', 'CHN']
>>> print(all_countries[0].capital)
'Kabul'
```

##### Find by name

Find countries with the query substring in the country's name or Alternate Name (altSpellings).

Let's find all countries and their capital which have "island" in their name.

```python
>>> countries_with_island_in_name = rc.find_by_name("island")

>>> for country in countries_with_island_in_name:
	    print("{} ------------------------- {}".format(country.country_name, country.capital))

Åland Islands ------------------------- Mariehamn
British Virgin Islands ------------------------- Road Town
Cayman Islands ------------------------- George Town
Christmas Island ------------------------- Flying Fish Cove
Cocos (Keeling) Islands ------------------------- West Island
Cook Islands ------------------------- Avarua
Falkland Islands ------------------------- Stanley
Faroe Islands ------------------------- Tórshavn
Finland ------------------------- Helsinki
...
...
...
```

Find country with their name exactly matching the query string.

```python
>>> country_for_name = rc.find_by_name("United States", full_text=True)
>>> print(country_for_name[0].country_name)
'United States'
```

##### Find by currency

Let's find countries using Pound sterling as one it's currency and lies in Europe.
Use [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) currency code as argument.

```python
>>> countries_using_gbp = rc.find_by_currency("GBP")
>>> countries_in_europe_using_gbp = []
>>> [countries_in_europe_using_gbp.append(country) for country in countries_using_gbp if country.region == "Europe"]
>>> print(countries_in_europe_using_gbp)
[Guernsey, Isle of Man, Jersey, United Kingdom]
```

##### Find by language

Let's find countries with French as one of it's official languages and lies in Asia.
Use [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language code as argument.

```python
>>> countries_speaking_french = rc.find_by_lang("fr")
>>> countries_in_asia_speaking_french = []
>>> [countries_in_asia_speaking_french.append(country) for country in countries_speaking_french if country.region == "Asia"]
>>> print(countries_in_asia_speaking_french)
[Lebanon]
```

##### Find by calling code

Find all countries having +1 calling code.

```python
>>> country_with_callingcode_1 = rc.find_by_callingcode("1")
>>> for country in country_with_callingcode_1:
        print(country.country_name)
'Canada'
'United States'
```

##### Find by Country Codes

Look for countries based on their country codes. 
Use __List__ containing either [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) or [ISO 3166-1 alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) country codes as arguments.

Let's find countries with country code NP, NZL, US, HKG

```python
>>> country_for_codes = rc.find_by_countrycodes(["NP", "NZL", "US", "HKG"])
>>> print(country_for_codes)
[Nepal, New Zealand, United States, Hong Kong]
```

##### Find by Region

Look for countries in a particular region. Region may be Asia, Africa, Europe, Americas, Oceania.

Let's find all countries in region Oceania with population less than 100000

```python
>>> countries_in_oceania = rc.find_by_region("Oceania")
>>> countries_with_pop_less_than_100_thou = []
>>> [countries_with_pop_less_than_100_thou.append(country) for country in countries_in_oceania if country.population < 100000]
>>> print(countries_with_pop_less_than_100_thou)
[American Samoa, Christmas Island, Cocos (Keeling) Islands, Cook Islands, Marshall Islands, Nauru, Niue, Norfolk Island, Northern Mariana Islands, Palau, Pitcairn Islands, Tokelau, Tuvalu, Wallis and Futuna]
```

##### Find by Subregion

Look for countries in a subregion. Subregion may be Southern Asia, Eastern Europe, South America, Northern America,etc.

Let's find countries in northern america sharing borders with USA.

```python
>>> countries_in_northern_america = rc.find_by_subregion("northern america")
>>> coun_in_northern_america_border_with_usa = []
>>> [coun_in_northern_america_border_with_usa.append(country) for country in countries_in_northern_america if "USA" in country.borders]
>>> print(coun_in_northern_border_with_usa)
[Canada]
```

##### Find by Capital

Look for country by its capital.

Let's find the name and calling code of country whose capital is Kathmandu.

```python
>>> coun = rc.find_by_capital("kathmandu")
>>> print("{} has calling code {}".format(coun[0].country_name, coun[0].callingCodes))
'Nepal has calling code ['977']'
```

### Attributes 
***
Country objects have following attributes:

```
country_name, area, latlng, currencies, subregion, relevance, callingCodes, alpha3Code, timezones, 
languages, population, capital, borders, demonym, topLevelDomain, altSpellings, translations, gini,
alpha2Code, region, nativeName
```

### Credits
***
Thanks to Fayder Florez for developing [REST Countries API] (https://github.com/fayder/restcountries)


### Related Projects
***
+ [gocountries](https://github.com/alediaferia/gocountries)
+ [restcountry](https://github.com/davidesantangelo/restcountry)

### License
***
This restcountries_py package is released under MIT License.