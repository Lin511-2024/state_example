import time
import logging
from transitions.extensions.states import Timeout, Tags, add_state_features

from transitions_gui import WebMachine  # noqa


@add_state_features(Timeout, Tags)
class CustomMachine(WebMachine):
    pass


logging.basicConfig(level=logging.INFO)

states = ['a', 'b','c','d','e','f','g','h','i','j','k','l', 'batman1','batman2','batman3','accepting']

transitions =transitions = [
    { 'trigger': 'Na', 'source': 'a', 'dest': 'b' },
    { 'trigger': 'Batman!', 'source': 'l', 'dest': 'batman1' },
    { 'trigger': 'Batman!', 'source': 'batman1', 'dest': 'batman2' },
    { 'trigger': 'Batman!', 'source': 'batman2', 'dest': 'batman3' },
    { 'trigger': 'Na', 'source': 'batman1', 'dest': 'b' },
    { 'trigger': 'Na', 'source': 'batman3', 'dest': 'b' },
    { 'trigger': 'ε', 'source': 'batman1', 'dest': 'accepting'}
]

na_labels = 'bcdefghijkl'
for idx, label in enumerate(na_labels):
    if idx+1 < len(na_labels):
        transitions.append(
            {'trigger': 'na', 'source': label, 'dest': na_labels[idx+1]}
        )

class Model(object):
    pass


machine = CustomMachine(Model(), states=states, transitions=transitions, initial='a',
                     name="Batman!",
                     ignore_invalid_triggers=True,
                     auto_transitions=False)

try:
    while True:
        time.sleep(5)
except KeyboardInterrupt:  # Ctrl + C will shutdown the machine
    machine.stop_server()