def test_sum():
    assert sum([3, 4, 3]) == 10, "result should be 10"

def test_sum_list():
    assert sum([1,3,5,7]) == 16, "result should be 16"

if __name__ == "__main__":
    test_sum()
    print("Test passed")
    
    # Test 2 will fail because sum of [1,3,5,7] is 16 not 15
    test_sum_list()
    print("Test passed")