import discord
import os
import asyncio
import random

client = discord.Client()

# Write your code here.

# def get_number_of_teams():
#     while True:
#         msg = await client.wait_for("message", check=check, timeout=30)
#         num_teams = input("\nPlease enter how many teams you want to enter for the tournament: ")
#         if num_teams.isdigit():
#             if int(num_teams) >= 2:
#                 num_teams = int(num_teams)
#                 break
#             else:
#                 print("You must have at least 2 teams. Please try again. ")
#         else:
#             print("Please enter a valid value.")

#     return num_teams

# def get_team_names(num_teams):

#     team_names = []

#     for num in range(num_teams):
#         while True:
#             teamName = input(f"\nPlease enter the name for Team {num+1} ")

#             if len(teamName.split(" ")) > 2:
#                 print(f"Please try again. {teamName} has more than 2 words therefore it is not a valid name.")
#             elif len(teamName) < 2:
#                 print(f"Please try again. {teamName} has less than 2 characters therefore it is not a valid name.")
#             else:
#                 break

#         team_names.append(teamName)

#     return team_names


def get_number_of_games_played(num_teams):
    games_played = num_teams - 1

    print(f"\nThe number of games played by each team is {games_played}. ")

    return games_played


# def get_team_wins(team_names, games_played):
#     team_wins = {}

#     for team in team_names:
#         while True:
#             wins = input(f"\nPlease enter the number of wins for {team} last season: ")

#             if wins.isdigit():
#                 wins = int(wins)

#                 if wins > games_played:
#                     print(f"Please try again. You have entered too many wins.")
#                 elif wins < 0:
#                     print(f"Please try again. An invalid value has been entered.")
#                 else:
#                     team_wins[team] = wins
#                     break
#             else:
#                 print(f"Please try again. {wins} is not a valid input.")

#     return team_wins


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("/hello"):
        await message.channel.send("Beep boop I am bobBot.")

    if message.content.startswith("/createTeams"):

        def check(m):
            return m.channel == message.channel

        while True:
            await message.channel.send("Please enter the number of players")
            numOfPlayers = await client.wait_for("message", check=check)

            if numOfPlayers.content.isdigit():
                if int(numOfPlayers.content) >= 2 and int(numOfPlayers.content) % 2 == 0:
                    await message.channel.send(f"You have entered {numOfPlayers.content} players.")
                    numOfPlayers = int(numOfPlayers.content)
                    break
                else:
                    await message.channel.send(
                        "Invalid amount of players. Please try again.")
                    await asyncio.sleep(1)
            else:
                await message.channel.send("Please enter a valid value.")
                await asyncio.sleep(1)

        playerNames = []

        for num in range(numOfPlayers):
            while True:
                await message.channel.send(f"Enter the name for player {num+1}")
                playerName = await client.wait_for("message", check=check)

                if len(playerName.content.split(" ")) > 2:
                    await message.channel.send("Please try again")
                elif len(playerName.content) < 1:
                    await message.channel.send("Please try again")
                else:
                    break
            playerNames.append(playerName.content)

        # Discarded this part of the code as it will not be neccessary for users' convenience
        # more likely to use the generator to randomize teams rather than create a complete tournament.
        '''games_played = get_number_of_games_played(numOfPlayers)
    
    team_wins = {}

    for team in team_names:
      while True:
        await message.channel.send(f"Please enter the number of wins for {team} last season: ")
        wins = await client.wait_for("message", check=check)
        
        if wins.content.isdigit():
          wins = int(wins.content)
          if wins > games_played:
            await message.channel.send(f"Please try again. You have entered too many wins.")
          elif wins < 0:
            message.channel.send(f"Please try again. An invalid value has been entered.")
          else:
            team_wins[team] = wins
            break
        else:
          message.channel.send(f"Please try again. {wins} is not a valid input.")

    
    team_names = get_team_names(numOfPlayers)
    games_played = get_number_of_games_played(numOfPlayers)
    team_wins = get_team_wins(team_names, games_played)
    
    print(team_names)
    print(games_played)
    print(team_wins)
    
    sorted_values = sorted(team_wins.values())
    sorted_teams = {}
    
    for i in sorted_values:
        for key in team_wins.keys():
            if team_wins[key] == i:
                sorted_teams[key] = team_wins[key] '''

        team1 = ""
        team2 = ""

        # sorted_teams = list(sorted_teams)
        random.shuffle(playerNames)

        for i in range(len(playerNames) // 2):
            team1 += playerNames[i] + "\n"

        for i in range(len(playerNames), len(playerNames) // 2, -1):
            team2 += playerNames[i - 1] + "\n"

        # print(f"\nsorted {sorted_teams}")
        # print(f"\npairings {pairings}")

        await message.channel.send("```Generating teams...```")
        await asyncio.sleep(3)

        await message.channel.send(f"```Team 1\n{team1}\nTeam 2\n{team2}```")

    # Tournament generator adapted to discord bot imperatively
    if message.content.startswith("/create1v1"):

        def check(m):
            return m.channel == message.channel

        while True:
            await message.channel.send(
                "Please enter the number of teams (At least 2)")
            num_teams = await client.wait_for("message", check=check)

            if num_teams.content.isdigit():
                if int(num_teams.content) >= 2:
                    await message.channel.send(
                        f"You have entered {num_teams.content} teams.")
                    num_teams = int(num_teams.content)
                    break
                else:
                    await message.channel.send(
                        "You must have at least 2 teams. Please try again. ")
                    await asyncio.sleep(1)
            else:
                await message.channel.send("Please enter a valid value.")
                await asyncio.sleep(1)

        team_names = []

        for num in range(num_teams):
            while True:
                await message.channel.send(f"name for team {num+1}")
                teamName = await client.wait_for("message", check=check)

                if len(teamName.content.split(" ")) > 2:
                    await message.channel.send("try again")
                elif len(teamName.content) < 1:
                    await message.channel.send("try again")
                else:
                    break
            team_names.append(teamName.content)

        games_played = get_number_of_games_played(num_teams)

        team_wins = {}

        for team in team_names:
            while True:
                await message.channel.send(
                    f"Please enter the number of wins for {team} last season: "
                )
                wins = await client.wait_for("message", check=check)

                if wins.content.isdigit():
                    wins = int(wins.content)
                    if wins > games_played:
                        await message.channel.send(
                            f"Please try again. You have entered too many wins."
                        )
                    elif wins < 0:
                        message.channel.send(
                            f"Please try again. An invalid value has been entered."
                        )
                    else:
                        team_wins[team] = wins
                        break
                else:
                    message.channel.send(
                        f"Please try again. {wins} is not a valid input.")

        # team_names = get_team_names(num_teams)
        # games_played = get_number_of_games_played(num_teams)
        # team_wins = get_team_wins(team_names, games_played)

        print(team_names)
        print(games_played)
        print(team_wins)

        sorted_values = sorted(team_wins.values())
        sorted_teams = {}

        for i in sorted_values:
            for key in team_wins.keys():
                if team_wins[key] == i:
                    sorted_teams[key] = team_wins[key]

        pairings = []

        gamesToMake = len(team_names) // 2

        sorted_teams = list(sorted_teams)

        for gameNum in range(gamesToMake):
            team1 = sorted_teams[gameNum]
            team2 = sorted_teams[num_teams - 1 - gameNum]
            pairings.append([team1, team2])

        # print(f"\nsorted {sorted_teams}")
        # print(f"\npairings {pairings}")

        await message.channel.send(
            f"```Generating the games to be played in the first round of the tournament...```"
        )
        await asyncio.sleep(3)

        for pairing in pairings:
            team1, team2 = pairing
            await message.channel.send(f"```{team1} vs {team2}```")


client.run("KEY HERE")
