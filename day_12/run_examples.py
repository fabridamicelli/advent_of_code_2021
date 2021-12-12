from solution import make_graph, search_paths


ex = [
    ["start","A"],
    ["start","b"],
    ["A","c"],
    ["A","b"],
    ["b","d"],
    ["A","end"],
    ["b","end"]
]

ex2 = [
    ["dc","end"],
    ["HN","start"],
    ["start","kj"],
    ["dc","start"],
    ["dc","HN"],
    ["LN","dc"],
    ["HN","end"],
    ["kj","sa"],
    ["kj","HN"],
    ["kj","dc"],
]

ex3 = [
    ["fs","end"],
    ["he","DX"],
    ["fs","he"],
    ["start","DX"],
    ["pj","DX"],
    ["end","zg"],
    ["zg","sl"],
    ["zg","pj"],
    ["pj","he"],
    ["RW","he"],
    ["fs","DX"],
    ["pj","RW"],
    ["zg","RW"],
    ["start","pj"],
    ["he","WI"],
    ["zg","he"],
    ["pj","fs"],
    ["start","RW"],
]

expected = (36, 103, 3509)

for example, expec in zip((ex, ex2, ex3), expected):
    g = make_graph(example)
    print(f"Expected: {expec}, got {len(search_paths(g, allow_one_repeat=True))}")
    print("----")
