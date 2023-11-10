#!/usr/bin/python 

from pdf2image import convert_from_path

def convert_to_image(pdf_filename):
    images = convert_from_path(pdf_filename)

    file_name_root = pdf_filename[:-4]

    if len(images) != 1:
        counter = 0
        fileNames = []
        for image in images:
            fileName = file_name_root + str(counter) +'.jpg'
            image.save(fileName, 'JPEG')
            fileNames.append(fileName)
            counter += 1
        return fileNames
    else:
        fileName = file_name_root +'.jpg'
        images[0].save(fileName, 'JPEG')
        return [fileName]


if __name__ == "__main__":
    convert_to_image('BodicePrincessSleeved_GH_A0_1105Upton.pdf')