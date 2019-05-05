#!/usr/bin/env python2
from hermes_python.hermes import Hermes

from ask_time import ask_time_action
from ask_name import ask_name_action
from small_talk import small_talk_action

MQTT_IP_ADDR = "localhost"
MQTT_PORT = 1883
MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT))

INTENT_PREFIX = 'Arkantos:'


def parse_intent_name(intent_name):
    if intent_name[:len(INTENT_PREFIX)] == INTENT_PREFIX:
        return intent_name[len(INTENT_PREFIX):]
    return intent_name


def on_intent_received(hermes, intent_message):
    intent_name = parse_intent_name(intent_message.intent.intent_name)
    response = ''

    if intent_name == 'giveName':
        if len(intent_message.slots.name) > 0:
            name = intent_message.slots.name.first().value
            response = ask_name_action(name)
    elif intent_name == 'askTime':
        response = ask_time_action()
    else:
        response = small_talk_action(intent_name)

    hermes.publish_end_session(intent_message.session_id, response)


with Hermes(MQTT_ADDR) as h:
    h.subscribe_intents(on_intent_received).start()
