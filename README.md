
# PasswordManager

A Python package for generating and validating strong passwords based on various criteria.

## Features:
- **Generate passwords** with customizable settings:
  - Include uppercase letters
  - Include numbers
  - Include special characters
  - Specify password length
- **Validate password strength** to ensure secure password creation.
- **Manage passwords** by saving them to a file for easy access.
- **Generate random passwords** with random settings for length, uppercase, numbers, and special characters.

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

4. **Manage passwords** by saving them to a file:
   ```python
   manager.managePassword(name="Instagram", username="user123", password="mypassword")
   ```

   - Saves the following data to a file named `social_media.txt`:
     ```
     {
         "social_media": "Instagram",
         "username": "user123",
         "password": "mypassword"
     }
     ```
   - Prints `Data saved successfully!` upon success.

5. **Generate a random password** with random settings for length, uppercase, numbers, and special characters:
   ```python
   random_password = manager.randomPassword()
   print(random_password)
   ```

   - Generates a password with random choices for length, whether to include uppercase letters, numbers, and special characters.

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

# Save the password to a file
manager.managePassword(name="Instagram", username="user123", password=password)

# Generate a random password
random_password = manager.randomPassword()
print(f"Random password: {random_password}")
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
