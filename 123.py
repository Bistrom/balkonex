from balcony_project import BalconyProject
#pathlib - biblioteka odpowiedziala za  ścieżki
import pathlib
from pathlib import Path

dir_path = Path("C:/Users/aleks/Documents/Nowy folder/zz/zzz")
dir_path.mkdir(parents=True,exist_ok=True)
#parents - tworzy czalosc sciezki
#exist_ok - nie wywali bledu jesli folder juz istnieje