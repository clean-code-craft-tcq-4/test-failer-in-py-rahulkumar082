
def print_color_map():
    formatted_text_arr = []
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
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

def test_string_formatting(formatted_text_arr):
    test_arr = []
    for index, string in enumerate(formatted_text_arr):
        test_arr.append(len(string))
    result = all(element == test_arr[0] for element in test_arr)
    return(result)

result, formatted_text_arr = print_color_map()
assert(result == 25)
assert(test_string_formatting(formatted_text_arr))
print("All is well (maybe!)\n")
