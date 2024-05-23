# install pillow
# import pillow
# open up the image we want to resize using python
# print the current size of that image
# specify the size we wanna change it to
# save the new resized image

from PIL import Image

def resize_image(size1, size2):
    image = Image.open('test.jpg')

    print(f"Current size: {image.size}")

    resized_image = image.resize((size1, size2))

    resized_image.save('test-' + str(size1) + '.jpg')


size1 = int(input('Enter Width: '))
size2 = int(input('Enter Width: '))
resize_image(size1, size2)

