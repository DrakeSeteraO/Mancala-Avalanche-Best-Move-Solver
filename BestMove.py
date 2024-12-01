def solve(good_spots: list, bad_spots: list):
    m1 = solve_best(good_spots, bad_spots, 0)
    m2 = solve_best(good_spots, bad_spots, 1)
    m3 = solve_best(good_spots, bad_spots, 2)
    m4 = solve_best(good_spots, bad_spots, 3)
    m5 = solve_best(good_spots, bad_spots, 4)
    m6 = solve_best(good_spots, bad_spots, 5)
    
    highest = m1
    if m2[0] > highest[0]:
        highest = m2
    if m3[0] > highest[0]:
        highest = m3
    if m4[0] > highest[0]:
        highest = m4
    if m5[0] > highest[0]:
        highest = m5
    if m6[0] > highest[0]:
        highest = m6
    
    display_moves(highest)
        
        
def display_moves(lst: list):
    moves_output = str()
    moves = lst[1]
    if isinstance(moves, int):
        moves_output = str(moves) + '    '
    else:
        for m in moves:
            if m == 99:
                moves_output += 'Any move    '
            else:
                moves_output += str(m + 1) + ' -> '
    moves_output = moves_output[:-4]
    print(f'The best moves to make are to select the rows\n{moves_output}\nThis should get you {lst[0]} points')
    


def solve_best(gs: list, bs: list, index: int):
    if gs[index] == 0:
        return [0, 99]
    
    good_spots = gs.copy()
    bad_spots = bs.copy()
    
    move = do_move(good_spots, bad_spots, index)
    
    if move[1]:
        m1 = solve_best(good_spots, bad_spots, 0)
        m2 = solve_best(good_spots, bad_spots, 1)
        m3 = solve_best(good_spots, bad_spots, 2)
        m4 = solve_best(good_spots, bad_spots, 3)
        m5 = solve_best(good_spots, bad_spots, 4)
        m6 = solve_best(good_spots, bad_spots, 5)
        
        highest = m1
        if m2[0] > highest[0]:
            highest = m2
        if m3[0] > highest[0]:
            highest = m3
        if m4[0] > highest[0]:
            highest = m4
        if m5[0] > highest[0]:
            highest = m5
        if m6[0] > highest[0]:
            highest = m6
        
        if isinstance(highest[1], int):
            highest[1] = [highest[1]]
            
        return [move[0] + highest[0], [index] + highest[1]]    
        
    else:
        return [move[0], index]


def do_move(good_spots: list, bad_spots: list, index: int):
    amount = 0
    if index <= 5:
        amount = good_spots[index]
        good_spots[index] = 0
    elif 7 <= index:
        amount = bad_spots[13 - index - 7]
        bad_spots[13 - index - 7] = 0
    else:
        return [0,True]
        
    points = 0
    current_index = 0
    for i in range(1,amount+1):
        current_index = (index + i) % 13
        if current_index <= 5:
            good_spots[current_index] += 1
        elif current_index == 6:
            points += 1
        else:
            bad_spots[13 - current_index - 7] += 1
    
    if current_index <= 5:
        if good_spots[current_index] > 1:
            output = do_move(good_spots, bad_spots, current_index)
            return [output[0] + points, output[1]]
        else:
            return [points,False]
    elif current_index == 6:
        return [points,True]
    else:
        if bad_spots[13 - current_index - 7] > 1:
            output = do_move(good_spots, bad_spots, current_index)
            return [output[0] + points, output[1]]
        else:
            return [points,False]


def main():
    good_spots = [0,0,0,0,0,0]
    bad_spots = [0,0,0,0,0,0]
    
    print("Input the 6 spots on your side from top to bottom")
    good_spots[0] = int(input())
    good_spots[1] = int(input())
    good_spots[2] = int(input())
    good_spots[3] = int(input())
    good_spots[4] = int(input())
    good_spots[5] = int(input())
    
    print("Input the 6 spots on the enemy side from top to bottom")
    bad_spots[0] = int(input())
    bad_spots[1] = int(input())
    bad_spots[2] = int(input())
    bad_spots[3] = int(input())
    bad_spots[4] = int(input())
    bad_spots[5] = int(input())
    
    solve(good_spots,bad_spots)
    
    
if __name__ == '__main__':
    main()
