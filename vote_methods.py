from itertools import islice


class PluralityVoting:
    def give_votes(self, priorities):
        choices = []
        votes = {}

        for priority in priorities:
            choices.append(priority)

        for choice in choices:
            votes[choice] = 0

        return votes

    def calculate_votes(self, votes, agents):
        for agent in agents:
            votes[agent.priorities[0]] += 1
            agent.vote_for = agent.priorities[0]

        votes = sorted(votes.items(), key=lambda x: (x[1], x[0]), reverse=True)

        print(f"\nWinner proposal is: {votes[0][0]} with {votes[0][1]} votes\n")

        for agent in agents:
            if agent.vote_for != votes[0][0]:
                print(
                    f"I ({agent.name}) didn't vote for {votes[0][0]}, because I support {agent.vote_for}"
                )
        return votes


class Runoff:
    def give_votes(self, priorities):
        choices = []
        votes = {}

        for priority in priorities:
            choices.append(priority)

        for choice in choices:
            votes[choice] = 0

        return votes

    def calculate_votes(self, votes, agents):
        votes_first_circle = first_circle_runoff(votes, agents)

        print(
            f"\nThe second round of voting includes {votes_first_circle[0][0]} and {votes_first_circle[1][0]} "
        )

        votes_first_circle = dict((x, y) for x, y in votes_first_circle)
        votes_first_circle = dict(list(votes_first_circle.items())[0:2])

        return second_circle(votes_first_circle, agents)


def first_circle_runoff(votes, agents):
    for agent in agents:
        votes[agent.priorities[0]] += 1
        agent.vote_for = agent.priorities[0]

    votes = sorted(votes.items(), key=lambda x: (x[1], x[0]), reverse=True)

    print(f"\nWinner of the first round is: {votes[0][0]} with {votes[0][1]} votes")

    return votes


def second_circle(votes, agents):
    votes = {x: 0 for x in votes}
    for agent in agents:
        if agent.priorities[0] in votes:
            votes[agent.priorities[0]] += 1
            agent.vote_for = agent.priorities[0]
            continue
        if agent.priorities[1] in votes:
            votes[agent.priorities[1]] += 1
            agent.vote_for = agent.priorities[1]
            continue
        if agent.priorities[2] in votes:
            votes[agent.priorities[2]] += 1
            agent.vote_for = agent.priorities[2]

    votes = sorted(votes.items(), key=lambda x: (x[1], x[0]), reverse=True)
    print(f"\nWinner proposal is: {votes[0][0]} with {votes[0][1]} votes\n")

    for agent in agents:
        if agent.vote_for != votes[0][0]:
            print(
                f"I ({agent.name}) didn't vote for {votes[0][0]}, because I support {agent.vote_for}"
            )
    return votes
