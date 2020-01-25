from django.shortcuts import render
from zdg.zdg import ZeroDivisorGraph

def home(request):
    if(request.GET.get('g0', False)):
        i = 1
        edges = []
        while(edge := request.GET.get('g' + str(i), False)):
            a, b = map(int, edge.split('e'))
            edges.append((a, b))
            i += 1
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
