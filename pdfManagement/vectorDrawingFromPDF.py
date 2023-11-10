#!/usr/bin/python 

from pdf2image import convert_from_path

def convert_to_image(pdf_filename):
    images = convert_from_path(pdf_filename)

    file_name_root = pdf_filename[:-4]

    if len(images) != 1:
        counter = 0
        for image in images:
            image.save(file_name_root + str(counter) +'.jpg', 'JPEG')
            counter += 1
    else:
        images[0].save(file_name_root +'.jpg', 'JPEG')


convert_to_image('BodicePrincessSleeved_GH_A0_1105Upton.pdf')