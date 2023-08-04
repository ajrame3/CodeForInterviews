items = ["wolf,", "goat", "cabbage"]
edges = []
location = ("source", "dest")

def invalid_state(item1, item2):
    if item1 == "goat" and item2 == "cabbage":
        return True
    
    elif item1 == "goat" and item2 == "cabbage":
        return True
    else:
        return False

def valid_state(item1, item2):
    if invalid_state(item1, item2) or invalid_state(item1, item2):
        return False
    else:
        return True

def safe_state(state):
    if state['boat'] == state['goat']:
        return True
    elif  state['goat'] == state['wolf']:
        return False
    elif state['goat'] == state['wolf']:
        return False
    else:
        return True

def goal_state(state):
    if not state:
        return False
    return ( state['boat']==location.dest 
            and state['cabbage']==location.dest
            and state['goat']==location.dest 
            and state['wolf']==location.dest)


def move(item, state):
    if state[item] == location.source:
        state[item] = location.dest
    else:
        state[item] = location.source
    return state


def next_states(state):
    neighbors = []
    neighbor = state.copy()
    move('man', neighbor)
    if safe_state(neighbor):
        neighbors.append(neighbor)
    
    for item in ["wolf", "cabbage", "goat"]:
        if state[item] == state["boat"]:
            neighbor = state.copy()
            move('boat', neighbor)
            move(item, neighbor)
            if safe_state(neighbor):
                neighbors.append(neighbor)

    return neighbors

def BFS(state):
    edges.append(state)
    next = state.copy()
    while next and not goal_state(next):
        ns = next_states(next)
        next = {}
        for eachState in ns:
            if not (eachState in edges):
                next = eachState
                edges.append(next)
                break
    return next

