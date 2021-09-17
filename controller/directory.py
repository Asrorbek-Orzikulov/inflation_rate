from os import path, chdir, mkdir
from pathlib import Path


def main():
    home_path = Path.home()
    chdir(home_path)
    if path.isdir('Desktop'):
        chdir('Desktop')
    else:
        mkdir('Desktop')
        chdir('Desktop')

    new_folder = 'Inflation_Rate'
    if path.isdir(new_folder):
        chdir(new_folder)
    else:
        mkdir(new_folder)
        chdir(new_folder)
