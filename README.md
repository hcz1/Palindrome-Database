# Palindrome-Database

## Prerequisites
 - Python 3 
 - pip3
 - flask
 - flask_restful

### How to run
  * python test.py
 
### Usage
* Use localhost/<nominated_port>
* /palindrome/<inputstring>
    * POST Request 
    * Returns true if palindrome, else false
    * Stores palindromes in dictionary
* /palindrome
    * GET Request
    * returns list of last 10 palindromes entered in the last 10 minutes
     
