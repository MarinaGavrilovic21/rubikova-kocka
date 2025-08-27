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

r_red_max = 80
g_red_max = 40
b_red_max = 115

r_yellow_max = 140
r_yellow_min = 95
g_yellow_max = 180
g_yellow_min = 135
b_yellow_max = 125
b_yellow_min = 95

r_green_max = 125
r_green_min = 80
g_green_max = 140
g_green_min = 105
b_green_max = 20

r_blue_max = 215
r_blue_min = 150
g_blue_max = 80
b_blue_max = 15

r_orange_max = 95
g_orange_max = 85
b_orange_max = 180
b_orange_min = 145

r_white_max = 235
r_white_min = 170
g_white_max = 175
g_white_min = 130
b_white_max = 145
b_white_min = 105

print('TOP')

r, g, b = cv2.split(img1)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < r_red_max and g_avg < g_red_max and b_avg < b_red_max:
    kocka2.face["Top"][0][0] = '🟥'
elif r_yellow_min < r_avg < r_yellow_max and g_yellow_min < g_avg < g_yellow_max and b_yellow_min < b_avg < b_yellow_max:
    kocka2.face["Top"][0][0] = '🟨'
elif r_green_min < r_avg < r_green_max and g_green_min < g_avg < g_green_max and b_avg < b_green_max:
    kocka2.face["Top"][0][0] = '🟩'
elif r_blue_min < r_avg < r_blue_max and g_avg < g_blue_max and b_avg < b_blue_max:
    kocka2.face["Top"][0][0] = '🟦'
elif r_avg < r_orange_max and g_avg < g_orange_max and b_orange_min < b_avg < b_orange_max:
    kocka2.face["Top"][0][0] = '🟧'
elif r_white_min < r_avg < r_white_max and g_white_min < g_avg < g_white_max and b_white_min < b_avg < b_white_max:
    kocka2.face["Top"][0][0] = '⬜'
else:
    kocka2.face["Top"][0][0] = 'nepoznata'
print(kocka2.face["Top"][0][0])

r, g, b = cv2.split(img2)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < r_red_max and g_avg < g_red_max and b_avg < b_red_max:
    kocka2.face["Top"][0][1] = '🟥'
elif r_yellow_min < r_avg < r_yellow_max and g_yellow_min < g_avg < g_yellow_max and b_yellow_min < b_avg < b_yellow_max:
    kocka2.face["Top"][0][1] = '🟨'
elif r_green_min < r_avg < r_green_max and g_green_min < g_avg < g_green_max and b_avg < b_green_max:
    kocka2.face["Top"][0][1] = '🟩'
elif r_blue_min < r_avg < r_blue_max and g_avg < g_blue_max and b_avg < b_blue_max:
    kocka2.face["Top"][0][1] = '🟦'
elif r_avg < r_orange_max and g_avg < g_orange_max and b_orange_min < b_avg < b_orange_max:
    kocka2.face["Top"][0][1] = '🟧'
elif r_white_min < r_avg < r_white_max and g_white_min < g_avg < g_white_max and b_white_min < b_avg < b_white_max:
    kocka2.face["Top"][0][1] = '⬜'
else:
    kocka2.face["Top"][0][1] = 'nepoznata'
print(kocka2.face["Top"][0][1])

r, g, b = cv2.split(img3)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < r_red_max and g_avg < g_red_max and b_avg < b_red_max:
    kocka2.face["Top"][0][2] = '🟥'
elif r_yellow_min < r_avg < r_yellow_max and g_yellow_min < g_avg < g_yellow_max and b_yellow_min < b_avg < b_yellow_max:
    kocka2.face["Top"][0][2] = '🟨'
elif r_green_min < r_avg < r_green_max and g_green_min < g_avg < g_green_max and b_avg < b_green_max:
    kocka2.face["Top"][0][2] = '🟩'
elif r_blue_min < r_avg < r_blue_max and g_avg < g_blue_max and b_avg < b_blue_max:
    kocka2.face["Top"][0][2] = '🟦'
elif r_avg < r_orange_max and g_avg < g_orange_max and b_orange_min < b_avg < b_orange_max:
    kocka2.face["Top"][0][2] = '🟧'
elif r_white_min < r_avg < r_white_max and g_white_min < g_avg < g_white_max and b_white_min < b_avg < b_white_max:
    kocka2.face["Top"][0][2] = '⬜'
else:
    kocka2.face["Top"][0][2] = 'nepoznata'
print(kocka2.face["Top"][0][2])

r, g, b = cv2.split(img4)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < r_red_max and g_avg < g_red_max and b_avg < b_red_max:
    kocka2.face["Top"][1][0] = '🟥'
elif r_yellow_min < r_avg < r_yellow_max and g_yellow_min < g_avg < g_yellow_max and b_yellow_min < b_avg < b_yellow_max:
    kocka2.face["Top"][1][0] = '🟨'
elif r_green_min < r_avg < r_green_max and g_green_min < g_avg < g_green_max and b_avg < b_green_max:
    kocka2.face["Top"][1][0] = '🟩'
elif r_blue_min < r_avg < r_blue_max and g_avg < g_blue_max and b_avg < b_blue_max:
    kocka2.face["Top"][1][0] = '🟦'
elif r_avg < r_orange_max and g_avg < g_orange_max and b_orange_min < b_avg < b_orange_max:
    kocka2.face["Top"][1][0] = '🟧'
elif r_white_min < r_avg < r_white_max and g_white_min < g_avg < g_white_max and b_white_min < b_avg < b_white_max:
    kocka2.face["Top"][1][0] = '⬜'
else:
    kocka2.face["Top"][1][0] = 'nepoznata'
print(kocka2.face["Top"][1][0])

r, g, b = cv2.split(img5)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < r_red_max and g_avg < g_red_max and b_avg < b_red_max:
    kocka2.face["Top"][1][1] = '🟥'
elif r_yellow_min < r_avg < r_yellow_max and g_yellow_min < g_avg < g_yellow_max and b_yellow_min < b_avg < b_yellow_max:
    kocka2.face["Top"][1][1] = '🟨'
elif r_green_min < r_avg < r_green_max and g_green_min < g_avg < g_green_max and b_avg < b_green_max:
    kocka2.face["Top"][1][1] = '🟩'
elif r_blue_min < r_avg < r_blue_max and g_avg < g_blue_max and b_avg < b_blue_max:
    kocka2.face["Top"][1][1] = '🟦'
elif r_avg < r_orange_max and g_avg < g_orange_max and b_orange_min < b_avg < b_orange_max:
    kocka2.face["Top"][1][1] = '🟧'
elif r_white_min < r_avg < r_white_max and g_white_min < g_avg < g_white_max and b_white_min < b_avg < b_white_max:
    kocka2.face["Top"][1][1] = '⬜'
else:
    kocka2.face["Top"][1][1] = 'nepoznata'
print(kocka2.face["Top"][1][1])

r, g, b = cv2.split(img6)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < r_red_max and g_avg < g_red_max and b_avg < b_red_max:
    kocka2.face["Top"][1][2] = '🟥'
elif r_yellow_min < r_avg < r_yellow_max and g_yellow_min < g_avg < g_yellow_max and b_yellow_min < b_avg < b_yellow_max:
    kocka2.face["Top"][1][2] = '🟨'
elif r_green_min < r_avg < r_green_max and g_green_min < g_avg < g_green_max and b_avg < b_green_max:
    kocka2.face["Top"][1][2] = '🟩'
elif r_blue_min < r_avg < r_blue_max and g_avg < g_blue_max and b_avg < b_blue_max:
    kocka2.face["Top"][1][2] = '🟦'
elif r_avg < r_orange_max and g_avg < g_orange_max and b_orange_min < b_avg < b_orange_max:
    kocka2.face["Top"][1][2] = '🟧'
elif r_white_min < r_avg < r_white_max and g_white_min < g_avg < g_white_max and b_white_min < b_avg < b_white_max:
    kocka2.face["Top"][1][2] = '⬜'
else:
    kocka2.face["Top"][1][2] = 'nepoznata'
print(kocka2.face["Top"][1][2])

r, g, b = cv2.split(img7)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < r_red_max and g_avg < g_red_max and b_avg < b_red_max:
    kocka2.face["Top"][2][0] = '🟥'
elif r_yellow_min < r_avg < r_yellow_max and g_yellow_min < g_avg < g_yellow_max and b_yellow_min < b_avg < b_yellow_max:
    kocka2.face["Top"][2][0] = '🟨'
elif r_green_min < r_avg < r_green_max and g_green_min < g_avg < g_green_max and b_avg < b_green_max:
    kocka2.face["Top"][2][0] = '🟩'
elif r_blue_min < r_avg < r_blue_max and g_avg < g_blue_max and b_avg < b_blue_max:
    kocka2.face["Top"][2][0] = '🟦'
elif r_avg < r_orange_max and g_avg < g_orange_max and b_orange_min < b_avg < b_orange_max:
    kocka2.face["Top"][2][0] = '🟧'
elif r_white_min < r_avg < r_white_max and g_white_min < g_avg < g_white_max and b_white_min < b_avg < b_white_max:
    kocka2.face["Top"][2][0] = '⬜'
else:
    kocka2.face["Top"][2][0] = 'nepoznata'
print(kocka2.face["Top"][2][0])

r, g, b = cv2.split(img8)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < r_red_max and g_avg < g_red_max and b_avg < b_red_max:
    kocka2.face["Top"][2][1] = '🟥'
elif r_yellow_min < r_avg < r_yellow_max and g_yellow_min < g_avg < g_yellow_max and b_yellow_min < b_avg < b_yellow_max:
    kocka2.face["Top"][2][1] = '🟨'
elif r_green_min < r_avg < r_green_max and g_green_min < g_avg < g_green_max and b_avg < b_green_max:
    kocka2.face["Top"][2][1] = '🟩'
elif r_blue_min < r_avg < r_blue_max and g_avg < g_blue_max and b_avg < b_blue_max:
    kocka2.face["Top"][2][1] = '🟦'
elif r_avg < r_orange_max and g_avg < g_orange_max and b_orange_min < b_avg < b_orange_max:
    kocka2.face["Top"][2][1] = '🟧'
elif r_white_min < r_avg < r_white_max and g_white_min < g_avg < g_white_max and b_white_min < b_avg < b_white_max:
    kocka2.face["Top"][2][1] = '⬜'
else:
    kocka2.face["Top"][2][1] = 'nepoznata'
print(kocka2.face["Top"][2][1])

r, g, b = cv2.split(img9)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < r_red_max and g_avg < g_red_max and b_avg < b_red_max:
    kocka2.face["Top"][2][2] = '🟥'
elif r_yellow_min < r_avg < r_yellow_max and g_yellow_min < g_avg < g_yellow_max and b_yellow_min < b_avg < b_yellow_max:
    kocka2.face["Top"][2][2] = '🟨'
elif r_green_min < r_avg < r_green_max and g_green_min < g_avg < g_green_max and b_avg < b_green_max:
    kocka2.face["Top"][2][2] = '🟩'
elif r_blue_min < r_avg < r_blue_max and g_avg < g_blue_max and b_avg < b_blue_max:
    kocka2.face["Top"][2][2] = '🟦'
elif r_avg < r_orange_max and g_avg < g_orange_max and b_orange_min < b_avg < b_orange_max:
    kocka2.face["Top"][2][2] = '🟧'
elif r_white_min < r_avg < r_white_max and g_white_min < g_avg < g_white_max and b_white_min < b_avg < b_white_max:
    kocka2.face["Top"][2][2] = '⬜'
else:
    kocka2.face["Top"][2][2] = 'nepoznata'
print(kocka2.face["Top"][2][2])

####################################################################

print('FRONT')

r, g, b = cv2.split(img11)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < r_red_max and g_avg < g_red_max and b_avg < b_red_max:
    kocka2.face["Front"][0][0] = '🟥'
elif r_yellow_min < r_avg < r_yellow_max and g_yellow_min < g_avg < g_yellow_max and b_yellow_min < b_avg < b_yellow_max:
    kocka2.face["Front"][0][0] = '🟨'
elif r_green_min < r_avg < r_green_max and g_green_min < g_avg < g_green_max and b_avg < b_green_max:
    kocka2.face["Front"][0][0] = '🟩'
elif r_blue_min < r_avg < r_blue_max and g_avg < g_blue_max and b_avg < b_blue_max:
    kocka2.face["Front"][0][0] = '🟦'
elif r_avg < r_orange_max and g_avg < g_orange_max and b_orange_min < b_avg < b_orange_max:
    kocka2.face["Front"][0][0] = '🟧'
elif r_white_min < r_avg < r_white_max and g_white_min < g_avg < g_white_max and b_white_min < b_avg < b_white_max:
    kocka2.face["Front"][0][0] = '⬜'
else:
    kocka2.face["Front"][0][0] = 'nepoznata'
print(kocka2.face["Front"][0][0])

r, g, b = cv2.split(img12)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < r_red_max and g_avg < g_red_max and b_avg < b_red_max:
    kocka2.face["Front"][0][1] = '🟥'
elif r_yellow_min < r_avg < r_yellow_max and g_yellow_min < g_avg < g_yellow_max and b_yellow_min < b_avg < b_yellow_max:
    kocka2.face["Front"][0][1] = '🟨'
elif r_green_min < r_avg < r_green_max and g_green_min < g_avg < g_green_max and b_avg < b_green_max:
    kocka2.face["Front"][0][1] = '🟩'
elif r_blue_min < r_avg < r_blue_max and g_avg < g_blue_max and b_avg < b_blue_max:
    kocka2.face["Front"][0][1] = '🟦'
elif r_avg < r_orange_max and g_avg < g_orange_max and b_orange_min < b_avg < b_orange_max:
    kocka2.face["Front"][0][1] = '🟧'
elif r_white_min < r_avg < r_white_max and g_white_min < g_avg < g_white_max and b_white_min < b_avg < b_white_max:
    kocka2.face["Front"][0][1] = '⬜'
else:
    kocka2.face["Front"][0][1] = 'nepoznata'
print(kocka2.face["Front"][0][1])

r, g, b = cv2.split(img13)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < r_red_max and g_avg < g_red_max and b_avg < b_red_max:
    kocka2.face["Front"][0][2] = '🟥'
elif r_yellow_min < r_avg < r_yellow_max and g_yellow_min < g_avg < g_yellow_max and b_yellow_min < b_avg < b_yellow_max:
    kocka2.face["Front"][0][2] = '🟨'
elif r_green_min < r_avg < r_green_max and g_green_min < g_avg < g_green_max and b_avg < b_green_max:
    kocka2.face["Front"][0][2] = '🟩'
elif r_blue_min < r_avg < r_blue_max and g_avg < g_blue_max and b_avg < b_blue_max:
    kocka2.face["Front"][0][2] = '🟦'
elif r_avg < r_orange_max and g_avg < g_orange_max and b_orange_min < b_avg < b_orange_max:
    kocka2.face["Front"][0][2] = '🟧'
elif r_white_min < r_avg < r_white_max and g_white_min < g_avg < g_white_max and b_white_min < b_avg < b_white_max:
    kocka2.face["Front"][0][2] = '⬜'
else:
    kocka2.face["Front"][0][2] = 'nepoznata'
print(kocka2.face["Front"][0][2])

r, g, b = cv2.split(img14)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < r_red_max and g_avg < g_red_max and b_avg < b_red_max:
    kocka2.face["Front"][1][0] = '🟥'
elif r_yellow_min < r_avg < r_yellow_max and g_yellow_min < g_avg < g_yellow_max and b_yellow_min < b_avg < b_yellow_max:
    kocka2.face["Front"][1][0] = '🟨'
elif r_green_min < r_avg < r_green_max and g_green_min < g_avg < g_green_max and b_avg < b_green_max:
    kocka2.face["Front"][1][0] = '🟩'
elif r_blue_min < r_avg < r_blue_max and g_avg < g_blue_max and b_avg < b_blue_max:
    kocka2.face["Front"][1][0] = '🟦'
elif r_avg < r_orange_max and g_avg < g_orange_max and b_orange_min < b_avg < b_orange_max:
    kocka2.face["Front"][1][0] = '🟧'
elif r_white_min < r_avg < r_white_max and g_white_min < g_avg < g_white_max and b_white_min < b_avg < b_white_max:
    kocka2.face["Front"][1][0] = '⬜'
else:
    kocka2.face["Front"][1][0] = 'nepoznata'
print(kocka2.face["Front"][1][0])

r, g, b = cv2.split(img15)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < r_red_max and g_avg < g_red_max and b_avg < b_red_max:
    kocka2.face["Front"][1][1] = '🟥'
elif r_yellow_min < r_avg < r_yellow_max and g_yellow_min < g_avg < g_yellow_max and b_yellow_min < b_avg < b_yellow_max:
    kocka2.face["Front"][1][1] = '🟨'
elif r_green_min < r_avg < r_green_max and g_green_min < g_avg < g_green_max and b_avg < b_green_max:
    kocka2.face["Front"][1][1] = '🟩'
elif r_blue_min < r_avg < r_blue_max and g_avg < g_blue_max and b_avg < b_blue_max:
    kocka2.face["Front"][1][1] = '🟦'
elif r_avg < r_orange_max and g_avg < g_orange_max and b_orange_min < b_avg < b_orange_max:
    kocka2.face["Front"][1][1] = '🟧'
elif r_white_min < r_avg < r_white_max and g_white_min < g_avg < g_white_max and b_white_min < b_avg < b_white_max:
    kocka2.face["Front"][1][1] = '⬜'
else:
    kocka2.face["Front"][1][1] = 'nepoznata'
print(kocka2.face["Front"][1][1])

r, g, b = cv2.split(img16)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < r_red_max and g_avg < g_red_max and b_avg < b_red_max:
    kocka2.face["Front"][1][2] = '🟥'
elif r_yellow_min < r_avg < r_yellow_max and g_yellow_min < g_avg < g_yellow_max and b_yellow_min < b_avg < b_yellow_max:
    kocka2.face["Front"][1][2] = '🟨'
elif r_green_min < r_avg < r_green_max and g_green_min < g_avg < g_green_max and b_avg < b_green_max:
    kocka2.face["Front"][1][2] = '🟩'
elif r_blue_min < r_avg < r_blue_max and g_avg < g_blue_max and b_avg < b_blue_max:
    kocka2.face["Front"][1][2] = '🟦'
elif r_avg < r_orange_max and g_avg < g_orange_max and b_orange_min < b_avg < b_orange_max:
    kocka2.face["Front"][1][2] = '🟧'
elif r_white_min < r_avg < r_white_max and g_white_min < g_avg < g_white_max and b_white_min < b_avg < b_white_max:
    kocka2.face["Front"][1][2] = '⬜'
else:
    kocka2.face["Front"][1][2] = 'nepoznata'
print(kocka2.face["Front"][1][2])

r, g, b = cv2.split(img17)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < r_red_max and g_avg < g_red_max and b_avg < b_red_max:
    kocka2.face["Front"][2][0] = '🟥'
elif r_yellow_min < r_avg < r_yellow_max and g_yellow_min < g_avg < g_yellow_max and b_yellow_min < b_avg < b_yellow_max:
    kocka2.face["Front"][2][0] = '🟨'
elif r_green_min < r_avg < r_green_max and g_green_min < g_avg < g_green_max and b_avg < b_green_max:
    kocka2.face["Front"][2][0] = '🟩'
elif r_blue_min < r_avg < r_blue_max and g_avg < g_blue_max and b_avg < b_blue_max:
    kocka2.face["Front"][2][0] = '🟦'
elif r_avg < r_orange_max and g_avg < g_orange_max and b_orange_min < b_avg < b_orange_max:
    kocka2.face["Front"][2][0] = '🟧'
elif r_white_min < r_avg < r_white_max and g_white_min < g_avg < g_white_max and b_white_min < b_avg < b_white_max:
    kocka2.face["Front"][2][0] = '⬜'
else:
    kocka2.face["Front"][2][0] = 'nepoznata'
print(kocka2.face["Front"][2][0])

r, g, b = cv2.split(img18)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < r_red_max and g_avg < g_red_max and b_avg < b_red_max:
    kocka2.face["Front"][2][1] = '🟥'
elif r_yellow_min < r_avg < r_yellow_max and g_yellow_min < g_avg < g_yellow_max and b_yellow_min < b_avg < b_yellow_max:
    kocka2.face["Front"][2][1] = '🟨'
elif r_green_min < r_avg < r_green_max and g_green_min < g_avg < g_green_max and b_avg < b_green_max:
    kocka2.face["Front"][2][1] = '🟩'
elif r_blue_min < r_avg < r_blue_max and g_avg < g_blue_max and b_avg < b_blue_max:
    kocka2.face["Front"][2][1] = '🟦'
elif r_avg < r_orange_max and g_avg < g_orange_max and b_orange_min < b_avg < b_orange_max:
    kocka2.face["Front"][2][1] = '🟧'
elif r_white_min < r_avg < r_white_max and g_white_min < g_avg < g_white_max and b_white_min < b_avg < b_white_max:
    kocka2.face["Front"][2][1] = '⬜'
else:
    kocka2.face["Front"][2][1] = 'nepoznata'
print(kocka2.face["Front"][2][1])

r, g, b = cv2.split(img19)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < r_red_max and g_avg < g_red_max and b_avg < b_red_max:
    kocka2.face["Front"][2][2] = '🟥'
elif r_yellow_min < r_avg < r_yellow_max and g_yellow_min < g_avg < g_yellow_max and b_yellow_min < b_avg < b_yellow_max:
    kocka2.face["Front"][2][2] = '🟨'
elif r_green_min < r_avg < r_green_max and g_green_min < g_avg < g_green_max and b_avg < b_green_max:
    kocka2.face["Front"][2][2] = '🟩'
elif r_blue_min < r_avg < r_blue_max and g_avg < g_blue_max and b_avg < b_blue_max:
    kocka2.face["Front"][2][2] = '🟦'
elif r_avg < r_orange_max and g_avg < g_orange_max and b_orange_min < b_avg < b_orange_max:
    kocka2.face["Front"][2][2] = '🟧'
elif r_white_min < r_avg < r_white_max and g_white_min < g_avg < g_white_max and b_white_min < b_avg < b_white_max:
    kocka2.face["Front"][2][2] = '⬜'
else:
    kocka2.face["Front"][2][2] = 'nepoznata'
print(kocka2.face["Front"][2][2])

########################################################################

print('BOTTOM')

r, g, b = cv2.split(img21)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < r_red_max and g_avg < g_red_max and b_avg < b_red_max:
    kocka2.face["Bottom"][0][0] = '🟥'
elif r_yellow_min < r_avg < r_yellow_max and g_yellow_min < g_avg < g_yellow_max and b_yellow_min < b_avg < b_yellow_max:
    kocka2.face["Bottom"][0][0] = '🟨'
elif r_green_min < r_avg < r_green_max and g_green_min < g_avg < g_green_max and b_avg < b_green_max:
    kocka2.face["Bottom"][0][0] = '🟩'
elif r_blue_min < r_avg < r_blue_max and g_avg < g_blue_max and b_avg < b_blue_max:
    kocka2.face["Bottom"][0][0] = '🟦'
elif r_avg < r_orange_max and g_avg < g_orange_max and b_orange_min < b_avg < b_orange_max:
    kocka2.face["Bottom"][0][0] = '🟧'
elif r_white_min < r_avg < r_white_max and g_white_min < g_avg < g_white_max and b_white_min < b_avg < b_white_max:
    kocka2.face["Bottom"][0][0] = '⬜'
else:
    kocka2.face["Bottom"][0][0] = 'nepoznata'
print(kocka2.face["Bottom"][0][0])

r, g, b = cv2.split(img22)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < r_red_max and g_avg < g_red_max and b_avg < b_red_max:
    kocka2.face["Bottom"][0][1] = '🟥'
elif r_yellow_min < r_avg < r_yellow_max and g_yellow_min < g_avg < g_yellow_max and b_yellow_min < b_avg < b_yellow_max:
    kocka2.face["Bottom"][0][1] = '🟨'
elif r_green_min < r_avg < r_green_max and g_green_min < g_avg < g_green_max and b_avg < b_green_max:
    kocka2.face["Bottom"][0][1] = '🟩'
elif r_blue_min < r_avg < r_blue_max and g_avg < g_blue_max and b_avg < b_blue_max:
    kocka2.face["Bottom"][0][1] = '🟦'
elif r_avg < r_orange_max and g_avg < g_orange_max and b_orange_min < b_avg < b_orange_max:
    kocka2.face["Bottom"][0][1] = '🟧'
elif r_white_min < r_avg < r_white_max and g_white_min < g_avg < g_white_max and b_white_min < b_avg < b_white_max:
    kocka2.face["Bottom"][0][1] = '⬜'
else:
    kocka2.face["Bottom"][0][1] = 'nepoznata'
print(kocka2.face["Bottom"][0][1])

r, g, b = cv2.split(img23)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < r_red_max and g_avg < g_red_max and b_avg < b_red_max:
    kocka2.face["Bottom"][0][2] = '🟥'
elif r_yellow_min < r_avg < r_yellow_max and g_yellow_min < g_avg < g_yellow_max and b_yellow_min < b_avg < b_yellow_max:
    kocka2.face["Bottom"][0][2] = '🟨'
elif r_green_min < r_avg < r_green_max and g_green_min < g_avg < g_green_max and b_avg < b_green_max:
    kocka2.face["Bottom"][0][2] = '🟩'
elif r_blue_min < r_avg < r_blue_max and g_avg < g_blue_max and b_avg < b_blue_max:
    kocka2.face["Bottom"][0][2] = '🟦'
elif r_avg < r_orange_max and g_avg < g_orange_max and b_orange_min < b_avg < b_orange_max:
    kocka2.face["Bottom"][0][2] = '🟧'
elif r_white_min < r_avg < r_white_max and g_white_min < g_avg < g_white_max and b_white_min < b_avg < b_white_max:
    kocka2.face["Bottom"][0][2] = '⬜'
else:
    kocka2.face["Bottom"][0][2] = 'nepoznata'
print(kocka2.face["Bottom"][0][2])

r, g, b = cv2.split(img24)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < r_red_max and g_avg < g_red_max and b_avg < b_red_max:
    kocka2.face["Bottom"][1][0] = '🟥'
elif r_yellow_min < r_avg < r_yellow_max and g_yellow_min < g_avg < g_yellow_max and b_yellow_min < b_avg < b_yellow_max:
    kocka2.face["Bottom"][1][0] = '🟨'
elif r_green_min < r_avg < r_green_max and g_green_min < g_avg < g_green_max and b_avg < b_green_max:
    kocka2.face["Bottom"][1][0] = '🟩'
elif r_blue_min < r_avg < r_blue_max and g_avg < g_blue_max and b_avg < b_blue_max:
    kocka2.face["Bottom"][1][0] = '🟦'
elif r_avg < r_orange_max and g_avg < g_orange_max and b_orange_min < b_avg < b_orange_max:
    kocka2.face["Bottom"][1][0] = '🟧'
elif r_white_min < r_avg < r_white_max and g_white_min < g_avg < g_white_max and b_white_min < b_avg < b_white_max:
    kocka2.face["Bottom"][1][0] = '⬜'
else:
    kocka2.face["Bottom"][1][0] = 'nepoznata'
print(kocka2.face["Bottom"][1][0])

r, g, b = cv2.split(img25)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < r_red_max and g_avg < g_red_max and b_avg < b_red_max:
    kocka2.face["Bottom"][1][1] = '🟥'
elif r_yellow_min < r_avg < r_yellow_max and g_yellow_min < g_avg < g_yellow_max and b_yellow_min < b_avg < b_yellow_max:
    kocka2.face["Bottom"][1][1] = '🟨'
elif r_green_min < r_avg < r_green_max and g_green_min < g_avg < g_green_max and b_avg < b_green_max:
    kocka2.face["Bottom"][1][1] = '🟩'
elif r_blue_min < r_avg < r_blue_max and g_avg < g_blue_max and b_avg < b_blue_max:
    kocka2.face["Bottom"][1][1] = '🟦'
elif r_avg < r_orange_max and g_avg < g_orange_max and b_orange_min < b_avg < b_orange_max:
    kocka2.face["Bottom"][1][1] = '🟧'
elif r_white_min < r_avg < r_white_max and g_white_min < g_avg < g_white_max and b_white_min < b_avg < b_white_max:
    kocka2.face["Bottom"][1][1] = '⬜'
else:
    kocka2.face["Bottom"][1][1] = 'nepoznata'
print(kocka2.face["Bottom"][1][1])

r, g, b = cv2.split(img26)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < r_red_max and g_avg < g_red_max and b_avg < b_red_max:
    kocka2.face["Bottom"][1][2] = '🟥'
elif r_yellow_min < r_avg < r_yellow_max and g_yellow_min < g_avg < g_yellow_max and b_yellow_min < b_avg < b_yellow_max:
    kocka2.face["Bottom"][1][2] = '🟨'
elif r_green_min < r_avg < r_green_max and g_green_min < g_avg < g_green_max and b_avg < b_green_max:
    kocka2.face["Bottom"][1][2] = '🟩'
elif r_blue_min < r_avg < r_blue_max and g_avg < g_blue_max and b_avg < b_blue_max:
    kocka2.face["Bottom"][1][2] = '🟦'
elif r_avg < r_orange_max and g_avg < g_orange_max and b_orange_min < b_avg < b_orange_max:
    kocka2.face["Bottom"][1][2] = '🟧'
elif r_white_min < r_avg < r_white_max and g_white_min < g_avg < g_white_max and b_white_min < b_avg < b_white_max:
    kocka2.face["Bottom"][1][2] = '⬜'
else:
    kocka2.face["Bottom"][1][2] = 'nepoznata'
print(kocka2.face["Bottom"][1][2])

r, g, b = cv2.split(img27)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < r_red_max and g_avg < g_red_max and b_avg < b_red_max:
    kocka2.face["Bottom"][2][0] = '🟥'
elif r_yellow_min < r_avg < r_yellow_max and g_yellow_min < g_avg < g_yellow_max and b_yellow_min < b_avg < b_yellow_max:
    kocka2.face["Bottom"][2][0] = '🟨'
elif r_green_min < r_avg < r_green_max and g_green_min < g_avg < g_green_max and b_avg < b_green_max:
    kocka2.face["Bottom"][2][0] = '🟩'
elif r_blue_min < r_avg < r_blue_max and g_avg < g_blue_max and b_avg < b_blue_max:
    kocka2.face["Bottom"][2][0] = '🟦'
elif r_avg < r_orange_max and g_avg < g_orange_max and b_orange_min < b_avg < b_orange_max:
    kocka2.face["Bottom"][2][0] = '🟧'
elif r_white_min < r_avg < r_white_max and g_white_min < g_avg < g_white_max and b_white_min < b_avg < b_white_max:
    kocka2.face["Bottom"][2][0] = '⬜'
else:
    kocka2.face["Bottom"][2][0] = 'nepoznata'
print(kocka2.face["Bottom"][2][0])

r, g, b = cv2.split(img28)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < r_red_max and g_avg < g_red_max and b_avg < b_red_max:
    kocka2.face["Bottom"][2][1] = '🟥'
elif r_yellow_min < r_avg < r_yellow_max and g_yellow_min < g_avg < g_yellow_max and b_yellow_min < b_avg < b_yellow_max:
    kocka2.face["Bottom"][2][1] = '🟨'
elif r_green_min < r_avg < r_green_max and g_green_min < g_avg < g_green_max and b_avg < b_green_max:
    kocka2.face["Bottom"][2][1] = '🟩'
elif r_blue_min < r_avg < r_blue_max and g_avg < g_blue_max and b_avg < b_blue_max:
    kocka2.face["Bottom"][2][1] = '🟦'
elif r_avg < r_orange_max and g_avg < g_orange_max and b_orange_min < b_avg < b_orange_max:
    kocka2.face["Bottom"][2][1] = '🟧'
elif r_white_min < r_avg < r_white_max and g_white_min < g_avg < g_white_max and b_white_min < b_avg < b_white_max:
    kocka2.face["Bottom"][2][1] = '⬜'
else:
    kocka2.face["Bottom"][2][1] = 'nepoznata'
print(kocka2.face["Bottom"][2][1])

r, g, b = cv2.split(img29)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < r_red_max and g_avg < g_red_max and b_avg < b_red_max:
    kocka2.face["Bottom"][2][2] = '🟥'
elif r_yellow_min < r_avg < r_yellow_max and g_yellow_min < g_avg < g_yellow_max and b_yellow_min < b_avg < b_yellow_max:
    kocka2.face["Bottom"][2][2] = '🟨'
elif r_green_min < r_avg < r_green_max and g_green_min < g_avg < g_green_max and b_avg < b_green_max:
    kocka2.face["Bottom"][2][2] = '🟩'
elif r_blue_min < r_avg < r_blue_max and g_avg < g_blue_max and b_avg < b_blue_max:
    kocka2.face["Bottom"][2][2] = '🟦'
elif r_avg < r_orange_max and g_avg < g_orange_max and b_orange_min < b_avg < b_orange_max:
    kocka2.face["Bottom"][2][2] = '🟧'
elif r_white_min < r_avg < r_white_max and g_white_min < g_avg < g_white_max and b_white_min < b_avg < b_white_max:
    kocka2.face["Bottom"][2][2] = '⬜'
else:
    kocka2.face["Bottom"][2][2] = 'nepoznata'
print(kocka2.face["Bottom"][2][2])

#########################################################################

print('LEFT')

r, g, b = cv2.split(img31)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < r_red_max and g_avg < g_red_max and b_avg < b_red_max:
    kocka2.face["Left"][0][0] = '🟥'
elif r_yellow_min < r_avg < r_yellow_max and g_yellow_min < g_avg < g_yellow_max and b_yellow_min < b_avg < b_yellow_max:
    kocka2.face["Left"][0][0] = '🟨'
elif r_green_min < r_avg < r_green_max and g_green_min < g_avg < g_green_max and b_avg < b_green_max:
    kocka2.face["Left"][0][0] = '🟩'
elif r_blue_min < r_avg < r_blue_max and g_avg < g_blue_max and b_avg < b_blue_max:
    kocka2.face["Left"][0][0] = '🟦'
elif r_avg < r_orange_max and g_avg < g_orange_max and b_orange_min < b_avg < b_orange_max:
    kocka2.face["Left"][0][0] = '🟧'
elif r_white_min < r_avg < r_white_max and g_white_min < g_avg < g_white_max and b_white_min < b_avg < b_white_max:
    kocka2.face["Left"][0][0] = '⬜'
else:
    kocka2.face["Left"][0][0] = 'nepoznata'
print(kocka2.face["Left"][0][0])

r, g, b = cv2.split(img32)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < r_red_max and g_avg < g_red_max and b_avg < b_red_max:
    kocka2.face["Left"][0][1] = '🟥'
elif r_yellow_min < r_avg < r_yellow_max and g_yellow_min < g_avg < g_yellow_max and b_yellow_min < b_avg < b_yellow_max:
    kocka2.face["Left"][0][1] = '🟨'
elif r_green_min < r_avg < r_green_max and g_green_min < g_avg < g_green_max and b_avg < b_green_max:
    kocka2.face["Left"][0][1] = '🟩'
elif r_blue_min < r_avg < r_blue_max and g_avg < g_blue_max and b_avg < b_blue_max:
    kocka2.face["Left"][0][1] = '🟦'
elif r_avg < r_orange_max and g_avg < g_orange_max and b_orange_min < b_avg < b_orange_max:
    kocka2.face["Left"][0][1] = '🟧'
elif r_white_min < r_avg < r_white_max and g_white_min < g_avg < g_white_max and b_white_min < b_avg < b_white_max:
    kocka2.face["Left"][0][1] = '⬜'
else:
    kocka2.face["Left"][1][0] = 'nepoznata'
print(kocka2.face["Left"][1][0])

r, g, b = cv2.split(img33)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < r_red_max and g_avg < g_red_max and b_avg < b_red_max:
    kocka2.face["Left"][0][2] = '🟥'
elif r_yellow_min < r_avg < r_yellow_max and g_yellow_min < g_avg < g_yellow_max and b_yellow_min < b_avg < b_yellow_max:
    kocka2.face["Left"][0][2] = '🟨'
elif r_green_min < r_avg < r_green_max and g_green_min < g_avg < g_green_max and b_avg < b_green_max:
    kocka2.face["Left"][0][2] = '🟩'
elif r_blue_min < r_avg < r_blue_max and g_avg < g_blue_max and b_avg < b_blue_max:
    kocka2.face["Left"][0][2] = '🟦'
elif r_avg < r_orange_max and g_avg < g_orange_max and b_orange_min < b_avg < b_orange_max:
    kocka2.face["Left"][0][2] = '🟧'
elif r_white_min < r_avg < r_white_max and g_white_min < g_avg < g_white_max and b_white_min < b_avg < b_white_max:
    kocka2.face["Left"][0][2] = '⬜'
else:
    kocka2.face["Left"][0][2] = 'nepoznata'
print(kocka2.face["Left"][0][2])

r, g, b = cv2.split(img34)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < r_red_max and g_avg < g_red_max and b_avg < b_red_max:
    kocka2.face["Left"][1][0] = '🟥'
elif r_yellow_min < r_avg < r_yellow_max and g_yellow_min < g_avg < g_yellow_max and b_yellow_min < b_avg < b_yellow_max:
    kocka2.face["Left"][1][0] = '🟨'
elif r_green_min < r_avg < r_green_max and g_green_min < g_avg < g_green_max and b_avg < b_green_max:
    kocka2.face["Left"][1][0] = '🟩'
elif r_blue_min < r_avg < r_blue_max and g_avg < g_blue_max and b_avg < b_blue_max:
    kocka2.face["Left"][1][0] = '🟦'
elif r_avg < r_orange_max and g_avg < g_orange_max and b_orange_min < b_avg < b_orange_max:
    kocka2.face["Left"][1][0] = '🟧'
elif r_white_min < r_avg < r_white_max and g_white_min < g_avg < g_white_max and b_white_min < b_avg < b_white_max:
    kocka2.face["Left"][1][0] = '⬜'
else:
    kocka2.face["Left"][1][0] = 'nepoznata'
print(kocka2.face["Left"][1][0])

r, g, b = cv2.split(img35)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < r_red_max and g_avg < g_red_max and b_avg < b_red_max:
    kocka2.face["Left"][1][1] = '🟥'
elif r_yellow_min < r_avg < r_yellow_max and g_yellow_min < g_avg < g_yellow_max and b_yellow_min < b_avg < b_yellow_max:
    kocka2.face["Left"][1][1] = '🟨'
elif r_green_min < r_avg < r_green_max and g_green_min < g_avg < g_green_max and b_avg < b_green_max:
    kocka2.face["Left"][1][1] = '🟩'
elif r_blue_min < r_avg < r_blue_max and g_avg < g_blue_max and b_avg < b_blue_max:
    kocka2.face["Left"][1][1] = '🟦'
elif r_avg < r_orange_max and g_avg < g_orange_max and b_orange_min < b_avg < b_orange_max:
    kocka2.face["Left"][1][1] = '🟧'
elif r_white_min < r_avg < r_white_max and g_white_min < g_avg < g_white_max and b_white_min < b_avg < b_white_max:
    kocka2.face["Left"][1][1] = '⬜'
else:
    kocka2.face["Left"][1][1] = 'nepoznata'
print(kocka2.face["Left"][1][1])

r, g, b = cv2.split(img36)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < r_red_max and g_avg < g_red_max and b_avg < b_red_max:
    kocka2.face["Left"][1][2] = '🟥'
elif r_yellow_min < r_avg < r_yellow_max and g_yellow_min < g_avg < g_yellow_max and b_yellow_min < b_avg < b_yellow_max:
    kocka2.face["Left"][1][2] = '🟨'
elif r_green_min < r_avg < r_green_max and g_green_min < g_avg < g_green_max and b_avg < b_green_max:
    kocka2.face["Left"][1][2] = '🟩'
elif r_blue_min < r_avg < r_blue_max and g_avg < g_blue_max and b_avg < b_blue_max:
    kocka2.face["Left"][1][2] = '🟦'
elif r_avg < r_orange_max and g_avg < g_orange_max and b_orange_min < b_avg < b_orange_max:
    kocka2.face["Left"][1][2] = '🟧'
elif r_white_min < r_avg < r_white_max and g_white_min < g_avg < g_white_max and b_white_min < b_avg < b_white_max:
    kocka2.face["Left"][1][2] = '⬜'
else:
    kocka2.face["Left"][1][2] = 'nepoznata'
print(kocka2.face["Left"][1][2])

r, g, b = cv2.split(img37)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < r_red_max and g_avg < g_red_max and b_avg < b_red_max:
    kocka2.face["Left"][2][0] = '🟥'
elif r_yellow_min < r_avg < r_yellow_max and g_yellow_min < g_avg < g_yellow_max and b_yellow_min < b_avg < b_yellow_max:
    kocka2.face["Left"][2][0] = '🟨'
elif r_green_min < r_avg < r_green_max and g_green_min < g_avg < g_green_max and b_avg < b_green_max:
    kocka2.face["Left"][2][0] = '🟩'
elif r_blue_min < r_avg < r_blue_max and g_avg < g_blue_max and b_avg < b_blue_max:
    kocka2.face["Left"][2][0] = '🟦'
elif r_avg < r_orange_max and g_avg < g_orange_max and b_orange_min < b_avg < b_orange_max:
    kocka2.face["Left"][2][0] = '🟧'
elif r_white_min < r_avg < r_white_max and g_white_min < g_avg < g_white_max and b_white_min < b_avg < b_white_max:
    kocka2.face["Left"][2][0] = '⬜'
else:
    kocka2.face["Left"][2][0] = 'nepoznata'
print(kocka2.face["Left"][2][0])

r, g, b = cv2.split(img38)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < r_red_max and g_avg < g_red_max and b_avg < b_red_max:
    kocka2.face["Left"][2][1] = '🟥'
elif r_yellow_min < r_avg < r_yellow_max and g_yellow_min < g_avg < g_yellow_max and b_yellow_min < b_avg < b_yellow_max:
    kocka2.face["Left"][2][1] = '🟨'
elif r_green_min < r_avg < r_green_max and g_green_min < g_avg < g_green_max and b_avg < b_green_max:
    kocka2.face["Left"][2][1] = '🟩'
elif r_blue_min < r_avg < r_blue_max and g_avg < g_blue_max and b_avg < b_blue_max:
    kocka2.face["Left"][2][1] = '🟦'
elif r_avg < r_orange_max and g_avg < g_orange_max and b_orange_min < b_avg < b_orange_max:
    kocka2.face["Left"][2][1] = '🟧'
elif r_white_min < r_avg < r_white_max and g_white_min < g_avg < g_white_max and b_white_min < b_avg < b_white_max:
    kocka2.face["Left"][2][1] = '⬜'
else:
    kocka2.face["Left"][2][1] = 'nepoznata'
print(kocka2.face["Left"][2][1])

r, g, b = cv2.split(img39)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < r_red_max and g_avg < g_red_max and b_avg < b_red_max:
    kocka2.face["Left"][2][2] = '🟥'
elif r_yellow_min < r_avg < r_yellow_max and g_yellow_min < g_avg < g_yellow_max and b_yellow_min < b_avg < b_yellow_max:
    kocka2.face["Left"][2][2] = '🟨'
elif r_green_min < r_avg < r_green_max and g_green_min < g_avg < g_green_max and b_avg < b_green_max:
    kocka2.face["Left"][2][2] = '🟩'
elif r_blue_min < r_avg < r_blue_max and g_avg < g_blue_max and b_avg < b_blue_max:
    kocka2.face["Left"][2][2] = '🟦'
elif r_avg < r_orange_max and g_avg < g_orange_max and b_orange_min < b_avg < b_orange_max:
    kocka2.face["Left"][2][2] = '🟧'
elif r_white_min < r_avg < r_white_max and g_white_min < g_avg < g_white_max and b_white_min < b_avg < b_white_max:
    kocka2.face["Left"][2][2] = '⬜'
else:
    kocka2.face["Left"][2][2] = 'nepoznata'
print(kocka2.face["Left"][2][2])

#################################################################

print('BACK')

r, g, b = cv2.split(img41)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < r_red_max and g_avg < g_red_max and b_avg < b_red_max:
    kocka2.face["Back"][0][0] = '🟥'
elif r_yellow_min < r_avg < r_yellow_max and g_yellow_min < g_avg < g_yellow_max and b_yellow_min < b_avg < b_yellow_max:
    kocka2.face["Back"][0][0] = '🟨'
elif r_green_min < r_avg < r_green_max and g_green_min < g_avg < g_green_max and b_avg < b_green_max:
    kocka2.face["Back"][0][0] = '🟩'
elif r_blue_min < r_avg < r_blue_max and g_avg < g_blue_max and b_avg < b_blue_max:
    kocka2.face["Back"][0][0] = '🟦'
elif r_avg < r_orange_max and g_avg < g_orange_max and b_orange_min < b_avg < b_orange_max:
    kocka2.face["Back"][0][0] = '🟧'
elif r_white_min < r_avg < r_white_max and g_white_min < g_avg < g_white_max and b_white_min < b_avg < b_white_max:
    kocka2.face["Back"][0][0] = '⬜'
else:
    kocka2.face["Back"][0][0] = 'nepoznata'
print( kocka2.face["Back"][0][0])

r, g, b = cv2.split(img42)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < r_red_max and g_avg < g_red_max and b_avg < b_red_max:
    kocka2.face["Back"][0][1] = '🟥'
elif r_yellow_min < r_avg < r_yellow_max and g_yellow_min < g_avg < g_yellow_max and b_yellow_min < b_avg < b_yellow_max:
    kocka2.face["Back"][0][1] = '🟨'
elif r_green_min < r_avg < r_green_max and g_green_min < g_avg < g_green_max and b_avg < b_green_max:
    kocka2.face["Back"][0][1] = '🟩'
elif r_blue_min < r_avg < r_blue_max and g_avg < g_blue_max and b_avg < b_blue_max:
    kocka2.face["Back"][0][1] = '🟦'
elif r_avg < r_orange_max and g_avg < g_orange_max and b_orange_min < b_avg < b_orange_max:
    kocka2.face["Back"][0][1] = '🟧'
elif r_white_min < r_avg < r_white_max and g_white_min < g_avg < g_white_max and b_white_min < b_avg < b_white_max:
    kocka2.face["Back"][0][1] = '⬜'
else:
    kocka2.face["Back"][0][1] = 'nepoznata'
print(kocka2.face["Back"][0][1])

r, g, b = cv2.split(img43)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < r_red_max and g_avg < g_red_max and b_avg < b_red_max:
    kocka2.face["Back"][0][2] = '🟥'
elif r_yellow_min < r_avg < r_yellow_max and g_yellow_min < g_avg < g_yellow_max and b_yellow_min < b_avg < b_yellow_max:
    kocka2.face["Back"][0][2] = '🟨'
elif r_green_min < r_avg < r_green_max and g_green_min < g_avg < g_green_max and b_avg < b_green_max:
    kocka2.face["Back"][0][2] = '🟩'
elif r_blue_min < r_avg < r_blue_max and g_avg < g_blue_max and b_avg < b_blue_max:
    kocka2.face["Back"][0][2] = '🟦'
elif r_avg < r_orange_max and g_avg < g_orange_max and b_orange_min < b_avg < b_orange_max:
    kocka2.face["Back"][0][2] = '🟧'
elif r_white_min < r_avg < r_white_max and g_white_min < g_avg < g_white_max and b_white_min < b_avg < b_white_max:
    kocka2.face["Back"][0][2] = '⬜'
else:
    kocka2.face["Back"][0][2] = 'nepoznata'
print(kocka2.face["Back"][0][2])

r, g, b = cv2.split(img44)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < r_red_max and g_avg < g_red_max and b_avg < b_red_max:
    kocka2.face["Back"][1][0] = '🟥'
elif r_yellow_min < r_avg < r_yellow_max and g_yellow_min < g_avg < g_yellow_max and b_yellow_min < b_avg < b_yellow_max:
    kocka2.face["Back"][1][0] = '🟨'
elif r_green_min < r_avg < r_green_max and g_green_min < g_avg < g_green_max and b_avg < b_green_max:
    kocka2.face["Back"][1][0] = '🟩'
elif r_blue_min < r_avg < r_blue_max and g_avg < g_blue_max and b_avg < b_blue_max:
    kocka2.face["Back"][1][0] = '🟦'
elif r_avg < r_orange_max and g_avg < g_orange_max and b_orange_min < b_avg < b_orange_max:
    kocka2.face["Back"][1][0] = '🟧'
elif r_white_min < r_avg < r_white_max and g_white_min < g_avg < g_white_max and b_white_min < b_avg < b_white_max:
    kocka2.face["Back"][1][0] = '⬜'
else:
    kocka2.face["Back"][1][0] = 'nepoznata'
print(kocka2.face["Back"][1][0])

r, g, b = cv2.split(img45)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < r_red_max and g_avg < g_red_max and b_avg < b_red_max:
    kocka2.face["Back"][1][1] = '🟥'
elif r_yellow_min < r_avg < r_yellow_max and g_yellow_min < g_avg < g_yellow_max and b_yellow_min < b_avg < b_yellow_max:
    kocka2.face["Back"][1][1] = '🟨'
elif r_green_min < r_avg < r_green_max and g_green_min < g_avg < g_green_max and b_avg < b_green_max:
    kocka2.face["Back"][1][1] = '🟩'
elif r_blue_min < r_avg < r_blue_max and g_avg < g_blue_max and b_avg < b_blue_max:
    kocka2.face["Back"][1][1] = '🟦'
elif r_avg < r_orange_max and g_avg < g_orange_max and b_orange_min < b_avg < b_orange_max:
    kocka2.face["Back"][1][1] = '🟧'
elif r_white_min < r_avg < r_white_max and g_white_min < g_avg < g_white_max and b_white_min < b_avg < b_white_max:
    kocka2.face["Back"][1][1] = '⬜'
else:
    kocka2.face["Back"][1][1] = 'nepoznata'
print(kocka2.face["Back"][1][1])

r, g, b = cv2.split(img46)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < r_red_max and g_avg < g_red_max and b_avg < b_red_max:
    kocka2.face["Back"][1][2] = '🟥'
elif r_yellow_min < r_avg < r_yellow_max and g_yellow_min < g_avg < g_yellow_max and b_yellow_min < b_avg < b_yellow_max:
    kocka2.face["Back"][1][2] = '🟨'
elif r_green_min < r_avg < r_green_max and g_green_min < g_avg < g_green_max and b_avg < b_green_max:
    kocka2.face["Back"][1][2] = '🟩'
elif r_blue_min < r_avg < r_blue_max and g_avg < g_blue_max and b_avg < b_blue_max:
    kocka2.face["Back"][1][2] = '🟦'
elif r_avg < r_orange_max and g_avg < g_orange_max and b_orange_min < b_avg < b_orange_max:
    kocka2.face["Back"][1][2] = '🟧'
elif r_white_min < r_avg < r_white_max and g_white_min < g_avg < g_white_max and b_white_min < b_avg < b_white_max:
    kocka2.face["Back"][1][2] = '⬜'
else:
    kocka2.face["Back"][1][2] = 'nepoznata'
print(kocka2.face["Back"][1][2])

r, g, b = cv2.split(img47)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < r_red_max and g_avg < g_red_max and b_avg < b_red_max:
    kocka2.face["Back"][2][0] = '🟥'
elif r_yellow_min < r_avg < r_yellow_max and g_yellow_min < g_avg < g_yellow_max and b_yellow_min < b_avg < b_yellow_max:
    kocka2.face["Back"][2][0] = '🟨'
elif r_green_min < r_avg < r_green_max and g_green_min < g_avg < g_green_max and b_avg < b_green_max:
    kocka2.face["Back"][2][0] = '🟩'
elif r_blue_min < r_avg < r_blue_max and g_avg < g_blue_max and b_avg < b_blue_max:
    kocka2.face["Back"][2][0] = '🟦'
elif r_avg < r_orange_max and g_avg < g_orange_max and b_orange_min < b_avg < b_orange_max:
    kocka2.face["Back"][2][0] = '🟧'
elif r_white_min < r_avg < r_white_max and g_white_min < g_avg < g_white_max and b_white_min < b_avg < b_white_max:
    kocka2.face["Back"][2][0] = '⬜'
else:
    kocka2.face["Back"][2][0] = 'nepoznata'
print(kocka2.face["Back"][2][0])

r, g, b = cv2.split(img48)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < r_red_max and g_avg < g_red_max and b_avg < b_red_max:
    kocka2.face["Back"][2][1] = '🟥'
elif r_yellow_min < r_avg < r_yellow_max and g_yellow_min < g_avg < g_yellow_max and b_yellow_min < b_avg < b_yellow_max:
    kocka2.face["Back"][2][1] = '🟨'
elif r_green_min < r_avg < r_green_max and g_green_min < g_avg < g_green_max and b_avg < b_green_max:
    kocka2.face["Back"][2][1] = '🟩'
elif r_blue_min < r_avg < r_blue_max and g_avg < g_blue_max and b_avg < b_blue_max:
    kocka2.face["Back"][2][1] = '🟦'
elif r_avg < r_orange_max and g_avg < g_orange_max and b_orange_min < b_avg < b_orange_max:
    kocka2.face["Back"][2][1] = '🟧'
elif r_white_min < r_avg < r_white_max and g_white_min < g_avg < g_white_max and b_white_min < b_avg < b_white_max:
    kocka2.face["Back"][2][1] = '⬜'
else:
    kocka2.face["Back"][2][1] = 'nepoznata'
print(kocka2.face["Back"][2][1])

r, g, b = cv2.split(img49)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < r_red_max and g_avg < g_red_max and b_avg < b_red_max:
    kocka2.face["Back"][2][2] = '🟥'
elif r_yellow_min < r_avg < r_yellow_max and g_yellow_min < g_avg < g_yellow_max and b_yellow_min < b_avg < b_yellow_max:
    kocka2.face["Back"][2][2] = '🟨'
elif r_green_min < r_avg < r_green_max and g_green_min < g_avg < g_green_max and b_avg < b_green_max:
    kocka2.face["Back"][2][2] = '🟩'
elif r_blue_min < r_avg < r_blue_max and g_avg < g_blue_max and b_avg < b_blue_max:
    kocka2.face["Back"][2][2] = '🟦'
elif r_avg < r_orange_max and g_avg < g_orange_max and b_orange_min < b_avg < b_orange_max:
    kocka2.face["Back"][2][2] = '🟧'
elif r_white_min < r_avg < r_white_max and g_white_min < g_avg < g_white_max and b_white_min < b_avg < b_white_max:
    kocka2.face["Back"][2][2] = '⬜'
else:
    kocka2.face["Back"][2][2] = 'nepoznata'
print(kocka2.face["Back"][2][2])

###############################################################

print('RIGHT')

r, g, b = cv2.split(img51)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < r_red_max and g_avg < g_red_max and b_avg < b_red_max:
    kocka2.face["Right"][0][0] = '🟥'
elif r_yellow_min < r_avg < r_yellow_max and g_yellow_min < g_avg < g_yellow_max and b_yellow_min < b_avg < b_yellow_max:
    kocka2.face["Right"][0][0] = '🟨'
elif r_green_min < r_avg < r_green_max and g_green_min < g_avg < g_green_max and b_avg < b_green_max:
    kocka2.face["Right"][0][0] = '🟩'
elif r_blue_min < r_avg < r_blue_max and g_avg < g_blue_max and b_avg < b_blue_max:
    kocka2.face["Right"][0][0] = '🟦'
elif r_avg < r_orange_max and g_avg < g_orange_max and b_orange_min < b_avg < b_orange_max:
    kocka2.face["Right"][0][0] = '🟧'
elif r_white_min < r_avg < r_white_max and g_white_min < g_avg < g_white_max and b_white_min < b_avg < b_white_max:
    kocka2.face["Right"][0][0] = '⬜'
else:
    kocka2.face["Right"][0][0] = 'nepoznata'
print(kocka2.face["Right"][0][0])

r, g, b = cv2.split(img52)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < r_red_max and g_avg < g_red_max and b_avg < b_red_max:
    kocka2.face["Right"][0][1] = '🟥'
elif r_yellow_min < r_avg < r_yellow_max and g_yellow_min < g_avg < g_yellow_max and b_yellow_min < b_avg < b_yellow_max:
    kocka2.face["Right"][0][1] = '🟨'
elif r_green_min < r_avg < r_green_max and g_green_min < g_avg < g_green_max and b_avg < b_green_max:
    kocka2.face["Right"][0][1] = '🟩'
elif r_blue_min < r_avg < r_blue_max and g_avg < g_blue_max and b_avg < b_blue_max:
    kocka2.face["Right"][0][1] = '🟦'
elif r_avg < r_orange_max and g_avg < g_orange_max and b_orange_min < b_avg < b_orange_max:
    kocka2.face["Right"][0][1] = '🟧'
elif r_white_min < r_avg < r_white_max and g_white_min < g_avg < g_white_max and b_white_min < b_avg < b_white_max:
    kocka2.face["Right"][0][1] = '⬜'
else:
    kocka2.face["Right"][0][1] = 'nepoznata'
print(kocka2.face["Right"][0][1])

r, g, b = cv2.split(img53)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < r_red_max and g_avg < g_red_max and b_avg < b_red_max:
    kocka2.face["Right"][0][2] = '🟥'
elif r_yellow_min < r_avg < r_yellow_max and g_yellow_min < g_avg < g_yellow_max and b_yellow_min < b_avg < b_yellow_max:
    kocka2.face["Right"][0][2] = '🟨'
elif r_green_min < r_avg < r_green_max and g_green_min < g_avg < g_green_max and b_avg < b_green_max:
    kocka2.face["Right"][0][2] = '🟩'
elif r_blue_min < r_avg < r_blue_max and g_avg < g_blue_max and b_avg < b_blue_max:
    kocka2.face["Right"][0][2] = '🟦'
elif r_avg < r_orange_max and g_avg < g_orange_max and b_orange_min < b_avg < b_orange_max:
    kocka2.face["Right"][0][2] = '🟧'
elif r_white_min < r_avg < r_white_max and g_white_min < g_avg < g_white_max and b_white_min < b_avg < b_white_max:
    kocka2.face["Right"][0][2] = '⬜'
else:
    kocka2.face["Right"][0][2] = 'nepoznata'
print(kocka2.face["Right"][0][2])

r, g, b = cv2.split(img54)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < r_red_max and g_avg < g_red_max and b_avg < b_red_max:
    kocka2.face["Right"][1][0] = '🟥'
elif r_yellow_min < r_avg < r_yellow_max and g_yellow_min < g_avg < g_yellow_max and b_yellow_min < b_avg < b_yellow_max:
    kocka2.face["Right"][1][0] = '🟨'
elif r_green_min < r_avg < r_green_max and g_green_min < g_avg < g_green_max and b_avg < b_green_max:
    kocka2.face["Right"][1][0] = '🟩'
elif r_blue_min < r_avg < r_blue_max and g_avg < g_blue_max and b_avg < b_blue_max:
    kocka2.face["Right"][1][0] = '🟦'
elif r_avg < r_orange_max and g_avg < g_orange_max and b_orange_min < b_avg < b_orange_max:
    kocka2.face["Right"][1][0] = '🟧'
elif r_white_min < r_avg < r_white_max and g_white_min < g_avg < g_white_max and b_white_min < b_avg < b_white_max:
    kocka2.face["Right"][1][0] = '⬜'
else:
    kocka2.face["Right"][1][0] = 'nepoznata'
print(kocka2.face["Right"][1][0])

r, g, b = cv2.split(img55)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < r_red_max and g_avg < g_red_max and b_avg < b_red_max:
    kocka2.face["Right"][1][1] = '🟥'
elif r_yellow_min < r_avg < r_yellow_max and g_yellow_min < g_avg < g_yellow_max and b_yellow_min < b_avg < b_yellow_max:
    kocka2.face["Right"][1][1] = '🟨'
elif r_green_min < r_avg < r_green_max and g_green_min < g_avg < g_green_max and b_avg < b_green_max:
    kocka2.face["Right"][1][1] = '🟩'
elif r_blue_min < r_avg < r_blue_max and g_avg < g_blue_max and b_avg < b_blue_max:
    kocka2.face["Right"][1][1] = '🟦'
elif r_avg < r_orange_max and g_avg < g_orange_max and b_orange_min < b_avg < b_orange_max:
    kocka2.face["Right"][1][1] = '🟧'
elif r_white_min < r_avg < r_white_max and g_white_min < g_avg < g_white_max and b_white_min < b_avg < b_white_max:
    kocka2.face["Right"][1][1] = '⬜'
else:
    kocka2.face["Right"][1][1] = 'nepoznata'
print(kocka2.face["Right"][1][1])

r, g, b = cv2.split(img56)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < r_red_max and g_avg < g_red_max and b_avg < b_red_max:
    kocka2.face["Right"][1][2] = '🟥'
elif r_yellow_min < r_avg < r_yellow_max and g_yellow_min < g_avg < g_yellow_max and b_yellow_min < b_avg < b_yellow_max:
    kocka2.face["Right"][1][2] = '🟨'
elif r_green_min < r_avg < r_green_max and g_green_min < g_avg < g_green_max and b_avg < b_green_max:
    kocka2.face["Right"][1][2] = '🟩'
elif r_blue_min < r_avg < r_blue_max and g_avg < g_blue_max and b_avg < b_blue_max:
    kocka2.face["Right"][1][2] = '🟦'
elif r_avg < r_orange_max and g_avg < g_orange_max and b_orange_min < b_avg < b_orange_max:
    kocka2.face["Right"][1][2] = '🟧'
elif r_white_min < r_avg < r_white_max and g_white_min < g_avg < g_white_max and b_white_min < b_avg < b_white_max:
    kocka2.face["Right"][1][2] = '⬜'
else:
    kocka2.face["Right"][1][2] = 'nepoznata'
print(kocka2.face["Right"][1][2])

r, g, b = cv2.split(img57)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < r_red_max and g_avg < g_red_max and b_avg < b_red_max:
    kocka2.face["Right"][2][0] = '🟥'
elif r_yellow_min < r_avg < r_yellow_max and g_yellow_min < g_avg < g_yellow_max and b_yellow_min < b_avg < b_yellow_max:
    kocka2.face["Right"][2][0] = '🟨'
elif r_green_min < r_avg < r_green_max and g_green_min < g_avg < g_green_max and b_avg < b_green_max:
    kocka2.face["Right"][2][0] = '🟩'
elif r_blue_min < r_avg < r_blue_max and g_avg < g_blue_max and b_avg < b_blue_max:
    kocka2.face["Right"][2][0] = '🟦'
elif r_avg < r_orange_max and g_avg < g_orange_max and b_orange_min < b_avg < b_orange_max:
    kocka2.face["Right"][2][0] = '🟧'
elif r_white_min < r_avg < r_white_max and g_white_min < g_avg < g_white_max and b_white_min < b_avg < b_white_max:
    kocka2.face["Right"][2][0] = '⬜'
else:
    kocka2.face["Right"][2][0] = 'nepoznata'
print(kocka2.face["Right"][2][0])

r, g, b = cv2.split(img58)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < r_red_max and g_avg < g_red_max and b_avg < b_red_max:
    kocka2.face["Right"][2][1] = '🟥'
elif r_yellow_min < r_avg < r_yellow_max and g_yellow_min < g_avg < g_yellow_max and b_yellow_min < b_avg < b_yellow_max:
    kocka2.face["Right"][2][1] = '🟨'
elif r_green_min < r_avg < r_green_max and g_green_min < g_avg < g_green_max and b_avg < b_green_max:
    kocka2.face["Right"][2][1] = '🟩'
elif r_blue_min < r_avg < r_blue_max and g_avg < g_blue_max and b_avg < b_blue_max:
    kocka2.face["Right"][2][1] = '🟦'
elif r_avg < r_orange_max and g_avg < g_orange_max and b_orange_min < b_avg < b_orange_max:
    kocka2.face["Right"][2][1] = '🟧'
elif r_white_min < r_avg < r_white_max and g_white_min < g_avg < g_white_max and b_white_min < b_avg < b_white_max:
    kocka2.face["Right"][2][1] = '⬜'
else:
    kocka2.face["Right"][2][1] = 'nepoznata'
print(kocka2.face["Right"][2][1])

r, g, b = cv2.split(img59)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < r_red_max and g_avg < g_red_max and b_avg < b_red_max:
    kocka2.face["Right"][2][2] = '🟥'
elif r_yellow_min < r_avg < r_yellow_max and g_yellow_min < g_avg < g_yellow_max and b_yellow_min < b_avg < b_yellow_max:
    kocka2.face["Right"][2][2] = '🟨'
elif r_green_min < r_avg < r_green_max and g_green_min < g_avg < g_green_max and b_avg < b_green_max:
    kocka2.face["Right"][2][2] = '🟩'
elif r_blue_min < r_avg < r_blue_max and g_avg < g_blue_max and b_avg < b_blue_max:
    kocka2.face["Right"][2][2] = '🟦'
elif r_avg < r_orange_max and g_avg < g_orange_max and b_orange_min < b_avg < b_orange_max:
    kocka2.face["Right"][2][2] = '🟧'
elif r_white_min < r_avg < r_white_max and g_white_min < g_avg < g_white_max and b_white_min < b_avg < b_white_max:
    kocka2.face["Right"][2][2] = '⬜'
else:
    kocka2.face["Right"][2][2] = 'nepoznata'
print(kocka2.face["Right"][2][2])

########################################################################


kocka2.draw_cube()
str = kocka2.cube_string()
kocka2.solver(str)
kocka2.draw_cube()

# Release the capture and writer objects
cam.release()
out.release()
cv2.destroyAllWindows()

#kocka2.draw_cube()
#str = kocka2.cube_string()
#kocka2.solver(str)
#kocka2.draw_cube()
