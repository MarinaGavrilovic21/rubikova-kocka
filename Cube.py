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

    def rotate_bottom_clockwise(self):
        self.rotate_face_clockwise("Bottom")
        temp = self.face["Front"][2]
        self.face["Front"][2] = self.face["Left"][2]
        self.face["Left"][2] = self.face["Back"][2]
        self.face["Back"][2] = self.face["Right"][2]
        self.face["Right"][2] = temp

    def rotate_left_clockwise(self):
        self.rotate_face_clockwise("Left")
        temp_col = [self.face["Top"][i][0] for i in range(3)]
        for i in range(3):
            self.face["Top"][i][0] = self.face["Back"][2 - i][2]
            self.face["Back"][2 - i][2] = self.face["Bottom"][i][0]
            self.face["Bottom"][i][0] = self.face["Front"][i][0]
            self.face["Front"][i][0] = temp_col[i]

    def rotate_right_clockwise(self):
        self.rotate_face_clockwise("Right")
        temp_col = [self.face["Top"][i][2] for i in range(3)]
        for i in range(3):
            self.face["Top"][i][2] = self.face["Front"][i][2]
            self.face["Front"][i][2] = self.face["Bottom"][i][2]
            self.face["Bottom"][i][2] = self.face["Back"][2 - i][0]
            self.face["Back"][2 - i][0] = temp_col[i]

    def rotate_front_clockwise(self):
        self.rotate_face_clockwise("Front")
        temp = [self.face["Top"][2][i] for i in range(3)]
        for i in range(3):
            self.face["Top"][2][i] = self.face["Left"][2 - i][2]
            self.face["Left"][i][2] = self.face["Bottom"][0][i]
            self.face["Bottom"][0][i] = self.face["Right"][2 - i][0]
            self.face["Right"][i][0] = temp[i]

    def rotate_back_clockwise(self):
        self.rotate_face_clockwise("Back")
        temp = [self.face["Top"][0][i] for i in range(3)]
        for i in range(3):
            self.face["Top"][0][i] = self.face["Right"][i][2]
            self.face["Right"][i][2] = self.face["Bottom"][2 - i][i]
            self.face["Bottom"][2][i] = self.face["Left"][i][0]
            self.face["Left"][i][0] = temp[2 - i]


kocka = Cube()
#print(kocka.face) probavanje
#kocka.rotate_top_clockwise()
#print(kocka.face)

