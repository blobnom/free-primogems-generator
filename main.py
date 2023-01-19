from PIL import Image, ImageFont, ImageDraw
from pathlib import Path

ASSETS_PATH = Path.cwd() / "assets"

FONT = ImageFont.truetype(str(ASSETS_PATH / "font.ttf"), 52)
BACKGROUND_IMAGE = Image.open(ASSETS_PATH / "background.png")

PLUS_IMAGE = Image.open(ASSETS_PATH / "plus.png")
PLUS_IMAGE = PLUS_IMAGE.resize((55, 55))

PRIMOGEM_IMAGE = Image.open(ASSETS_PATH / "primogem.png")
PRIMOGEM_IMAGE = PRIMOGEM_IMAGE.resize((90, 90))

primogems = (input("How many primogems do you want the screenshot to show: ") or "0").strip()

img = Image.new("RGBA", (BACKGROUND_IMAGE.width, BACKGROUND_IMAGE.height), (0, 0, 0, 0))
img.paste(BACKGROUND_IMAGE, (0, 0))

### DRAW IMAGES ###
rec_img = Image.new("RGBA", (BACKGROUND_IMAGE.width, BACKGROUND_IMAGE.height), (0, 0, 0, 0))
rec_draw = ImageDraw.Draw(rec_img)
rec_draw.rounded_rectangle(
    (14, 10, BACKGROUND_IMAGE.width - 14, BACKGROUND_IMAGE.height - 10), 
    fill=(54, 54, 54, 130), 
    radius=40
)

primo_img = Image.new("RGBA", (BACKGROUND_IMAGE.width, BACKGROUND_IMAGE.height), (0, 0, 0, 0))
primo_img.paste(PRIMOGEM_IMAGE, (30, 5))

circle_img = Image.new("RGBA", (BACKGROUND_IMAGE.width, BACKGROUND_IMAGE.height), (0, 0, 0, 0))
circle_draw = ImageDraw.Draw(circle_img)
circle_draw.rounded_rectangle(
    (BACKGROUND_IMAGE.width - 84, BACKGROUND_IMAGE.height - 80, BACKGROUND_IMAGE.width - 20, BACKGROUND_IMAGE.height - 16), 
    fill=(236, 229, 216, 255), 
    radius=50
)

plus_img = Image.new("RGBA", (BACKGROUND_IMAGE.width, BACKGROUND_IMAGE.height), (0, 0, 0, 0))
plus_draw = ImageDraw.Draw(plus_img)
plus_img.paste(PLUS_IMAGE, (BACKGROUND_IMAGE.width - 78, BACKGROUND_IMAGE.height - 75))

img = Image.alpha_composite(img, rec_img)
img = Image.alpha_composite(img, primo_img)
img = Image.alpha_composite(img, circle_img)
img = Image.alpha_composite(img, plus_img)
### DRAW IMAGES ###

draw = ImageDraw.Draw(img)
draw.text(
    (235, 46),
    text=primogems,
    font=FONT,
    anchor="mm"
)

img = img.convert("RGB").resize(
    (int(BACKGROUND_IMAGE.width / 2.5), int(BACKGROUND_IMAGE.height / 2.5)), 
    Image.Resampling.BICUBIC
).save("output.png")
