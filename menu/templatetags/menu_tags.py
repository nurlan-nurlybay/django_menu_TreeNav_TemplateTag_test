from django import template
from menu.utils import get_menu_data

register = template.Library()

@register.inclusion_tag('menu/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    metadata, children = get_menu_data(menu_name)
    
    request = context.get('request')
    current_path = request.path if request else ''
    
    active_id = None
    for node_id, node in metadata.items():
        if node.get_absolute_url() == current_path:
            active_id = node_id
            break
    
    expanded_ids = set()
    if active_id:
        current_id = active_id
        while current_id:
            expanded_ids.add(current_id)
            node = metadata.get(current_id)
            current_id = node.parent_id if node else None
    
    top_level_nodes = children.get(None, [])
    start_parent_id = None
    
    if len(top_level_nodes) == 1:
        root_node = top_level_nodes[0]
        start_parent_id = root_node.id
        # expanded_ids.add(root_node.id) 
    
    return {
        'children_map': children,
        'expanded_ids': expanded_ids,
        'active_id': active_id,
        'parent_id': start_parent_id,
    }


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)
