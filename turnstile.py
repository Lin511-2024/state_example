import time
import logging
from transitions.extensions.states import Timeout, Tags, add_state_features


from transitions_gui import WebMachine  # noqa


@add_state_features(Timeout, Tags)
class CustomMachine(WebMachine):
    pass


logging.basicConfig(level=logging.INFO)

states = ['locked', "unlocked"]

transitions =transitions = [
    { 'trigger': 'push', 'source': 'locked', 'dest': 'locked' },
    { 'trigger': 'coin', 'source': 'locked', 'dest': 'unlocked' },
    { 'trigger': 'push', 'source': 'unlocked', 'dest': 'locked' },
    { 'trigger': 'coin', 'source': 'unlocked', 'dest': 'unlocked' }
]

class Model(object):
    pass


machine = CustomMachine(Model(), states=states, transitions=transitions, initial='locked',
                     name="System State",
                     ignore_invalid_triggers=True,
                     auto_transitions=False)

try:
    while True:
        time.sleep(5)
except KeyboardInterrupt:  # Ctrl + C will shutdown the machine
    machine.stop_server()