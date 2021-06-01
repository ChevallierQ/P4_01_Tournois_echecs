from os import system as sys
from time import sleep as sl


def report():
    sys("flake8 --max-line-length=119 --format=html --htmldir=flake8_rapport \
        vues/* controleurs/* modeles/* TournoisSuisse.py")
    sl(2)
    sys("open flake8_rapport/index.html")
