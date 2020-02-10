from django.shortcuts import render
from zdg.zdg import ZeroDivisorGraph
import json

def semigroup_view(request):
    if (raw_graph := request.POST.get('graph', False)):
        print(raw_graph)
        raw_graph = json.loads(raw_graph)
        edges = []
        for edge in raw_graph['edges']:
            edges.append((edge['v1'], edge['v2']))
        graph = ZeroDivisorGraph(*edges)
        semigroups = graph.semigroups()
        if semigroups:
            context = {
                'semigroups': len(semigroups),
            }
        else:
            context = {
                'semigroups': '0',
            }
        return render(request, 'home/home.html', context)    
    else:
        return render(request, 'home/home.html') 
