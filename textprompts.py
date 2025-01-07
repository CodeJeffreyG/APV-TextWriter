import pyperclip

def clipboard_urgent_care_questions_injury():
    """
    Returns a single string of urgent care questions formatted for easy copying.
    """
    questions = [
        
        "What seems to be the issue or concern?: ",
        "When did the incident or symptoms start?: ",
        "Is your animals behavior normal?: ",
        "Is your pet currently eating, drinking, urinating, or defecating normally?: ",
        "What was injured or affected? Can you describe the condition (e.g., swelling, bleeding, etc.)?: ",
        "Has your pet eaten or drank anything unusual recently?",
        "Is your pet experiencing any pain or discomfort? If so, how severe does it seem?: ",
        "Have there been any changes in behavior (e.g., lethargy, aggression, hiding)?: ",
        "Have you tried any treatments or interventions at home (e.g., first aid, over-the-counter medication)?: ",
        "Is your pet able to stand, walk, or move normally?: "
    ]
    pyperclip.copy("\n\n".join(questions));
    print("injury questions copied.")

