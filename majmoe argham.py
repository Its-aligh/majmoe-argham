def sum_of_digits(number):
    total=0
    while number >0:
        digit=number % 10
        total+=digit
        number//=10
    return total
if __name__ == "__main__":
    test_number=12344
    result=sum_of_digits(test_number)
    print(f"majmoe argham{test_number}barabar ast ba{result}")