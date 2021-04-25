# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

import pandas as pd
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []



class ActionAskUsername(Action):

    def name(self) -> Text:
        return "action_ask_username"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        str((tracker.latest_message)['text'])
        dispatcher.utter_message(template="utter_ask_username")

        return []

class ActionAskPassword(Action):

    def name(self) -> Text:
        return "action_ask_password"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        str((tracker.latest_message)['text'])
        dispatcher.utter_message(template="utter_ask_password")

        return []

class ActionValidateUserAndUpdateStatus(Action):

    def name(self) -> Text:
        return "action_validate_user_and_update_status"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        messages = []
        print("tracker : ", tracker)
        for event in (list(tracker.events)):
            print("Event : ",event)
            if event.get("event") == "user":
                messages.append(event.get("text"))
        print("Messages : ",messages)


        user_name = messages[-2]
        password = str((tracker.latest_message)['text'])

        df_member_details = pd.read_csv('./ey_team_members_details.csv')
        df_status_tracker = pd.read_csv('./status_tracker.csv')
        
        result_text = f"""We are planning to schedule interview for the '{df_status_tracker.iloc[0]['Position']}' position
    
    You can find further details below:
    ---------------------------------------------------------------
    Candidate     - '{df_status_tracker.iloc[0]['Candidate']}'
    Recruiter     - '{df_status_tracker.iloc[0]['Recruiter']}'
    Interviewer1  - '{df_status_tracker.iloc[0]['Interviewer1']}'
    Interviewer2  - '{df_status_tracker.iloc[0]['Interviewer2']}'
    Interviewer3  - '{df_status_tracker.iloc[0]['Interviewer3']}'
    Location      - '{df_status_tracker.iloc[0]['Location']}'
    Start         - '{df_status_tracker.iloc[0]['Start']}' 
    End           - '{df_status_tracker.iloc[0]['End']}'  
    ----------------------------------------------------------------
    Shall we block this slot for you?  
  """

        dispatcher.utter_message(text=result_text)
        return []

class ActionUpdateMemberDetailsAccepted(Action):

    def name(self) -> Text:
        return "action_update_member_details_accepted"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Thank you, we will get back to you once the slot is confirmed by others as well")

        return []

class ActionUpdateMemberDetailsRejected(Action):

    def name(self) -> Text:
        return "action_update_member_details_rejected"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="No problem, I'll try to check another slot, and get back to you. Thank you")

        return []