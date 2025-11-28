# django_menu_TreeNav_TemplateTag_test
A reusable Django app implementing a dynamic, hierarchical menu tree. Data is DB-stored and rendered via a custom template tag ({% draw_menu 'name' %}). The core logic dynamically expands the menu to display only the active URL path and its immediate children. The solution adheres to a strict single-query performance constraint.
