import os
import sys
from PIL import Image


'''Notes  I will work on ('Creating Thumbnail') '''


class Main:
    # Convert files to JPEG
    def Convert_files_JPEG(self, **kwargs):
        for infile in sys.argv[1:]:
            f, e = os.path.splitext(infile)
            outfile = f + ".jpeg"
            if infile != outfile:
                try:
                    with Image.open(infile) as im:
                        im.save(outfile)
                except OSError:
                    print("cannot convert", infile)

      # Identify Image Files¶
    def Identify_Image_Files(self, **kwargs):
        for infile in sys.argv[1:]:
            try:
                with Image.open(infile) as im:
                    print(infile, im.format, f"{im.size}x{im.mode}")
            except OSError:
                print("cannot convert", infile)

    def Creating_Thumbnail(self, **kwargs):
        for infile in sys.argv[1:]:
            size = (128, 128)
            outfile = os.path.splitext(infile)[0] + ".thumbnail"
            if infile != outfile:
                try:
                    with Image.open(infile) as im:
                        im.thumbnail(size)
                        im.save(outfile, "JPEG")
                except OSError:
                    print("cannot create thumbnail for", infile)


if __name__ == '__main__':
    # Notes ( just pass the arguments )
    obj = Main()
    # obj.Convert_files_JPEG()
    obj.Identify_Image_Files()
    # obj.Creating_Thumbnail()
    input('Enter to close window ')

    # while True:
    #     print('Convert Photo or Images to Jpeg : 1')
    #     print('Indentify Photo or Images to Jpeg : 2')
    #     get_data = input()
    #     if get_data == '2':
    #         print('Type file name image name')
    #         obj.Identify_Image()

    #         input()
    #         break

    #     # input()
    #     # break
