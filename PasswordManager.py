import random
import string

class PasswordManager:
    
    def __init__(self):
        pass
    
    def _get_characters(self, includeUppercase: bool, includeNumbers: bool, includeSpecialCharacters: bool):
        spacialChar = "@#$%*!?_=+"
        characters = string.ascii_lowercase
        if includeUppercase:
            characters += string.ascii_uppercase
        if includeNumbers:
            characters += string.digits
        if includeSpecialCharacters:
            characters += spacialChar
        return characters
    
    def generatePassword(self, length: int,includeUppercase: bool = False, includeNumbers: bool = False, includeSpecialCharacters: bool = False):

        spacialChar = "@#$%*!?_=+"
        password = random.choice(string.ascii_lowercase)
        if includeUppercase == True:
            password += random.choice(string.ascii_uppercase)
        if includeNumbers == True:
            password += random.choice(string.digits)
        if includeSpecialCharacters == True:
            password += random.choice(spacialChar)
        remaining_length = length - len(password)
        for i in range(remaining_length):
            password += random.choice(self._get_characters(includeUppercase, includeNumbers, includeSpecialCharacters))
        return password
    