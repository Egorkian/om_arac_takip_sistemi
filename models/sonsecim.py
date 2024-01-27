from odoo import api,fields,models

class SonSecim(models.Model):
    _name ="sonsecim"
    _description ="Arac Secim Son"

    arac_id = fields.Many2one('araclarin.bilgileri',string="Arac")
    sofor_id = fields.Many2one('kayitsofor.bilgisi',string="Sofor")
    zaman_time = fields.Datetime(string='Baslangıc')
    tarih_date = fields.Date(string='Bitis')