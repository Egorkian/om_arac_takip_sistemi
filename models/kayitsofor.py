from odoo import api, fields, models


class KayitSofor(models.Model):
    _name = "kayitsofor.bilgisi"
    _description = "Sofor Kayit"

    isim = fields.Char(string="Isim")
    soyad = fields.Char(string="Soyad")
