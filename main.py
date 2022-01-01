from spade.behaviour import State
from spade.message import Message
import threading
import random
import time
import json
from vote_methods import PluralityVoting, Runoff
from agents import ChairmanAgent, MemberAgent, Voting
from global_settings import *
import sys


class StateDiscussion(State):
    async def run(self):
        print("\nWe will now discuss about the proposal.\n")
        self.set_next_state(STATE_TWO)
        print_agent_preferences(AGENTS)

        time.sleep(PAUSE)


class StateVoting(State):
    async def run(self):
        print("\nMembers are allowed to vote.")
        votes = voting_method.give_votes(PRIORITIES)

        msg = Message(to=str(self.agent.jid))
        msg.body = f"{votes}"
        await self.send(msg)
        self.set_next_state(STATE_THREE)

        time.sleep(PAUSE)


class StateVotingEnd(State):
    async def run(self):
        print("\nVoting is over.")
        msg = await self.receive(timeout=5)
        votes = json.loads(msg.body.replace("'", '"'))
        voting_method.calculate_votes(votes, AGENTS)

        time.sleep(PAUSE)


def create_chairman_agent(account_info):
    agent = ChairmanAgent(account_info[0], account_info[1])
    agent.set_agent_details("Bruno", PROPOSAL)
    CHAIRMAN.append(agent)
    future = agent.start()
    future.result()


def create_member_agent(account_info, i):
    agent = MemberAgent(account_info[0], account_info[1])
    new_priorities = random.sample(PRIORITIES, len(PRIORITIES))
    agent.set_agent_details("Member" + str(i), new_priorities)
    AGENTS.append(agent)
    future = agent.start()
    future.result()


def create_voting_agent(account_info):
    voting = Voting(account_info[0], account_info[1])
    VOTING.append(voting)
    future = voting.start()
    voting.fsm.add_state(name=STATE_ONE, state=StateDiscussion(), initial=True)
    voting.fsm.add_state(name=STATE_TWO, state=StateVoting())
    voting.fsm.add_state(name=STATE_THREE, state=StateVotingEnd())
    voting.fsm.add_transition(source=STATE_ONE, dest=STATE_TWO)
    voting.fsm.add_transition(source=STATE_TWO, dest=STATE_THREE)
    voting.add_behaviour(voting.fsm)
    future.result()


def print_agent_preferences(agents):
    for agent in agents:
        print(f"My ({agent.name}) priorities are: {agent.priorities}")


if __name__ == "__main__":

    try:
        method = sys.argv[1]
        agent_number = sys.argv[2]
    except:
        sys.exit()

    if method == "plurality":
        voting_method = PluralityVoting()
    elif method == "runoff":
        voting_method = Runoff()
    else:
        print("Method doesn't exist! Exiting . . .")
        sys.exit()

    for i in range(1, int(agent_number) + 1):
        account_info = ("agent@rec.foi.hr", "tajna")
        thread1 = threading.Thread(
            target=create_member_agent(account_info, i), args=(account_info, i)
        ).start()

    account_info = ("bzitkovic@rec.foi.hr", "agent48")
    thread2 = threading.Thread(
        target=create_chairman_agent(account_info), args=(account_info)
    ).start()

    account_info = ("posiljatelj@rec.foi.hr", "tajna")
    thread3 = threading.Thread(
        target=create_voting_agent(account_info), args=(account_info)
    ).start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopping program...")
