#!/usr/bin/env python

import unittest
from acme import Product
from acme import BoxingGlove
from acme_report import generate_products


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)
        
    def test_default_product_weight(self):
        """Test default product weight being 20."""
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)
        
    def test_default_product_flam(self):
        """Test default product flammability being .5."""
        prod = Product('Test Product')
        self.assertEqual(prod.flammability, .5)        
 
    def test_stealability(self):
        """Test product stealability."""
        glove = BoxingGlove('Test Product', 10, 20, .5)
        self.assertEqual(glove.explode, '...boom!')   
                    
    def test_punchability(self):
        """Test product punchability."""
        glove = BoxingGlove('Test Product', 10, 20, .5)
        self.assertEqual(glove.punch, 'OUCH!')  
        
    def test_explode(self):
        """Test product punchability."""
        glove = BoxingGlove('Test Product', 10, 20, .5)
        self.assertEqual(glove.explode, "...it's a glove")         

if __name__ == '__main__':
    unittest.main()