## XML Data Exporter
This is an application for parsing data about available products from **XML** file.

First, the application downloads the latest data in *ZIP* archive file, which is then extracted
and the data are parsed from the extracted **XML** file.

User can choose from three options, what he desires to return:

```
1 - Count of all products
2 - List of all products
3 - List of product with spare parts
4 - Download latest data
```

### Products structure
In the root of the **XML** file, product names are stored in *items* node.

Some products
have available spare parts in *parts* node where **categoryId** attribute have 
value of 1 (spare parts category).

### REST API endpoints
Downloading the latest data is using GET endpoint, for ease of testing. Correct method should
be **PUT**.

### Docker
The application runs in *Docker*.