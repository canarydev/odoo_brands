# -*- coding: utf-8 -*-

from odoo import models, fields, api

class CustomBrand(models.Model):
    _inherit = 'product.template'
    brand = fields.Selection([("N", "Nike"), ("A", "Adidas")], string="Brand")
