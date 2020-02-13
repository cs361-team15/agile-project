def row_puzzle(int_list, current_index = 0, past_indices = []):
      
    print ("past_indices: ", past_indices)

    last_index = len(int_list) - 1
    #
    # print("currently at", "int_list", [current_index], "=", int_list[current_index])

    left_move = current_index - int_list[current_index]
    right_move = current_index + int_list[current_index]


    # base case - when marker has reached the end of the list
    if int_list[current_index] == 0 and current_index == last_index:
        past_indices.clear ()
        return True

    # dead end - infinite loop occurs when the current_index is in the past_indices (marker should only go to each index at most once)
    if current_index in past_indices:
        return False
    else:
      past_indices.append(current_index)


    # dead end - if marker is on a "0" that is NOT at the end of the list; marker cannot make anymore moves
    if int_list[current_index] == 0 and current_index != last_index:
        return False


    # dead end - both directional movement causes marker to be out-of-bounds each time
    if left_move < 0 and right_move > last_index:
        return False

    # marker can move both L and R
    if left_move >= 0 and right_move <= last_index:

        #past_indices.append(current_index)

        return row_puzzle(int_list, left_move, past_indices) or row_puzzle(int_list, right_move, past_indices)

    # marker can only move L
    if left_move >= 0 and right_move > last_index:

        #past_indices.append(current_index)

        return row_puzzle(int_list, left_move, past_indices)

    # marker can only move R
    if right_move <= last_index and left_move < 0:

        #past_indices.append(current_index)

        return row_puzzle(int_list, right_move, past_indices)


#puz_list2 = [2, 4, 5, 3, 1, 3, 1, 4, 0]  # True
#print(row_puzzle(puz_list2))






puz_list1 = [1, 3, 2, 1, 3, 4, 0]  # False
puz_list2 = [2, 4, 5, 3, 1, 3, 1, 4, 0]  # True
# puz_list3 = [3, 3, 1000, 1, 4, 2, 0, 0]  # False

print(row_puzzle(puz_list1))
print(row_puzzle(puz_list2))
# print(row_puzzle(puz_list3))