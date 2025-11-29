from django.views import generic
from collections import defaultdict
from .models import Node


class IndexView(generic.ListView):
    template_name = "menu/index.html"
    context_object_name = "all_nodes"

    def get_queryset(self):
        return Node.objects.all().order_by('pk')


class NodesDictView(generic.TemplateView):
    template_name = "menu/nodes_dict.html"

    def get_context_data(self, **kwargs):
        """
        ### input
        
        id | label | parent | path
        1 | root | None | /
        3 | Smartphones | root | /smartphones
        2 | Laptops | root | /laptops

        ### output
        
        {
            None: [                                  # top-level nodes (parent is None)
                {"id": 1, "label": "root", "path": "/"}
            ],
            1: [                                     # entry for node id=1 (root)
                {"parent_id": None, "parent_path": None},   # parent info for node 1
                {"id": 3, "label": "Smartphones", "path": "/smartphones"},
                {"id": 2, "label": "Laptops", "path": "/laptops"}
            ],
            3: [                                     # entry for node id=3
                {"parent_id": 1, "parent_path": "/"}       # parent info for Smartphones
            ],
            2: [                                     # entry for node id=2
                {"parent_id": 1, "parent_path": "/"}       # parent info for Laptops
            ]
        }
        """
        context = super().get_context_data(**kwargs)
        nodes = Node.objects.all().order_by('pk')
        nodes_dict = defaultdict(list)
        nodes_dict[None] = []
        for node in nodes:
            parent_id = node.parent.id if node.parent else None
            parent_path = node.parent.path if node.parent else None
            nodes_dict[node.pk].append({
                "parent_id": parent_id,
                "parent_path": parent_path
            })
            nodes_dict[parent_id].append({
                "id": node.pk,
                "label": node.label,
                "path": node.path,
            })

        context["nodes_dict"] = dict(nodes_dict)
        return context
    