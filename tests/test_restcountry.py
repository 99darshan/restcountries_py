"""
This test suite test functions in restcountry module
"""

import unittest
import restcountry as rc
from restcountry import restcountry as rc




class TestRestcountry(unittest.TestCase):

	def test_get_by_name(self):
		# expect Country object with name attribute Nepal
		self.assertTrue("Nepal", rc.get_by_name("Nepal").name)
		# expect Country
		#
		# object with capital attribute Ottawa
		self.assertTrue("Ottawa", rc.get_by_name("Canada").capital)

if __name__ == '__main__':
	unittest.main()

