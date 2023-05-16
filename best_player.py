best_player_name = ""
best_player_score = 0
goals_scored = 0

while True:
    data = str(input())
    player_name = data

    if data == "END":
        break

    goals_scored = int(input())

    if goals_scored > best_player_score:
        best_player_name = player_name
        best_player_score = goals_scored

    print(f'{best_player_name} is the best player!', end=' ')
    if best_player_score >= 3:
        print(f'He has scored {best_player_score} goals and made a hat-trick !!!')
    else:
        print(f'He has scored {best_player_score} goals.')
