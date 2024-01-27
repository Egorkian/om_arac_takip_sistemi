from odoo import api, fields, models
from odoo import http
from odoo.http import request


class AraclarinBilgileri(models.Model):
    _name = "araclarin.bilgileri"
    _description = "Araba Uygulamasi"

    marka = fields.Char(string="Marka")
    model = fields.Integer(string="Model")
    renk = fields.Char(string="Renk")
    kapi_sayisi = fields.Integer(string="Kapi Sayisi")
    beygir = fields.Integer(string="Beygir")
    kilometre = fields.Integer(string="Km")
    fiyat = fields.Integer(string="Fiyat")


class BilgilerGoster(models.TransientModel):
    _name = "bilgiler.goster"
    _description = "Secim"

    @api.model
    def goster(self):
        araclarinbilgileri = self.env['araclarin.bilgileri'].search([])
        for bilgi in araclarinbilgileri:
            print(bilgi.marka)
            print(bilgi.model)
            print(bilgi.renk)
            print(bilgi.kapi_sayisi)
            print(bilgi.beygir)
            print(bilgi.kilometre)
            print(bilgi.fiyat)


