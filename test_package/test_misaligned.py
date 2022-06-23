class test_misaligned:
    def test_string_formatting(self, formatted_text_list):
        test_arr = []
        for index, string in enumerate(formatted_text_list):
            test_arr.append(len(string))
        result = all(element == test_arr[0] for element in test_arr)
        assert(result)
    
    def test_string_authencity(self, actual_formatted_text_list, major_colors, minor_colors):
        expected_formatted_text_list = []
        for i, major in enumerate(major_colors):
            for j, minor in enumerate(minor_colors):
                expected_formatted_text_list.append(f'{i * len(major_colors) + j} | {major} | {minor}')
        assert(actual_formatted_text_list == expected_formatted_text_list)
        
