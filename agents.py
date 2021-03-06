from spade.agent import Agent
from spade.behaviour import OneShotBehaviour
from spade.message import Message
from spade.template import Template
from behaviors import VotingProcess


class ChairmanAgent(Agent):
    name = "Bruno"
    proposal = ""
    vote_for = ""

    def set_agent_details(self, name, proposal):
        self.name = name
        self.proposal = proposal

    class InformBehav(OneShotBehaviour):
        async def run(self):
            print("Chairman speaks:")
            msg = Message(to="agent@rec.foi.hr")
            msg.set_metadata("performative", "inform")
            msg.body = (
                f"We have gathered today to discuss the proposal: {self.agent.proposal}"
            )

            await self.send(msg)

    async def setup(self):
        print(f"\nHello! I'm the chairman {self.name}")
        b = self.InformBehav()
        self.add_behaviour(b)


class MemberAgent(Agent):
    name = "unknown"
    priorities = []

    def set_agent_details(self, name, priorities):
        self.name = name
        self.priorities = priorities

    class RecvBehav(OneShotBehaviour):
        async def run(self):
            msg = await self.receive(timeout=50)
            if msg:
                print("\nMessage received with content: {}".format(msg.body))
            else:
                print("Did not received any message after 10 seconds")

    async def setup(self):
        print(f"Hello! I'm member {self.name}")
        b = self.RecvBehav()
        template = Template()
        template.set_metadata("performative", "inform")
        self.add_behaviour(b, template)


class Voting(Agent):
    fsm = VotingProcess()

    async def setup(self):
        self.fsm
