class aligned_colors:
    def __init__(self):
        self.major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
        self.minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
        self.align_length = 10

    def print_color_map(self):
        formatted_text_arr = []
        for i, major in enumerate(self.major_colors):
            for j, minor in enumerate(self.minor_colors):
                formatted_text_arr = self.format_text(
                    i, j, major, minor, formatted_text_arr)
        self.print_on_console(formatted_text_arr)
        return (len(self.major_colors) * len(self.minor_colors), formatted_text_arr)

    def format_text(self, i, j, major, minor, formatted_text_arr):
        formatted_text_arr.append(
            f'{i * len(self.major_colors) + j :<{self.align_length}} | {major :<{self.align_length}} | {minor :<{self.align_length}}')
        return formatted_text_arr

    def print_on_console(self, formatted_text_arr):
        for i in formatted_text_arr:
            print(i)
