from emoji import emojize

user_input = input("Input: ")

user_output = emojize(user_input, language="alias")

print(f"Output: {user_output}")
