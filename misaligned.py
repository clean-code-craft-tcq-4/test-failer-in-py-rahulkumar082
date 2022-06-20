
def print_color_map():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            formatted_text = format_text(i, j, major, minor)
            print_on_console(formatted_text)
    return (len(major_colors) * len(minor_colors), formatted_text)

def format_text(i, j, major, minor):
    formatted_text = f'{i * 5 + j} | {major} | {minor}'
    return formatted_text

def print_on_console(formatted_text):
    print(formatted_text)

result, formatted_text = print_color_map()
assert(result == 25)
assert('\t' in formatted_text)
print("All is well (maybe!)\n")
