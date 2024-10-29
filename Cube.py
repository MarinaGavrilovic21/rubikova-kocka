from array import array

import random

class Cube:
    def __init__(self):
        self.face = {
            "Top": [
                ["⬜", "⬜", "⬜"],
                ["⬜", "⬜", "⬜"],
                ["⬜", "⬜", "⬜"]
            ],
            "Bottom": [
                ["🟨", "🟨", "🟨"],
                ["🟨", "🟨", "🟨"],
                ["🟨", "🟨", "🟨"]
            ],
            "Left": [
                ["🟩", "🟩", "🟩"],
                ["🟩", "🟩", "🟩"],
                ["🟩", "🟩", "🟩"]
            ],
            "Right": [
                ["🟦", "🟦", "🟦"],
                ["🟦", "🟦", "🟦"],
                ["🟦", "🟦", "🟦"]
            ],
            "Front": [
                ["🟥", "🟥", "🟥"],
                ["🟥", "🟥", "🟥"],
                ["🟥", "🟥", "🟥"]
            ],
            "Back": [
                ["🟧", "🟧", "🟧"],
                ["🟧", "🟧", "🟧"],
                ["🟧", "🟧", "🟧"]
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

    #def draw_cube(self):

    def print_cube(self, face):
        content = f"---|{face}|---\n"
        for row in self.face[face]:
            content += f"\n|{row[0]} | {row[1]} | {row[2]} |\n"
        return content



kocka = Cube()

kocka.scramble(25)

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


print(kocka.print_cube("Top"))
print(kocka.print_cube("Front"))
print(kocka.print_cube("Left"))
print(kocka.print_cube("Right"))
print(kocka.print_cube("Back"))
print(kocka.print_cube("Bottom"))


