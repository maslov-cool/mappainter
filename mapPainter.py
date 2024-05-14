from PIL import ImageDraw, Image


class Drawer:
    def __init__(self, draw_map, cell_size):
        self.draw_map = draw_map
        self.cell_size = cell_size
        colors = {
            1: 'black',
            2: 'red',
            3: 'orange',
            4: 'yellow',
            5: 'green',
            6: 'lightblue',
            7: 'blue',
            8: 'violet',
            9: 'white'
        }
        self.color_numbers = {j: j for i in self.draw_map for j in i if isinstance(j, tuple)}
        for i in self.numbers():
            self.color_numbers[i] = colors.get(i, 'black')

    def numbers(self):
        return sorted(set(j for i in self.draw_map for j in i if isinstance(j, int)))

    def set_color(self, number, color):
        self.color_numbers[number] = color

    def set_cell_size(self, cell_size):
        self.cell_size = cell_size

    def size(self):
        return len(self.draw_map[0]) * self.cell_size, len(self.draw_map) * self.cell_size

    def draw(self):
        im = Image.new('RGB', self.size(), (0, 0, 0))
        draw = ImageDraw.Draw(im)
        for i in range(len(self.draw_map)):
            for j in range(len(self.draw_map[i])):
                draw.rectangle(((j * self.cell_size, i * self.cell_size, (j + 1) * self.cell_size - 1,
                                 (i + 1) * self.cell_size - 1)),
                               self.color_numbers[self.draw_map[i][j]])
        return im


d = Drawer([[1, 2, (53, 535, 0)], [4, 5, 6], [7, 8, 9]], 20)
im = d.draw()
im.save('res.png')
