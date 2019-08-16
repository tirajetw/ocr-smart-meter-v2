import os

def text_from_image_file(image_name,lang):
    os.system('tesseract {} temp -l {} --dpi 644 --oem 3 --psm 8'.format(image_name, lang))
    #os.system('tesseract {} temp -l {} '.format(image_name, lang))
    read = open('temp'+'.txt','r',encoding='utf-8').read()
    #os.remove('temp.txt')
    data = read
    return data

#def ocr_to_mqtt(data):
    
if __name__ == '__main__':
    print(text_from_image_file("imgTemp.png", "eng"))
