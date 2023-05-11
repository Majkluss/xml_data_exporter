"""Data exporter application main file"""
from os import remove
from os.path import exists
from xml.etree.ElementTree import parse
import zipfile
import wget
from flask import Flask, render_template

app = Flask(__name__)

ZIP_FILE_URL = "https://www.retailys.cz/wp-content/uploads/astra_export_xml.zip"
ZIP_FILE = "astra_export_xml.zip"
XML_FILE = "export_full.xml"


@app.route("/")
def index():
    """Index page with available endpoints"""
    return """
    <a href="/products/1">Počet produktů</a><br/>
    <a href="/products/2">Seznam produktů</a><br/>
    <a href="/products/3">Seznam produktů s náhradními díly</a><br/>
    <a href="/products/4">Aktualizovat data</a><br/>
    """


@app.route("/products/1")
def products_count():
    """Return count of all products"""
    return f"Počet produktů: {len(get_xml()[0])}"


@app.route("/products/2")
def products_list():
    """Return list of all products"""
    return render_template("products.html", products=get_products(get_xml()))


@app.route("/products/3")
def products_with_parts_count():
    """Return list of products with spare parts"""
    return render_template("products_with_parts.html",
                           products=get_products(get_xml(), with_parts_only=True))


@app.route("/products/4")
def update_products_data():
    """Update products with spare parts"""
    download_latest_data()
    return "Data aktualizována"


def download_latest_data():
    """Download ZIP file with latest data and replace current file"""
    if exists(ZIP_FILE):
        remove(ZIP_FILE)
    wget.download(ZIP_FILE_URL)


def get_xml():
    """Read data from the ZIP archive file"""
    if not exists(ZIP_FILE):
        download_latest_data()

    # Open ZIP archive file
    with zipfile.ZipFile(f"{ZIP_FILE}", "r") as archive:

        # Open XML file from ZIP archive
        with archive.open(XML_FILE) as xml_file:
            xml_file = parse(xml_file)
    return xml_file.getroot()


def get_products(xml_data, with_parts_only=False):
    """Return list of all products names or list of products with spare parts"""
    items = []
    # If True, select products with spare parts only
    if with_parts_only:
        # Find the node items
        for element in xml_data.find("items"):
            for child in element.findall("parts"):
                for parts in child:
                    # ID of the spare parts category
                    if parts.attrib["categoryId"] == "1":
                        items.append({
                            "name": element.attrib["name"],
                            "parts": [part.attrib for part in parts]
                        })
    else:
        items = [element.attrib["name"] for element in xml_data.find("items")]

    return items


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
