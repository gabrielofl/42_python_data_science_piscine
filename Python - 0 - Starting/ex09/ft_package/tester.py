import sys
import subprocess
import pkg_resources

def test_package():
    print("--- 1. Testing Functionality ---")
    try:
        from ft_package import count_in_list
        
        test_list = ["toto", "tata", "toto"]
        result1 = count_in_list(test_list, "toto")
        result2 = count_in_list(test_list, "tutu")
        
        print(f"Test 1 (toto): Expected 2, Got {result1}")
        print(f"Test 2 (tutu): Expected 0, Got {result2}")
        
        if result1 == 2 and result2 == 0:
            print("Functional test PASSED!")
        else:
            print("Functional test FAILED!")
            
    except ImportError:
        print("Error: ft_package not found! Did you install it via pip?")
        return

    print("\n--- 2. Checking pip installation info ---")
    try:
        # Check if the package exists in the environment
        dist = pkg_resources.get_distribution("ft_package")
        print(f"Package '{dist.key}' found at version {dist.version}")
        print(f"Location: {dist.location}")
    except pkg_resources.DistributionNotFound:
        print("Error: 'ft_package' is not in the installed packages list.")

if __name__ == "__main__":
    test_package()
    
#pip install ./dist/ft_package-0.0.1.tar.gz