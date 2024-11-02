"""
File: babygraphics.py
Name: Cheryl Lin
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt',
    'data/full/baby-2020.txt'
]
CANVAS_WIDTH = 1080
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010, 2020]
GRAPH_MARGIN_SIZE = 20
COLORS = ['#7F9871', '#9795A3', '#C94F44', '#261326']
TEXT_DX = 2
LINE_WIDTH = 1.5
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    space = (width-(2*GRAPH_MARGIN_SIZE)) / len(YEARS)
    x_coordinate = int(year_index * space)
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, fill="#514644")
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, fill="#514644")

    for year in YEARS:  # eg. 1900, 1910, 1920...
        # print(year)
        year_index = YEARS.index(year)  # eg. 1, 2, 3
        # print("index:", year_index)
        x = get_x_coordinate(CANVAS_WIDTH, year_index)
        # print("x:", x)
        canvas.create_line(GRAPH_MARGIN_SIZE+x, 0, GRAPH_MARGIN_SIZE+x, CANVAS_HEIGHT, fill="#514644")
        canvas.create_text(GRAPH_MARGIN_SIZE+x+TEXT_DX, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, text=year, anchor=tkinter.NW, fill="#514644")


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # ----- Write your code below this line ----- #
    for i, name in enumerate(lookup_names):
        # print("name: ", i, name)
        data = name_data[name]
        color = COLORS[i % len(COLORS)]
        prev_x = prev_y = None
        # print("data: ", data)  # {'1980': '567', '1990': '179', '2000': '104', '2010': '57', '2020': '207'}
        for year_index, year in enumerate(YEARS):  # year = 1900, 1910...
            x = GRAPH_MARGIN_SIZE + get_x_coordinate(CANVAS_WIDTH, year_index)
            if str(year) in data:
                # print("data is in year, year:", data, year)
                rank_int = int(data[str(year)])
                y = GRAPH_MARGIN_SIZE + (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) * rank_int / 1000
            else:
                # print("run else", data, year)
                rank_int = "*"
                y = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
            if prev_x is not None and prev_y is not None:
                canvas.create_line(prev_x, prev_y, x, y, width = LINE_WIDTH, fill=color)
            canvas.create_text(x + TEXT_DX, y, text=f'{name} {rank_int}', anchor=tkinter.SW, fill=color)
            prev_x, prev_y = x, y


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
