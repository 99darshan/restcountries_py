# restcountries_py
***
This is a Python wrapper library around the API provided by REST Countries v1.1.2
By calling the functions provided by *restcountries_py* you can simplify your code and access vast amount of data
about different countries. To learn more about the restcountries API, check out their website http://restcountries.eu

### Installation
***
*restcountries_py* is available on the Python Package Index(PyPi) at TODO

You can install *restcountries_py* using one of the following methods:

+ Use pip

'''
pip install restcountries_py
'''

+ Install it yourself by downloading .zip or .tar.gz file from PyPi
+ Install it on your own by downloading [source from Github](TODO: put link to github)

If you install it yourself, also install [requests](http://www.python-requests.org/en/latest/).

### Example Usage
***

Once you have the *restcountries_py* installed, you could start playing around.

First, import the restcountry module where all the functions for finding countries are defined

'''python
>>> import restcountries_py.restcountry as rc
'''

To communicate with the REST countries API, call one of the functions provided in restcountry module. These
function return a list of Country objects. Access the instance attributes on the country objects

###### Find all countries

'''python
# find_all()
>>> all_countries = rc.find_all()

# Access attributes for a Country
>>> print(all_countries[0].country_name)
'Afghanistan'
>>> print(all_countries[0].borders)
>>> print(all_countries[0].capital)

'''


