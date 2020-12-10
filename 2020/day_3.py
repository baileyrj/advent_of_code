
path_strategies = [
    {'right': 1, 'down': 1}, 
    {'right': 3, 'down': 1}, 
    {'right': 5, 'down': 1}, 
    {'right': 7, 'down': 1}, 
    {'right': 1, 'down': 2}]
TREE = '#'
results = []


def solve():
    with open('data/day_3_input.txt', 'r') as f:
        slopes = f.read().splitlines()

    for strat in path_strategies:
        trees_hit = 0
        down = strat.get('down')
        right = strat.get('right')

        for i in range(len(slopes)):
            segment = slopes[i]

            if i >= down and i % down == 0:
                multiplier = int(i / down)
                x_pos = (right* multiplier) % len(segment)

                if segment[x_pos] == TREE:
                    trees_hit += 1

        results.append({'strat': strat, 'trees_hit': trees_hit})   
    return results

res = solve()
total_trees = 1

for s in res:
    total_trees *= s.get('trees_hit')

print(res)
print(f'total trees hit: {total_trees}')
