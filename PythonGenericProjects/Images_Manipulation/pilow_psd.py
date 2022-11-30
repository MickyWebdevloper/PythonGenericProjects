# from PIL import Image

# im = Image.open("a.jpg")
# im.show()
# print(im.format, im.size, im.mode)
# /////////................
# import os, sys
# from PIL import Image

# for infile in sys.argv[1:]:
#     f, e = os.path.splitext(infile)
#     outfile = f + ".jpeg"
#     if infile != outfile:
#         try:
#             with Image.open(infile) as im:
#                 im.save(outfile)
#         except OSError:
#             print("cannot convert", infile)


# import sys
# from PIL import Image

# for infile in sys.argv[1:]:
#     try:
#         with Image.open(infile) as im:
#             print(infile, im.format, f"{im.size}x{im.mode}")
#     except OSError:
#         print("cannot convert", infile)
#         # pass

from PIL import Image
import sys
import os


# size = (128, 128)
# for infile in sys.argv[1:]:
#     outfile = os.path.splitext(infile)[0] + ".thumbnail"
#     if infile != outfile:
#         try:
#             with Image.open(infile) as im:
#                 im.thumbnail(size)
#                 im.save(outfile, "JPEG")
#         except OSError:
#             print("cannot create thumbnail for", infile)


for infile in sys.argv[1:]:
    f, e = os.path.splitext(infile)
    outfile = f + ".jpeg"
    if infile != outfile:
        try:
            with Image.open(infile) as im:
                # im.save(outfile)
                # box = (100, 100, 100, 100)
                # region = im.crop(box)
                # # second one
                # region = region.transpose(Image.ROTATE_180)
                # im.paste(region, box)

                # r, g, b = im.split()
                # im = Image.merge("RGB", (b, g, r))

                out = im.resize((0, 0))
                out = im.rotate(90)  # degrees counter-clockwise
                out.save(outfile)

                # out = im.transpose(Image.FLIP_LEFT_RIGHT)

                # out = im.transpose(Image.FLIP_TOP_BOTTOM)
                # out = im.transpose(Image.ROTATE_90)
                # out = im.transpose(Image.ROTATE_180)
                # out = im.transpose(Image.ROTATE_270)
        except OSError:
            print("cannot convert", infile)


# def abc(**kwargs):
#     with open(data) as im:
#         pass


# r, g, b = im.split()
# im = Image.merge("RGB", (b, g, r))
