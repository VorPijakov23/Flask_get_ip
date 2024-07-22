"""Скрипт для сокращения URL с помощью Yandex click"""
from pyshorteners import Shortener

print(Shortener().clckru.short(input("Write url: ")))
