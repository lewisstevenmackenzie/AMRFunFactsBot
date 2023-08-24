# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, FollowupAction


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
        
        followUp = False
        #location = "0"
        facts = pd.read_csv('dataset/AntibioticFactsSheet3.csv')
        
        factsAsked = tracker.slots.get("factsAsked")
        moreInfo = tracker.slots.get("moreInfo")

        # if factsAsked is not None:

        #     factsAskedArray = factsAsked.split(",")

        #     for num in  factsAskedArray:
        #         index = "'" + num + "'"
        #         facts = facts[facts.Fact != index]
        # else:

        #     factsAsked = ""
        

        # factNumber = rnd.randint(0, len(facts) - 1)
        # print("FactNUMERO: " + str(factNumber))

        # if moreInfo is None:
        #     msg = facts['Part1'].iloc[factNumber]
        #     print("pt1: " + str(msg))

        # elif moreInfo == "0":
        #     msg = facts['Part1'].iloc[factNumber]
        #     print("pt1.5: " + str(msg))

        # else:
        #     location = "'Part" + str(1 + int(moreInfo) + "'")
            
        #     if facts[location].iloc[factNumber] != "":
        #         msg = facts[location].iloc[factNumber]
        #         print("pt2: " + str(msg))
           
        #     else:
        #         print("ERROR: nothing to print")

        # print("factNumber:" + str(facts['Fact'].iloc[factNumber]))
        # print("pt3: " + str(msg))

        # if moreInfo is None:
        #     if facts['Part2'].iloc[factNumber] == "" or pd.isnull(facts['Part2'].iloc[factNumber]):
        #         followUp = False
        #         print("part2 is ...:"+ str(facts['Part2'].iloc[factNumber]))
        #     else:
        #         followUp = True
        #         print("part2 is actually...:"+ str(facts['Part2'].iloc[factNumber]))
        #     location = "1"
        # else:
        #     location = "Part" + str(2 + int(moreInfo))
        #     #location = location + "'"
        #     if facts[location].iloc[factNumber] == "" or pd.isnull(facts[location].iloc[factNumber]):
        #         followUp = False
        #         moreInfo = "0"
        #     else:
        #         followUp = True
        #         location = str(1 + int(moreInfo))



        if factsAsked is not None:

            factsAskedArray = factsAsked.split(",")

            for num in factsAskedArray:
                index = "'" + num + "'"
                facts = facts[facts.Fact != index]
        else:

            factsAsked = ""


        factNumber = rnd.randint(0, len(facts) - 1)
        print("FactNUMERO: " + str(factNumber))

        if moreInfo is None:
            msg = facts['Part1'].iloc[factNumber]
            print("pt1: " + str(msg))

        elif moreInfo == "0":
            msg = facts['Part1'].iloc[factNumber]
            print("pt1.5: " + str(msg))

        else:
            location = "Part" + str(1 + int(moreInfo))

            factNumber = factsAskedArray[-1]
            print("Current fact NUMBERRRR: " + factNumber)
            factNumber = int(factNumber)-1

            #added a -1 here    !!!!!!!!!!!!!!!
            if facts[location].iloc[factNumber] is None:
                 print(" This VALUE IS NONE ")
            
            elif facts[location].iloc[factNumber] != "":
                msg = facts[location].iloc[factNumber]
                print("pt2: " + str(msg))

            else:
                print("ERROR: nothing to print")

        print("factNumber:" + str(facts['Fact'].iloc[factNumber]))
        print("pt3: " + str(msg))

        if moreInfo is None:
            if facts['Part2'].iloc[factNumber] == "" or pd.isnull(facts['Part2'].iloc[factNumber]):
                followUp = False
                print("part2 is ...:"+ str(facts['Part2'].iloc[factNumber]))
            else:
                followUp = True
                print("part2 is actually...:"+ str(facts['Part2'].iloc[factNumber]))
            location = "1"
        else:
            if moreInfo == "0":
                location = "Part" + str(2 + int(moreInfo))
            else:
                location = "Part" + str(2 + int(moreInfo))

            if facts[location].iloc[factNumber] == "" or pd.isnull(facts[location].iloc[factNumber]):
                followUp = False
                moreInfo = "0"
                print("pt4: Nothing to see here..........")
            else:
                followUp = True
                
                print("pt4.5: " + facts[location].iloc[factNumber])

                location = str(1 + int(moreInfo))

        #dispatcher.utter_message(text=msg)
        print(msg)
        factsAsked = factsAsked + "," + str(facts['Fact'].iloc[factNumber])

        slotToBeSet = "factsAsked"

        print("This is the facts asked: " + factsAsked)


        dispatcher.utter_message(text=msg)

        factsAsked = factsAsked + "," + str(facts['Fact'].iloc[factNumber])

        slotToBeSet = "factsAsked"

        # if  moreInfo is None:
        #     moreInfo = "1"
        # else:
        #     moreInfo = str(int(moreInfo) + 1)

        if followUp == True:
            return [FollowupAction("action_followUp_question"), SlotSet(slotToBeSet, factsAsked), SlotSet("moreInfo",location)]
        else:
            return [FollowupAction("action_noFollowUp_question"), SlotSet(slotToBeSet, factsAsked), SlotSet("moreInfo", "0")]
                

class ActionFollowUpQuestion(Action):

    def name(self) -> Text:
        return "action_followUp_question"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        msg = "Do you want to learn more about this fact?"

        dispatcher.utter_message(text=msg)

        return []
    

    
class ActionNoFollowUpQuestion(Action):

    def name(self) -> Text:
        return "action_noFollowUp_question"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


        msg = "That's all the information i have regarding this fact. Do you want to hear about another fact?"

        dispatcher.utter_message(text=msg)

        return [SlotSet("moreInfo", "0")]
    
class ActionDenyFollowUpQuestion(Action):

    def name(self) -> Text:
        return "action_another_question"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        msg = "Would you like to learn about another fact?"

        dispatcher.utter_message(text=msg)

        return [SlotSet("moreInfo", "0")]

class ActionWarnAntibioticUse(Action):

    def name(self) -> Text:
        return "action_warn_antibiotic_use"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        AntibioticWarning = tracker.slots.get("warnAntibiotics")

        if AntibioticWarning is None:

            msg = "Before being prescribed antibiotics from a GP it is vital that you understand the dangers that overprescribing this medication can lead to. Lately there has been an increase in antimicrobial resistance due to misprescribing, this has lead to antbiotics becoming less effective on patients that have required treatment. Hence, leading to an increased mortality rate."

        elif AntibioticWarning == "0":
            msg = "Before being prescribed antibiotics from a GP it is vital that you understand the dangers that overprescribing this medication can lead to. Lately there has been an increase in antimicrobial resistance due to misprescribing, this has lead to antbiotics becoming less effective on patients that have required treatment. Hence, leading to an increased mortality rate."
            
        elif AntibioticWarning == "1":
            msg = "Increased antimicrobial resistance is the cause of severe infections, complications, longer hospital stays and increased mortality. Overprescribing of antibiotics is associated with an increased risk of adverse effects, more frequent re-attendance and increased medicalization of self-limiting conditions."

        else:
            msg = "Error"
            print("\n Error in warning message.")

        dispatcher.utter_message(text=msg)

        return [SlotSet("warnAntibiotics", "1")]

class ActionFollowDoctorsOrders(Action):

    def name(self) -> Text:
        return "action_follow_doctors_instructions"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        msg = "You should follow the instuctions given to you by your doctor when the medication was prescribed. It is important to not stop your treatement early as this may result in the bacterial infection growing immune in the future."

        dispatcher.utter_message(text=msg)

        return []

class ActionAntibioticUse(Action):

    def name(self) -> Text:
        return "action_antibiotic_use"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        msg = "Antibiotics are used to treat or prevent some types of bacterial infections. They're not effective against viral infections, such as the common cold or flu. Antibiotics should only be prescribed to treat health problems: that are not serious but are unlikely to clear up without antibiotics – such as acne"

        dispatcher.utter_message(text=msg)

        return []


class ActionAntibioticUse(Action):

    def name(self) -> Text:
        return "action_antibiotic_alternatives"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        msg = "If your GP has determined that antibiotics are not required for treatment then there are a number of over the counter medications that can be taken to relieve pain. Ibuprofen and Paracetamol are a great place to start."

        dispatcher.utter_message(text=msg)

        return []
    

class ActionAntibioticsideaffects(Action):

    def name(self) -> Text:
        return "action_antibiotic_sideaffects"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        msg = "Antibiotics can have side effects such as diarrhoea and feeling sick. These side effects are usually mild and should pass once you finish your course of treatment. If you get any additional side effects, contact your GP or the doctor in charge of your care for advice."

        dispatcher.utter_message(text=msg)

        return []
    
# class ActionGeneralResponse(Action):

#     def name(self) -> Text:
#         return "action_general_response"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         msg = "I'm Sorry, I don't know how to assist you with this issue. Perhaps you can find the answer you're looking for here: https://www.nhs.uk/conditions/antibiotics/"
#         dispatcher.utter_message(text=msg)

#         return []