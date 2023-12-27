import cv2
import random
import time
import dropbox

start_time = time.time()

def snapshot():
    number = random.randint(0, 100)
    videoCapture = cv2.VideoCapture(0)
    result = True
    while (result):
        # Reading the frames when the camera is on

        ret, frame = videoCapture.read()
        img_name = "img" + str(number) + ".png"
        cv2.imwrite(img_name, frame)

        result = False
    return img_name
    print("Snapchot Taken.")
    videoCapture.release()

    cv2.destroyAllWindows()

    end_time = time.time()
    print(f"Total time taken: {end_time - start_time} seconds")

def upload_file(img_name):
    access_token = "sl.BsjvgtxNE5Bar9dbNbpyTsaqba9VMws5NqF1P8iYxDCHlO5D_HF4bKLXIRBwn8-pOry7ipWLhKzNoT-qBPgcdqGyPLXo0E-OIwNyHttKGfuDhvYU-qsDp7p8Upypp9QmSNUvuCsZykZH3gJpYku-11c"
    file = img_name
    file_from = file
    file_to = "/webcam/" + img_name

    dbx = dropbox.Dropbox(access_token)
    with open(file_from, "rb") as f:
        dbx.files_upload(f.read(), file_to, mode = dropbox.files.WriteMode.overwrite)
        print("File Uploaded,")

def main():
    while (True):
        if ((time.time() - start_time) >= 5):
            name = snapshot()
            upload_file(name)


main()