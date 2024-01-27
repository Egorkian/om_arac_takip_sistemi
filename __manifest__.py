{
    'name':'Arac Uygulaması',
    'version':'1.0.0',
    'category':'Araba',
    'author':'Ege Akbaba',
    'sequence':-100,
    'summary':'Takip uygulama',
    'description':"""Arac Takip Sistemi""",
    'depends':[],
    'data':[
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/kayit_view.xml',
        'views/kayit_sofor_view.xml',
        'views/arac_biliger_sec.xml',
        'views/sonsecim_view.xml',
    ],
    'demo':[],
    'application':True,
    'auto_install':False,
    'license':'LGPL-3'
}