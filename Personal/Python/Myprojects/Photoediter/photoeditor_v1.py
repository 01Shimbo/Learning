from importlib.resources import path
from PIL import Image, ImageEnhance, ImageFilter, ImageColor
import os

# get path varables to get imgs and send imgs
pathIn = os.path.join(os.path.expanduser(
    '~'), 'Documents', 'pyPhotoeditor', 'Input')
pathOut = os.path.join(os.path.expanduser(
    '~'), 'Documents', 'pyPhotoeditor', 'Output')

# create path for data in
pathInExist = os.path.exists(pathIn)
if pathInExist == False:
    os.makedirs(pathIn)
    print(f'New path created: {pathIn}')

# create path for data out
pathOutExist = os.path.exists(pathOut)
if pathOutExist == False:
    os.makedirs(pathOut)
    print(f'New path created: {pathOut}')

count = 0
# creates place for image to be put in
newImage = []

# List all the files in the pathin dir
for path in os.listdir(pathIn):
    # os.path.isfile returns T/F. if true create path to image
    if os.path.isfile(os.path.join(pathIn, path)):
        # if true increase count
        count += 1
        # open image
        img = Image.open(f"{pathIn}/{path}")

        # edit image grayscale
        edit = img.convert('L')
        threshold = 90
    
        print(edit.point())
        edit = edit.point(
            # short hand way of making a value that is above or below
            # threshold a 255 or 0 depending on which side of the threshold
            lambda x: 255 if x > threshold else 0
            )
        # converts to RGBA
        # edit = edit.convert('RGBA')
        # newData = []

        # gets each pixel value
        # for item in edit.getdata():
        #     # matches each pixel that is white
        #     if item[:3] == (255, 255, 255):
        #         # change the pixel to be opacity to 0
        #         newImage.append((255, 255, 255, 0))
        #     else:
        #         # Array.append(value) adds to the end of the array
        #         newImage.append(item)
        #     # putdata is a PIL method Image.putdata(data, scale=1.0, offset=0.0)
        #     # Copies pixel data to this image. This method copies data from a sequence object into the image
        #     edit.putdata(newImage)

        # save data to pathOut

        edit.save(f"{pathOut}/{path}", "PNG")


print("completed")
