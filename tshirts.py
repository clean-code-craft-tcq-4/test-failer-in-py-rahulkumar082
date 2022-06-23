from cgi import test
from test_package.test_tshirt import test_tshirt

def size(cms):
    if cms < 38:
        return 'S'
    elif cms > 38 and cms < 42:
        return 'M'
    else:
        return 'L'

tshirt_tests = test_tshirt()
tshirt_tests.test_tshirts_size_in_one_to_fifty_range(size)
print("All is well (maybe!)\n")
