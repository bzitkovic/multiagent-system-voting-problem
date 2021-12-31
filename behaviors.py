from spade.behaviour import FSMBehaviour


class VotingProcess(FSMBehaviour):
    async def on_start(self):
        print(f"\nMeeting starts at {self.current_state}")

    async def on_end(self):
        print(f"\nMeeting ends at state {self.current_state}")
