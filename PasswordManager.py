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
        if(length < 4):
            return "min length is 4!"
        else:
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
    
    def validatePasswordStrength(self,password : str):
        hasSpecialCharacter = False
        spacialChar = "@#$%*!?_=+1234567890"
        for char in spacialChar:
                if(char in password):
                    hasSpecialCharacter = True
                    break
        if(len(password) <= 4):
            return "Password is very weak"
        elif(4 < len(password) <= 8):
            if(hasSpecialCharacter == True):
                return "Password is average"
            else:
                return "Password is weak"
        elif(8 < len(password) <= 16):
            if(hasSpecialCharacter == True):
                return "Password is strong"
            else:
                return " Password is good"
        else:
            if(hasSpecialCharacter == True):
                return "Password is very strong"
            else:
                return " Password is good"