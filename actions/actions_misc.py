from typing import Any, Text, Dict, List
from actions.utils import *
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from actions.constants import *


class ActionTellJoke(Action):
    def name(self) -> Text:
        return "action_tell_joke"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        joke = get_joke()
        dispatcher.utter_message(response="utter_tell_joke")
        dispatcher.utter_message(text=joke)
        return []
