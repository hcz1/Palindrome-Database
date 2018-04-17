import unittest
import requests
import json

class TestPalindrome(unittest.TestCase):
    def test_for_palindrome(self):
    	response = requests.post('http://127.0.0.1:5000/palindrome/abba')
        assert "true" in response.text

class TestNonPalindrome(unittest.TestCase):
	def test_for_non_palindrome(self):
	    response = requests.post('http://127.0.0.1:5000/palindrome/abbaa')
	    assert "false" in response.text

class TestSanitise(unittest.TestCase):
	def test_sanitise(self):
		requests.post('http://127.0.0.1:5000/palindrome/Dammit I\'m Mad')
		response = requests.get('http://127.0.0.1:5000/palindrome/')
		assert 'dammitimmad' in response.text

class TestGET(unittest.TestCase):
	def test_get(self):
		originalList = ['racecar', 'civic', 'noon', 'mom', 'level', 'moom', 'lol', 'madam', 'rotor', 'stats', 'wow']
		for item in originalList:
			requests.post('http://127.0.0.1:5000/palindrome/'+item)
		response = requests.get('http://127.0.0.1:5000/palindrome/')
		assert "racecar" not in response.text
		
		
		
		

if __name__ == "__main__":
    unittest.main()