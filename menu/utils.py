from collections import defaultdict
from .models import Node

def get_menu_data(menu_name_filter):
    """
    Returns two dicts:
    1. metadata: {id: NodeObj} (For metadata & tracing parents)
    2. children: {parent_id: [NodeObj, ...]} (For rendering children)
    """
    queryset = Node.objects.filter(menu_name=menu_name_filter).order_by('pk')
    
    metadata = {}
    children = defaultdict(list)
    
    for node in queryset:
        metadata[node.pk] = node
        children[node.parent_id].append(node)  # type: ignore
        
    return metadata, children
