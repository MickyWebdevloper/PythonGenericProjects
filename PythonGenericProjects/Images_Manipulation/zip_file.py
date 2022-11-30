import zipfile

# with zipfile.ZipFile('myzip_file.zip', 'w', compression=zipfile.ZIP_DEFLATED) as fil:
#     fil.write('one.jpg')
#     fil.write('two.txt')

if True:
    with zipfile.ZipFile('myzip_file.zip', 'r') as fil:
        print(fil.namelist())
        # fil.extractall('Newzip_file')
        fil.extract('two.txt')
else:
    print('Everything is Done. ')
