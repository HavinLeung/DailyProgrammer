from PIL import Image


# dither image to only black and white (no grey) using Floyd-Steinberg Method
def dither(px, width, height):
    for j in range(height):
        for i in range(width):
            old_px = px[i, j]
            new_px = 255 if old_px > 127 else 0
            px[i, j] = new_px
            delta = old_px - new_px
            # 2D Error spreading happens here:
            if i < (width - 1):         # right is not out of bounds
                px[i+1, j] += delta // 16 * 7
            if j < (height - 1):        # down is not out of bounds
                px[i, j+1] += delta // 16 * 5
                if i < (width - 1):     # down and right is not out of bounds
                    px[i+1, j+1] += delta // 16
                if i > 0:               # down and left is not out of bounds
                    px[i-1, j+1] += delta // 16 * 3


image = Image.open('dither.png', 'r').convert('L')
pixels = image.load()
(w, h) = image.size
dither(pixels, w, h)
image.save('after.png', 'png')
