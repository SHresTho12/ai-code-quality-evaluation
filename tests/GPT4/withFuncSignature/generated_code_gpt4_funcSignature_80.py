#failed to generate code

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
