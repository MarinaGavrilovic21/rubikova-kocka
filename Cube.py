import random

import numpy as np
import cv2 as cv
import twophase.solver as sv

class Cube:
    def __init__(self):
        self.face = {
            "Top": [
                ["🟦", "🟦", "🟦"],
                ["🟦", "🟦", "🟦"],
                ["🟦", "🟦", "🟦"]
            ],
            "Bottom": [
                ["🟩", "🟩", "🟩"],
                ["🟩", "🟩", "🟩"],
                ["🟩", "🟩", "🟩"]
            ],
            "Left": [
                ["🟧", "🟧", "🟧"],
                ["🟧", "🟧", "🟧"],
                ["🟧", "🟧", "🟧"]
            ],
            "Right": [
                ["🟥", "🟥", "🟥"],
                ["🟥", "🟥", "🟥"],
                ["🟥", "🟥", "🟥"]
            ],
            "Front": [
                ["🟨", "🟨", "🟨"],
                ["🟨", "🟨", "🟨"],
                ["🟨", "🟨", "🟨"]
            ],
            "Back": [
                ["⬜", "⬜", "⬜"],
                ["⬜", "⬜", "⬜"],
                ["⬜", "⬜", "⬜"]
            ]
        }

    def rotate_face_clockwise(self, face_name):
        face = self.face[face_name]
        ####### Rotacija kockica na uglovima ######
        temp = face[0][0]
        face[0][0] = face[2][0]
        face[2][0] = face[2][2]
        face[2][2] = face[0][2]
        face[0][2] = temp

        ###### Rotacija kockica u stranicama ######
        temp = face[0][1]
        face[0][1] = face[1][0]
        face[1][0] = face[2][1]
        face[2][1] = face[1][2]
        face[1][2] = temp

    def rotate_face_counter_clockwise(self, face_name):
        face = self.face[face_name]
        ####### Rotacija kockica na uglovima ######
        temp = face[0][0]
        face[0][0] = face[0][2]
        face[0][2] = face[2][2]
        face[2][2] = face[2][0]
        face[2][0] = temp

        ###### Rotacija kockica u stranicama ######
        temp = face[0][1]
        face[0][1] = face[1][2]
        face[1][2] = face[2][1]
        face[2][1] = face[1][0]
        face[1][0] = temp

    def rotate_top_clockwise(self):
        self.rotate_face_clockwise("Top")
        temp = self.face["Front"][0]
        self.face["Front"][0] = self.face["Right"][0]
        self.face["Right"][0] = self.face["Back"][0]
        self.face["Back"][0] = self.face["Left"][0]
        self.face["Left"][0] = temp

    def rotate_top_counter_clockwise(self):
        self.rotate_face_counter_clockwise("Top")
        temp = self.face["Front"][0]
        self.face["Front"][0] = self.face["Left"][0]
        self.face["Left"][0] = self.face["Back"][0]
        self.face["Back"][0] = self.face["Right"][0]
        self.face["Right"][0] = temp

    def rotate_bottom_clockwise(self):
        self.rotate_face_clockwise("Bottom")
        temp = self.face["Front"][2]
        self.face["Front"][2] = self.face["Left"][2]
        self.face["Left"][2] = self.face["Back"][2]
        self.face["Back"][2] = self.face["Right"][2]
        self.face["Right"][2] = temp

    def rotate_bottom_counter_clockwise(self):
        self.rotate_face_counter_clockwise("Bottom")
        temp = self.face["Front"][2]
        self.face["Front"][2] = self.face["Right"][2]
        self.face["Right"][2] = self.face["Back"][2]
        self.face["Back"][2] = self.face["Left"][2]
        self.face["Left"][2] = temp

    def rotate_left_clockwise(self):
        self.rotate_face_clockwise("Left")
        temp_col = [self.face["Top"][i][0] for i in range(3)]
        for i in range(3):
            self.face["Top"][i][0] = self.face["Back"][2 - i][2]
            self.face["Back"][2 - i][2] = self.face["Bottom"][i][0]
            self.face["Bottom"][i][0] = self.face["Front"][i][0]
            self.face["Front"][i][0] = temp_col[i]

    def rotate_left_counter_clockwise(self):
        self.rotate_face_counter_clockwise("Left")
        temp_col = [self.face["Top"][i][0] for i in range(3)]
        for i in range(3):
            self.face["Top"][i][0] = self.face["Front"][i][0]
            self.face["Front"][i][0] = self.face["Bottom"][i][0]
            self.face["Bottom"][i][0] = self.face["Back"][2 - i][2]
            self.face["Back"][2 - i][2] = temp_col[i]

    def rotate_right_clockwise(self):
        self.rotate_face_clockwise("Right")
        temp_col = [self.face["Top"][i][2] for i in range(3)]
        for i in range(3):
            self.face["Top"][i][2] = self.face["Front"][i][2]
            self.face["Front"][i][2] = self.face["Bottom"][i][2]
            self.face["Bottom"][i][2] = self.face["Back"][2 - i][0]
            self.face["Back"][2 - i][0] = temp_col[i]

    def rotate_right_counter_clockwise(self):
        self.rotate_face_counter_clockwise("Right")
        temp_col = [self.face["Top"][i][2] for i in range(3)]
        for i in range(3):
            self.face["Top"][i][2] = self.face["Back"][2 - i][0]
            self.face["Back"][2 - i][0] = self.face["Bottom"][i][2]
            self.face["Bottom"][i][2] = self.face["Front"][i][2]
            self.face["Front"][i][2] = temp_col[i]

    def rotate_front_clockwise(self):
        self.rotate_face_clockwise("Front")
        temp = [self.face["Top"][2][i] for i in range(3)]
        for i in range(3):
            self.face["Top"][2][i] = self.face["Left"][2 - i][2]
            self.face["Left"][2 - i][2] = self.face["Bottom"][0][2 - i]
            self.face["Bottom"][0][2 - i] = self.face["Right"][i][0]
            self.face["Right"][i][0] = temp[i]

    def rotate_front_counter_clockwise(self):
        self.rotate_face_counter_clockwise("Front")
        temp = [self.face["Top"][2][i] for i in range(3)]
        for i in range(3):
            self.face["Top"][2][i] = self.face["Right"][i][0]
            self.face["Right"][i][0] = self.face["Bottom"][0][2 - i]
            self.face["Bottom"][0][2 - i] = self.face["Left"][2 - i][2]
            self.face["Left"][2 - i][2] = temp[i]

    def rotate_back_clockwise(self):
        self.rotate_face_clockwise("Back")
        temp = [self.face["Top"][0][i] for i in range(3)]
        for i in range(3):
            self.face["Top"][0][i] = self.face["Right"][i][2]
            self.face["Right"][i][2] = self.face["Bottom"][2][2 - i]
            self.face["Bottom"][2][2 - i] = self.face["Left"][2 - i][0]
            self.face["Left"][2 - i][0] = temp[i]

    def rotate_back_counter_clockwise(self):
        self.rotate_face_counter_clockwise("Back")
        temp = [self.face["Top"][0][i] for i in range(3)]
        for i in range(3):
            self.face["Top"][0][i] = self.face["Left"][2 - i][0]
            self.face["Left"][2 - i][0] = self.face["Bottom"][2][2 - i]
            self.face["Bottom"][2][2 - i] = self.face["Right"][i][2]
            self.face["Right"][i][2] = temp[i]

    def scramble(self, n):

        functions = ['top_clk', 'bottom_clk', 'left_clk', 'right_clk', 'front_clk', 'back_clk', 'top_c_clk',
                     'bottom_c_clk', 'left_c_clk', 'right_c_clk', 'front_c_clk', 'back_c_clk']
        for i in range(n):
            selected_function = random.choice(functions)
            if selected_function == functions[0]:
                kocka.rotate_top_clockwise()
            elif selected_function == functions[1]:
                kocka.rotate_bottom_clockwise()
            elif selected_function == functions[2]:
                kocka.rotate_left_clockwise()
            elif selected_function == functions[3]:
                kocka.rotate_right_clockwise()
            elif selected_function == functions[4]:
                kocka.rotate_front_clockwise()
            elif selected_function == functions[5]:
                kocka.rotate_back_clockwise()
            elif selected_function == functions[6]:
                kocka.rotate_top_counter_clockwise()
            elif selected_function == functions[7]:
                kocka.rotate_bottom_counter_clockwise()
            elif selected_function == functions[8]:
                kocka.rotate_left_counter_clockwise()
            elif selected_function == functions[9]:
                kocka.rotate_right_counter_clockwise()
            elif selected_function == functions[10]:
                kocka.rotate_front_counter_clockwise()
            elif selected_function == functions[11]:
                kocka.rotate_back_counter_clockwise()

    def draw_cube(self):

        dictionary = {
            "⬜": (255, 255, 255),
            "🟨": (0, 255, 255),
            "🟩": (0, 200, 60),
            "🟦": (255, 0, 0),
            "🟥": (0, 0, 255),
            "🟧": (0, 90, 235)
        }

        # Create a black image
        img = np.zeros((1200, 1200, 3), np.uint8)

        # Drawing rectangle
        # Top
        # Prva kolona
        cv.rectangle(img, (242, 5), (316, 79), dictionary[self.face["Top"][0][0]], -1)
        cv.rectangle(img, (242, 81), (316, 155), dictionary[self.face["Top"][1][0]], -1)
        cv.rectangle(img, (242, 157), (316, 231), dictionary[self.face["Top"][2][0]], -1)
        # Druga kolona
        cv.rectangle(img, (318, 5), (392, 79), dictionary[self.face["Top"][0][1]], -1)
        cv.rectangle(img, (318, 81), (392, 155), dictionary[self.face["Top"][1][1]], -1)
        cv.rectangle(img, (318, 157), (392, 231), dictionary[self.face["Top"][2][1]], -1)
        # Treca kolona
        cv.rectangle(img, (394, 5), (468, 79), dictionary[self.face["Top"][0][2]], -1)
        cv.rectangle(img, (394, 81), (468, 155), dictionary[self.face["Top"][1][2]], -1)
        cv.rectangle(img, (394, 157), (468, 231), dictionary[self.face["Top"][2][2]], -1)

        # Front
        # Prva kolona
        cv.rectangle(img, (242, 247), (316, 321), dictionary[self.face["Front"][0][0]], -1)
        cv.rectangle(img, (242, 323), (316, 397), dictionary[self.face["Front"][1][0]], -1)
        cv.rectangle(img, (242, 399), (316, 473), dictionary[self.face["Front"][2][0]], -1)
        # Druga kolona
        cv.rectangle(img, (318, 247), (392, 321), dictionary[self.face["Front"][0][1]], -1)
        cv.rectangle(img, (318, 323), (392, 397), dictionary[self.face["Front"][1][1]], -1)
        cv.rectangle(img, (318, 399), (392, 473), dictionary[self.face["Front"][2][1]], -1)
        # Treca kolona
        cv.rectangle(img, (394, 247), (468, 321), dictionary[self.face["Front"][0][2]], -1)
        cv.rectangle(img, (394, 323), (468, 397), dictionary[self.face["Front"][1][2]], -1)
        cv.rectangle(img, (394, 399), (468, 473), dictionary[self.face["Front"][2][2]], -1)

        # Bottom
        # Prva kolona
        cv.rectangle(img, (242, 489), (316, 563), dictionary[self.face["Bottom"][0][0]], -1)
        cv.rectangle(img, (242, 565), (316, 639), dictionary[self.face["Bottom"][1][0]], -1)
        cv.rectangle(img, (242, 641), (316, 715), dictionary[self.face["Bottom"][2][0]], -1)
        # Druga kolona
        cv.rectangle(img, (318, 489), (392, 563), dictionary[self.face["Bottom"][0][1]], -1)
        cv.rectangle(img, (318, 565), (392, 639), dictionary[self.face["Bottom"][1][1]], -1)
        cv.rectangle(img, (318, 641), (392, 715), dictionary[self.face["Bottom"][2][1]], -1)
        # Treca kolona
        cv.rectangle(img, (394, 489), (468, 563), dictionary[self.face["Bottom"][0][2]], -1)
        cv.rectangle(img, (394, 565), (468, 639), dictionary[self.face["Bottom"][1][2]], -1)
        cv.rectangle(img, (394, 641), (468, 715), dictionary[self.face["Bottom"][2][2]], -1)

        # Left
        # Prva kolona
        cv.rectangle(img, (0, 247), (74, 321), dictionary[self.face["Left"][0][0]], -1)
        cv.rectangle(img, (0, 323), (74, 397), dictionary[self.face["Left"][1][0]], -1)
        cv.rectangle(img, (0, 399), (74, 473), dictionary[self.face["Left"][2][0]], -1)
        # Druga kolona
        cv.rectangle(img, (76, 247), (150, 321), dictionary[self.face["Left"][0][1]], -1)
        cv.rectangle(img, (76, 323), (150, 397), dictionary[self.face["Left"][1][1]], -1)
        cv.rectangle(img, (76, 399), (150, 473), dictionary[self.face["Left"][2][1]], -1)
        # Treca kolona
        cv.rectangle(img, (152, 247), (226, 321), dictionary[self.face["Left"][0][2]], -1)
        cv.rectangle(img, (152, 323), (226, 397), dictionary[self.face["Left"][1][2]], -1)
        cv.rectangle(img, (152, 399), (226, 473), dictionary[self.face["Left"][2][2]], -1)

        # Right
        # Prva kolona
        cv.rectangle(img, (484, 247), (558, 321), dictionary[self.face["Right"][0][0]], -1)
        cv.rectangle(img, (484, 323), (558, 397), dictionary[self.face["Right"][1][0]], -1)
        cv.rectangle(img, (484, 399), (558, 473), dictionary[self.face["Right"][2][0]], -1)
        # Druga kolona
        cv.rectangle(img, (560, 247), (634, 321), dictionary[self.face["Right"][0][1]], -1)
        cv.rectangle(img, (560, 323), (634, 397), dictionary[self.face["Right"][1][1]], -1)
        cv.rectangle(img, (560, 399), (634, 473), dictionary[self.face["Right"][2][1]], -1)
        # Treca kolona
        cv.rectangle(img, (636, 247), (710, 321), dictionary[self.face["Right"][0][2]], -1)
        cv.rectangle(img, (636, 323), (710, 397), dictionary[self.face["Right"][1][2]], -1)
        cv.rectangle(img, (636, 399), (710, 473), dictionary[self.face["Right"][2][2]], -1)

        # Back
        # Prva kolona
        cv.rectangle(img, (726, 247), (800, 321), dictionary[self.face["Back"][0][0]], -1)
        cv.rectangle(img, (726, 323), (800, 397), dictionary[self.face["Back"][1][0]], -1)
        cv.rectangle(img, (726, 399), (800, 473), dictionary[self.face["Back"][2][0]], -1)
        # Druga kolona
        cv.rectangle(img, (802, 247), (876, 321), dictionary[self.face["Back"][0][1]], -1)
        cv.rectangle(img, (802, 323), (876, 397), dictionary[self.face["Back"][1][1]], -1)
        cv.rectangle(img, (802, 399), (876, 473), dictionary[self.face["Back"][2][1]], -1)
        # Treca kolona
        cv.rectangle(img, (878, 247), (952, 321), dictionary[self.face["Back"][0][2]], -1)
        cv.rectangle(img, (878, 323), (952, 397), dictionary[self.face["Back"][1][2]], -1)
        cv.rectangle(img, (878, 399), (952, 473), dictionary[self.face["Back"][2][2]], -1)

        cv.imshow("Cube", img)
        cv.waitKey(0)
        cv.destroyAllWindows()

    # ZA OCITAVANJE SA KAMERE (NIJE ZAVRSENO)

    def color_recognition(patch):
        # Funkcija koja detektuje boju na osnovu RGB vrednosti
        # patch - jedan kvadrat na rubikovoj kocki

        b, g, r = np.mean(patch, axis=(0, 1)) # računa prosečne vrednosti boja (R, G, B) preko svih piksela u kvadratu
        if r > 200 and g < 100 and b < 100:
            return 'crvena'
        elif r > 200 and g > 200 and b < 100:
            return 'žuta'
        elif r < 100 and g > 200 and b < 100:
            return 'zelena'
        elif r < 100 and g > 100 and b > 200:  #g<200
            return 'plava'
        elif r > 200 and g < 100 and b > 200:  #g<200 b<100
            return 'narandžasta'
        elif r > 200 and g > 200 and b > 200:
            return 'bela'
        else:
            return 'nepoznata'

    def face_detection(frame):
        # funkcija koja detektuje boje na jednoj stranici kocke

        # Postavljamo kvadrate za detekciju boje
        # velicina kvadrata u pikselima
        velicina = 50
        # pocetne koordinate kvadrata na slici
        pozicije = [(150 + j * velicina, 150 + i * velicina) for i in range(3) for j in range(3)]

        # lista koja sadrži boje svih kvadrata jedne strane kocke
        stranica = []
        # za svih 9 kvadrata na stranici pravi se patch, prepoznaje se boja i dodaje u niz
        for (x, y) in pozicije:
            patch = frame[y:y + velicina, x:x + velicina]
            boja = frame.color_recognition
            # dodaje prepoznatu boju kvadrata na listu za jednu stranicu
            stranica.append(boja)
            # crta kvadrat na slici gde se detektuje boja
            cv.rectangle(frame, (x, y), (x + velicina, y + velicina), (255, 255, 255), 2)

        return stranica

    def record_face(self):
        # Funkcija za očitavanje svih stranica Rubikove kocke pomoću kamere

        # otvaranje video strima sa uredjaja
        cap = cv.VideoCapture(0)
        # cap je objekat koji omogućava čitanje frejmova (slika) sa kamere pomoću metode cap.read()
        stranice = []

        while len(stranice) < 6:
            # ret je boolean vrednost koja označava da li je frejm uspešno pročitan (True) ili nije (False)
            # frame je trenutni frejm (slika) sa kamere
            ret, frame = cap.read()
            if not ret:
                print("Greška u čitanju kamere!")
                break

        frame = cv.flip(frame, 1)
        stranica = self.face_detection
        cv.putText(frame, f"Stranica {len(stranice) + 1}: {stranica}", (10, 30), cv.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

        cv.imshow("Rubikova kocka", frame)

        key = cv.waitKey(1)
        if key == ord('s'):  # 's' za snimanje stranice
            stranice.append(stranica)
            print(f"Stranica {len(stranice)} snimljena: {stranica}")
        elif key == ord('q'): # 'q' za izlazak
            "break"

        # kada se završi sa korišćenjem kamere, obavezno je osloboditi resurse
        cap.release()
        cv.destroyAllWindows()
        return stranice

    # SOLVER

    def cube_string(self):

        dictionary = {
            "⬜": "B",
            "🟨": "F",
            "🟩": "D",
            "🟦": "U",
            "🟥": "R",
            "🟧": "L"
        }

        string = ''
        for i in range(3):
            for j in range(3):
                string += dictionary[self.face["Top"][i][j]]
        for k in range(3):
            for l in range(3):
                string += dictionary[self.face["Right"][k][l]]
        for a in range(3):
            for b in range(3):
                string += dictionary[self.face["Front"][a][b]]
        for m in range(3):
            for n in range(3):
                string += dictionary[self.face["Bottom"][m][n]]
        for c in range(3):
            for d in range(3):
                string += dictionary[self.face["Left"][c][d]]
        for e in range(3):
            for f in range(3):
                string += dictionary[self.face["Back"][e][f]]

        print(string)
        return string

    def solver(self, string):

        cubestring = string
        solution1 = sv.solve(cubestring, 19, 2)
        print(solution1) #provera

        p1 = solution1.replace(" ", "")
        print(p1) #provera
        length = len(p1)
        print(length) #provera
        p2 = p1[0:length-5]
        print(p2) #provera

        p21 = p2.replace("F", "")
        p211 = p21.replace("B", "")
        p212 = p211.replace("L", "")
        p213 = p212.replace("R", "")
        p214 = p213.replace("D", "")
        p215 = p214.replace("U", "")
        numbers = p215
        print(numbers) #provera
        p22 = p2.replace("1", "")
        p221 = p22.replace("2", "")
        p222 = p221.replace("3", "")
        letters = p222
        print(letters) #provera

        len_letters = len(letters)
        for i in range (len_letters):
            if letters[i] == 'U':
                if numbers[i] == '1':
                    kocka.rotate_top_clockwise()
                elif numbers[i] == '2':
                    kocka.rotate_top_clockwise()
                    kocka.rotate_top_clockwise()
                elif numbers[i] == '3':
                    kocka.rotate_top_clockwise()
                    kocka.rotate_top_clockwise()
                    kocka.rotate_top_clockwise()
            elif letters[i] == 'D':
                if numbers[i] == '1':
                    kocka.rotate_bottom_clockwise()
                elif numbers[i] == '2':
                    kocka.rotate_bottom_clockwise()
                    kocka.rotate_bottom_clockwise()
                elif numbers[i] == '3':
                    kocka.rotate_bottom_clockwise()
                    kocka.rotate_bottom_clockwise()
                    kocka.rotate_bottom_clockwise()
            elif letters[i] == 'L':
                if numbers[i] == '1':
                    kocka.rotate_left_clockwise()
                elif numbers[i] == '2':
                    kocka.rotate_left_clockwise()
                    kocka.rotate_left_clockwise()
                elif numbers[i] == '3':
                    kocka.rotate_left_clockwise()
                    kocka.rotate_left_clockwise()
                    kocka.rotate_left_clockwise()
            elif letters[i] == 'R':
                if numbers[i] == '1':
                    kocka.rotate_right_clockwise()
                elif numbers[i] == '2':
                    kocka.rotate_right_clockwise()
                    kocka.rotate_right_clockwise()
                elif numbers[i] == '3':
                    kocka.rotate_right_clockwise()
                    kocka.rotate_right_clockwise()
                    kocka.rotate_right_clockwise()
            elif letters[i] == 'F':
                if numbers[i] == '1':
                    kocka.rotate_front_clockwise()
                elif numbers[i] == '2':
                    kocka.rotate_front_clockwise()
                    kocka.rotate_front_clockwise()
                elif numbers[i] == '3':
                    kocka.rotate_front_clockwise()
                    kocka.rotate_front_clockwise()
                    kocka.rotate_front_clockwise()
            elif letters[i] == 'B':
                if numbers[i] == '1':
                    kocka.rotate_back_clockwise()
                elif numbers[i] == '2':
                    kocka.rotate_back_clockwise()
                    kocka.rotate_back_clockwise()
                elif numbers[i] == '3':
                    kocka.rotate_back_clockwise()
                    kocka.rotate_back_clockwise()
                    kocka.rotate_back_clockwise()

        kocka.draw_cube()

    def print_cube(self, face):
        content = f"---|{face}|---\n"
        for row in self.face[face]:
            content += f"\n|{row[0]} | {row[1]} | {row[2]} |\n"
        return content



kocka = Cube()

kocka.scramble(35)

#kocka.rotate_top_clockwise()       #slike 1-1 i 1-2
#kocka.rotate_bottom_clockwise()    #slike 2-1 i 2-2
#kocka.rotate_left_clockwise()      #slike 3-1 i 3-2
#kocka.rotate_right_clockwise()     #slike 4-1 i 4-2
#kocka.rotate_front_clockwise()     #slike 5-1 i 5-2
#kocka.rotate_back_clockwise()      #slike 6-1 i 6-2

#kocka.rotate_top_counter_clockwise()
#kocka.rotate_bottom_counter_clockwise()
#kocka.rotate_left_counter_clockwise()
#kocka.rotate_right_counter_clockwise()
#kocka.rotate_front_counter_clockwise()
#kocka.rotate_back_counter_clockwise()

kocka.draw_cube()
s = kocka.cube_string()
kocka.solver(s)

#print(kocka.print_cube("Top"))
#print(kocka.print_cube("Front"))
#print(kocka.print_cube("Left"))
#print(kocka.print_cube("Right"))
#print(kocka.print_cube("Back"))
#print(kocka.print_cube("Bottom"))


