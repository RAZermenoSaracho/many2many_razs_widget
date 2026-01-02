{
    "name": "Many2many Razs Tags Widget",
    "version": "16.0.1.0.0",
    "category": "Technical",
    "summary": "Custom many2many tags widget for all view types",
    "description": """
Many2many Razs Tags Widget

This module adds a custom many2many widget that displays records as clean,
modern tags across all Odoo view types, improving readability and usability.

The widget is lightweight, non-intrusive, and fully compatible with Odoo’s
standard many2many behavior.

Demo:
https://drive.google.com/file/d/1lZom6mxbyCVIQvfjezfESfoTeqg-VYlo/view?usp=sharing
    """,
    "author": "Ricardo Zermeño",
    "website": "https://github.com/razs",
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
