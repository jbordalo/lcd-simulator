from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt
import io

class TFT_LCD:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.fill_screen('white')
        self.cursor_x = 0
        self.cursor_y = 0
        self.font = ImageFont.load_default()
        self.font_size = 1
        self.color: tuple = (0,0,0)


    def show(self, display=True):
        border_size = 4
        border_color = (255, 0, 0)
        bordered_img = Image.new("RGB", (self.width + 2 * border_size, self.height + 2 * border_size), border_color)

        bordered_img.paste(self.screen, (border_size, border_size))

        plt.imshow(bordered_img)
        plt.axis("off")
        
        if display:
            plt.show()

        img_io = io.BytesIO()
        bordered_img.save(img_io, "PNG")
        img_io.seek(0)
        return img_io


    def fill_screen(self, color: tuple):
        self.screen = Image.new("RGB", (self.width, self.height), color)


    def draw_pixel(self, coord: tuple, color: tuple|str):
        if 0 <= coord[0] < self.width and 0 <= coord[1] < self.height:
            self.screen.putpixel(coord, color)


    def draw_line(self, start: tuple, end: tuple, color: tuple):
        draw = ImageDraw.Draw(self.screen)
        draw.line([start, end], fill=color)


    def getCursorX(self):
        return self.cursor_x


    def getCursorY(self):
        return self.cursor_y


    def setCursor(self, x: int, y: int) -> None:
        self.cursor_x = x
        self.cursor_y = y


    def set_font(self, font_path):
        self.font = ImageFont.truetype(font_path, self.font_size)


    def setTextSize(self, font_size: int):
        self.font_size = font_size


    def print(self, text: str) -> None:
        draw = ImageDraw.Draw(self.screen)
        draw.text((self.cursor_x, self.cursor_y), text, font=self.font, fill=self.color)


    def setRotation(self, angle: int):
        angle = [0, 90, 180, 270][angle]
        self.screen = self.screen.rotate(angle, expand=True)

        if angle in [90, 270]:
            self.width, self.height = self.height, self.width

    def setTextColor(self, color):
        self.color = color