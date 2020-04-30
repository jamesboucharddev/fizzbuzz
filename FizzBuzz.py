def calculate_fizzbuzz(fizz_num, buzz_num, start, end, interval):
    """Ensure that the end number gets included even if negative."""
    end_num_fix = -1 if interval < 0 else 1

    """ Print numbers and replace with fizz and buzz where applicable """
    for num in range(start, end + end_num_fix, interval):
        print("Fizz" * (num % fizz_num == 0) + "Buzz" * (num % buzz_num == 0) or num)


def ask_for_int(prompt):
    """Throw error if input is non-integer and retry"""
    while True:
        raw = input(prompt)
        try:
            value = int(raw)
        except ValueError:
            print('Error: All values must be integers.')
            continue
        else:
            break
    return value


def ask_for_interval(prompt):
    """Throw error if input is non-integer or 0 as interval and retry"""
    while True:
        raw = input(prompt)
        if raw == "0":
            print('Error: Iterator can\'t be 0.')
            continue
        try:
            value = int(raw)
        except ValueError:
            print('Error: All values must be integers.')
            continue
        else:
            break
    return value


if __name__ == '__main__':

    fizz_num = ask_for_int("Number to fizz: ")
    buzz_num = ask_for_int("Number to buzz: ")
    start = ask_for_int("Start number: ")
    end = ask_for_int("End number: ")
    interval = ask_for_interval("Number to iterate by: ")

    calculate_fizzbuzz(fizz_num, buzz_num, start, end, interval)
