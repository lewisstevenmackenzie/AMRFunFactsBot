# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionUtterFact(Action):

    def name(self) -> Text:
        return "action_utter_fact"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        #importing necessary libraries
        #import numpy as np
        import pandas as pd
        import os
        import csv
        import random as rnd


        # cur_path = os.path.dirname(__file__)
        # file_path = os.path.join(cur_path, '..\\dataset\\AntibioticFactsSheet.csv')
        
        
        facts = pd.read_csv('dataset\modulesMovieStyle2.csv')

        #factNumber = rnd.randint(0, len(facts) - 1)

        msg = facts['Part1'].iloc[2]

        print(msg)

        dispatcher.utter_message(text=msg)

        return []
