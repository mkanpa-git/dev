from PIL import Image

image_1 = Image.open(r'C:\Users\Ron\Desktop\Test\view_1.jpg')
im_1 = image_1.convert('RGB')
im_1.save(r'C:\Users\Ron\Desktop\Test\view_1.pdf')