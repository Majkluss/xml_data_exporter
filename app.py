"""Data exporter application main file"""
from os import remove
from os.path import exists
import zipfile
import wget
from xml.etree.ElementTree import parse

ZIP_FILE_URL = "https://www.retailys.cz/wp-content/uploads/astra_export_xml.zip"
ZIP_FILE = "astra_export_xml.zip"
XML_FILE = "export_full.xml"


def download_latest_data():
    """Download ZIP file with latest data and replace current file"""
    if exists(ZIP_FILE):
        remove(ZIP_FILE)
    wget.download(ZIP_FILE_URL)


def get_xml():
    """Read data from the ZIP archive file"""
    if not exists(ZIP_FILE):
        download_latest_data()
    archive = zipfile.ZipFile(f"{ZIP_FILE}", "r")
    xml_file = parse(archive.open(XML_FILE))
    return xml_file.getroot()


def get_products(xml_data, with_parts_only=False):
    """Return list of all products names or list of products with spare parts"""
    items = []

    # Find the node items
    for element in xml_data.find("items"):

        # If True, select products with spare parts only
        if with_parts_only:
            for child in element.findall("parts"):
                for parts in child:
                    # ID of the spare parts category
                    if parts.attrib["categoryId"] == "1":
                        print(f'{element.attrib["name"]}\nNáhradní díly:')
                        for part in parts:
                            print(part.attrib)
                        print("\n")
        else:
            print(element.attrib["name"])


def select_operation():
    """Gives operation choices to user and handle the response"""
    res = input("Vyberte výpis: \n"
                "1 - Počet produktů\n"
                "2 - Seznam všech produktů\n"
                "3 - Seznam produktů s náhradními díly\n"
                "4 - Stáhnout aktuální data\n")

    if res == "1":
        print(f"Počet produktů: {len(get_xml()[0])}")
    elif res == "2":
        get_products(get_xml())
    elif res == "3":
        get_products(get_xml(), with_parts_only=True)
    elif res == "4":
        download_latest_data()
    else:
        print("Neplatný výběr")

#TODO endpointy pro každý z výběrů (4 by neměl být GET, ale PUT, zmínit)


select_operation()
