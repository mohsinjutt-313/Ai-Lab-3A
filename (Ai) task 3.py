class ModelBasedReflexAgent:
    def __init__(self, desired_temperature):
        self.desired_temperature = desired_temperature
        self.previous_action = None

    def act(self, current_temperature):
        if current_temperature < self.desired_temperature and self.previous_action != "Turn on heater":
            action = "Turn on heater"
        elif current_temperature >= self.desired_temperature and self.previous_action != "Turn off heater":
            action = "Turn off heater"
        else:
            action = "No change"
        self.previous_action = action
        return action

rooms = {
    "Living Room": 18,
    "Bedroom": 22,
    "Kitchen": 20,
    "Bathroom": 24
}
desired_temperature = 22
agent = ModelBasedReflexAgent(desired_temperature)

for room, temperature in rooms.items():
    action = agent.act(temperature)
    print(f"{room}: Current temperature = {temperature}°C. {action}.")