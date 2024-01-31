import unittest
from unittest.mock import patch
import tkinter as tk
from tkinter import messagebox
from logpassform import LoginForm, login, login_with_session
import random
import string

class TestLoginFormSecurity(unittest.TestCase):

    def setUp(self):
        self.root = tk.Tk()
        self.app = LoginForm(self.root)

    def tearDown(self):
        self.root.destroy()

    def test_sql_injection_attack(self):
        username = "hacker_user'; DROP TABLE users;"
        password = "password123"
        result = login(username, password)
        self.assertFalse(result)  # Checking the query for SQL injection

    def test_cross_site_scripting(self):
        username = "<script>alert('XSS');</script>"
        password = "password4123"
        result = login(username, password)
        self.assertFalse(result)  # Check for XSS attacks

    def test_bruteforce_attack(self):
        username = "user13223"
        password_list = ["password221", "password332", "password113"]
        
        for password in password_list:
            result = login(username, password)
            self.assertFalse(result)  # Check for Brut force attacks


    def test_dictionary_attack(self):
        usernames = ["user1", "user2", "user3"] # Brute force login using dictionary
        password = "password123" 

        for username in usernames:
            result = login(username, password)
            self.assertFalse(result, f"Failed for username: {username}")

    def test_password_dictionary_attack(self):
        username = "user123"
        passwords = ["pass123", "password123", "letmein"] # Brute force password using dictionary

        for invalid_password in passwords:
            result = login(username, invalid_password)
            self.assertFalse(result, f"Failed for password: {invalid_password}")

    def test_combined_dictionary_attack(self):
        usernames = ["user1", "user2", "user3"]
        passwords = ["pass123", "password123", "letmein"] # Brute force login and password using dictionary

        for username in usernames:
            for invalid_password in passwords:
                result = login(username, invalid_password)
                self.assertFalse(result, f"Failed for username: {username}, password: {invalid_password}")

    def test_complex_password_formats_attack(self):
        username = "user123"
        passwords = ["Pass@123", "123456", "AbCdEfG!@#"] # Brute force complex password formats  using dictionary

        for invalid_password in passwords:
            result = login(username, invalid_password)
            self.assertFalse(result, f"Failed for password: {invalid_password}")

    def test_special_characters_attack(self):
        username = "user123"
        passwords = ["!@#$%^&*()", "_+{}|:<>?"] # Brute force spec characters passsword using dictionary

        for invalid_password in passwords:
            result = login(username, invalid_password)
            self.assertFalse(result, f"Failed for password: {invalid_password}")

    def test_case_insensitivity_attack(self):
        username = "user123"
        passwords = ["PassWord123", "pAsSwOrD123", "PASSWORD123"] # Brute force case intensitivity password using dictionary

        for invalid_password in passwords:
            result = login(username, invalid_password)
            self.assertFalse(result, f"Failed for password: {invalid_password}")

    def test_combined_complex_attack(self):
        usernames = ["user1", "user2", "user3"]
        passwords = ["Pass@123", "123456", "AbCdEfG!@#"] # Brute force combined complex login and password using dictionary

        for username in usernames:
            for invalid_password in passwords:
                result = login(username, invalid_password)
                self.assertFalse(result, f"Failed for username: {username}, password: {invalid_password}")

    def test_random_combinations_attack(self):
        username = "user123"
        password_length = 12
        num_tests = 10 # Brute force random combinations attack

        for _ in range(num_tests):
            invalid_password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=password_length))
            result = login(username, invalid_password)
            self.assertFalse(result, f"Failed for random password: {invalid_password}")

    def test_session_fixation_attack(self):
        username = "user123324"
        password = "password1234234"
        
        initial_session = login(username, password)

        result = login_with_session(username, password, initial_session)
        self.assertFalse(result)  # Checking the system's resistance to session fixation attacks

if __name__ == '__main__':
    unittest.main()
