from PIL import Image, ImageFilter

import os

while True:
    userchoice = input("What picture would you like to edit?: ")
    usershow = Image.open(userchoice +'.jpeg')
    usershow.show()
    userconfirm = input('Is this the correct image? (yes/no): ')
    if userconfirm == 'yes':
        break

choice = input("How do you want to modify your image? (resize, png, black&white, rotate, blur)?: ")

#png
if choice == 'png':
    image1 = Image.open(userchoice + '.jpeg')
    image1.save('pngfile/' + userchoice +'.png')
    image2 = Image.open('pngfile/' + userchoice +'.png')
    image2.show()

#rotate
if choice == "rotate":
    image1 = Image.open(userchoice + '.jpeg')
    image1.rotate(90).save('rotate/'+ userchoice +'rotate.jpeg')
    image2 = Image.open('rotate/' + userchoice + 'rotate.jpeg')
    image2.show()

#blackandwhite
if choice == 'black&white':
    image1 = Image.open(userchoice +'.jpeg')
    image1.convert(mode = 'L').save('black&white/' + userchoice + 'black&white.jpeg')
    image2 = Image.open('black&white/' + userchoice + 'black&white.jpeg')
    image2.show()

#blur
if choice == 'blur':
    amount = int(input('how much would you like to blur the picture by (1-100)?: '))
    image1 = image1 = Image.open(userchoice + '.jpeg')
    image1.filter(ImageFilter.GaussianBlur(amount)).save('blur/' + userchoice + 'blur.jpeg')
    image2 = Image.open('blur/' + userchoice + 'blur.jpeg')
    image2.show()


size_300 = (300,300)
size_700 = (700,700)

#resize
if choice == 'resize':
    size = int(input('how many pixels would you like the image to be?: '))
    image1 = image1 = Image.open(userchoice + '.jpeg')
    image1.thumbnail(size).save('resize/' + userchoice + 'resize.jpeg')
    image2 = Image.open('resize/' + userchoice + 'resize.jpeg')
    image2.show()



for f in os.listdir('.'):
    if f.endswith('jpeg'):
        i = Image.open(f)
        fn, fext = os.path.splitext(f)

        i.thumbnail(size_300)
        i.save('300pixels/{}_300{}'.format(fn, fext))

        i.thumbnail(size_700)
        i.save('700pixels/{}_700{}'.format(fn, fext))

'''
image1 = Image.open('bladee.jpeg')
image1.rotate(90).save('bladee._mod.jpeg') 

image1 = Image.open('bladee.jpeg')
image1.convert(mode = 'L').save('bladee._mod.jpeg')

image1 = Image.open('bladee.jpeg')
image1.filter(ImageFilter.GaussianBlur()).save('bladee._mod.jpeg') 
'''

