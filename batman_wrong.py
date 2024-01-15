import time
import logging
from transitions.extensions.states import Timeout, Tags, add_state_features

from transitions_gui import WebMachine  # noqa


@add_state_features(Timeout, Tags)
class CustomMachine(WebMachine):
    pass


logging.basicConfig(level=logging.INFO)

states = ['a', 'b', 'batman', 'accepting']

transitions =transitions = [
    { 'trigger': 'Na', 'source': 'a', 'dest': 'b' },
    { 'trigger': 'na', 'source': 'b', 'dest': 'b' },    
    { 'trigger': 'Batman!', 'source': 'b', 'dest': 'batman' },
    { 'trigger': 'Batman!', 'source': 'batman', 'dest': 'batman' },
    { 'trigger': 'Na', 'source': 'batman', 'dest': 'b' },
    { 'trigger': 'ε', 'source': 'batman', 'dest': 'accepting'}
]


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