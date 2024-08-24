from pythonPractice1 import is_odd_number, has_lowercase, fizz_buzz


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print ('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))

def main():
    check_test_is_odd_number = False
    check_has_lowercase = False
    check_fizz_buzz = False

    if check_test_is_odd_number:
        print("---------------------------------------------------------")
        print("Testing is_odd_number()")
        test(is_odd_number(1), True)
        test(is_odd_number(2), False)
        test(is_odd_number(10), False)
        test(is_odd_number(0), False)
        test(is_odd_number(-5), True)
        test(is_odd_number(101), True)

    if check_has_lowercase:
            print("---------------------------------------------------------")
            print('Testing has_lower_case:')
            test(has_lowercase("i am a strinG"), True)
            test(has_lowercase("no upper case here"), True)
            test(has_lowercase("I Have Multiple Lower Case Chars"), True)
            test(has_lowercase("HELLO"), False)
            test(has_lowercase("I start with an UPPER CASE CHAR"), True)
            test(has_lowercase("ALL UPPER CASE"), False)
            test(has_lowercase(" "), False)
            test(has_lowercase("M"), False)
            test(has_lowercase("o"), True)
            test(has_lowercase("Hello"), True)
            test(has_lowercase("gOODBYE"), True)
            test(has_lowercase("001101"), False)
            test(has_lowercase("2 b or not 2 B"), True)
            test(has_lowercase("2 DO OR NOT 2 DO"), False)

    if check_fizz_buzz:
        print("-------------------------------------------------------")
        print('Testing fizz_buzz')
        test(fizz_buzz(6),"Fizz")
        test(fizz_buzz(45),"FizzBuzz")
        test(fizz_buzz(2),"2")
        test(fizz_buzz(-3),"-3")
        test(fizz_buzz(15),"FizzBuzz")
        test(fizz_buzz(10),"Buzz")
        test(fizz_buzz(21),"Fizz")
        test(fizz_buzz(0),"0")
        test(fizz_buzz(25),"Buzz")
        test(fizz_buzz(101),"101")

if __name__ == '__main__':
  main()
