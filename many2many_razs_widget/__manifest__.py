{
    "name": "Many2many Razs Tags Widget",
    "version": "16.0.1.0.0",
    "category": "Technical",
    "summary": "Configurable many2many tags widget for all view types",
    "description": """
Many2many Razs Tags Widget

This module provides a custom many2many widget that displays related records
as clean and modern tags across all Odoo view types.

Unlike the standard many2many tag widget, this widget allows you to configure
which fields of the related record are displayed inside each tag, making it
possible to show additional context such as email, phone, internal reference,
or any other relevant field.

The widget is lightweight, non-intrusive, and fully compatible with Odoo’s
standard many2many behavior, while significantly improving readability and
usability for relational fields.

Demo:
https://drive.google.com/file/d/1lZom6mxbyCVIQvfjezfESfoTeqg-VYlo/view?usp=sharing
    """,
    "author": "Ricardo Zermeño",
    "website": "https://razs.vercel.app/",
    "license": "LGPL-3",
    "depends": ["web"],
    "assets": {
        "web.assets_backend": [
            "many2many_razs_widget/static/src/js/many2many_razs_tags.js",
            "many2many_razs_widget/static/src/xml/many2many_razs_tags.xml",
            "many2many_razs_widget/static/src/scss/many2many_razs_tags.scss",
        ],
    },
    "installable": True,
    "application": False,
}
