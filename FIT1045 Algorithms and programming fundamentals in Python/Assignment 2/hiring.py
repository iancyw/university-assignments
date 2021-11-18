jess = (["php", "java"], 200)
clark = (["php", "c++", "go"], 1000)
john = (["lua"], 500)
cindy = (["php", "go", "word"], 240)
candidates = [jess, clark, john, cindy]
project = ["php", "java", "c++", "lua", "go"]


# cost
def cost(candidates):
    total_cost = 0
    n = len(candidates)
    for i in range(n):
        total_cost += candidates[i][1]
    return total_cost


# skills
def skills(candidates):
    skills_list = []
    n = len(candidates)
    for i in range(n):
        for j in range(len(candidates[i][0])):
            if candidates[i][0][j] not in skills_list:
                skills_list.append(candidates[i][0][j])
    return skills_list


# uncovered
def uncovered(project, skills):
    needed_skills = []
    for skill in project:
        if skill not in skills:
            needed_skills.append(skill)
    return needed_skills


# best_individual_candidate
def best_individual_candidate(project, candidates):
    skills_lst = []
    for candidate in candidates:
        valid_skills = 0
        for i in range(len(candidate[0])):
            if candidate[0][i] in project:
                valid_skills += 1
        skills_per_rate = valid_skills / candidate[1]
        skills_lst.append(skills_per_rate)
    max_skill = skills_lst[0]
    max_index = 0
    for i in range(len(skills_lst)):
        if skills_lst[i] > max_skill:
            max_skill = skills_lst[i]
            max_index = i
    return max_index


# team_of_best_individuals
def team_of_best_individuals(project, candidates):
    n = len(candidates)
    team = []
    for i in range(n):
        j = best_individual_candidate(project, candidates)
        team.append(candidates[j])
        for skill in candidates[j][0]:
            if skill in project:
                project.remove(skill)
        candidates.remove(candidates[j])
    return team


# code taken from brute force lecture slides
def lex_suc(bitlst):
    tmp = bitlst[:]
    i = len(tmp) - 1
    while tmp[i] == 1:
        tmp[i] = 0
        i -= 1
    tmp[i] = 1
    return tmp


# code taken from brute force lecture slides
def bitlists(n):
    first = n*[0]
    last = n*[1]
    tmp = [first]
    while tmp[-1] != last:
        tmp += [lex_suc(tmp[-1])]
    return tmp


# best_team (0 = empty, 1 = person is there)
def best_team(project, candidates):
    n = len(candidates)
    possible_teams = bitlists(n)
    feasible_teams = []
    for team in possible_teams:
        covered_skills = []
        for i in range(len(team)):
            if team[i] == 1:
                covered_skills += candidates[i][0]
        if not uncovered(project, covered_skills):
            feasible_teams.append(team)
    team_prices = []
    for team in feasible_teams:
        price = 0
        for i in range(len(team)):
            if team[i] == 1:
                price += candidates[i][1]
        team_prices.append(price)
    min_index = team_prices.index(min(team_prices))
    opt_team = []
    for i in range(len(feasible_teams[min_index])):
        if feasible_teams[min_index][i] == 1:
            opt_team.append(candidates[i])
    return opt_team
