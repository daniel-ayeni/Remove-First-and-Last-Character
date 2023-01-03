def remove_chars(s):
  # create a new string that excludes the first and last characters of the original string
  new_s = s[1:-1]
  return new_s

# test the function
string = "Hello, world!"
print(remove_chars(string)) # prints "ello, worl"
