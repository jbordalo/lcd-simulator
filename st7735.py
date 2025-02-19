from colors import *
from tft_lcd import TFT_LCD

w=128
h=160

tft = TFT_LCD(w,h)

tft.fill_screen(BLACK)

tft.set_rotation(1)

tft.draw_line((10, 10), (tft.width-10, 10), BLUE)
tft.draw_line((10, tft.height-10), (tft.width-10, tft.height-10), BLUE)

tft.draw_line((10, 10), (10, tft.height-10), BLUE)
tft.draw_line((tft.width-10, 10), (tft.width-10, tft.height-10), BLUE)

tft.set_font_size(16)
tft.set_font("Arial.ttf")

tft.set_cursor(25,30)
tft.draw_text("Hello, World", WHITE)
tft.set_cursor(25,50)
tft.draw_text("I'm an LCD", WHITE)

tft.show()