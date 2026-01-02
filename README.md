# Many2many Razs Tags Widget

A powerful and flexible **Many2many widget for Odoo** that renders many2many fields as clean, modern, and responsive **tags**, allowing you to **choose exactly which fields of the related record are displayed inside each tag**.

This makes it ideal for scenarios where showing only the record name is not enough, and additional context (email, code, phone, etc.) is required — all while working seamlessly across **all Odoo view types**.

The widget is lightweight, easy to integrate, and fully aligned with Odoo’s native UX.

---

## 🚀 Key Features

- 🏷️ Displays many2many records as tag-style elements
- 🧩 Works on **all Odoo view types** (form, tree, kanban, etc.)
- 🔧 **Configurable tag content**: select which related fields appear in each tag
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

Apply the widget to any many2many field and specify which related fields should be displayed inside the tag using the `options` attribute.

### Example

```xml
<field name="tag_ids"
       widget="many2many_razs"
       options="{'fields': ['name', 'email', 'phone']}"/>
```

Each tag will render the selected fields in a compact and readable format, giving users immediate context without opening the related record.

---

## 🎯 Use Cases

- Tags with additional metadata
- Contacts (name + email / phone)
- Products (name + internal reference)
- Skills with levels or categories
- Labels where extra context improves usability

Any many2many relationship that benefits from **rich, informative tags**.

---

## 🧩 Compatibility

- Odoo 19+
- Community & Enterprise editions
- No external dependencies

---

## 🎨 Styling

A dedicated SCSS file is included, making it easy to:

- Customize colors
- Adjust spacing
- Adapt the widget to your custom theme

Styles can be safely overridden from your own theme if needed.

---

## 🧪 Technical Notes

- JavaScript logic is isolated and non-intrusive
- No core overrides
- Safe to use alongside standard Odoo widgets
- Does not affect existing many2many behavior

---

## 📄 License

LGPL-3
