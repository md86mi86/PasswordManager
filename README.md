
# PasswordManager

A Python package for generating and validating strong passwords based on various criteria.

## Features:
- **Generate passwords** with customizable settings:
  - Include uppercase letters
  - Include numbers
  - Include special characters
  - Specify password length
- **Validate password strength** to ensure secure password creation.

## Installation

You can clone the repository to your local machine using the following command:

```bash
git clone https://github.com/md86mi86/PasswordManager.git
```

## Usage

1. **Create an instance of the `PasswordManager` class**:
   ```python
   from PasswordManager import PasswordManager
   
   manager = PasswordManager()
   ```

2. **Generate a password** with customizable options:
   ```python
   password = manager.generatePassword(length=12, includeUppercase=True, includeNumbers=True, includeSpecialCharacters=True)
   print(password)
   ```

   - `length`: The length of the generated password (must be an integer).
   - `includeUppercase`: Boolean, whether to include uppercase letters in the password (default is `False`).
   - `includeNumbers`: Boolean, whether to include numbers (default is `False`).
   - `includeSpecialCharacters`: Boolean, whether to include special characters (default is `False`).

3. **Validate the strength of a password**:
   ```python
   strength = manager.validatePasswordStrength(password)
   print(strength)
   ```

   - Returns:
     - "Password is very weak"
     - "Password is weak"
     - "Password is average"
     - "Password is good"
     - "Password is strong"
     - "Password is very strong"

## Example

```python
from PasswordManager import PasswordManager

manager = PasswordManager()

# Generate a password of length 12, including uppercase letters, numbers, and special characters
password = manager.generatePassword(length=12, includeUppercase=True, includeNumbers=True, includeSpecialCharacters=True)
print(f"Generated password: {password}")

# Validate password strength
strength = manager.validatePasswordStrength(password)
print(f"Password strength: {strength}")
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
