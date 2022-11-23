from shutil import copy2
import uuid
from pathlib import Path

import numpy as np
import cv2


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
        "pot_number": 12,
        "pot_lengt":20,
        "pot_wide":10
    }
    plants = {"mak", "tulipan", "truskawka"}
#
# #         user_dir_path = self.create_user_dir(), stworzenie folderu o nazwie ip urzytkownika w folderze bazy danych
#
def create_user_dir(user_imput, database_path):
    database_path=Path(database_path)
    user_dir_path=database_path.joinpath(user_imput["user_id"])
    user_dir_path.mkdir(parents=True, exist_ok=True)
    user_imput["user_dir_path"]=user_dir_path # dopsuje ścieżkę do user imput automatycznie
    return user_imput
#
# #         project_drawing = self.draw_balcony()   #TODO po projec_drowning daj przecinek i liczbe doniczek z rysowania
#
user_pots_number=12

pot_lenght = 20
pot_wide = 10

def pot_ammount_on_sides():
    user_imput["balcony_x"] // user_imput["pot_lengt"]

def pot_ammount_on_main_side():
    (user_imput["balcony_y"] - (2 * user_imput["pot_wide"])) // user_imput["pot_lengt"]

def space_beetween_pots_on_slides()
    int(((user_imput["balcony_x"] % pot_lenght)) / pot_ammount_on_sides())

def space_beetween_pots_on_main_side():
    int(((user_imput["balcony_y"] - (2 * pot_wide)) % pot_lenght) / pot_ammount_on_main_side())

def total_pot_ammount():
    space_beetween_pots_on_slides() + pot_ammount_on_main_side()

def pot_arragment (pots_number):
    plants = ["mak", "pomidor", "tulipan"]
    return(np.random.choice(plants, size=pots_number))
 #teraz mi wypirntuje liste 12 losowych roślin teraz trzeba tą listę jakby załadować do rysowania (doniczka nr. 1 to pozycja nr. 2 itd)

print (pot_arragment(pots_number=user_pots_number))
i = pot_arragment(pots_number=user_pots_number)
print(i)

# user_wide_imput = 100
# user_hight_imput = 50


def drawning_balcon ():

    image_wide = int(user_imput["balcony_y"] + (user_imput["balcony_x"] * 0.8))
    draw_starting_point = int(user_imput["balcony_y"] - (user_imput["balcony_y"] * 0.25))
    image_lenght = int(user_imput["balcony_x"] + (user_imput["balcony_x"] * 2))
    #number_of_pots_on_sides = user_imput["balcony_x"]// pot_lenght
   # space_beetween_pots_on_slides = int(((user_imput["balcony_x"] % pot_lenght)) / number_of_pots_on_sides) #TODO DZIELENIE PRZEZ ZERO!!!! SZYBKO DO NAPRAWY
   # number_of_pots_on_main_side = (user_imput["balcony_y"] - (2 * pot_wide)) // pot_lenght
   # space_beetween_pots_on_main_side =int(
   #     ((user_imput["balcony_y"] - (2 * pot_wide)) % pot_lenght) / number_of_pots_on_main_side)
   # space_beetween_pots = int((user_imput["balcony_x"] % pot_lenght) / number_of_pots_on_main_side)

    blank_image = np.zeros((image_wide, user_imput["balcony_x"] + image_lenght, 3), np.uint8)
    blank_image = blank_image + 255

    cv2.rectangle(blank_image, (draw_starting_point, user_imput["balcony_x"] * 2),
                  (draw_starting_point + user_imput["balcony_y"], user_imput["balcony_x"]* 3), (0, 0, 255), 2)
    cv2.line(blank_image, (0, user_imput["balcony_x"] * 3),
             (user_imput["balcony_y"] * 3, user_imput["balcony_x"] * 3), (0, 0, 0), 2)



    print("dupa")


    for i in range(pot_ammount_on_main_side()):

        i = i + 1
        x1 = draw_starting_point
        y1 = user_imput["balcony_y"] * 3 - i * pot_lenght - i * space_beetween_pots_on_slides
        x2 = draw_starting_point + pot_wide
        y2 = (user_imput["balcony_y"] * 3 + pot_lenght) - i * pot_lenght - i * space_beetween_pots_on_slides

        x11 = x1 + user_imput["balcony_x"]
        x22 = x11 - pot_wide


        cv2.rectangle(blank_image, (x1, y1), (x2, y2), (0, 0, 0), 2)
        cv2.rectangle(blank_image, (x11, y1), (x22, y2), (0, 0, 0), 2)

        xx1 = (draw_starting_point + i * pot_lenght + i * space_beetween_pots_on_main_side) - int(
            0.4 * pot_lenght)
        yy1 = user_imput["balcony_x"] * 2
        xx2 = x1 + pot_lenght
        yy2 = y1 + pot_wide
        cv2.rectangle(blank_image, (xx1, yy1), (xx2, yy2), (0, 0, 0), 1)

        cv2.imwrite("dupaaa.jpg", blank_image)
        print("dupa")



def save_balkon_picture (user_dir_path,project_drawing):
    projec_draw_path=user_dir_path.joinpath("dupa.jpg")
    cv2.imwrite(project_drawing_path.as_posix(), project_drawing)

# def load_balkon_picture
#
# def draw_legend
# #
# def save_project_picture
#
# def copy_platns_pdf():
#     copy2
#     shutil.copyfile(pdf_deposytory_bla, dest_file, *, follow_symlinks=True)
# # def zip_files
# #
# def zip_path_file

       #
       # # self.save_balkon_picture(user_dir_path, project_drawing)  #<-- WYWOŁYWANIE METODY
       #  # random choise for plant and schem of plants
       #  pot_number=12
       #  self.create_pot_arrangement(pot_number)


        # rysowanie legendy
        # kopiowanie plikow
        # copy pdf
        # zip
        # return path to zip file


    drawning_balcon(user_imput["balcony_x"], user_imput["balcony_y"])
