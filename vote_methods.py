class PluralityVoting:
    def give_votes(self, PRIORITIES):
        choices = []
        votes = {}

        for priority in PRIORITIES:
            choices.append(priority)

        for choice in choices:
            votes[choice] = 0

        return votes

    def calculate_votes(self, votes, AGENTS):
        for agent in AGENTS:
            print(agent.priorities)
            votes[agent.priorities[0]] += 1

        print(sorted(votes.items(), key=lambda x: (x[1], x[0]), reverse=True))
        votes = sorted(votes.items(), key=lambda x: (x[1], x[0]), reverse=True)
        return votes
