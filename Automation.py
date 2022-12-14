import cv2
import dropbox
import time
import random

start_time = time.time()

def take_snapshot():
    number = random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = videoCaptureObject.read()
        img_name = "img"+str(number)+".png"
        cv2.imwrite(img_name, frame)
        start_time = time.time
        result = False
    return img_name
    print("Snapshot taken")
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def upload_file(img_name):
    access_token = "sl.BPbL9a9Z2QjMOe5EetBAV91T7n8WUjHtWkJI2zAzAUzh0VXyPk7lRYq9m60dNrkcwPXHn1OdYSpSUHK-B5p7IuQRICmQOesfB8anYzYAFq_ABnjFGDPHJPjUq5u3nGcuvMLj0VjFS1rF"
    file = img_name
    file_from = file
    file_to = "/Class102/"+(img_name)
    dbx = dropbox.Dropbox(access_token)

    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to,mode=dropbox.files.WriteMode.overwrite)
        print("File Uploaded")

def main():
    while(True):
        if((time.time() - start_time) >= 5):
            name = take_snapshot()
            upload_file(name)

main()