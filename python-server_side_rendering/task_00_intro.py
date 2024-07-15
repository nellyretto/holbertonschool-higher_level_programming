#!/usr/bin/python3

template = "Hello {name}, You are invited to the {event_title} on {event_date} at {event_location}. We look forward to your presence. Best regards, Event Team"

def generate_invitation(templates, attendees):
    
    template = []

    attendees = []
    
    if isinstance(template,str):
        print("template is a string")
    else:
        print("template is not a string")


    if isinstance(attendees, list):
        print("attendess is a list")
    else:
        print("attendees is not a list")