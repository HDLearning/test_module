# -*- coding: utf-8 -*-
from odoo import models, api
import pandas as pd

class XLSXGenerator(models.Model):
    _name = 'xlsx.generator'
    _description = 'XLSX File Generator'

    @api.model
    def generate_xlsx_file(self):
        file_path = '/tmp/test.xlsx'  # Adjust the path if needed
        
        data = {
            'Name': ['Alice', 'Bob', 'Charlie'],
            'Age': [25, 30, 35],
            'City': ['New York', 'Los Angeles', 'Chicago']
        }
        
        df = pd.DataFrame(data)
        df.to_excel(file_path, index=False)
        
        return file_path

    @api.model
    def _install_hook(self):
        self.generate_xlsx_file()
