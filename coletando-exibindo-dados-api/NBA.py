# Esse é o link do site no qual vamos fazer a requisição: http://data.nba.net/prod/v1/today.json e o mesmo
# vai trazer uma estrutura de dicionário, arquivo json
# devemos ir entendendo a estrutura do json, raramente à API vai trazer os dados prontos para
# serem consumidos


 # queremos solicitar alguma informação através do get

# variável global (letra maíscula- BASE_URL) no qual conseguimos usar durante o nosso código

# o .keys vai trazer o dicionário de um jeito mais organizado que facilita a exploração

from requests import get

BASE_URL = "http://data.nba.net" # essa base não vai mudar
ALL_JSON = "/prod/v1/today.json" # essa pode modificar de acordo com a nossa requisição

def get_links():
   response = get(BASE_URL+ALL_JSON).json() # o .json() é pra forçar o retorno no formato de dicionário
   return response["links"]

def get_currentScoreboard():
    response = get(BASE_URL+get_links()["currentScoreboard"]).json()
    games = response["games"]

    for game in games:
        home_team = game["hTeam"] # time da casa
        away_team = game["vTeam"] # time visitante
        clock = game["clock"]
        period = game["period"]

        print("##################################\n") # o # é para separar
        print(f"{home_team['triCode']} vs {away_team['triCode']}")
        print(f"SCORE: {home_team['score']} x {away_team['score']}")
        print(f"{clock} - {period['current']}\n")


# detalhes em relação aos times

def get_teams_stats():
    stats = get_links()["leagueTeamStatsLeaders"]
    data = get(BASE_URL+stats).json()
    teams = data["league"]["standard"]["regularSeason"]["teams"]

    teams = list(filter(lambda x: x["name"] != "Team", teams))
    teams.sort(key = lambda x: x["ppg"]["rank"])) # sort é pra ordenar
    # esse x é cada linha, dicionário do time

    for team in teams:
        team_name = team["name"]
        nickname = team["nickname"]
        ppg = team["ppg"]

    print(f"{team_name} - {nickname} | PPG: {ppg}")

print(get_teams_stats())


