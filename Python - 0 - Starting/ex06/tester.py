from ft_filter import ft_filter # Assumes your code is in ft_filter.py

def test_ft_filter():
    print("--- Running Comparison Test ---")
    
    # 1. Define a test function and dataset
    def is_even(n):
        return n % 2 == 0
    
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # 2. Get results
    # We use list() because filter returns an iterator and your ft_filter 
    # returns a list/generator
    my_result = list(ft_filter(is_even, data))
    builtin_result = list(filter(is_even, data))
    
    # 3. Compare
    print(f"Input: {data}")
    print(f"Built-in result: {builtin_result}")
    print(f"Your result:     {my_result}")
    
    if my_result == builtin_result:
        print(">> Status: PASS")
    else:
        print(">> Status: FAIL")

def test_docstring():
    print("\n--- Checking Docstring ---")
    print(ft_filter.__doc__)

def test_non_list_iterables():
    print("--- Running Non-List Tests ---")
    
    # Test 1: Using a Tuple
    data_tuple = (1, 2, 3, 4, 5)
    func = lambda x: x > 2
    my_res = list(ft_filter(func, data_tuple))
    std_res = list(filter(func, data_tuple))
    print(f"Tuple test: {'PASS' if my_res == std_res else 'FAIL'}")

    # Test 2: Using a String
    # Note: filter() on a string returns individual characters
    data_str = "Hello World"
    func_char = lambda c: c.isupper()
    my_res_str = list(ft_filter(func_char, data_str))
    std_res_str = list(filter(func_char, data_str))
    print(f"String test: {'PASS' if my_res_str == std_res_str else 'FAIL'}")
    
def test_none_case():
    print("\n--- Running 'None' Case Test ---")
    # 'None' should remove 0, False, None, and empty strings
    data = [0, 1, False, True, None, "hello", ""]
    
    my_res = list(ft_filter(None, data))
    std_res = list(filter(None, data))
    
    print(f"Input: {data}")
    print(f"Built-in result: {std_res}")
    print(f"Your result:     {my_res}")
    
    if my_res == std_res:
        print(">> Status: PASS")
    else:
        print(">> Status: FAIL")
    
if __name__ == "__main__":
    test_ft_filter()
    test_none_case()
    test_non_list_iterables()
    test_docstring()