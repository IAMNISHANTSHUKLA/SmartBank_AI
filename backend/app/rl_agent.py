def generate_suggestion(user_id: int):
    actions = ["Save 20% more this month", "Invest in low-risk funds", "Cut down discretionary spending"]
    import random
    return random.choice(actions)
