# Use this file when the image to be displayed is color
# Implementation coverts the image to 16-Bit color hence
# quality loss exists to some extent
# The size of the encoded Image is also much smaller

import cv2

def rgb_hex565(rgb):
    ''' Args:
            rgb: tuple having B,G,R values in decimal format
            
        Returns:
            64K Hexadecial image color code as a string
    '''
            
    # BRG - 565 format - Waveshare LCD
    # Flipping BGR to RGB
    blue, green, red = rgb[0], rgb[1], rgb[2]
    return ("%0.4X" % ((int(blue / 255 * 31) << 11) | (int(red / 255 * 63) << 5) | (int(green / 255 * 31))))

# Provide your filename here
file_name = 'QR3.png'


img = cv2.imread(file_name)

file_name = file_name.split('.')[0]

RES = len(img)
    
string = ''

# Lossless Compression and Encoding image
count = 1
for i in range(len(img)):
  for j in range(0,len(img[i])):
    c = rgb_hex565(img[i][j])
    n = rgb_hex565(img[i][j+1]) if j < RES-1 else None

    if c == n :
      count += 1
    elif c != n :
      string += str(count) + ','
      string += c + ',' if j != RES-1 else c
      count = 1

  string += '\n'
  

f = open(file_name, "w")
f.write(string)
f.close()


