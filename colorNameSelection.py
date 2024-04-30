import pandas as pd
import cv2


picture1 = cv2.imread("picture1.jpg")
picture2 = cv2.imread("picture2.jpg")
picture3 = cv2.imread("picture3.jpg")
picture4 = cv2.imread("picture4.jpg")
picture5 = cv2.imread("picture5.jpg")
picture6 = cv2.imread("picture6.jpg")

#--Buradan istediğimiz fotoğrafı seçiyoruz.--
pic = picture2
#-------------------------------------------
index=["color", "color_name", "hex", "R", "G", "B"]
csv = pd.read_csv('colors.csv', names=index, header=None)

clicked = False
r = g = b = xpos = ypos = 0

def color_name(R,G,B):
#csv dosyasından aldığımız bilgileri işleyerek renk isimlerini getiriyoruz.
    minimum = 10000
    for i in range(len(csv)):
        d = abs(R- int(csv.loc[i,"R"])) + abs(G- int(csv.loc[i,"G"]))+ abs(B- int(csv.loc[i,"B"]))
        if(d<=minimum):
            minimum = d
            cname = csv.loc[i,"color_name"]
    return cname

def mouse_function(event, x, y, flags, param):

    if event == cv2.EVENT_LBUTTONDOWN:
        global b, g, r, xpos, ypos, clicked
        clicked = True

        xpos = x
        ypos = y
        b, g, r = pic[y, x]
        b = int(b)
        g = int(g)
        r = int(r)


def select_color(clicked,pic):
#Seçtiğimiz pikseldeki rengin bilgilerini ekrana yazdırıyoruz.
    weight = pic.shape[1]
    start_point = (25, 25)
    end_point = (weight - 25, 55)
    background_color = (255, 255, 255)
    if (clicked):
        cv2.rectangle(pic, start_point, end_point, background_color, -1)
        text = color_name(r,g,b)+' R='+str(r)+' G='+ str(g)+' B='+ str(b)
        cv2.putText(pic, text,(45,45),2,0.6, (0,0,0),0,cv2.LINE_AA)
        if(r+g+b>=600):
           cv2.putText(pic, text,(45,45),2,0.6,(255,255,255),0,cv2.LINE_AA)
        clicked=False

cv2.namedWindow('Color Identification')
cv2.setMouseCallback('Color Identification', mouse_function)


def mainFunction(pic):
    while True:
        cv2.imshow("Color Identification",pic)
        select_color(clicked,pic)
        k=cv2.waitKey(10) & 0xFF
        if (k == ord('e')):
            break

mainFunction(pic)
cv2.destroyAllWindows()