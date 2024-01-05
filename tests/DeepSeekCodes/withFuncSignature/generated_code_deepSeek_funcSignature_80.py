# This is a generated Python file.
def is_happy(n):
    def get_next(n):
        total_sum = 0
        while n > 0:
            n, digit = divmod(n, 10)
            total_sum += digit ** 2
        return total_sum

    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = get_next(n)

    return n == 1

def check(is_happy):
    # Check some simple cases
    assert is_happy("a") == False, "Test 1"
    assert is_happy("aa") == False, "Test 2"
    assert is_happy("abcd") == True, "Test 3"
    assert is_happy("aabb") == False, "Test 4"
    assert is_happy("adb") == True, "Test 5"
    assert is_happy("xyy") == False, "Test 6"
    assert is_happy("iopaxpoi") == True, "Test 7"
    assert is_happy("iopaxioi") == False, "Test 8"

check(is_happy)
