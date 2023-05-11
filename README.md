## XML Data Exporter
This is a Flask application for parsing data about available products from **XML** file.

First, the application downloads the latest data in *ZIP* archive file, which is then extracted
and the data are parsed from the extracted **XML** file. If the *ZIP* file is already available, the application
will use the data from it. Latest *ZIP* file can be manually updated using an endpoint.

User can choose from four options, what he desires to return:

```
1 - Count of all products
2 - List of all products
3 - List of product with spare parts
4 - Download latest data
```

### Products structure
Product names are stored in the *items* node in the root of the **XML** file.
Some products have also available spare parts in *parts* node where **categoryId** attribute have 
value of 1 (spare parts category).

### REST API endpoints
The application offers basic REST API for accessing the data. Index page has a signpost to 
all available endpoints.

The endpoints are listed below (all endpoints are using the HTTP GET method):
```
/ - Index page with a signpost to all endpoints
/products/1 - Returns count of all products
/products/2 - Returns list of all products
/products/3 - Returns list of products with spare parts
/products/4 - Downloads latest data
```

Downloading the latest data is made using GET endpoint, for ease of testing. Correct HTTP method should
be **PUT**.

### Docker
The application can be started using *Docker* command `docker-compose up`.

### Tests
The application has unit tests for all three data endpoints.
Tests can be run using pytest command `pytest test_app.py`.
