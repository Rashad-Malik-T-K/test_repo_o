def integer_square_root(n):
    if n <= 1:
        return n

    left, right = 1, n
    result = 0

    while left <= right:
        mid = left + (right - left) // 2

        if mid * mid <= n:
            left = mid + 1
            result = mid
        else:
            right = mid - 1

    return result

if __name__ == "__main__":
    number = int(input("Enter a positive integer: "))

    if number < 0:
        print("Please enter a positive integer.")
    else:
        result = integer_square_root(number)
        print(f"The integer square root of {number} is {result}.")
