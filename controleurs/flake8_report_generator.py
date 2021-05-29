from os import system as sys
from time import sleep as sl


def report():
    sys("flake8 --max-line-length=119 --format=html --htmldir=flake-report \
        vues/* controleurs/* modeles/* TournoisSuisse.py")
    sl(2)
    sys("open flake-report/index.html")
