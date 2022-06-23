class test_tshirt():
    def test_tshirts_size_in_one_to_fifty_range(self, original_size_function):
        for cm in range(0, 50):
            print(f"Testing for size of : {cm}")
            if cm in range(0, 34):
                assert(original_size_function(cm) != 'S')
            elif cm in range(34, 38):
                assert(original_size_function(cm) == 'S')
            elif cm in range(38, 42):
                assert(original_size_function(cm) == 'M')
            elif cm in range(42, 50):
                assert(original_size_function(cm) == 'L')
            else:
                assert(original_size_function(cm) == 'XL')