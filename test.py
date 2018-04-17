import re, time
from flask import Flask, jsonify
from flask_restful import Resource, Api
from collections import OrderedDict

app = Flask(__name__)
api = Api(app)

palindromes = {}
orderedpals = OrderedDict()

def Sanitize(input_string):
		input_string = input_string.replace(' ', '') #space deletion
		input_string = re.sub(r'[^\w\s]','',input_string) #puncuation deletion
		input_string = input_string.lower() #lower case
		return input_string

#if the input string is a palindrome add its time stamp as key to dictionary, 
#return true if palindrome, else false
class Palindrome(Resource):
	def post(self, input_string):
		newStr = Sanitize(input_string)
		if newStr == newStr[::-1]:   
			epoch_time = time.time()
			palindromes[epoch_time] = newStr
		return jsonify(newStr == newStr[::-1])

#order dictionary by order added then reverse for newest values. 
#Check for 10 mins ago, add key values until that time to new list. Return newest 10 using epoch difference
class PalindromeList(Resource):
	def get(self):
		epoch_time = time.time()
		TEN_MINUTES = 10*60
		palindromeListReturn = []
		ordered = OrderedDict(sorted(palindromes.items(), key=lambda t: t[0], reverse=True)) 
		i = 1
		for key, value in ordered.items():
			if i > 10:
				break
			i = i + 1
			time_passed = epoch_time - TEN_MINUTES
			if time_passed < key:
				palindromeListReturn.append(value)
		return jsonify(palindromeListReturn)


api.add_resource(Palindrome, '/palindrome/<input_string>')
api.add_resource(PalindromeList, '/palindrome/')


if __name__ == '__main__':
    app.run(debug=True)