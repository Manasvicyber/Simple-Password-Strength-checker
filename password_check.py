def check_password_strength(password):
    if len(password) < 8:
      return "Weak: Password must be atleast 8 characters long." 

    has_number = any(char.isdigit() for char in password) 
    has_upper = any(char.isupper() for char in password)

    if has_number and has_upper:
      return "Strong Password!"
    else:
      return "Moderate: Try adding capital letters and numbers."



user_password = input("Enter a password to test: ")
print(check_password_strength(user_password))
