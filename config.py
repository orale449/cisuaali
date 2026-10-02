# config.py
import os

# Määritetään kohdekansiot eri tiedostotyypeille
DIRECTORY_MAPPING = {
    'Kuvat': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg'],
    'Dokumentit': ['.pdf', '.docx', '.doc', '.txt', '.xlsx', '.pptx', '.odt'],
    'Asennustiedostot': ['.exe', '.msi', '.dmg', '.pkg'],
    'Paketit': ['.zip', '.rar', '.7z', '.tar', '.gz'],
    'Videot_ja_Aani': ['.mp4', '.mkv', '.mp3', '.wav', '.mov']
}
