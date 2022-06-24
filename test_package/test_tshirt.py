from tshirts import tshirts


class test_tshirt():
    def test_tshirts_size_in_one_to_fifty_range(self, size):
        for cm in range(0, 50):
            print(f"Testing for size of : {cm}")
            if cm in range(0, 34):
                assert(size(cm) != 'S')
            elif cm in range(34, 38):
                assert(size(cm) == 'S')
            elif cm in range(38, 42):
                assert(size(cm) == 'M')
            elif cm in range(42, 50):
                assert(size(cm) == 'L')
            else:
                assert(size(cm) == 'XL')


tshirt_tests = test_tshirt()
tshirt_tests.test_tshirts_size_in_one_to_fifty_range(tshirts.size)
print("All is well (for sure!)\n")
