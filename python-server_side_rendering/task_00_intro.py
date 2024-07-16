#!/usr/bin/python3

import os

def generate_invitations(template, attendees):
    if not isinstance(template, str):
        raise TypeError("Template must be a string")
    
    if not isinstance(attendees, list) or not all(isinstance(item, dict) for item in attendees):
        raise TypeError("Attendees must be a list of dictionaries")
         
    if not template == "":
        raise ValueError("Template is empty")
    
    if len(attendees) == 0:
        raise ValueError("Attendees list is empty")
    
    for index, attendee in enumerate(attendees, start=1):
        modified_template = template.replace("{name}", attendee.get('name', 'N/A'))
        modified_template = modified_template.replace("{event_title}", attendee.get('event_title', 'N/A'))
        modified_template = modified_template.replace("{event_date}", attendee.get('event_date', 'N/A'))
        modified_template = modified_template.replace("{event_location}", attendee.get('event_location', 'N/A'))

        output_file = f"output_{index}.txt"

        with open(output_file, 'w') as file:
            file.write(modified_template)