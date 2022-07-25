import numpy as np

import cv2

# This is a sample Python script.
user_imput={
    "balcony_x":100,
    "balcony_y":50,
    "balcony_z":1500,
    "balcony_transparent":False,
    #przy orientation wywala mi błąd. dlatego, że po dwukropku jest string??
    "balcon_orientation":"east",
    "balcony_hight":5000,
    "plant_climber":False,
    "balcony_pot":False
    }

pots_imput={
    "pot_wide":15,
    "pot_lenght":20
}

class BalconyProject:

  def __init__(self):
    self.balcony_x=None
    self.balcony_y=None
    self.balcony_z=None
    self.balcony_transparent=None
    self.balcony_hight=None
    self.plant_climber=None
    self.balcony_pot=None

  def create_project(self,user_imput):
    self.unpack_user_imput(user_imput)

  def unpack_user_imput(self,user_imput):
    self.balcony_x=user_imput["balcony_x"]
    self.balcony_y=user_imput["balcony_y"]
    self.balcony_z=user_imput["balcony_z"]
    self.balcony_transparent=user_imput["balcony_transparent"]
    self.balcony_hight=user_imput["balcony_hight"]
    self.plant_climber=user_imput["plant_climber"]
    self.balcony_pot=user_imput["balcony_pot"]


class CreatePots:

  def __init__(self):
    self.pot_wide=None
    self.pot_lenght=None

  def create_pot(self,pots_imput):
    self.unpack_pots_imput(pots_imput)

  def unpack_pots_imput(self,pots_imput):
    self.pot_wide=pots_imput["pot_wide"]
    self.pot_lenght=pots_imput["pot_lenght"]


balcon_project=BalconyProject()
balcon_project.create_project(user_imput)
balcon_project.balcony_x
balcon_project.balcony_z

pot=CreatePots()
pot.create_pot(pots_imput)
pot.pot_lenght
pot.pot_wide

import cv2


image_wide = int(balcon_project.balcony_x + (balcon_project.balcony_x * 0.8))
draw_starting_point = int(balcon_project.balcony_x - (balcon_project.balcony_x * 0.25))
image_lenght = int(balcon_project.balcony_y + (balcon_project.balcony_y * 2))
image_lenght_1 = int(balcon_project.balcony_y - (balcon_project.balcony_y * 1))
blank_image = np.zeros((image_wide, balcon_project.balcony_y + image_lenght, 3), np.uint8)

(blank_image)
blank_image = blank_image + 255

cv2.rectangle(blank_image, (draw_starting_point, balcon_project.balcony_y * 2),
              (draw_starting_point + balcon_project.balcony_x, balcon_project.balcony_y * 3), (0, 0, 255), 2)
cv2.line(blank_image, (0, balcon_project.balcony_y * 3), (balcon_project.balcony_x * 3, balcon_project.balcony_y * 3),
         (0, 0, 0), 2)

number_of_pots_on_sides = balcon_project.balcony_y // pot.pot_lenght
space_beetween_pots_on_slides = int(((balcon_project.balcony_y % pot.pot_lenght)) / number_of_pots_on_sides)
###WPIERDOL FORY W DEF - aby rysowanie doniczek wynikalo z funkcji
for i in range(number_of_pots_on_sides):
    i = i + 1
    x1 = draw_starting_point
    y1 = balcon_project.balcony_y * 3 - i * pot.pot_lenght - i * space_beetween_pots_on_slides
    x2 = draw_starting_point + pot.pot_wide
    y2 = (balcon_project.balcony_y * 3 + pot.pot_lenght) - i * pot.pot_lenght - i * space_beetween_pots_on_slides

    x11 = x1 + balcon_project.balcony_x
    x22 = x11 - pot.pot_wide

    cv2.rectangle(blank_image, (x1, y1), (x2, y2), (0, 0, 0), 1)
    cv2.rectangle(blank_image, (x11, y1), (x22, y2), (0, 0, 0), 1)

    # przerwa między doniczkami to wynika dzielenia pozostałej długości (to co pozostaje po tym jak następna doniczka nie ma miejsca)

number_of_pots_on_main_side = (balcon_project.balcony_x - (2 * pot.pot_wide)) // pot.pot_lenght
space_beetween_pots_on_main_side = int(
    ((balcon_project.balcony_x - (2 * pot.pot_wide)) % pot.pot_lenght) / number_of_pots_on_main_side)
# s#liczba doniczek na głownej ścinaie razy długość doniczki - potem dodac 2 razy szerokość doniczki
space_beetween_pots = int((balcon_project.balcony_x % pot.pot_lenght) / number_of_pots_on_main_side)

for i in range(number_of_pots_on_main_side):
    i = i + 1

    x1 = balcon_project.balcony_x - (2 * pot.pot_wide) + i * pot.pot_lenght + i * space_beetween_pots_on_main_side
    y1 = balcon_project.balcony_y * 2
    x2 = x1 + pot.pot_lenght
    y2 = y1 + pot.pot_wide

    cv2.rectangle(blank_image, (x1, y1), (x2, y2), (0, 0, 0), 1)


cv2.imwrite("dupa.jpg",blank_image)




# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


#def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    #print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
   # blank_image = np.zeros((200, 200, 3), np.uint8)
   # cv2.imwrite("dupa.jpg",blank_image) #pierwsze to nazwa którą ma mieć zdjęcie a drugie to samo zdjęcie

# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
   # print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
