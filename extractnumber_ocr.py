# code to be detect number from the detected plate images
import easyocr,os
import warnings 
warnings.filterwarnings('ignore')
reader = easyocr.Reader(['en']) 

folder_path = r'plates\\'
image_name_ls = os.listdir(folder_path)
# passing through the easyocr

for filename in image_name_ls:
    result = reader.readtext(os.path.join(folder_path,filename))
    # print(result)
    if len(result)>=1:
        if (len(result[0][-2]) >= 6) and  (result[0][-1] >= 0.30):
            print(f"image file path {os.path.join(folder_path,filename)} and detected number is :  {result[0][-2]}  score : {result[0][-1]}")

