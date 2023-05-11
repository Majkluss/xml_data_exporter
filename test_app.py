"""Tests for the XML data exporter application"""
from app import app


class TestsProducts:
    """Test class for products endpoints"""

    def test_get_products_count(self):
        """Get count of all products"""
        with app.test_client() as client:
            response = client.get('/products/1')
            assert response.status_code == 200
            assert len(response.text) > 0

    def test_get_all_products(self):
        """Get list of all products"""
        with app.test_client() as client:
            response = client.get('/products/2')
            assert response.status_code == 200
            assert len(response.text) > 0

    def test_get_products_with_parts(self):
        """Get list of products with spare parts"""
        with app.test_client() as client:
            response = client.get('/products/3')
            assert response.status_code == 200
            assert len(response.text) > 0
