# Write your code here.

def get_number_of_teams():
    while True:
        num_teams = input("\nPlease enter how many teams you want to enter for the tournament: ")
        if num_teams.isdigit():
            if int(num_teams) >= 2:
                num_teams = int(num_teams)
                break
            else:
                print("You must have at least 2 teams. Please try again. ")
        else:
            print("Please enter a valid value.")

    return num_teams


def get_team_names(num_teams):
    
    team_names = []

    for num in range(num_teams):
        while True:
            teamName = input(f"\nPlease enter the name for Team {num+1} ")

            if len(teamName.split(" ")) > 2:
                print(f"Please try again. {teamName} has more than 2 words therefore it is not a valid name.")
            elif len(teamName) < 2:
                print(f"Please try again. {teamName} has less than 2 characters therefore it is not a valid name.")
            else:
                break

        team_names.append(teamName)

    return team_names

def get_number_of_games_played(num_teams):
    games_played = num_teams - 1
    
    print(f"\nThe number of games played by each team is {games_played}. ")

    return games_played


def get_team_wins(team_names, games_played):
    team_wins = {}

    for team in team_names:
        while True:
            wins = input(f"\nPlease enter the number of wins for {team} last season: ")
            
            if wins.isdigit():
                wins = int(wins)

                if wins > games_played:
                    print(f"Please try again. You have entered too many wins.")
                elif wins < 0:
                    print(f"Please try again. An invalid value has been entered.")
                else:
                    team_wins[team] = wins
                    break
            else:
                print(f"Please try again. {wins} is not a valid input.")
    
    return team_wins

num_teams = get_number_of_teams()
team_names = get_team_names(num_teams)
games_played = get_number_of_games_played(num_teams)
team_wins = get_team_wins(team_names, games_played)

print("\nGenerating the games to be played in the first round of the tournament...")
# print(team_names)
# print(games_played)
# print(team_wins)

sorted_values = sorted(team_wins.values())
sorted_teams = {}

for i in sorted_values:
    for key in team_wins.keys():
        if team_wins[key] == i:
            sorted_teams[key] = team_wins[key]

pairings = []

gamesToMake = len(sorted_teams) // 2

sorted_teams = list(sorted_teams)

for gameNum in range(gamesToMake):
    team1 = sorted_teams[gameNum]
    team2 = sorted_teams[num_teams - 1 - gameNum]
    pairings.append([team1, team2])

# print(f"\nsorted {sorted_teams}")
# print(f"\npairings {pairings}")

for pairing in pairings:
    team1, team2 = pairing
    print(f"\n{team1} VS {team2}")

