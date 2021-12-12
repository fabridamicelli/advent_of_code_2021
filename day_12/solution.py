from collections import defaultdict, Counter


def load_inputs(filename):
    with open(filename) as file:
        return [line.strip().split("-") for line in file]


def make_graph(inputs):
    g = defaultdict(tuple)
    for i, j in inputs:
        if i == "start":
            g[i] += (j,)
        elif j == "start":
            g[j] += (i,)
        else:
            g[i] += (j,)
            g[j] += (i,)
    return g


def repeated_lower_case(path):
    lower_cases = tuple(node for node in path if node.islower())
    return any(val != 1 for val in Counter(lower_cases).values())


def update_path(path, g, allow_one_repeat=False):
    last_node = path[-1]
    neighbors = g[last_node]
    new_paths = []
    for j in neighbors:
        # This disregards paths leading to dead ends
        if (
            j not in path or
            j.isupper() or
            (allow_one_repeat and not repeated_lower_case(path))
        ):
            new_paths.append(path + (j,))
    return new_paths


def filter_paths(paths):
    keep = []
    end = []
    for path in paths:
        if path[-1] == "end":
            end.append(path)
        else:
            keep.append(path)
    return {"end": end, "keep": keep}


def search_paths(g, allow_one_repeat=False):
    successful_paths = []
    paths = [("start",)]
    while True:
        updated_paths = []
        for path in paths:
            new_paths = filter_paths(
                update_path(path, g, allow_one_repeat=allow_one_repeat)
            )
            successful_paths += new_paths["end"]
            updated_paths += new_paths["keep"]
        if not updated_paths:
            return successful_paths
        paths = updated_paths


if __name__ == "__main__":
    g = make_graph(load_inputs("inputs.txt"))
    print("Solution part 1:", len(search_paths(g, allow_one_repeat=False)))
    print("Solution part 2:", len(search_paths(g, allow_one_repeat=True)))
