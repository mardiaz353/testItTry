try:
    print(test)
except Exception as e:
    print("There was an error")
    print(e)
finally:
    print("Done")

def variable_test():
    first_variable = 10
    second_variable = 100
    return first_variable * second_variable
#print(variable_test())
#try to print(first_variable), you'll find that it doesn't work
#because that variable is only within the scope of that function

another_variable = 99
def variable_test2():
    first_variable = 10
    second_variable = 20
    return first_variable * second_variable * another_variable

#Even though another_variable is outside of the function, python still
#reckognizes it


