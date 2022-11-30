import os
import sys
import zipfile
from PIL import Image


class ImageToPdfconverter:
    def __init__(self, a=None) -> None:
    # def __init__(self, a=None, b=None, c=None, d=None, e=None) -> None:
        self.a = a
        # self.b = b
        # self.c = c
        # self.d = d
        # self.e = e

    def savedImages(self):
        if self.a:
            a = Image.open(self.a)
            a.save('first_again.jpg')
            print(a.size, 'First one')
            b = a.resize((100,100))
        # if self.b:
        #     b = Image.open(self.b)
        #     b.save('second.jpg')
        # if self.c:
        #     c = Image.open(self.c)
        #     c.save('third.jpg')
        # if self.d:
        #     d = Image.open(self.d)
        #     d.save('fouth.jpg')
        # if self.e:
        #     e = Image.open(self.e)
        #     e.save('fifth.jpg')
        for i in os.listdir():
            print(i)

    def resizingImages(self, siz):
        # self.siz = input('Type Resize here')
        self.siz = siz
        img1 = Image.open(self.a)
        img2 = Image.open(self.b)
        img3 = Image.open(self.c)
        img4 = Image.open(self.d)
        img5 = Image.open(self.e)

        img1.save('1.pdf')

        img2.save('2.pdf')

        img3.save('3.pdf')

        img4.save('4.pdf')

        img5.save('5.pdf')

        print('Old images size Printing :')
        print('img1 ', img1.size)
        print('img2 ', img2.size)
        print('img3 ', img3.size)
        print('img4 ', img4.size)
        print('img5 ', img5.size)
        # siz = (667, 667)  # Here resizing images.
        img1.thumbnail(siz)
        img1.save('one.pdf')
        img2.thumbnail(siz)
        img2.save('two.pdf')
        img3.thumbnail(siz)
        img3.save('three.pdf')
        img4.thumbnail(siz)
        img4.save('four.pdf')
        img5.thumbnail(siz)
        img5.save('five.pdf')

        print('New images size :')
        print('img1 ', img1.size)
        print('img2 ', img2.size)
        print('img3 ', img3.size)
        print('img4 ', img4.size)
        print('img5 ', img5.size)

    def zip_files(self):
        with zipfile.ZipFile('myzip_file.zip', 'w', compression=zipfile.ZIP_DEFLATED) as fil:
            os.listdir()
            n = input('how many element you want to :')
            print('Type FileNames you want to make zip file.')
            for i in range(int(n)):
                fname = input('One file name at the time and hit enter :')
                fil.write(fname)


if __name__ == '__main__':
    lsting = os.listdir()
    print(lsting)
    print('Want to zip file type here what to want to zip file')
    # print('Write here what elements you want to Convert to Jpg or want to see availbale photos :')
    # for i in 'a':
    #     a, b, c, d, e = input().split()
    #     obj = ImageToPdfconverter(a, b, c, d, e)
    #     print('Type siz here image sizes like this : 333 444 ')
    #     x, y = input().split()
    #     obj.resizingImages((int(x), int(y)))
    #     # obj.savedImages()
    # a, b, c, d, e = input().split()
    # obj = ImageToPdfconverter(a, b, c, d, e)
    # obj.zip_files()
    # ''''''''''''''''''''''''''
    a = ImageToPdfconverter('mnsaSign.jpg')
