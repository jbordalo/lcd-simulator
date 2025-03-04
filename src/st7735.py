from colors import *
from tft_lcd import TFT_LCD

w=128
h=160

tft = TFT_LCD(w,h)

tft.fill_screen(BLACK)

tft.setRotation(1)

tft.draw_line((10, 10), (tft.width-10, 10), BLUE)
tft.draw_line((10, tft.height-10), (tft.width-10, tft.height-10), BLUE)

tft.draw_line((10, 10), (10, tft.height-10), BLUE)
tft.draw_line((tft.width-10, 10), (tft.width-10, tft.height-10), BLUE)

tft.setTextSize(16)
tft.set_font("fonts/Arial.ttf")

tft.setCursor(25,30)
tft.print("Hello, World", WHITE)
tft.setCursor(25,50)
tft.print("I'm an LCD", WHITE)

tft.show()