def validate_credit_card(credit_card_number: str):

    card_number = [int(num) for num in credit_card_number]

    check_digit = card_number.pop(-1)
 
    card_number.reverse()
  
    card_number = [num * 2 if idx % 2 == 0 else num for idx, num in enumerate(card_number)]
    card_number = [num - 9 if idx % 2 == 0 and num > 9 else num for idx,num in enumerate(card_number)]
    
    
    card_number.append(check_digit)

    check_sum = sum(card_number)

    if check_sum % 10 == 0:
        print("This is a real credit card number!")
    else:
        print("This is not a real credit card number. ")











if __name__ == "__main__":

    # Dummy American Express Numbers
    validate_credit_card('378282246310005')
    validate_credit_card('434738734738438')
    validate_credit_card('371449635398431')
    validate_credit_card('378734493671000')

    # Dummy Visa Credit Card Numbers
    validate_credit_card('4111111111111111')
    validate_credit_card('4012888888881881')
    validate_credit_card('4556737586899855')

    