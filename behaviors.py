from spade.behaviour import FSMBehaviour


class VotingProcess(FSMBehaviour):
    async def on_start(self):
        print(f"FSM starting at {self.current_state}")

    async def on_end(self):
        print(f"FSM finished at state {self.current_state}")
