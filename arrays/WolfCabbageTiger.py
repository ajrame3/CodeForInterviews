def print_state(state):
    left_bank, right_bank = state
    print("#### CURRENT STATE OF PUZZLE ####")
    print("")
    left_bank_display = [names[item] for item in left_bank]
    right_bank_display = [names[item] for item in right_bank]
    print left_bank_display, "|", right_bank_display if right_bank else "[]" # Add brackets for Python 3
    print("")


def get_move():
    print("Which item do you wish to take across the river?")
    answer = ""
    while answer.upper() not in ["F", "W", "G", "C"]:
        answer = input("Just Farmer (f), Wolf (w), Goat (g) or Cabbage (c)? ")

    return answer.upper()


def process_move(move, state):
    # We need to "think ahead" to see if move is illegal.
    temp_state = [state[0].copy(), state[1].copy()]
    containing_set = 0 if move in state[0] else 1
    if "F" not in state[containing_set]:
        print("Not allowed - the farmer must accompany the item.")
        print("")
        return state
    if containing_set == 0:
        temp_state[0].difference_update({move, "F"})
        temp_state[1].update([move, "F"])
    elif containing_set == 1:
        temp_state[1].difference_update({move, "F"})
        temp_state[0].update([move, "F"])
    if temp_state[0] not in forbidden_states and temp_state[1] not in forbidden_states:
        state = [temp_state[0].copy(), temp_state[1].copy()]
    else:
        print("Not allowed - one of your items would be eaten!")
    print("")
    return state