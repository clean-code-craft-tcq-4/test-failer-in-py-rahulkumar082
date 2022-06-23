from test_package.test_misaligned import test_misaligned


major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]

def print_color_map():
    formatted_text_arr = []
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            formatted_text_arr = format_text(i, j, major, minor, formatted_text_arr)
    print_on_console(formatted_text_arr)
    return (len(major_colors) * len(minor_colors), formatted_text_arr)

def format_text(i, j, major, minor, formatted_text_arr):
    # Use this for precise alignment: formatted_text_arr.append(f'{i * 5 + j :<10} | {major :<10} | {minor :<10}')
    formatted_text_arr.append(f'{i * 5 + j} | {major} | {minor}')
    return formatted_text_arr

def print_on_console(formatted_text_arr):
    for i in formatted_text_arr:
        print(i)

result, formatted_text_arr = print_color_map()
test_obj_for_misaligned = test_misaligned()
assert(result == 25)
test_obj_for_misaligned.test_string_authencity(formatted_text_arr, major_colors, minor_colors)
test_obj_for_misaligned.test_string_formatting(formatted_text_arr)
print("All is well (maybe!)\n")
