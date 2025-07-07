import cv2
from Cube import Cube
import numpy as np
import matplotlib.pyplot as plt

kocka2 = Cube()

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

while True:
    ret, frame = cam.read()

    cv2.rectangle(frame, (100, 70), (200, 170), color=(255, 0, 0), thickness=2)
    cv2.rectangle(frame, (200, 70), (300, 170), color=(255, 0, 0), thickness=2)
    cv2.rectangle(frame, (300, 70), (400, 170), color=(255, 0, 0), thickness=2)
    cv2.rectangle(frame, (100, 170), (200, 270), color=(255, 0, 0), thickness=2)
    cv2.rectangle(frame, (200, 170), (300, 270), color=(255, 0, 0), thickness=2)
    cv2.rectangle(frame, (300, 170), (400, 270), color=(255, 0, 0), thickness=2)
    cv2.rectangle(frame, (100, 270), (200, 370), color=(255, 0, 0), thickness=2)
    cv2.rectangle(frame, (200, 270), (300, 370), color=(255, 0, 0), thickness=2)
    cv2.rectangle(frame, (300, 270), (400, 370), color=(255, 0, 0), thickness=2)

    # Write the frame to the output file
    out.write(frame)

    # Display the captured frame
    cv2.imshow('Camera', frame)

    # Press 's' to record a face
    if cv2.waitKey(1) == ord('s'):

        img1 = frame[70:170, 100:200]
        cv2.imshow('Polje11', img1)
        img2 = frame[70:170, 200:300]
        cv2.imshow('Polje12', img2)
        img3 = frame[70:170, 300:400]
        cv2.imshow('Polje13', img3)
        img4 = frame[170:270, 100:200]
        cv2.imshow('Polje21', img4)
        img5 = frame[170:270, 200:300]
        cv2.imshow('Polje22', img5)
        img6 = frame[170:270, 300:400]
        cv2.imshow('Polje23', img6)
        img7 = frame[270:370, 100:200]
        cv2.imshow('Polje31', img7)
        img8 = frame[270:370, 200:300]
        cv2.imshow('Polje32', img8)
        img9 = frame[270:370, 300:400]
        cv2.imshow('Polje33', img9)

    # Press 'q' to exit the loop
    if cv2.waitKey(2) == ord('q'):
       break

#plt.figure()
#plt.imshow(img1)
#plt.show()

polje11 = []
polje12 = []
polje13 = []
polje21 = []
polje22 = []
polje23 = []
polje31 = []
polje32 = []
polje33 = []

r, g, b = cv2.split(img1)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < 65 and g_avg < 50 and b_avg < 125:
    polje11 = 'crvena'
elif 75 < r_avg < 115 and 110 < g_avg < 155 and 60 < b_avg < 105:
    polje11 = 'žuta'
elif 70 < r_avg < 110 and 90 < g_avg < 125 and b_avg < 30:
    polje11 = 'zelena'
elif 120 < r_avg < 180 and g_avg < 90 and b_avg < 50:
    polje11 = 'plava'
elif r_avg < 90 and g_avg < 90 and b_avg < 160:  # g<200 b<100
    polje11 = 'narandžasta'
elif 140 < r_avg < 195 and 110 < g_avg < 150 and 80 < b_avg < 115:
    polje11 = 'bela'
else:
    polje11 = 'nepoznata'
print(polje11)

r, g, b = cv2.split(img2)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < 65 and g_avg < 50 and b_avg < 125:
    polje12 = 'crvena'
elif 75 < r_avg < 115 and 110 < g_avg < 155 and 60 < b_avg < 105:
    polje12 = 'žuta'
elif 70 < r_avg < 110 and 90 < g_avg < 125 and b_avg < 30:
    polje12 = 'zelena'
elif 120 < r_avg < 180 and g_avg < 90 and b_avg < 50:
    polje12 = 'plava'
elif r_avg < 90 and g_avg < 90 and b_avg < 160:
    polje12 = 'narandžasta'
elif 140 < r_avg < 195 and 110 < g_avg < 150 and 80 < b_avg < 115:
    polje12 = 'bela'
else:
    polje12 = 'nepoznata'
print(polje12)

r, g, b = cv2.split(img3)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < 65 and g_avg < 50 and b_avg < 125:
    polje13 = 'crvena'
elif 75 < r_avg < 115 and 110 < g_avg < 155 and 60 < b_avg < 105:
    polje13 = 'žuta'
elif 70 < r_avg < 110 and 90 < g_avg < 125 and b_avg < 30:
    polje13 = 'zelena'
elif 120 < r_avg < 180 and g_avg < 90 and b_avg < 50:
    polje13 = 'plava'
elif r_avg < 90 and g_avg < 90 and b_avg < 160:
    polje13 = 'narandžasta'
elif 140 < r_avg < 195 and 110 < g_avg < 150 and 80 < b_avg < 115:
    polje13 = 'bela'
else:
    polje13 = 'nepoznata'
print(polje13)

r, g, b = cv2.split(img4)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < 65 and g_avg < 50 and b_avg < 125:
    polje21 = 'crvena'
elif 75 < r_avg < 115 and 110 < g_avg < 155 and 60 < b_avg < 105:
    polje21 = 'žuta'
elif 70 < r_avg < 110 and 90 < g_avg < 125 and b_avg < 30:
    polje21 = 'zelena'
elif 120 < r_avg < 180 and g_avg < 90 and b_avg < 50:
    polje21 = 'plava'
elif r_avg < 90 and g_avg < 90 and b_avg < 160:
    polje21 = 'narandžasta'
elif 140 < r_avg < 195 and 110 < g_avg < 150 and 80 < b_avg < 115:
    polje21 = 'bela'
else:
    polje21 = 'nepoznata'
print(polje21)

r, g, b = cv2.split(img5)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < 65 and g_avg < 50 and b_avg < 125:
    polje22 = 'crvena'
elif 75 < r_avg < 115 and 110 < g_avg < 155 and 60 < b_avg < 105:
    polje22 = 'žuta'
elif 70 < r_avg < 110 and 90 < g_avg < 125 and b_avg < 30:
    polje22 = 'zelena'
elif 120 < r_avg < 180 and g_avg < 90 and b_avg < 50:
    polje22 = 'plava'
elif r_avg < 90 and g_avg < 90 and b_avg < 160:
    polje22 = 'narandžasta'
elif 140 < r_avg < 195 and 110 < g_avg < 150 and 80 < b_avg < 115:
    polje22 = 'bela'
else:
    polje22 = 'nepoznata'
print(polje22)

r, g, b = cv2.split(img6)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < 65 and g_avg < 50 and b_avg < 125:
    polje23 = 'crvena'
elif 75 < r_avg < 115 and 110 < g_avg < 155 and 60 < b_avg < 105:
    polje23 = 'žuta'
elif 70 < r_avg < 110 and 90 < g_avg < 125 and b_avg < 30:
    polje23 = 'zelena'
elif 120 < r_avg < 180 and g_avg < 90 and b_avg < 50:
    polje23 = 'plava'
elif r_avg < 90 and g_avg < 90 and b_avg < 160:
    polje23 = 'narandžasta'
elif 140 < r_avg < 195 and 110 < g_avg < 150 and 80 < b_avg < 115:
    polje23 = 'bela'
else:
    polje23 = 'nepoznata'
print(polje23)

r, g, b = cv2.split(img7)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < 65 and g_avg < 50 and b_avg < 125:
    polje31 = 'crvena'
elif 75 < r_avg < 115 and 110 < g_avg < 155 and 60 < b_avg < 105:
    polje31 = 'žuta'
elif 70 < r_avg < 110 and 90 < g_avg < 125 and b_avg < 30:
    polje31 = 'zelena'
elif 120 < r_avg < 180 and g_avg < 90 and b_avg < 50:
    polje31 = 'plava'
elif r_avg < 90 and g_avg < 90 and b_avg < 160:
    polje31 = 'narandžasta'
elif 140 < r_avg < 195 and 110 < g_avg < 150 and 80 < b_avg < 115:
    polje31 = 'bela'
else:
    polje31 = 'nepoznata'
print(polje31)

r, g, b = cv2.split(img8)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < 65 and g_avg < 50 and b_avg < 125:
    polje32 = 'crvena'
elif 75 < r_avg < 115 and 110 < g_avg < 155 and 60 < b_avg < 105:
    polje32 = 'žuta'
elif 70 < r_avg < 110 and 90 < g_avg < 125 and b_avg < 30:
    polje32 = 'zelena'
elif 120 < r_avg < 180 and g_avg < 90 and b_avg < 50:
    polje32 = 'plava'
elif r_avg < 90 and g_avg < 90 and b_avg < 160:
    polje32 = 'narandžasta'
elif 140 < r_avg < 195 and 110 < g_avg < 150 and 80 < b_avg < 115:
    polje32 = 'bela'
else:
    polje32 = 'nepoznata'
print(polje32)

r, g, b = cv2.split(img9)
r_avg = cv2.mean(r)[0]
g_avg = cv2.mean(g)[0]
b_avg = cv2.mean(b)[0]
print(int(r_avg),int(g_avg),int(b_avg))

if r_avg < 65 and g_avg < 50 and b_avg < 125:
    polje33 = 'crvena'
elif 75 < r_avg < 115 and 110 < g_avg < 155 and 60 < b_avg < 105:
    polje33 = 'žuta'
elif 70 < r_avg < 110 and 90 < g_avg < 125 and b_avg < 30:
    polje33 = 'zelena'
elif 120 < r_avg < 180 and g_avg < 90 and b_avg < 50:
    polje33 = 'plava'
elif r_avg < 90 and g_avg < 90 and b_avg < 160:
    polje33 = 'narandžasta'
elif 140 < r_avg < 195 and 110 < g_avg < 150 and 80 < b_avg < 115:
    polje33 = 'bela'
else:
    polje33 = 'nepoznata'
print(polje33)


if polje11 == 'crvena':
    polje11 = "🟥"
elif polje11 == 'plava':
    polje11 = "🟦"
elif polje11 == 'žuta':
    polje11 = "🟨"
elif polje11 == 'zelena':
    polje11 = "🟩"
elif polje11 == 'bela':
    polje11 = "⬜"
elif polje11 == 'narandžasta':
    polje11 = "🟧"

if polje12 == 'crvena':
    polje12 = "🟥"
elif polje12 == 'plava':
    polje12 = "🟦"
elif polje12 == 'žuta':
    polje12 = "🟨"
elif polje12 == 'zelena':
    polje12 = "🟩"
elif polje12 == 'bela':
    polje12 = "⬜"
elif polje12 == 'narandžasta':
    polje12 = "🟧"

if polje13 == 'crvena':
    polje13 = "🟥"
elif polje13 == 'plava':
    polje13 = "🟦"
elif polje13 == 'žuta':
    polje13 = "🟨"
elif polje13 == 'zelena':
    polje13 = "🟩"
elif polje13 == 'bela':
    polje13 = "⬜"
elif polje13 == 'narandžasta':
    polje13 = "🟧"

if polje21 == 'crvena':
    polje21 = "🟥"
elif polje21 == 'plava':
    polje21 = "🟦"
elif polje21 == 'žuta':
    polje21 = "🟨"
elif polje21 == 'zelena':
    polje21 = "🟩"
elif polje21 == 'bela':
    polje21 = "⬜"
elif polje21 == 'narandžasta':
    polje21 = "🟧"

if polje22 == 'crvena':
    polje22 = "🟥"
elif polje22 == 'plava':
    polje22 = "🟦"
elif polje22 == 'žuta':
    polje22 = "🟨"
elif polje22 == 'zelena':
    polje22 = "🟩"
elif polje22 == 'bela':
    polje22 = "⬜"
elif polje22 == 'narandžasta':
    polje22 = "🟧"

if polje23 == 'crvena':
    polje23 = "🟥"
elif polje23 == 'plava':
    polje23 = "🟦"
elif polje23 == 'žuta':
    polje23 = "🟨"
elif polje23 == 'zelena':
    polje23 = "🟩"
elif polje23 == 'bela':
    polje23 = "⬜"
elif polje23 == 'narandžasta':
    polje23 = "🟧"

if polje31 == 'crvena':
    polje31 = "🟥"
elif polje31 == 'plava':
    polje31 = "🟦"
elif polje31 == 'žuta':
    polje31 = "🟨"
elif polje31 == 'zelena':
    polje31 = "🟩"
elif polje31 == 'bela':
    polje31 = "⬜"
elif polje31 == 'narandžasta':
    polje31 = "🟧"

if polje32 == 'crvena':
    polje32 = "🟥"
elif polje32 == 'plava':
    polje32 = "🟦"
elif polje32 == 'žuta':
    polje32 = "🟨"
elif polje32 == 'zelena':
    polje32 = "🟩"
elif polje32 == 'bela':
    polje32 = "⬜"
elif polje32 == 'narandžasta':
    polje32 = "🟧"

if polje33 == 'crvena':
    polje33 = "🟥"
elif polje33 == 'plava':
    polje33 = "🟦"
elif polje33 == 'žuta':
    polje33 = "🟨"
elif polje33 == 'zelena':
    polje33 = "🟩"
elif polje33 == 'bela':
    polje33 = "⬜"
elif polje33 == 'narandžasta':
    polje33 = "🟧"


kocka2.face["Top"][0][0] = polje11
kocka2.face["Top"][0][1] = polje12
kocka2.face["Top"][0][2] = polje13
kocka2.face["Top"][1][0] = polje21
kocka2.face["Top"][1][1] = polje22
kocka2.face["Top"][1][2] = polje23
kocka2.face["Top"][2][0] = polje31
kocka2.face["Top"][2][1] = polje32
kocka2.face["Top"][2][2] = polje33

kocka2.draw_cube()


# Release the capture and writer objects
cam.release()
out.release()
cv2.destroyAllWindows()


