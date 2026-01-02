# Many2many Razs Tags Widget

A custom **Many2many widget for Odoo** that renders many2many fields as clean, modern, and responsive **tags**, improving usability and visual clarity across **all view types**.

The widget is lightweight, easy to integrate, and fully aligned with Odoo’s native UX.

---

## 🚀 Features

- 📌 Displays many2many fields as tag-style elements
- 🧩 Works on **all Odoo view types** (form, tree, kanban, etc.)
- 🎨 Clean and modern UI using SCSS
- ⚡ Lightweight JavaScript implementation
- 🔌 Easy integration in any view
- 🖱️ Native add/remove many2many interactions
- 🧠 Non-intrusive and fully compatible with standard Odoo behavior

---

## 🎥 Demo

Watch the widget in action:  
https://drive.google.com/file/d/1lZom6mxbyCVIQvfjezfESfoTeqg-VYlo/view?usp=sharing

---

## 🧱 Module Structure

```
many2many_razs_widget/
├── __init__.py
├── __manifest__.py
└── static/src
    ├── js
    │   └── many2many_razs_tags.js
    ├── scss
    │   └── many2many_razs_tags.scss
    └── xml
        └── many2many_razs_tags.xml
```

---

## 📦 Installation

1. Copy the `many2many_razs_widget` folder into your Odoo `addons` directory.
2. Restart the Odoo server.
3. Enable **Developer Mode**.
4. Go to **Apps** and install **Many2many Razs Tags Widget**.

---

## 🛠️ Usage

Use the widget on any many2many field in any view:

```xml
<field name="tag_ids" widget="many2many_razs_tags"/>
```

The field will automatically render as styled tags.

---

## 🎯 Use Cases

- Tags
- Categories
- Skills
- Labels
- Any many2many relationship that benefits from a compact visual display

---

## 🧩 Compatibility

- Odoo 16+
- Community & Enterprise editions
- No external dependencies

---

## 🎨 Styling

A dedicated SCSS file is included, making it easy to customize colors, spacing,
and adapt the widget to your custom theme.

Styles can be safely overridden from your own theme if needed.

---

## 🧪 Technical Notes

- JavaScript logic is isolated and non-intrusive
- No core overrides
- Safe to use alongside standard Odoo widgets

---

## 📄 License

LGPL-3
