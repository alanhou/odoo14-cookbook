{
    'name': "My library",
    'summary': "轻松管理图书",
    'description': """
Manage Library
==============
Description related to library.
     """,
    'author': "Alan Hou",
    'website': "https://alanhou.org",
    'category': 'Library',
    'version': '14.0.1',
    'depends': ['base_setup', 'contacts'],
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        "views/library_book.xml",
        'views/library_book_categ.xml',
        'views/library_book_rent.xml',
        'data/library_stage.xml',
        'reports/book_rent_report.xml',
        'reports/book_rent_templates.xml',
    ],
    # 'demo': ['demo.xml'],
}
