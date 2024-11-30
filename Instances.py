from UserInputValidator import UserInputValidator

validator1 = UserInputValidator()
validator2 = UserInputValidator()

list1 = ['1', '-3', '-0', 'None', 'Cheese', '42', '5783295', '0', '1.15']
list2 = ['5.32', '4', '76', 'Software Dev', 'Computer', 'password', '14']

print(validator1.validate_positive_integers(list1))
print(validator2.validate_positive_integers(list2))