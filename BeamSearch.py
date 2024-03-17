from numpy import array

def beam_search(distances, beta):
    paths_so_far = [[list(),0]]

    for idx,tier in enumerate(distances):
        if idx > 0:
            print(f"Paths kept after tier {idx-1}: ")
            print(*paths_so_far, sep='\n')
        paths_at_tier = list()


            