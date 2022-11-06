from shutil import copy2
import uuid
from pathlib import Path

import numpy as np
import cv2

class BalconyProject:
    PLANT_GUIDE_DIR_PATH=Path(__file__).parent.joinpath("guide_plant_database")
    def __init__(self, database_path=None):  # <--TO SĄ ARGUMENTY
        if not database_path:
            self.database_path= Path(__file__).parent.joinpath("database")
            self.database_path.mkdir(parents=True,exist_ok=True)

        self.balcony_x = None
        self.balcony_y = None
        self.balcony_z = None
        self.balcony_transparent = None
        self.balcony_hight = None
        self.plant_climber = None
        self.balcony_pot = None

    def create_project(self, user_imput):   # <--argumenty
        self.unpack_user_imput(user_imput)
        user_dir_path = self.create_user_dir()
        project_drawing = self.draw_balcony() #TODO po projec_drowning daj przecinek i liczbe doniczek z rysowania
        self.save_balkon_picture(user_dir_path, project_drawing)  #<-- WYWOŁYWANIE METODY
        # random choise for plant and schem of plants
        pot_number=12
        self.create_pot_arrangement(pot_number)

        # rysowanie legendy
        # kopiowanie plikow
        # copy pdf
        # zip
        # return path to zip file

    def unpack_user_imput(self, user_imput):
        self.balcony_x = user_imput["balcony_x"]
        self.balcony_y = user_imput["balcony_y"]
        self.balcony_z = user_imput["balcony_z"]
        self.balcony_transparent = user_imput["balcony_transparent"]
        self.balcony_hight = user_imput["balcony_hight"]
        self.plant_climber = user_imput["plant_climber"]
        self.balcony_pot = user_imput["balcony_pot"]

    def create_user_dir(self):
            user_dir_path = self.database_path.joinpath(user_imput["user_id"])
            user_dir_path.mkdir(parents=True, exist_ok=True)
            return user_dir_path

    def draw_balcony(self):
        # TODO napisanie numerów doniczki podczas rysowania doniczek (index doniczek/roslin)
        image_wide = int(self.balcony_x + (self.balcony_x * 0.8))
        draw_starting_point = int(self.balcony_x - (self.balcony_x * 0.25))
        image_lenght = int(self.balcony_y + (self.balcony_y * 2))
        blank_image = np.zeros((image_wide, self.balcony_y + image_lenght, 3), np.uint8)
        blank_image = blank_image + 255
        # TODO liczba doniczek na balkonie - dodac i zwrocic
        cv2.rectangle(
            blank_image,
            (draw_starting_point, self.balcony_y * 2),
            (draw_starting_point + self.balcony_x, self.balcony_y * 3),
            (0, 0, 255),
            2,
        )
        cv2.line(
            blank_image,
            (0, self.balcony_y * 3),
            (self.balcony_x * 3, self.balcony_y * 3),
            (0, 0, 0),
            2,
        )

        number_of_pots_on_sides = self.balcony_y // 20
        space_beetween_pots_on_slides = int(
            ((self.balcony_y % 20)) / number_of_pots_on_sides
        )

        for i in range(number_of_pots_on_sides):
            i = i + 1
            x1 = draw_starting_point
            y1 = (
                    balcon_project.balcony_y * 3
                    - i * 20
                    - i * space_beetween_pots_on_slides
            )
            x2 = draw_starting_point + 15
            y2 = (
                    (balcon_project.balcony_y * 3 + 20)
                    - i * 20
                    - i * space_beetween_pots_on_slides
            )

            x11 = x1 + balcon_project.balcony_x
            x22 = x11 - 15

            cv2.rectangle(blank_image, (x1, y1), (x2, y2), (0, 0, 0), 1)
            cv2.rectangle(blank_image, (x11, y1), (x22, y2), (0, 0, 0), 1)

            # przerwa między doniczkami to wynika dzielenia pozostałej długości (to co pozostaje po tym jak następna doniczka nie ma miejsca)

        number_of_pots_on_main_side = (
                                              balcon_project.balcony_x - (2 * 15)
                                      ) // 20
        space_beetween_pots_on_main_side = int(
            ((balcon_project.balcony_x - (2 * 15)) % 20)
            / number_of_pots_on_main_side
        )
        # s#liczba doniczek na głownej ścinaie razy długość doniczki - potem dodac 2 razy szerokość doniczki
        space_beetween_pots = int(
            (balcon_project.balcony_x % 20) / number_of_pots_on_main_side
        )

        for i in range(number_of_pots_on_main_side):
            i = i + 1

            # x1=draw_starting_point-(2*pot.pot_wide)+i*pot.pot_lenght+i*space_beetween_pots_on_main_side
            x1 = (
                         draw_starting_point
                         + i * 20
                         + i * space_beetween_pots_on_main_side
                 ) - int(0.4 * 20)
            y1 = balcon_project.balcony_y * 2
            x2 = x1 + 20
            y2 = y1 + 15

            cv2.rectangle(blank_image, (x1, y1), (x2, y2), (0, 0, 0), 1)

        return blank_image  # TODO dodac liczbe doniczek na balkonie - tutaj zwrócicć(po przecinku)

    # def copy_pdf_to_user_dir(self, user_dir_path,):
    #     copy2()

    def save_balkon_picture(self, user_dir_path, project_drawing):  # <--metoda
            project_drawing_path = user_dir_path.joinpath("projekt.jpg")
            cv2.imwrite(project_drawing_path.as_posix(), project_drawing)  # as_posix - shlashe nie maja juz znaczenia

    def create_pot_arrangement(self,pot_number):
       # self.

      #  plants= ["Mak","Pomidor", "Tulipan" ]

        #TODO funkcja ma zwracać słownik gdzie kluczem jest indeks doniczki (trzeba zaindeksować doniczki) a wartością kwiat
        #TODO indeks doniczek/roslin (drugie rysowanie)
        # czy odwoluje się do guide_plant_database (stąd ma brać)



if __name__ == "__main__":
    # This is a sample Python script.
    user_imput = {
        "user_id": str(uuid.uuid4()),
        "balcony_x": 100,
        "balcony_y": 50,
        "balcony_z": 1500,
        "balcony_transparent": False,
        # przy orientation wywala mi błąd. dlatego, że po dwukropku jest string??
        "balcon_orientation": "east",
        "balcony_hight": 5000,
        "plant_climber": False,
        "balcony_pot": False,
    }
    pots_imput = {"pot_wide": 15, "pot_lenght": 20}

    balcon_project = BalconyProject()
    balcon_project.create_project(user_imput)

