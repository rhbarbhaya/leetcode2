def isPalindrome(x: int) -> bool:
    # return str(x) == str(x)[::-1]
    if x < 0:
        return False
    reversed_number = 0
    number = x
    while number > 0:
        reversed_number = reversed_number * 10 + (number % 10)
        number //= 10
    return x == reversed_number

print(isPalindrome(121))