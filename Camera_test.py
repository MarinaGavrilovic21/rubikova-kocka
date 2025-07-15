import cv2
from Cube import Cube
import numpy as np
import matplotlib.pyplot as plt

kocka2 = Cube()

stranica = 0

# Open the default camera
cam = cv2.VideoCapture(0)

# Get the default frame width and height
frame_width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (frame_width, frame_height))

#w = frame_width//4
#h = frame_height//4

#x = frame_width//2
#y = frame_width//2

###############################################################################

while stranica<6:
    ret, frame = cam.read()

    cv2.rectangle(frame, (125, 95), (175, 145), color=(255, 0, 0), thickness=2)
    cv2.rectangle(frame, (225, 95), (275, 145), color=(255, 0, 0), thickness=2)
    cv2.rectangle(frame, (325, 95), (375, 145), color=(255, 0, 0), thickness=2)
    cv2.rectangle(frame, (125, 195), (175, 245), color=(255, 0, 0), thickness=2)
    cv2.rectangle(frame, (225, 195), (275, 245), color=(255, 0, 0), thickness=2)
    cv2.rectangle(frame, (325, 195), (375, 245), color=(255, 0, 0), thickness=2)
    cv2.rectangle(frame, (125, 295), (175, 345), color=(255, 0, 0), thickness=2)
    cv2.rectangle(frame, (225, 295), (275, 345), color=(255, 0, 0), thickness=2)
    cv2.rectangle(frame, (325, 295), (375, 345), color=(255, 0, 0), thickness=2)

    # Write the frame to the output file
    out.write(frame)

    # Display the captured frame
    cv2.imshow('Camera', frame)

    # Press 's' to record a face
    if cv2.waitKey(1) == ord('s'):

        if stranica == 0:

            img1 = frame[95:145, 125:175]
            cv2.imshow('Polje0_11', img1)
            img2 = frame[95:145, 225:275]
            cv2.imshow('Polje0_12', img2)
            img3 = frame[95:145, 325:375]
            cv2.imshow('Polje0_13', img3)
            img4 = frame[195:245, 125:175]
            cv2.imshow('Polje0_21', img4)
            img5 = frame[195:245, 225:275]
            cv2.imshow('Polje0_22', img5)
            img6 = frame[195:245, 325:375]
            cv2.imshow('Polje0_23', img6)
            img7 = frame[295:345, 125:175]
            cv2.imshow('Polje0_31', img7)
            img8 = frame[295:345, 225:275]
            cv2.imshow('Polje0_32', img8)
            img9 = frame[295:345, 325:375]
            cv2.imshow('Polje0_33', img9)

        elif stranica == 1:

            img11 = frame[95:145, 125:175]
            cv2.imshow('Polje1_11', img11)
            img12 = frame[95:145, 225:275]
            cv2.imshow('Polje1_12', img12)
            img13 = frame[95:145, 325:375]
            cv2.imshow('Polje1_13', img13)
            img14 = frame[195:245, 125:175]
            cv2.imshow('Polje1_21', img14)
            img15 = frame[195:245, 225:275]
            cv2.imshow('Polje1_22', img15)
            img16 = frame[195:245, 325:375]
            cv2.imshow('Polje1_23', img16)
            img17 = frame[295:345, 125:175]
            cv2.imshow('Polje1_31', img17)
            img18 = frame[295:345, 225:275]
            cv2.imshow('Polje1_32', img18)
            img19 = frame[295:345, 325:375]
            cv2.imshow('Polje1_33', img19)

        elif stranica == 2:

            img21 = frame[95:145, 125:175]
            cv2.imshow('Polje2_11', img21)
            img22 = frame[95:145, 225:275]
            cv2.imshow('Polje2_12', img22)
            img23 = frame[95:145, 325:375]
            cv2.imshow('Polje2_13', img23)
            img24 = frame[195:245, 125:175]
            cv2.imshow('Polje2_21', img24)
            img25 = frame[195:245, 225:275]
            cv2.imshow('Polje2_22', img25)
            img26 = frame[195:245, 325:375]
            cv2.imshow('Polje2_23', img26)
            img27 = frame[295:345, 125:175]
            cv2.imshow('Polje2_31', img27)
            img28 = frame[295:345, 225:275]
            cv2.imshow('Polje2_32', img28)
            img29 = frame[295:345, 325:375]
            cv2.imshow('Polje2_33', img29)

        elif stranica == 3:

            img31 = frame[95:145, 125:175]
            cv2.imshow('Polje3_11', img31)
            img32 = frame[95:145, 225:275]
            cv2.imshow('Polje3_12', img32)
            img33 = frame[95:145, 325:375]
            cv2.imshow('Polje3_13', img33)
            img34 = frame[195:245, 125:175]
            cv2.imshow('Polje3_21', img34)
            img35 = frame[195:245, 225:275]
            cv2.imshow('Polje3_22', img35)
            img36 = frame[195:245, 325:375]
            cv2.imshow('Polje3_23', img36)
            img37 = frame[295:345, 125:175]
            cv2.imshow('Polje3_31', img37)
            img38 = frame[295:345, 225:275]
            cv2.imshow('Polje3_32', img38)
            img39 = frame[295:345, 325:375]
            cv2.imshow('Polje3_33', img39)

        elif stranica == 4:

            img41 = frame[95:145, 125:175]
            cv2.imshow('Polje4_11', img41)
            img42 = frame[95:145, 225:275]
            cv2.imshow('Polje4_12', img42)
            img43 = frame[95:145, 325:375]
            cv2.imshow('Polje4_13', img43)
            img44 = frame[195:245, 125:175]
            cv2.imshow('Polje4_21', img44)
            img45 = frame[195:245, 225:275]
            cv2.imshow('Polje4_22', img45)
            img46 = frame[195:245, 325:375]
            cv2.imshow('Polje4_23', img46)
            img47 = frame[295:345, 125:175]
            cv2.imshow('Polje4_31', img47)
            img48 = frame[295:345, 225:275]
            cv2.imshow('Polje4_32', img48)
            img49 = frame[295:345, 325:375]
            cv2.imshow('Polje4_33', img49)

        elif stranica == 5:

            img51 = frame[95:145, 125:175]
            cv2.imshow('Polje5_11', img51)
            img52 = frame[95:145, 225:275]
            cv2.imshow('Polje5_12', img52)
            img53 = frame[95:145, 325:375]
            cv2.imshow('Polje5_13', img53)
            img54 = frame[195:245, 125:175]
            cv2.imshow('Polje5_21', img54)
            img55 = frame[195:245, 225:275]
            cv2.imshow('Polje5_22', img55)
            img56 = frame[195:245, 325:375]
            cv2.imshow('Polje5_23', img56)
            img57 = frame[295:345, 125:175]
            cv2.imshow('Polje5_31', img57)
            img58 = frame[295:345, 225:275]
            cv2.imshow('Polje5_32', img58)
            img59 = frame[295:345, 325:375]
            cv2.imshow('Polje5_33', img59)

        stranica = stranica + 1

    # Press 'q' to exit the loop
    if cv2.waitKey(2) == ord('q'):
       break

#plt.figure()
#plt.imshow(img1)
#plt.show()

##########################################################################

print('TOP')

polje0_11 = []
polje0_12 = []
polje0_13 = []
polje0_21 = []
polje0_22 = []
polje0_23 = []
polje0_31 = []
polje0_32 = []
polje0_33 = []

r, g, b = cv2.split(img1)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < 80 and g_avg < 40 and b_avg < 115:
    polje0_11 = 'crvena'
elif 95 < r_avg < 140 and 135 < g_avg < 180 and 95 < b_avg < 125:
    polje0_11 = 'žuta'
elif 80 < r_avg < 125 and 105 < g_avg < 140 and b_avg < 20:
    polje0_11 = 'zelena'
elif 150 < r_avg < 215 and g_avg < 80 and b_avg < 15:
    polje0_11 = 'plava'
elif r_avg < 95 and g_avg < 85 and 145 < b_avg < 180:  # g<200 b<100
    polje0_11 = 'narandžasta'
elif 170 < r_avg < 235 and 130 < g_avg < 175 and 105 < b_avg < 145:
    polje0_11 = 'bela'
else:
    polje0_11 = 'nepoznata'
print(polje0_11)

r, g, b = cv2.split(img2)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < 80 and g_avg < 40 and b_avg < 115:
    polje0_12 = 'crvena'
elif 95 < r_avg < 140 and 135 < g_avg < 180 and 95 < b_avg < 125:
    polje0_12 = 'žuta'
elif 80 < r_avg < 125 and 105 < g_avg < 140 and b_avg < 20:
    polje0_12 = 'zelena'
elif 150 < r_avg < 215 and g_avg < 80 and b_avg < 15:
    polje0_12 = 'plava'
elif r_avg < 95 and g_avg < 85 and 145 < b_avg < 180:
    polje0_12 = 'narandžasta'
elif 170 < r_avg < 235 and 130 < g_avg < 175 and 105 < b_avg < 145:
    polje0_12 = 'bela'
else:
    polje0_12 = 'nepoznata'
print(polje0_12)

r, g, b = cv2.split(img3)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < 80 and g_avg < 40 and b_avg < 115:
    polje0_13 = 'crvena'
elif 95 < r_avg < 140 and 135 < g_avg < 180 and 95 < b_avg < 125:
    polje0_13 = 'žuta'
elif 80 < r_avg < 125 and 105 < g_avg < 140 and b_avg < 20:
    polje0_13 = 'zelena'
elif 150 < r_avg < 215 and g_avg < 80 and b_avg < 15:
    polje0_13 = 'plava'
elif r_avg < 95 and g_avg < 85 and 145 < b_avg < 180:
    polje0_13 = 'narandžasta'
elif 170 < r_avg < 235 and 130 < g_avg < 175 and 105 < b_avg < 145:
    polje0_13 = 'bela'
else:
    polje0_13 = 'nepoznata'
print(polje0_13)

r, g, b = cv2.split(img4)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < 80 and g_avg < 40 and b_avg < 115:
    polje0_21 = 'crvena'
elif 95 < r_avg < 140 and 135 < g_avg < 180 and 95 < b_avg < 125:
    polje0_21 = 'žuta'
elif 80 < r_avg < 125 and 105 < g_avg < 140 and b_avg < 20:
    polje0_21 = 'zelena'
elif 150 < r_avg < 215 and g_avg < 75 and b_avg < 15:
    polje0_21 = 'plava'
elif r_avg < 95 and g_avg < 85 and 145 < b_avg < 180:
    polje0_21 = 'narandžasta'
elif 170 < r_avg < 235 and 130 < g_avg < 175 and 105 < b_avg < 145:
    polje0_21 = 'bela'
else:
    polje0_21 = 'nepoznata'
print(polje0_21)

r, g, b = cv2.split(img5)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < 80 and g_avg < 40 and b_avg < 115:
    polje0_22 = 'crvena'
elif 95 < r_avg < 140 and 135 < g_avg < 180 and 95 < b_avg < 125:
    polje0_22 = 'žuta'
elif 80 < r_avg < 125 and 105 < g_avg < 140 and b_avg < 20:
    polje0_22 = 'zelena'
elif 150 < r_avg < 215 and g_avg < 75 and b_avg < 15:
    polje0_22 = 'plava'
elif r_avg < 95 and g_avg < 85 and 145 < b_avg < 180:
    polje0_22 = 'narandžasta'
elif 170 < r_avg < 235 and 130 < g_avg < 175 and 105 < b_avg < 145:
    polje0_22 = 'bela'
else:
    polje0_22 = 'nepoznata'
print(polje0_22)

r, g, b = cv2.split(img6)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < 80 and g_avg < 40 and b_avg < 115:
    polje0_23 = 'crvena'
elif 95 < r_avg < 140 and 135 < g_avg < 180 and 95 < b_avg < 125:
    polje0_23 = 'žuta'
elif 80 < r_avg < 125 and 105 < g_avg < 140 and b_avg < 20:
    polje0_23 = 'zelena'
elif 150 < r_avg < 215 and g_avg < 75 and b_avg < 15:
    polje0_23 = 'plava'
elif r_avg < 95 and g_avg < 85 and 145 < b_avg < 180:
    polje0_23 = 'narandžasta'
elif 170 < r_avg < 235 and 130 < g_avg < 175 and 105 < b_avg < 145:
    polje0_23 = 'bela'
else:
    polje0_23 = 'nepoznata'
print(polje0_23)

r, g, b = cv2.split(img7)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < 80 and g_avg < 40 and b_avg < 115:
    polje0_31 = 'crvena'
elif 95 < r_avg < 140 and 135 < g_avg < 180 and 95 < b_avg < 125:
    polje0_31 = 'žuta'
elif 80 < r_avg < 125 and 105 < g_avg < 140 and b_avg < 20:
    polje0_31 = 'zelena'
elif 150 < r_avg < 215 and g_avg < 75 and b_avg < 15:
    polje0_31 = 'plava'
elif r_avg < 95 and g_avg < 85 and 145 < b_avg < 180:
    polje0_31 = 'narandžasta'
elif 170 < r_avg < 235 and 130 < g_avg < 175 and 105 < b_avg < 145:
    polje0_31 = 'bela'
else:
    polje0_31 = 'nepoznata'
print(polje0_31)

r, g, b = cv2.split(img8)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < 80 and g_avg < 40 and b_avg < 115:
    polje0_32 = 'crvena'
elif 95 < r_avg < 140 and 135 < g_avg < 180 and 95 < b_avg < 125:
    polje0_32 = 'žuta'
elif 80 < r_avg < 125 and 105 < g_avg < 140 and b_avg < 20:
    polje0_32 = 'zelena'
elif 150 < r_avg < 215 and g_avg < 75 and b_avg < 15:
    polje0_32 = 'plava'
elif r_avg < 95 and g_avg < 85 and 145 < b_avg < 180:
    polje0_32 = 'narandžasta'
elif 170 < r_avg < 235 and 130 < g_avg < 175 and 105 < b_avg < 145:
    polje0_32 = 'bela'
else:
    polje0_32 = 'nepoznata'
print(polje0_32)

r, g, b = cv2.split(img9)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < 80 and g_avg < 40 and b_avg < 115:
    polje0_33 = 'crvena'
elif 95 < r_avg < 140 and 135 < g_avg < 180 and 95 < b_avg < 125:
    polje0_33 = 'žuta'
elif 80 < r_avg < 125 and 105 < g_avg < 140 and b_avg < 20:
    polje0_33 = 'zelena'
elif 150 < r_avg < 215 and g_avg < 75 and b_avg < 15:
    polje0_33 = 'plava'
elif r_avg < 95 and g_avg < 85 and 145 < b_avg < 180:
    polje0_33 = 'narandžasta'
elif 170 < r_avg < 235 and 130 < g_avg < 175 and 105 < b_avg < 145:
    polje0_33 = 'bela'
else:
    polje0_33 = 'nepoznata'
print(polje0_33)

####################################################################

print('FRONT')

polje1_11 = []
polje1_12 = []
polje1_13 = []
polje1_21 = []
polje1_22 = []
polje1_23 = []
polje1_31 = []
polje1_32 = []
polje1_33 = []

r, g, b = cv2.split(img11)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < 80 and g_avg < 40 and b_avg < 115:
    polje1_11 = 'crvena'
elif 95 < r_avg < 140 and 135 < g_avg < 180 and 95 < b_avg < 125:
    polje1_11 = 'žuta'
elif 80 < r_avg < 125 and 105 < g_avg < 140 and b_avg < 20:
    polje1_11 = 'zelena'
elif 150 < r_avg < 215 and g_avg < 75 and b_avg < 15:
    polje1_11 = 'plava'
elif r_avg < 95 and g_avg < 85 and 145 < b_avg < 180:
    polje1_11 = 'narandžasta'
elif 170 < r_avg < 235 and 130 < g_avg < 175 and 105 < b_avg < 145:
    polje1_11 = 'bela'
else:
    polje1_11 = 'nepoznata'
print(polje1_11)

r, g, b = cv2.split(img12)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < 80 and g_avg < 40 and b_avg < 115:
    polje1_12 = 'crvena'
elif 95 < r_avg < 140 and 135 < g_avg < 180 and 95 < b_avg < 125:
    polje1_12 = 'žuta'
elif 80 < r_avg < 125 and 105 < g_avg < 140 and b_avg < 20:
    polje1_12 = 'zelena'
elif 150 < r_avg < 215 and g_avg < 75 and b_avg < 15:
    polje1_12 = 'plava'
elif r_avg < 95 and g_avg < 85 and 145 < b_avg < 180:
    polje1_12 = 'narandžasta'
elif 170 < r_avg < 235 and 130 < g_avg < 175 and 105 < b_avg < 145:
    polje1_12 = 'bela'
else:
    polje1_12 = 'nepoznata'
print(polje1_12)

r, g, b = cv2.split(img13)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < 80 and g_avg < 40 and b_avg < 115:
    polje1_13 = 'crvena'
elif 95 < r_avg < 140 and 135 < g_avg < 180 and 95 < b_avg < 125:
    polje1_13 = 'žuta'
elif 80 < r_avg < 125 and 105 < g_avg < 140 and b_avg < 20:
    polje1_13 = 'zelena'
elif 150 < r_avg < 215 and g_avg < 75 and b_avg < 15:
    polje1_13 = 'plava'
elif r_avg < 95 and g_avg < 85 and 145 < b_avg < 180:
    polje1_13 = 'narandžasta'
elif 170 < r_avg < 235 and 130 < g_avg < 175 and 105 < b_avg < 145:
    polje1_13 = 'bela'
else:
    polje1_13 = 'nepoznata'
print(polje1_13)

r, g, b = cv2.split(img14)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < 80 and g_avg < 40 and b_avg < 115:
    polje1_21 = 'crvena'
elif 95 < r_avg < 140 and 135 < g_avg < 180 and 95 < b_avg < 125:
    polje1_21 = 'žuta'
elif 80 < r_avg < 125 and 105 < g_avg < 140 and b_avg < 20:
    polje1_21 = 'zelena'
elif 150 < r_avg < 215 and g_avg < 75 and b_avg < 15:
    polje1_21 = 'plava'
elif r_avg < 95 and g_avg < 85 and 145 < b_avg < 180:
    polje1_21 = 'narandžasta'
elif 170 < r_avg < 235 and 130 < g_avg < 175 and 105 < b_avg < 145:
    polje1_21 = 'bela'
else:
    polje1_21 = 'nepoznata'
print(polje1_21)

r, g, b = cv2.split(img15)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < 80 and g_avg < 40 and b_avg < 115:
    polje1_22 = 'crvena'
elif 95 < r_avg < 140 and 135 < g_avg < 180 and 95 < b_avg < 125:
    polje1_22 = 'žuta'
elif 80 < r_avg < 125 and 105 < g_avg < 140 and b_avg < 20:
    polje1_22 = 'zelena'
elif 150 < r_avg < 215 and g_avg < 75 and b_avg < 15:
    polje1_22 = 'plava'
elif r_avg < 95 and g_avg < 85 and 145 < b_avg < 180:
    polje1_22 = 'narandžasta'
elif 170 < r_avg < 235 and 130 < g_avg < 175 and 105 < b_avg < 145:
    polje1_22 = 'bela'
else:
    polje1_22 = 'nepoznata'
print(polje1_22)

r, g, b = cv2.split(img16)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < 80 and g_avg < 40 and b_avg < 115:
    polje1_23 = 'crvena'
elif 95 < r_avg < 140 and 135 < g_avg < 180 and 95 < b_avg < 125:
    polje1_23 = 'žuta'
elif 80 < r_avg < 125 and 105 < g_avg < 140 and b_avg < 20:
    polje1_23 = 'zelena'
elif 150 < r_avg < 215 and g_avg < 75 and b_avg < 15:
    polje1_23 = 'plava'
elif r_avg < 95 and g_avg < 85 and 145 < b_avg < 180:
    polje1_23 = 'narandžasta'
elif 170 < r_avg < 235 and 130 < g_avg < 175 and 105 < b_avg < 145:
    polje1_23 = 'bela'
else:
    polje1_23 = 'nepoznata'
print(polje1_23)

r, g, b = cv2.split(img17)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < 80 and g_avg < 40 and b_avg < 115:
    polje1_31 = 'crvena'
elif 95 < r_avg < 140 and 135 < g_avg < 180 and 95 < b_avg < 125:
    polje1_31 = 'žuta'
elif 80 < r_avg < 125 and 105 < g_avg < 140 and b_avg < 20:
    polje1_31 = 'zelena'
elif 150 < r_avg < 215 and g_avg < 75 and b_avg < 15:
    polje1_31 = 'plava'
elif r_avg < 95 and g_avg < 85 and 145 < b_avg < 180:
    polje1_31 = 'narandžasta'
elif 170 < r_avg < 235 and 130 < g_avg < 175 and 105 < b_avg < 145:
    polje1_31 = 'bela'
else:
    polje1_31 = 'nepoznata'
print(polje1_31)

r, g, b = cv2.split(img18)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < 80 and g_avg < 40 and b_avg < 115:
    polje1_32 = 'crvena'
elif 95 < r_avg < 140 and 135 < g_avg < 180 and 95 < b_avg < 125:
    polje1_32 = 'žuta'
elif 80 < r_avg < 125 and 105 < g_avg < 140 and b_avg < 20:
    polje1_32 = 'zelena'
elif 150 < r_avg < 215 and g_avg < 75 and b_avg < 15:
    polje1_32 = 'plava'
elif r_avg < 95 and g_avg < 85 and 145 < b_avg < 180:
    polje1_32 = 'narandžasta'
elif 170 < r_avg < 235 and 130 < g_avg < 175 and 105 < b_avg < 145:
    polje1_32 = 'bela'
else:
    polje1_32 = 'nepoznata'
print(polje1_32)

r, g, b = cv2.split(img19)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < 80 and g_avg < 40 and b_avg < 115:
    polje1_33 = 'crvena'
elif 95 < r_avg < 140 and 135 < g_avg < 180 and 95 < b_avg < 125:
    polje1_33 = 'žuta'
elif 80 < r_avg < 125 and 105 < g_avg < 140 and b_avg < 20:
    polje1_33 = 'zelena'
elif 150 < r_avg < 215 and g_avg < 75 and b_avg < 15:
    polje1_33 = 'plava'
elif r_avg < 95 and g_avg < 85 and 145 < b_avg < 180:
    polje1_33 = 'narandžasta'
elif 170 < r_avg < 235 and 130 < g_avg < 175 and 105 < b_avg < 145:
    polje1_33 = 'bela'
else:
    polje1_33 = 'nepoznata'
print(polje1_33)

########################################################################

print('BOTTOM')

polje2_11 = []
polje2_12 = []
polje2_13 = []
polje2_21 = []
polje2_22 = []
polje2_23 = []
polje2_31 = []
polje2_32 = []
polje2_33 = []

r, g, b = cv2.split(img21)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < 80 and g_avg < 40 and b_avg < 115:
    polje2_11 = 'crvena'
elif 95 < r_avg < 140 and 135 < g_avg < 180 and 95 < b_avg < 125:
    polje2_11 = 'žuta'
elif 80 < r_avg < 125 and 105 < g_avg < 140 and b_avg < 20:
    polje2_11 = 'zelena'
elif 150 < r_avg < 215 and g_avg < 75 and b_avg < 15:
    polje2_11 = 'plava'
elif r_avg < 95 and g_avg < 85 and 145 < b_avg < 180:
    polje2_11 = 'narandžasta'
elif 170 < r_avg < 235 and 130 < g_avg < 175 and 105 < b_avg < 145:
    polje2_11 = 'bela'
else:
    polje2_11 = 'nepoznata'
print(polje2_11)

r, g, b = cv2.split(img22)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < 80 and g_avg < 40 and b_avg < 115:
    polje2_12 = 'crvena'
elif 95 < r_avg < 140 and 135 < g_avg < 180 and 95 < b_avg < 125:
    polje2_12 = 'žuta'
elif 80 < r_avg < 125 and 105 < g_avg < 140 and b_avg < 20:
    polje2_12 = 'zelena'
elif 150 < r_avg < 215 and g_avg < 75 and b_avg < 15:
    polje2_12 = 'plava'
elif r_avg < 95 and g_avg < 85 and 145 < b_avg < 180:
    polje2_12 = 'narandžasta'
elif 170 < r_avg < 235 and 130 < g_avg < 175 and 105 < b_avg < 145:
    polje2_12 = 'bela'
else:
    polje2_12 = 'nepoznata'
print(polje2_12)

r, g, b = cv2.split(img23)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < 80 and g_avg < 40 and b_avg < 115:
    polje2_13 = 'crvena'
elif 95 < r_avg < 140 and 135 < g_avg < 180 and 95 < b_avg < 125:
    polje2_13 = 'žuta'
elif 80 < r_avg < 125 and 105 < g_avg < 140 and b_avg < 20:
    polje2_13 = 'zelena'
elif 150 < r_avg < 215 and g_avg < 75 and b_avg < 15:
    polje2_13 = 'plava'
elif r_avg < 95 and g_avg < 85 and 145 < b_avg < 180:
    polje2_13 = 'narandžasta'
elif 170 < r_avg < 235 and 130 < g_avg < 175 and 105 < b_avg < 145:
    polje2_13 = 'bela'
else:
    polje2_13 = 'nepoznata'
print(polje2_13)

r, g, b = cv2.split(img24)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < 80 and g_avg < 40 and b_avg < 115:
    polje2_21 = 'crvena'
elif 95 < r_avg < 140 and 135 < g_avg < 180 and 95 < b_avg < 125:
    polje2_21 = 'žuta'
elif 80 < r_avg < 125 and 105 < g_avg < 140 and b_avg < 20:
    polje2_21 = 'zelena'
elif 150 < r_avg < 215 and g_avg < 75 and b_avg < 15:
    polje2_21 = 'plava'
elif r_avg < 95 and g_avg < 85 and 145 < b_avg < 180:
    polje2_21 = 'narandžasta'
elif 170 < r_avg < 235 and 130 < g_avg < 175 and 105 < b_avg < 145:
    polje2_21 = 'bela'
else:
    polje2_21 = 'nepoznata'
print(polje2_21)

r, g, b = cv2.split(img25)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < 80 and g_avg < 40 and b_avg < 115:
    polje2_22 = 'crvena'
elif 95 < r_avg < 140 and 135 < g_avg < 180 and 95 < b_avg < 125:
    polje2_22 = 'žuta'
elif 80 < r_avg < 125 and 105 < g_avg < 140 and b_avg < 20:
    polje2_22 = 'zelena'
elif 150 < r_avg < 215 and g_avg < 75 and b_avg < 15:
    polje2_22 = 'plava'
elif r_avg < 95 and g_avg < 85 and 145 < b_avg < 180:
    polje2_22 = 'narandžasta'
elif 170 < r_avg < 235 and 130 < g_avg < 175 and 105 < b_avg < 145:
    polje2_22 = 'bela'
else:
    polje2_22 = 'nepoznata'
print(polje2_22)

r, g, b = cv2.split(img26)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < 80 and g_avg < 40 and b_avg < 115:
    polje2_23 = 'crvena'
elif 95 < r_avg < 140 and 135 < g_avg < 180 and 95 < b_avg < 125:
    polje2_23 = 'žuta'
elif 80 < r_avg < 125 and 105 < g_avg < 140 and b_avg < 20:
    polje2_23 = 'zelena'
elif 150 < r_avg < 215 and g_avg < 75 and b_avg < 15:
    polje2_23 = 'plava'
elif r_avg < 95 and g_avg < 85 and 145 < b_avg < 180:
    polje2_23 = 'narandžasta'
elif 170 < r_avg < 235 and 130 < g_avg < 175 and 105 < b_avg < 145:
    polje2_23 = 'bela'
else:
    polje2_23 = 'nepoznata'
print(polje2_23)

r, g, b = cv2.split(img27)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < 80 and g_avg < 40 and b_avg < 115:
    polje2_31 = 'crvena'
elif 95 < r_avg < 140 and 135 < g_avg < 180 and 95 < b_avg < 125:
    polje2_31 = 'žuta'
elif 80 < r_avg < 125 and 105 < g_avg < 140 and b_avg < 20:
    polje2_31 = 'zelena'
elif 150 < r_avg < 215 and g_avg < 75 and b_avg < 15:
    polje2_31 = 'plava'
elif r_avg < 95 and g_avg < 85 and 145 < b_avg < 180:
    polje2_31 = 'narandžasta'
elif 170 < r_avg < 235 and 130 < g_avg < 175 and 105 < b_avg < 145:
    polje2_31 = 'bela'
else:
    polje2_31 = 'nepoznata'
print(polje2_31)

r, g, b = cv2.split(img28)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < 80 and g_avg < 40 and b_avg < 115:
    polje2_32 = 'crvena'
elif 95 < r_avg < 140 and 135 < g_avg < 180 and 95 < b_avg < 125:
    polje2_32 = 'žuta'
elif 80 < r_avg < 125 and 105 < g_avg < 140 and b_avg < 20:
    polje2_32 = 'zelena'
elif 150 < r_avg < 215 and g_avg < 75 and b_avg < 15:
    polje2_32 = 'plava'
elif r_avg < 95 and g_avg < 85 and 145 < b_avg < 180:
    polje2_32 = 'narandžasta'
elif 170 < r_avg < 235 and 130 < g_avg < 175 and 105 < b_avg < 145:
    polje2_32 = 'bela'
else:
    polje2_32 = 'nepoznata'
print(polje2_32)

r, g, b = cv2.split(img29)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < 80 and g_avg < 40 and b_avg < 115:
    polje2_33 = 'crvena'
elif 95 < r_avg < 140 and 135 < g_avg < 180 and 95 < b_avg < 125:
    polje2_33 = 'žuta'
elif 80 < r_avg < 125 and 105 < g_avg < 140 and b_avg < 20:
    polje2_33 = 'zelena'
elif 150 < r_avg < 215 and g_avg < 75 and b_avg < 15:
    polje2_33 = 'plava'
elif r_avg < 95 and g_avg < 85 and 145 < b_avg < 180:
    polje2_33 = 'narandžasta'
elif 170 < r_avg < 235 and 130 < g_avg < 175 and 105 < b_avg < 145:
    polje2_33 = 'bela'
else:
    polje2_33 = 'nepoznata'
print(polje2_33)

#########################################################################

print('LEFT')

polje3_11 = []
polje3_12 = []
polje3_13 = []
polje3_21 = []
polje3_22 = []
polje3_23 = []
polje3_31 = []
polje3_32 = []
polje3_33 = []

r, g, b = cv2.split(img31)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < 80 and g_avg < 40 and b_avg < 115:
    polje3_11 = 'crvena'
elif 95 < r_avg < 140 and 135 < g_avg < 180 and 95 < b_avg < 125:
    polje3_11 = 'žuta'
elif 80 < r_avg < 125 and 105 < g_avg < 140 and b_avg < 20:
    polje3_11 = 'zelena'
elif 150 < r_avg < 215 and g_avg < 75 and b_avg < 15:
    polje3_11 = 'plava'
elif r_avg < 95 and g_avg < 85 and 145 < b_avg < 180:
    polje3_11 = 'narandžasta'
elif 170 < r_avg < 235 and 130 < g_avg < 175 and 105 < b_avg < 145:
    polje3_11 = 'bela'
else:
    polje3_11 = 'nepoznata'
print(polje3_11)

r, g, b = cv2.split(img32)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < 80 and g_avg < 40 and b_avg < 115:
    polje3_12 = 'crvena'
elif 95 < r_avg < 140 and 135 < g_avg < 180 and 95 < b_avg < 125:
    polje3_12 = 'žuta'
elif 80 < r_avg < 125 and 105 < g_avg < 140 and b_avg < 20:
    polje3_12 = 'zelena'
elif 150 < r_avg < 215 and g_avg < 75 and b_avg < 15:
    polje3_12 = 'plava'
elif r_avg < 95 and g_avg < 85 and 145 < b_avg < 180:
    polje3_12 = 'narandžasta'
elif 170 < r_avg < 235 and 130 < g_avg < 175 and 105 < b_avg < 145:
    polje3_12 = 'bela'
else:
    polje3_12 = 'nepoznata'
print(polje3_12)

r, g, b = cv2.split(img33)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < 80 and g_avg < 40 and b_avg < 115:
    polje3_13 = 'crvena'
elif 95 < r_avg < 140 and 135 < g_avg < 180 and 95 < b_avg < 125:
    polje3_13 = 'žuta'
elif 80 < r_avg < 125 and 105 < g_avg < 140 and b_avg < 20:
    polje3_13 = 'zelena'
elif 150 < r_avg < 215 and g_avg < 75 and b_avg < 15:
    polje3_13 = 'plava'
elif r_avg < 95 and g_avg < 85 and 145 < b_avg < 180:
    polje3_13 = 'narandžasta'
elif 170 < r_avg < 235 and 130 < g_avg < 175 and 105 < b_avg < 145:
    polje3_13 = 'bela'
else:
    polje3_13 = 'nepoznata'
print(polje3_13)

r, g, b = cv2.split(img34)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < 80 and g_avg < 40 and b_avg < 115:
    polje3_21 = 'crvena'
elif 95 < r_avg < 140 and 135 < g_avg < 180 and 95 < b_avg < 125:
    polje3_21 = 'žuta'
elif 80 < r_avg < 125 and 105 < g_avg < 140 and b_avg < 20:
    polje3_21 = 'zelena'
elif 150 < r_avg < 215 and g_avg < 75 and b_avg < 15:
    polje3_21 = 'plava'
elif r_avg < 95 and g_avg < 85 and 145 < b_avg < 180:
    polje3_21 = 'narandžasta'
elif 170 < r_avg < 235 and 130 < g_avg < 175 and 105 < b_avg < 145:
    polje3_21 = 'bela'
else:
    polje3_21 = 'nepoznata'
print(polje3_21)

r, g, b = cv2.split(img35)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < 80 and g_avg < 40 and b_avg < 115:
    polje3_22 = 'crvena'
elif 95 < r_avg < 140 and 135 < g_avg < 180 and 95 < b_avg < 125:
    polje3_22 = 'žuta'
elif 80 < r_avg < 125 and 105 < g_avg < 140 and b_avg < 20:
    polje3_22 = 'zelena'
elif 150 < r_avg < 215 and g_avg < 75 and b_avg < 15:
    polje3_22 = 'plava'
elif r_avg < 95 and g_avg < 85 and 145 < b_avg < 180:
    polje3_22 = 'narandžasta'
elif 170 < r_avg < 235 and 130 < g_avg < 175 and 105 < b_avg < 145:
    polje3_22 = 'bela'
else:
    polje3_22 = 'nepoznata'
print(polje3_22)

r, g, b = cv2.split(img36)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < 80 and g_avg < 40 and b_avg < 115:
    polje3_23 = 'crvena'
elif 95 < r_avg < 140 and 135 < g_avg < 180 and 95 < b_avg < 125:
    polje3_23 = 'žuta'
elif 80 < r_avg < 125 and 105 < g_avg < 140 and b_avg < 20:
    polje3_23 = 'zelena'
elif 150 < r_avg < 215 and g_avg < 75 and b_avg < 15:
    polje3_23 = 'plava'
elif r_avg < 95 and g_avg < 85 and 145 < b_avg < 180:
    polje3_23 = 'narandžasta'
elif 170 < r_avg < 235 and 130 < g_avg < 175 and 105 < b_avg < 145:
    polje3_23 = 'bela'
else:
    polje3_23 = 'nepoznata'
print(polje3_23)

r, g, b = cv2.split(img37)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < 80 and g_avg < 40 and b_avg < 115:
    polje3_31 = 'crvena'
elif 95 < r_avg < 140 and 135 < g_avg < 180 and 95 < b_avg < 125:
    polje3_31 = 'žuta'
elif 80 < r_avg < 125 and 105 < g_avg < 140 and b_avg < 20:
    polje3_31 = 'zelena'
elif 150 < r_avg < 215 and g_avg < 75 and b_avg < 15:
    polje3_31 = 'plava'
elif r_avg < 95 and g_avg < 85 and 145 < b_avg < 180:
    polje3_31 = 'narandžasta'
elif 170 < r_avg < 235 and 130 < g_avg < 175 and 105 < b_avg < 145:
    polje3_31 = 'bela'
else:
    polje3_31 = 'nepoznata'
print(polje3_31)

r, g, b = cv2.split(img38)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < 80 and g_avg < 40 and b_avg < 115:
    polje3_32 = 'crvena'
elif 95 < r_avg < 140 and 135 < g_avg < 180 and 95 < b_avg < 125:
    polje3_32 = 'žuta'
elif 80 < r_avg < 125 and 105 < g_avg < 140 and b_avg < 20:
    polje3_32 = 'zelena'
elif 150 < r_avg < 215 and g_avg < 75 and b_avg < 15:
    polje3_32 = 'plava'
elif r_avg < 95 and g_avg < 85 and 145 < b_avg < 180:
    polje3_32 = 'narandžasta'
elif 170 < r_avg < 235 and 130 < g_avg < 175 and 105 < b_avg < 145:
    polje3_32 = 'bela'
else:
    polje3_32 = 'nepoznata'
print(polje3_32)

r, g, b = cv2.split(img39)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < 80 and g_avg < 40 and b_avg < 115:
    polje3_33 = 'crvena'
elif 95 < r_avg < 140 and 135 < g_avg < 180 and 95 < b_avg < 125:
    polje3_33 = 'žuta'
elif 80 < r_avg < 125 and 105 < g_avg < 140 and b_avg < 20:
    polje3_33 = 'zelena'
elif 150 < r_avg < 215 and g_avg < 75 and b_avg < 15:
    polje3_33 = 'plava'
elif r_avg < 95 and g_avg < 85 and 145 < b_avg < 180:
    polje3_33 = 'narandžasta'
elif 170 < r_avg < 235 and 130 < g_avg < 175 and 105 < b_avg < 145:
    polje3_33 = 'bela'
else:
    polje3_33 = 'nepoznata'
print(polje3_33)

#################################################################

print('BACK')

polje4_11 = []
polje4_12 = []
polje4_13 = []
polje4_21 = []
polje4_22 = []
polje4_23 = []
polje4_31 = []
polje4_32 = []
polje4_33 = []

r, g, b = cv2.split(img41)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < 80 and g_avg < 40 and b_avg < 115:
    polje4_11 = 'crvena'
elif 95 < r_avg < 140 and 135 < g_avg < 180 and 95 < b_avg < 125:
    polje4_11 = 'žuta'
elif 80 < r_avg < 125 and 105 < g_avg < 140 and b_avg < 20:
    polje4_11 = 'zelena'
elif 150 < r_avg < 215 and g_avg < 75 and b_avg < 15:
    polje4_11 = 'plava'
elif r_avg < 95 and g_avg < 85 and 145 < b_avg < 180:
    polje4_11 = 'narandžasta'
elif 170 < r_avg < 235 and 130 < g_avg < 175 and 105 < b_avg < 145:
    polje4_11 = 'bela'
else:
    polje4_11 = 'nepoznata'
print(polje4_11)

r, g, b = cv2.split(img42)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < 80 and g_avg < 40 and b_avg < 115:
    polje4_12 = 'crvena'
elif 95 < r_avg < 140 and 135 < g_avg < 180 and 95 < b_avg < 125:
    polje4_12 = 'žuta'
elif 80 < r_avg < 125 and 105 < g_avg < 140 and b_avg < 20:
    polje4_12 = 'zelena'
elif 150 < r_avg < 215 and g_avg < 75 and b_avg < 15:
    polje4_12 = 'plava'
elif r_avg < 95 and g_avg < 85 and 145 < b_avg < 180:
    polje4_12 = 'narandžasta'
elif 170 < r_avg < 235 and 130 < g_avg < 175 and 105 < b_avg < 145:
    polje4_12 = 'bela'
else:
    polje4_12 = 'nepoznata'
print(polje4_12)

r, g, b = cv2.split(img43)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < 80 and g_avg < 40 and b_avg < 115:
    polje4_13 = 'crvena'
elif 95 < r_avg < 140 and 135 < g_avg < 180 and 95 < b_avg < 125:
    polje4_13 = 'žuta'
elif 80 < r_avg < 125 and 105 < g_avg < 140 and b_avg < 20:
    polje4_13 = 'zelena'
elif 150 < r_avg < 215 and g_avg < 75 and b_avg < 15:
    polje4_13 = 'plava'
elif r_avg < 95 and g_avg < 85 and 145 < b_avg < 180:
    polje4_13 = 'narandžasta'
elif 170 < r_avg < 235 and 130 < g_avg < 175 and 105 < b_avg < 145:
    polje4_13 = 'bela'
else:
    polje4_13 = 'nepoznata'
print(polje4_13)

r, g, b = cv2.split(img44)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < 80 and g_avg < 40 and b_avg < 115:
    polje4_21 = 'crvena'
elif 95 < r_avg < 140 and 135 < g_avg < 180 and 95 < b_avg < 125:
    polje4_21 = 'žuta'
elif 80 < r_avg < 125 and 105 < g_avg < 140 and b_avg < 20:
    polje4_21 = 'zelena'
elif 150 < r_avg < 215 and g_avg < 75 and b_avg < 15:
    polje4_21 = 'plava'
elif r_avg < 95 and g_avg < 85 and 145 < b_avg < 180:
    polje4_21 = 'narandžasta'
elif 170 < r_avg < 235 and 130 < g_avg < 175 and 105 < b_avg < 145:
    polje4_21 = 'bela'
else:
    polje4_21 = 'nepoznata'
print(polje4_21)

r, g, b = cv2.split(img45)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < 80 and g_avg < 40 and b_avg < 115:
    polje4_22 = 'crvena'
elif 95 < r_avg < 140 and 135 < g_avg < 180 and 95 < b_avg < 125:
    polje4_22 = 'žuta'
elif 80 < r_avg < 125 and 105 < g_avg < 140 and b_avg < 20:
    polje4_22 = 'zelena'
elif 150 < r_avg < 215 and g_avg < 75 and b_avg < 15:
    polje4_22 = 'plava'
elif r_avg < 95 and g_avg < 85 and 145 < b_avg < 180:
    polje4_22 = 'narandžasta'
elif 170 < r_avg < 235 and 130 < g_avg < 175 and 105 < b_avg < 145:
    polje4_22 = 'bela'
else:
    polje4_22 = 'nepoznata'
print(polje4_22)

r, g, b = cv2.split(img46)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < 80 and g_avg < 40 and b_avg < 115:
    polje4_23 = 'crvena'
elif 95 < r_avg < 140 and 135 < g_avg < 180 and 95 < b_avg < 125:
    polje4_23 = 'žuta'
elif 80 < r_avg < 125 and 105 < g_avg < 140 and b_avg < 20:
    polje4_23 = 'zelena'
elif 150 < r_avg < 215 and g_avg < 75 and b_avg < 15:
    polje4_23 = 'plava'
elif r_avg < 95 and g_avg < 85 and 145 < b_avg < 180:
    polje4_23 = 'narandžasta'
elif 170 < r_avg < 235 and 130 < g_avg < 175 and 105 < b_avg < 145:
    polje4_23 = 'bela'
else:
    polje4_23 = 'nepoznata'
print(polje4_23)

r, g, b = cv2.split(img47)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < 80 and g_avg < 40 and b_avg < 115:
    polje4_31 = 'crvena'
elif 95 < r_avg < 140 and 135 < g_avg < 180 and 95 < b_avg < 125:
    polje4_31 = 'žuta'
elif 80 < r_avg < 125 and 105 < g_avg < 140 and b_avg < 20:
    polje4_31 = 'zelena'
elif 150 < r_avg < 215 and g_avg < 75 and b_avg < 15:
    polje4_31 = 'plava'
elif r_avg < 95 and g_avg < 85 and 145 < b_avg < 180:
    polje4_31 = 'narandžasta'
elif 170 < r_avg < 235 and 130 < g_avg < 175 and 105 < b_avg < 145:
    polje4_31 = 'bela'
else:
    polje4_31 = 'nepoznata'
print(polje4_31)

r, g, b = cv2.split(img48)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < 80 and g_avg < 40 and b_avg < 115:
    polje4_32 = 'crvena'
elif 95 < r_avg < 140 and 135 < g_avg < 180 and 95 < b_avg < 125:
    polje4_32 = 'žuta'
elif 80 < r_avg < 125 and 105 < g_avg < 140 and b_avg < 20:
    polje4_32 = 'zelena'
elif 150 < r_avg < 215 and g_avg < 75 and b_avg < 15:
    polje4_32 = 'plava'
elif r_avg < 95 and g_avg < 85 and 145 < b_avg < 180:
    polje4_32 = 'narandžasta'
elif 170 < r_avg < 235 and 130 < g_avg < 175 and 105 < b_avg < 145:
    polje4_32 = 'bela'
else:
    polje4_32 = 'nepoznata'
print(polje4_32)

r, g, b = cv2.split(img49)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < 80 and g_avg < 40 and b_avg < 115:
    polje4_33 = 'crvena'
elif 95 < r_avg < 140 and 135 < g_avg < 180 and 95 < b_avg < 125:
    polje4_33 = 'žuta'
elif 80 < r_avg < 125 and 105 < g_avg < 140 and b_avg < 20:
    polje4_33 = 'zelena'
elif 150 < r_avg < 215 and g_avg < 75 and b_avg < 15:
    polje4_33 = 'plava'
elif r_avg < 95 and g_avg < 85 and 145 < b_avg < 180:
    polje4_33 = 'narandžasta'
elif 170 < r_avg < 235 and 130 < g_avg < 175 and 105 < b_avg < 145:
    polje4_33 = 'bela'
else:
    polje4_33 = 'nepoznata'
print(polje4_33)

###############################################################

print('RIGHT')

polje5_11 = []
polje5_12 = []
polje5_13 = []
polje5_21 = []
polje5_22 = []
polje5_23 = []
polje5_31 = []
polje5_32 = []
polje5_33 = []

r, g, b = cv2.split(img51)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < 80 and g_avg < 40 and b_avg < 115:
    polje5_11 = 'crvena'
elif 95 < r_avg < 140 and 135 < g_avg < 180 and 95 < b_avg < 125:
    polje5_11 = 'žuta'
elif 80 < r_avg < 125 and 105 < g_avg < 140 and b_avg < 20:
    polje5_11 = 'zelena'
elif 150 < r_avg < 215 and g_avg < 75 and b_avg < 15:
    polje5_11 = 'plava'
elif r_avg < 95 and g_avg < 85 and 145 < b_avg < 180:
    polje5_11 = 'narandžasta'
elif 170 < r_avg < 235 and 130 < g_avg < 175 and 105 < b_avg < 145:
    polje5_11 = 'bela'
else:
    polje5_11 = 'nepoznata'
print(polje5_11)

r, g, b = cv2.split(img52)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < 80 and g_avg < 40 and b_avg < 115:
    polje5_12 = 'crvena'
elif 95 < r_avg < 140 and 135 < g_avg < 180 and 95 < b_avg < 125:
    polje5_12 = 'žuta'
elif 80 < r_avg < 125 and 105 < g_avg < 140 and b_avg < 20:
    polje5_12 = 'zelena'
elif 150 < r_avg < 215 and g_avg < 75 and b_avg < 15:
    polje5_12 = 'plava'
elif r_avg < 95 and g_avg < 85 and 145 < b_avg < 180:
    polje5_12 = 'narandžasta'
elif 170 < r_avg < 235 and 130 < g_avg < 175 and 105 < b_avg < 145:
    polje5_12 = 'bela'
else:
    polje5_12 = 'nepoznata'
print(polje5_12)

r, g, b = cv2.split(img53)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < 80 and g_avg < 40 and b_avg < 115:
    polje5_13 = 'crvena'
elif 95 < r_avg < 140 and 135 < g_avg < 180 and 95 < b_avg < 125:
    polje5_13 = 'žuta'
elif 80 < r_avg < 125 and 105 < g_avg < 140 and b_avg < 20:
    polje5_13 = 'zelena'
elif 150 < r_avg < 215 and g_avg < 75 and b_avg < 15:
    polje5_13 = 'plava'
elif r_avg < 95 and g_avg < 85 and 145 < b_avg < 180:
    polje5_13 = 'narandžasta'
elif 170 < r_avg < 235 and 130 < g_avg < 175 and 105 < b_avg < 145:
    polje5_13 = 'bela'
else:
    polje5_13 = 'nepoznata'
print(polje5_13)

r, g, b = cv2.split(img54)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < 80 and g_avg < 40 and b_avg < 115:
    polje5_21 = 'crvena'
elif 95 < r_avg < 140 and 135 < g_avg < 180 and 95 < b_avg < 125:
    polje5_21 = 'žuta'
elif 80 < r_avg < 125 and 105 < g_avg < 140 and b_avg < 20:
    polje5_21 = 'zelena'
elif 150 < r_avg < 215 and g_avg < 75 and b_avg < 15:
    polje5_21 = 'plava'
elif r_avg < 95 and g_avg < 85 and 145 < b_avg < 180:
    polje5_21 = 'narandžasta'
elif 170 < r_avg < 235 and 130 < g_avg < 175 and 105 < b_avg < 145:
    polje5_21 = 'bela'
else:
    polje5_21 = 'nepoznata'
print(polje5_21)

r, g, b = cv2.split(img55)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < 80 and g_avg < 40 and b_avg < 115:
    polje5_22 = 'crvena'
elif 95 < r_avg < 140 and 135 < g_avg < 180 and 95 < b_avg < 125:
    polje5_22 = 'žuta'
elif 80 < r_avg < 125 and 105 < g_avg < 140 and b_avg < 20:
    polje5_22 = 'zelena'
elif 150 < r_avg < 215 and g_avg < 75 and b_avg < 15:
    polje5_22 = 'plava'
elif r_avg < 95 and g_avg < 85 and 145 < b_avg < 180:
    polje5_22 = 'narandžasta'
elif 170 < r_avg < 235 and 130 < g_avg < 175 and 105 < b_avg < 145:
    polje5_22 = 'bela'
else:
    polje5_22 = 'nepoznata'
print(polje5_22)

r, g, b = cv2.split(img56)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < 80 and g_avg < 40 and b_avg < 115:
    polje5_23 = 'crvena'
elif 95 < r_avg < 140 and 135 < g_avg < 180 and 95 < b_avg < 125:
    polje5_23 = 'žuta'
elif 80 < r_avg < 125 and 105 < g_avg < 140 and b_avg < 20:
    polje5_23 = 'zelena'
elif 150 < r_avg < 215 and g_avg < 75 and b_avg < 15:
    polje5_23 = 'plava'
elif r_avg < 95 and g_avg < 85 and 145 < b_avg < 180:
    polje5_23 = 'narandžasta'
elif 170 < r_avg < 235 and 130 < g_avg < 175 and 105 < b_avg < 145:
    polje5_23 = 'bela'
else:
    polje5_23 = 'nepoznata'
print(polje5_23)

r, g, b = cv2.split(img57)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < 80 and g_avg < 40 and b_avg < 115:
    polje5_31 = 'crvena'
elif 95 < r_avg < 140 and 135 < g_avg < 180 and 95 < b_avg < 125:
    polje5_31 = 'žuta'
elif 80 < r_avg < 125 and 105 < g_avg < 140 and b_avg < 20:
    polje5_31 = 'zelena'
elif 150 < r_avg < 215 and g_avg < 75 and b_avg < 15:
    polje5_31 = 'plava'
elif r_avg < 95 and g_avg < 85 and 145 < b_avg < 180:
    polje5_31 = 'narandžasta'
elif 170 < r_avg < 235 and 130 < g_avg < 175 and 105 < b_avg < 145:
    polje5_31 = 'bela'
else:
    polje5_31 = 'nepoznata'
print(polje5_31)

r, g, b = cv2.split(img58)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < 80 and g_avg < 40 and b_avg < 115:
    polje5_32 = 'crvena'
elif 95 < r_avg < 140 and 135 < g_avg < 180 and 95 < b_avg < 125:
    polje5_32 = 'žuta'
elif 80 < r_avg < 125 and 105 < g_avg < 140 and b_avg < 20:
    polje5_32 = 'zelena'
elif 150 < r_avg < 215 and g_avg < 75 and b_avg < 15:
    polje5_32 = 'plava'
elif r_avg < 95 and g_avg < 85 and 145 < b_avg < 180:
    polje5_32 = 'narandžasta'
elif 170 < r_avg < 235 and 130 < g_avg < 175 and 105 < b_avg < 145:
    polje5_32 = 'bela'
else:
    polje5_32 = 'nepoznata'
print(polje5_32)

r, g, b = cv2.split(img59)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < 80 and g_avg < 40 and b_avg < 115:
    polje5_33 = 'crvena'
elif 95 < r_avg < 140 and 135 < g_avg < 180 and 95 < b_avg < 125:
    polje5_33 = 'žuta'
elif 80 < r_avg < 125 and 105 < g_avg < 140 and b_avg < 20:
    polje5_33 = 'zelena'
elif 150 < r_avg < 215 and g_avg < 75 and b_avg < 15:
    polje5_33 = 'plava'
elif r_avg < 95 and g_avg < 85 and 145 < b_avg < 180:
    polje5_33 = 'narandžasta'
elif 170 < r_avg < 235 and 130 < g_avg < 175 and 105 < b_avg < 145:
    polje5_33 = 'bela'
else:
    polje5_33 = 'nepoznata'
print(polje5_33)

########################################################################
#TOP

if polje0_11 == 'crvena':
    polje0_11 = "🟥"
elif polje0_11 == 'plava':
    polje0_11 = "🟦"
elif polje0_11 == 'žuta':
    polje0_11 = "🟨"
elif polje0_11 == 'zelena':
    polje0_11 = "🟩"
elif polje0_11 == 'bela':
    polje0_11 = "⬜"
elif polje0_11 == 'narandžasta':
    polje0_11 = "🟧"

if polje0_12 == 'crvena':
    polje0_12 = "🟥"
elif polje0_12 == 'plava':
    polje0_12 = "🟦"
elif polje0_12 == 'žuta':
    polje0_12 = "🟨"
elif polje0_12 == 'zelena':
    polje0_12 = "🟩"
elif polje0_12 == 'bela':
    polje0_12 = "⬜"
elif polje0_12 == 'narandžasta':
    polje0_12 = "🟧"

if polje0_13 == 'crvena':
    polje0_13 = "🟥"
elif polje0_13 == 'plava':
    polje0_13 = "🟦"
elif polje0_13 == 'žuta':
    polje0_13 = "🟨"
elif polje0_13 == 'zelena':
    polje0_13 = "🟩"
elif polje0_13 == 'bela':
    polje0_13 = "⬜"
elif polje0_13 == 'narandžasta':
    polje0_13 = "🟧"

if polje0_21 == 'crvena':
    polje0_21 = "🟥"
elif polje0_21 == 'plava':
    polje0_21 = "🟦"
elif polje0_21 == 'žuta':
    polje0_21 = "🟨"
elif polje0_21 == 'zelena':
    polje0_21 = "🟩"
elif polje0_21 == 'bela':
    polje0_21 = "⬜"
elif polje0_21 == 'narandžasta':
    polje0_21 = "🟧"

if polje0_22 == 'crvena':
    polje0_22 = "🟥"
elif polje0_22 == 'plava':
    polje0_22 = "🟦"
elif polje0_22 == 'žuta':
    polje0_22 = "🟨"
elif polje0_22 == 'zelena':
    polje0_22 = "🟩"
elif polje0_22 == 'bela':
    polje0_22 = "⬜"
elif polje0_22 == 'narandžasta':
    polje0_22 = "🟧"

if polje0_23 == 'crvena':
    polje0_23 = "🟥"
elif polje0_23 == 'plava':
    polje0_23 = "🟦"
elif polje0_23 == 'žuta':
    polje0_23 = "🟨"
elif polje0_23 == 'zelena':
    polje0_23 = "🟩"
elif polje0_23 == 'bela':
    polje0_23 = "⬜"
elif polje0_23 == 'narandžasta':
    polje0_23 = "🟧"

if polje0_31 == 'crvena':
    polje0_31 = "🟥"
elif polje0_31 == 'plava':
    polje0_31 = "🟦"
elif polje0_31 == 'žuta':
    polje0_31 = "🟨"
elif polje0_31 == 'zelena':
    polje0_31 = "🟩"
elif polje0_31 == 'bela':
    polje0_31 = "⬜"
elif polje0_31 == 'narandžasta':
    polje0_31 = "🟧"

if polje0_32 == 'crvena':
    polje0_32 = "🟥"
elif polje0_32 == 'plava':
    polje0_32 = "🟦"
elif polje0_32 == 'žuta':
    polje0_32 = "🟨"
elif polje0_32 == 'zelena':
    polje0_32 = "🟩"
elif polje0_32 == 'bela':
    polje0_32 = "⬜"
elif polje0_32 == 'narandžasta':
    polje0_32 = "🟧"

if polje0_33 == 'crvena':
    polje0_33 = "🟥"
elif polje0_33 == 'plava':
    polje0_33 = "🟦"
elif polje0_33 == 'žuta':
    polje0_33 = "🟨"
elif polje0_33 == 'zelena':
    polje0_33 = "🟩"
elif polje0_33 == 'bela':
    polje0_33 = "⬜"
elif polje0_33 == 'narandžasta':
    polje0_33 = "🟧"


kocka2.face["Top"][0][0] = polje0_11
kocka2.face["Top"][0][1] = polje0_12
kocka2.face["Top"][0][2] = polje0_13
kocka2.face["Top"][1][0] = polje0_21
kocka2.face["Top"][1][1] = polje0_22
kocka2.face["Top"][1][2] = polje0_23
kocka2.face["Top"][2][0] = polje0_31
kocka2.face["Top"][2][1] = polje0_32
kocka2.face["Top"][2][2] = polje0_33

#########################################################
#FRONT

if polje1_11 == 'crvena':
    polje1_11 = "🟥"
elif polje1_11 == 'plava':
    polje1_11 = "🟦"
elif polje1_11 == 'žuta':
    polje1_11 = "🟨"
elif polje1_11 == 'zelena':
    polje1_11 = "🟩"
elif polje1_11 == 'bela':
    polje1_11 = "⬜"
elif polje1_11 == 'narandžasta':
    polje1_11 = "🟧"

if polje1_12 == 'crvena':
    polje1_12 = "🟥"
elif polje1_12 == 'plava':
    polje1_12 = "🟦"
elif polje1_12 == 'žuta':
    polje1_12 = "🟨"
elif polje1_12 == 'zelena':
    polje1_12 = "🟩"
elif polje1_12 == 'bela':
    polje1_12 = "⬜"
elif polje1_12 == 'narandžasta':
    polje1_12 = "🟧"

if polje1_13 == 'crvena':
    polje1_13 = "🟥"
elif polje1_13 == 'plava':
    polje1_13 = "🟦"
elif polje1_13 == 'žuta':
    polje1_13 = "🟨"
elif polje1_13 == 'zelena':
    polje1_13 = "🟩"
elif polje1_13 == 'bela':
    polje1_13 = "⬜"
elif polje1_13 == 'narandžasta':
    polje1_13 = "🟧"

if polje1_21 == 'crvena':
    polje1_21 = "🟥"
elif polje1_21 == 'plava':
    polje1_21 = "🟦"
elif polje1_21 == 'žuta':
    polje1_21 = "🟨"
elif polje1_21 == 'zelena':
    polje1_21 = "🟩"
elif polje1_21 == 'bela':
    polje1_21 = "⬜"
elif polje1_21 == 'narandžasta':
    polje1_21 = "🟧"

if polje1_22 == 'crvena':
    polje1_22 = "🟥"
elif polje1_22 == 'plava':
    polje1_22 = "🟦"
elif polje1_22 == 'žuta':
    polje1_22 = "🟨"
elif polje1_22 == 'zelena':
    polje1_22 = "🟩"
elif polje1_22 == 'bela':
    polje1_22 = "⬜"
elif polje1_22 == 'narandžasta':
    polje1_22 = "🟧"

if polje1_23 == 'crvena':
    polje1_23 = "🟥"
elif polje1_23 == 'plava':
    polje1_23 = "🟦"
elif polje1_23 == 'žuta':
    polje1_23 = "🟨"
elif polje1_23 == 'zelena':
    polje1_23 = "🟩"
elif polje1_23 == 'bela':
    polje1_23 = "⬜"
elif polje1_23 == 'narandžasta':
    polje1_23 = "🟧"

if polje1_31 == 'crvena':
    polje1_31 = "🟥"
elif polje1_31 == 'plava':
    polje1_31 = "🟦"
elif polje1_31 == 'žuta':
    polje1_31 = "🟨"
elif polje1_31 == 'zelena':
    polje1_31 = "🟩"
elif polje1_31 == 'bela':
    polje1_31 = "⬜"
elif polje1_31 == 'narandžasta':
    polje1_31 = "🟧"

if polje1_32 == 'crvena':
    polje1_32 = "🟥"
elif polje1_32 == 'plava':
    polje1_32 = "🟦"
elif polje1_32 == 'žuta':
    polje1_32 = "🟨"
elif polje1_32 == 'zelena':
    polje1_32 = "🟩"
elif polje1_32 == 'bela':
    polje1_32 = "⬜"
elif polje1_32 == 'narandžasta':
    polje1_32 = "🟧"

if polje1_33 == 'crvena':
    polje1_33 = "🟥"
elif polje1_33 == 'plava':
    polje1_33 = "🟦"
elif polje1_33 == 'žuta':
    polje1_33 = "🟨"
elif polje1_33 == 'zelena':
    polje1_33 = "🟩"
elif polje1_33 == 'bela':
    polje1_33 = "⬜"
elif polje1_33 == 'narandžasta':
    polje1_33 = "🟧"


kocka2.face["Front"][0][0] = polje1_11
kocka2.face["Front"][0][1] = polje1_12
kocka2.face["Front"][0][2] = polje1_13
kocka2.face["Front"][1][0] = polje1_21
kocka2.face["Front"][1][1] = polje1_22
kocka2.face["Front"][1][2] = polje1_23
kocka2.face["Front"][2][0] = polje1_31
kocka2.face["Front"][2][1] = polje1_32
kocka2.face["Front"][2][2] = polje1_33

##################################################
#BOTTOM

if polje2_11 == 'crvena':
    polje2_11 = "🟥"
elif polje2_11 == 'plava':
    polje2_11 = "🟦"
elif polje2_11 == 'žuta':
    polje2_11 = "🟨"
elif polje2_11 == 'zelena':
    polje2_11 = "🟩"
elif polje2_11 == 'bela':
    polje2_11 = "⬜"
elif polje2_11 == 'narandžasta':
    polje2_11 = "🟧"

if polje2_12 == 'crvena':
    polje2_12 = "🟥"
elif polje2_12 == 'plava':
    polje2_12 = "🟦"
elif polje2_12 == 'žuta':
    polje2_12 = "🟨"
elif polje2_12 == 'zelena':
    polje2_12 = "🟩"
elif polje2_12 == 'bela':
    polje2_12 = "⬜"
elif polje2_12 == 'narandžasta':
    polje2_12 = "🟧"

if polje2_13 == 'crvena':
    polje2_13 = "🟥"
elif polje2_13 == 'plava':
    polje2_13 = "🟦"
elif polje2_13 == 'žuta':
    polje2_13 = "🟨"
elif polje2_13 == 'zelena':
    polje2_13 = "🟩"
elif polje2_13 == 'bela':
    polje2_13 = "⬜"
elif polje2_13 == 'narandžasta':
    polje2_13 = "🟧"

if polje2_21 == 'crvena':
    polje2_21 = "🟥"
elif polje2_21 == 'plava':
    polje2_21 = "🟦"
elif polje2_21 == 'žuta':
    polje2_21 = "🟨"
elif polje2_21 == 'zelena':
    polje2_21 = "🟩"
elif polje2_21 == 'bela':
    polje2_21 = "⬜"
elif polje2_21 == 'narandžasta':
    polje2_21 = "🟧"

if polje2_22 == 'crvena':
    polje2_22 = "🟥"
elif polje2_22 == 'plava':
    polje2_22 = "🟦"
elif polje2_22 == 'žuta':
    polje2_22 = "🟨"
elif polje2_22 == 'zelena':
    polje2_22 = "🟩"
elif polje2_22 == 'bela':
    polje2_22 = "⬜"
elif polje2_22 == 'narandžasta':
    polje2_22 = "🟧"

if polje2_23 == 'crvena':
    polje2_23 = "🟥"
elif polje2_23 == 'plava':
    polje2_23 = "🟦"
elif polje2_23 == 'žuta':
    polje2_23 = "🟨"
elif polje2_23 == 'zelena':
    polje2_23 = "🟩"
elif polje2_23 == 'bela':
    polje2_23 = "⬜"
elif polje2_23 == 'narandžasta':
    polje2_23 = "🟧"

if polje2_31 == 'crvena':
    polje2_31 = "🟥"
elif polje2_31 == 'plava':
    polje2_31 = "🟦"
elif polje2_31 == 'žuta':
    polje2_31 = "🟨"
elif polje2_31 == 'zelena':
    polje2_31 = "🟩"
elif polje2_31 == 'bela':
    polje2_31 = "⬜"
elif polje2_31 == 'narandžasta':
    polje2_31 = "🟧"

if polje2_32 == 'crvena':
    polje2_32 = "🟥"
elif polje2_32 == 'plava':
    polje2_32 = "🟦"
elif polje2_32 == 'žuta':
    polje2_32 = "🟨"
elif polje2_32 == 'zelena':
    polje2_32 = "🟩"
elif polje2_32 == 'bela':
    polje2_32 = "⬜"
elif polje2_32 == 'narandžasta':
    polje2_32 = "🟧"

if polje2_33 == 'crvena':
    polje2_33 = "🟥"
elif polje2_33 == 'plava':
    polje2_33 = "🟦"
elif polje2_33 == 'žuta':
    polje2_33 = "🟨"
elif polje2_33 == 'zelena':
    polje2_33 = "🟩"
elif polje2_33 == 'bela':
    polje2_33 = "⬜"
elif polje2_33 == 'narandžasta':
    polje2_33 = "🟧"


kocka2.face["Bottom"][0][0] = polje2_11
kocka2.face["Bottom"][0][1] = polje2_12
kocka2.face["Bottom"][0][2] = polje2_13
kocka2.face["Bottom"][1][0] = polje2_21
kocka2.face["Bottom"][1][1] = polje2_22
kocka2.face["Bottom"][1][2] = polje2_23
kocka2.face["Bottom"][2][0] = polje2_31
kocka2.face["Bottom"][2][1] = polje2_32
kocka2.face["Bottom"][2][2] = polje2_33

###########################################################
#LEFT

if polje3_11 == 'crvena':
    polje3_11 = "🟥"
elif polje3_11 == 'plava':
    polje3_11 = "🟦"
elif polje3_11 == 'žuta':
    polje3_11 = "🟨"
elif polje3_11 == 'zelena':
    polje3_11 = "🟩"
elif polje3_11 == 'bela':
    polje3_11 = "⬜"
elif polje3_11 == 'narandžasta':
    polje3_11 = "🟧"

if polje3_12 == 'crvena':
    polje3_12 = "🟥"
elif polje3_12 == 'plava':
    polje3_12 = "🟦"
elif polje3_12 == 'žuta':
    polje3_12 = "🟨"
elif polje3_12 == 'zelena':
    polje3_12 = "🟩"
elif polje3_12 == 'bela':
    polje3_12 = "⬜"
elif polje3_12 == 'narandžasta':
    polje3_12 = "🟧"

if polje3_13 == 'crvena':
    polje3_13 = "🟥"
elif polje3_13 == 'plava':
    polje3_13 = "🟦"
elif polje3_13 == 'žuta':
    polje3_13 = "🟨"
elif polje3_13 == 'zelena':
    polje3_13 = "🟩"
elif polje3_13 == 'bela':
    polje3_13 = "⬜"
elif polje3_13 == 'narandžasta':
    polje3_13 = "🟧"

if polje3_21 == 'crvena':
    polje3_21 = "🟥"
elif polje3_21 == 'plava':
    polje3_21 = "🟦"
elif polje3_21 == 'žuta':
    polje3_21 = "🟨"
elif polje3_21 == 'zelena':
    polje3_21 = "🟩"
elif polje3_21 == 'bela':
    polje3_21 = "⬜"
elif polje3_21 == 'narandžasta':
    polje3_21 = "🟧"

if polje3_22 == 'crvena':
    polje3_22 = "🟥"
elif polje3_22 == 'plava':
    polje3_22 = "🟦"
elif polje3_22 == 'žuta':
    polje3_22 = "🟨"
elif polje3_22 == 'zelena':
    polje3_22 = "🟩"
elif polje3_22 == 'bela':
    polje3_22 = "⬜"
elif polje3_22 == 'narandžasta':
    polje3_22 = "🟧"

if polje3_23 == 'crvena':
    polje3_23 = "🟥"
elif polje3_23 == 'plava':
    polje3_23 = "🟦"
elif polje3_23 == 'žuta':
    polje3_23 = "🟨"
elif polje3_23 == 'zelena':
    polje3_23 = "🟩"
elif polje3_23 == 'bela':
    polje3_23 = "⬜"
elif polje3_23 == 'narandžasta':
    polje3_23 = "🟧"

if polje3_31 == 'crvena':
    polje3_31 = "🟥"
elif polje3_31 == 'plava':
    polje3_31 = "🟦"
elif polje3_31 == 'žuta':
    polje3_31 = "🟨"
elif polje3_31 == 'zelena':
    polje3_31 = "🟩"
elif polje3_31 == 'bela':
    polje3_31 = "⬜"
elif polje3_31 == 'narandžasta':
    polje3_31 = "🟧"

if polje3_32 == 'crvena':
    polje3_32 = "🟥"
elif polje3_32 == 'plava':
    polje3_32 = "🟦"
elif polje3_32 == 'žuta':
    polje3_32 = "🟨"
elif polje3_32 == 'zelena':
    polje3_32 = "🟩"
elif polje3_32 == 'bela':
    polje3_32 = "⬜"
elif polje3_32 == 'narandžasta':
    polje3_32 = "🟧"

if polje3_33 == 'crvena':
    polje3_33 = "🟥"
elif polje3_33 == 'plava':
    polje3_33 = "🟦"
elif polje3_33 == 'žuta':
    polje3_33 = "🟨"
elif polje3_33 == 'zelena':
    polje3_33 = "🟩"
elif polje3_33 == 'bela':
    polje3_33 = "⬜"
elif polje3_33 == 'narandžasta':
    polje3_33 = "🟧"


kocka2.face["Left"][0][0] = polje3_11
kocka2.face["Left"][0][1] = polje3_12
kocka2.face["Left"][0][2] = polje3_13
kocka2.face["Left"][1][0] = polje3_21
kocka2.face["Left"][1][1] = polje3_22
kocka2.face["Left"][1][2] = polje3_23
kocka2.face["Left"][2][0] = polje3_31
kocka2.face["Left"][2][1] = polje3_32
kocka2.face["Left"][2][2] = polje3_33

#####################################################################
#BACK

if polje4_11 == 'crvena':
    polje4_11 = "🟥"
elif polje4_11 == 'plava':
    polje4_11 = "🟦"
elif polje4_11 == 'žuta':
    polje4_11 = "🟨"
elif polje4_11 == 'zelena':
    polje4_11 = "🟩"
elif polje4_11 == 'bela':
    polje4_11 = "⬜"
elif polje4_11 == 'narandžasta':
    polje4_11 = "🟧"

if polje4_12 == 'crvena':
    polje4_12 = "🟥"
elif polje4_12 == 'plava':
    polje4_12 = "🟦"
elif polje4_12 == 'žuta':
    polje4_12 = "🟨"
elif polje4_12 == 'zelena':
    polje4_12 = "🟩"
elif polje4_12 == 'bela':
    polje4_12 = "⬜"
elif polje4_12 == 'narandžasta':
    polje4_12 = "🟧"

if polje4_13 == 'crvena':
    polje4_13 = "🟥"
elif polje4_13 == 'plava':
    polje4_13 = "🟦"
elif polje4_13 == 'žuta':
    polje4_13 = "🟨"
elif polje4_13 == 'zelena':
    polje4_13 = "🟩"
elif polje4_13 == 'bela':
    polje4_13 = "⬜"
elif polje4_13 == 'narandžasta':
    polje4_13 = "🟧"

if polje4_21 == 'crvena':
    polje4_21 = "🟥"
elif polje4_21 == 'plava':
    polje4_21 = "🟦"
elif polje4_21 == 'žuta':
    polje4_21 = "🟨"
elif polje4_21 == 'zelena':
    polje4_21 = "🟩"
elif polje4_21 == 'bela':
    polje4_21 = "⬜"
elif polje4_21 == 'narandžasta':
    polje4_21 = "🟧"

if polje4_22 == 'crvena':
    polje4_22 = "🟥"
elif polje4_22 == 'plava':
    polje4_22 = "🟦"
elif polje4_22 == 'žuta':
    polje4_22 = "🟨"
elif polje4_22 == 'zelena':
    polje4_22 = "🟩"
elif polje4_22 == 'bela':
    polje4_22 = "⬜"
elif polje4_22 == 'narandžasta':
    polje4_22 = "🟧"

if polje4_23 == 'crvena':
    polje4_23 = "🟥"
elif polje4_23 == 'plava':
    polje4_23 = "🟦"
elif polje4_23 == 'žuta':
    polje4_23 = "🟨"
elif polje4_23 == 'zelena':
    polje4_23 = "🟩"
elif polje4_23 == 'bela':
    polje4_23 = "⬜"
elif polje4_23 == 'narandžasta':
    polje4_23 = "🟧"

if polje4_31 == 'crvena':
    polje4_31 = "🟥"
elif polje4_31 == 'plava':
    polje4_31 = "🟦"
elif polje4_31 == 'žuta':
    polje4_31 = "🟨"
elif polje4_31 == 'zelena':
    polje4_31 = "🟩"
elif polje4_31 == 'bela':
    polje4_31 = "⬜"
elif polje4_31 == 'narandžasta':
    polje4_31 = "🟧"

if polje4_32 == 'crvena':
    polje4_32 = "🟥"
elif polje4_32 == 'plava':
    polje4_32 = "🟦"
elif polje4_32 == 'žuta':
    polje4_32 = "🟨"
elif polje4_32 == 'zelena':
    polje4_32 = "🟩"
elif polje4_32 == 'bela':
    polje4_32 = "⬜"
elif polje4_32 == 'narandžasta':
    polje4_32 = "🟧"

if polje4_33 == 'crvena':
    polje4_33 = "🟥"
elif polje4_33 == 'plava':
    polje4_33 = "🟦"
elif polje4_33 == 'žuta':
    polje4_33 = "🟨"
elif polje4_33 == 'zelena':
    polje4_33 = "🟩"
elif polje4_33 == 'bela':
    polje4_33 = "⬜"
elif polje4_33 == 'narandžasta':
    polje4_33 = "🟧"


kocka2.face["Back"][0][0] = polje4_11
kocka2.face["Back"][0][1] = polje4_12
kocka2.face["Back"][0][2] = polje4_13
kocka2.face["Back"][1][0] = polje4_21
kocka2.face["Back"][1][1] = polje4_22
kocka2.face["Back"][1][2] = polje4_23
kocka2.face["Back"][2][0] = polje4_31
kocka2.face["Back"][2][1] = polje4_32
kocka2.face["Back"][2][2] = polje4_33

################################################################
#RIGHT

if polje5_11 == 'crvena':
    polje5_11 = "🟥"
elif polje5_11 == 'plava':
    polje5_11 = "🟦"
elif polje5_11 == 'žuta':
    polje5_11 = "🟨"
elif polje5_11 == 'zelena':
    polje5_11 = "🟩"
elif polje5_11 == 'bela':
    polje5_11 = "⬜"
elif polje5_11 == 'narandžasta':
    polje5_11 = "🟧"

if polje5_12 == 'crvena':
    polje5_12 = "🟥"
elif polje5_12 == 'plava':
    polje5_12 = "🟦"
elif polje5_12 == 'žuta':
    polje5_12 = "🟨"
elif polje5_12 == 'zelena':
    polje5_12 = "🟩"
elif polje5_12 == 'bela':
    polje5_12 = "⬜"
elif polje5_12 == 'narandžasta':
    polje5_12 = "🟧"

if polje5_13 == 'crvena':
    polje5_13 = "🟥"
elif polje5_13 == 'plava':
    polje5_13 = "🟦"
elif polje5_13 == 'žuta':
    polje5_13 = "🟨"
elif polje5_13 == 'zelena':
    polje5_13 = "🟩"
elif polje5_13 == 'bela':
    polje5_13 = "⬜"
elif polje5_13 == 'narandžasta':
    polje5_13 = "🟧"

if polje5_21 == 'crvena':
    polje5_21 = "🟥"
elif polje5_21 == 'plava':
    polje5_21 = "🟦"
elif polje5_21 == 'žuta':
    polje5_21 = "🟨"
elif polje5_21 == 'zelena':
    polje5_21 = "🟩"
elif polje5_21 == 'bela':
    polje5_21 = "⬜"
elif polje5_21 == 'narandžasta':
    polje5_21 = "🟧"

if polje5_22 == 'crvena':
    polje5_22 = "🟥"
elif polje5_22 == 'plava':
    polje5_22 = "🟦"
elif polje5_22 == 'žuta':
    polje5_22 = "🟨"
elif polje5_22 == 'zelena':
    polje5_22 = "🟩"
elif polje5_22 == 'bela':
    polje5_22 = "⬜"
elif polje5_22 == 'narandžasta':
    polje5_22 = "🟧"

if polje5_23 == 'crvena':
    polje5_23 = "🟥"
elif polje5_23 == 'plava':
    polje5_23 = "🟦"
elif polje5_23 == 'žuta':
    polje5_23 = "🟨"
elif polje5_23 == 'zelena':
    polje5_23 = "🟩"
elif polje5_23 == 'bela':
    polje5_23 = "⬜"
elif polje5_23 == 'narandžasta':
    polje5_23 = "🟧"

if polje5_31 == 'crvena':
    polje5_31 = "🟥"
elif polje5_31 == 'plava':
    polje5_31 = "🟦"
elif polje5_31 == 'žuta':
    polje5_31 = "🟨"
elif polje5_31 == 'zelena':
    polje5_31 = "🟩"
elif polje5_31 == 'bela':
    polje5_31 = "⬜"
elif polje5_31 == 'narandžasta':
    polje5_31 = "🟧"

if polje5_32 == 'crvena':
    polje5_32 = "🟥"
elif polje5_32 == 'plava':
    polje5_32 = "🟦"
elif polje5_32 == 'žuta':
    polje5_32 = "🟨"
elif polje5_32 == 'zelena':
    polje5_32 = "🟩"
elif polje5_32 == 'bela':
    polje5_32 = "⬜"
elif polje5_32 == 'narandžasta':
    polje5_32 = "🟧"

if polje5_33 == 'crvena':
    polje5_33 = "🟥"
elif polje5_33 == 'plava':
    polje5_33 = "🟦"
elif polje5_33 == 'žuta':
    polje5_33 = "🟨"
elif polje5_33 == 'zelena':
    polje5_33 = "🟩"
elif polje5_33 == 'bela':
    polje5_33 = "⬜"
elif polje5_33 == 'narandžasta':
    polje5_33 = "🟧"


kocka2.face["Right"][0][0] = polje5_11
kocka2.face["Right"][0][1] = polje5_12
kocka2.face["Right"][0][2] = polje5_13
kocka2.face["Right"][1][0] = polje5_21
kocka2.face["Right"][1][1] = polje5_22
kocka2.face["Right"][1][2] = polje5_23
kocka2.face["Right"][2][0] = polje5_31
kocka2.face["Right"][2][1] = polje5_32
kocka2.face["Right"][2][2] = polje5_33

kocka2.draw_cube()


# Release the capture and writer objects
cam.release()
out.release()
cv2.destroyAllWindows()


