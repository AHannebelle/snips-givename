import random


def small_talk_action(intent):
    if intent == "merci":
        response = random.choice(
            ["Je t'en prie", "avec plaisir", "ca me fait plaisir"])
        return response

    if intent == "congrats":
        response = random.choice(
            ["Merci !", "merci", "merci", "c'est gentil", "arrete, tu vas me faire rougir"])
        return response

    else:
        return 'Hmmm ' + intent
