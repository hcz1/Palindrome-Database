import re, time
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

palindromes = {}


def Sanitize(input_string):
		input_string = input_string.replace(' ', '')
		input_string = re.sub(r'[^\w\s]','',input_string)
		input_string = input_string.lower()
		return input_string


class Palindrome(Resource):
	def post(self, input_string):
		newStr = Sanitize(input_string)
		if newStr == newStr[::-1]:
			epoch_time = int(time.time())
			palindromes[epoch_time] = newStr
		return newStr == newStr[::-1]

class PalindromeList(Resource):
	def get(self):
		epoch_time = int(time.time())
		TEN_MINUTES = 10*60
		palindromeListReturn = []
		for key, value in palindromes.items():
			time_passed = epoch_time - TEN_MINUTES
			if time_passed < key:
				palindromeListReturn.insert(0,value)
		return palindromeListReturn



api.add_resource(Palindrome, '/palindrome/<input_string>')
api.add_resource(PalindromeList, '/palindrome/')


if __name__ == '__main__':
    app.run(debug=True)