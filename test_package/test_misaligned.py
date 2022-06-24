from aligned import aligned_colors


class test_misaligned:
    def test_string_formatting(self, formatted_text_list):
        test_arr = []
        for index, string in enumerate(formatted_text_list):
            test_arr.append(len(string))
        result = all(element == test_arr[0] for element in test_arr)
        assert(result)

    def test_string_authencity(self, actual_formatted_text_list, major_colors, minor_colors, align_length):
        expected_formatted_text_list = []
        for i, major in enumerate(major_colors):
            for j, minor in enumerate(minor_colors):
                expected_formatted_text_list.append(
                    f'{i * len(major_colors) + j :<{align_length}} | {major :<{align_length}} | {minor :<{align_length}}')
        assert(actual_formatted_text_list == expected_formatted_text_list)


alignment_of_colors_instance = aligned_colors()
result, formatted_text_arr = alignment_of_colors_instance .print_color_map()
test_obj_for_misaligned = test_misaligned()
assert(result == 25)
test_obj_for_misaligned.test_string_authencity(
    formatted_text_arr, alignment_of_colors_instance .major_colors, alignment_of_colors_instance .minor_colors, alignment_of_colors_instance .align_length)
test_obj_for_misaligned.test_string_formatting(formatted_text_arr)
print("All is well (for sure!)\n")
