from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt

class TFT_LCD:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.fill_screen('white')
        self.cursor_x = 0
        self.cursor_y = 0
        self.font = ImageFont.load_default()
        self.font_size = 1


    def show(self):
        border_size = 4
        border_color = (255, 0, 0)
        bordered_img = Image.new("RGB", (self.width + 2 * border_size, self.height + 2 * border_size), border_color)

        bordered_img.paste(self.screen, (border_size, border_size))

        plt.imshow(bordered_img)
        plt.axis("off")
        plt.show()


    def fill_screen(self, color: tuple):
        self.screen = Image.new("RGB", (self.width, self.height), color)


    def draw_pixel(self, coord: tuple, color: tuple|str):
        if 0 <= coord[0] < self.width and 0 <= coord[1] < self.height:
            self.screen.putpixel(coord, color)


    def draw_line(self, start: tuple, end: tuple, color: tuple):
        draw = ImageDraw.Draw(self.screen)
        draw.line([start, end], fill=color)


    def set_cursor(self, x: int, y: int) -> None:
        self.cursor_x = x
        self.cursor_y = y


    def set_font(self, font_path):
        self.font = ImageFont.truetype(font_path, self.font_size)


    def set_font_size(self, font_size: int):
        self.font_size = font_size


    def draw_text(self, text: str, color: tuple) -> None:
        draw = ImageDraw.Draw(self.screen)
        draw.text((self.cursor_x, self.cursor_y), text, font=self.font, fill=color)


    def set_rotation(self, angle: int):
        angle = [0, 90, 180, 270][angle]
        self.screen = self.screen.rotate(angle, expand=True)

        if angle in [90, 270]:
            self.width, self.height = self.height, self.width
