import pydot

with open("webapp/pictures/monitor.svg", "w") as mon_svg:

# Передаём в переменную dot-строку. Можно передать файл.
    dot_string = """graph my_graph{     
        bgcolor="yellow";
        a [label="Foo"];
        b [shape=circle];
        a -- b -- c [color=blue];
    }"""   

# Строим графы из строки
    graphs = pydot.graph_from_dot_data(dot_string) 
    graph = graphs[0]

# Создаём svg файл из графа
    mon_svg.write(str(graph.create_svg()))
