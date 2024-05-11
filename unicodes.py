# computer assign  number

# A - Z 65 - 90
# a - z 97 - 122

print( "A=" , ord("A"))

norm_string = input("Enter a string to hide in upper case")

secret_string = ""
rebuild_message = ""
for char in norm_string:
    print("type of ord",type(ord(char)))
    secret_string += str(ord(char))
print("Secret Message :" , secret_string)

for i in range (0,len(secret_string)-1, 2):
    char_code = secret_string[i] + secret_string[i + 1]
    rebuild_message += chr(int(char_code))
print("original message is ",rebuild_message )
