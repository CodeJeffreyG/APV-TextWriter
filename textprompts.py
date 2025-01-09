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
        ,"Resolution? :"
    ]
    pyperclip.copy("\n\n".join(questions));
    print("injury questions copied.")

def clipboard_urgent_care_questions_gi():
    """
    Returns a single string of urgent care questions formatted for easy copying.
    """
    questions = [
        "What seems to be the issue or concern?: ",
        "When did the incident or symptoms start?: ",
        "Is your animal's behavior normal?: ",
        "Is your pet currently eating, drinking, urinating, or defecating normally?: ",
        "What does the stool/vomit look like? (foam, blood, undigested food?): ",
        "Has your pet's diet changed recently? If so, what changed?: ",
        "What has your pet eaten in the last 24-48 hours?: ",
        "Has your pet had access to garbage, toxins, or foreign objects?: ",
        "How frequent are the episodes (vomiting, diarrhea, etc.)?: ",
        "Is your pet showing signs of discomfort, such as bloating or straining to defecate?: ",
        "Have you noticed any weight loss, lethargy, or dehydration symptoms?: ",
        "Has your pet been treated with any medications, dewormers, or supplements recently?: ",
        "Has your pet had a history of GI issues or sensitivities in the past?: ",
        "Are there any other pets in the household experiencing similar symptoms?: "
        ,"Resolution? :"
    ]
    pyperclip.copy("\n\n".join(questions))
    print("GI questions copied.")

def clipboard_urgent_care_questions_ear():
    """
    Returns a single string of urgent care questions formatted for easy copying.
    """
    questions = [
        "How long has the ear infection persisted?: ",
        "Is your animal's behavior normal?: ",
        "Is your pet currently eating, drinking, urinating, or defecating normally?: ",
        "Has your pet been shaking their head or scratching their ears excessively?: ",
        "Have you noticed any redness, swelling, or discharge in the ear?: ",
        "Does your pet seem sensitive or in pain when you touch their ear?: ",
        "Have you noticed an unusual odor coming from the ear?: ",
        "Has your pet had any history of ear infections or ear-related issues in the past?: ",
        "Have you tried any treatments or interventions at home (e.g., ear cleaning, medications)?: ",
        "Are there any other symptoms you’ve observed, such as balance issues or head tilting?: "
        ,"Resolution? :"
    ]
    pyperclip.copy("\n\n".join(questions))
    print("Ear questions copied.")

def clipboard_urgent_care_questions_uri():
    """
    Returns a single string of urgent care questions formatted for easy copying.
    """
    questions = [
        "How long has your pet been showing symptoms of a respiratory infection?: ",
        "Is your animal's behavior normal?: ",
        "Is your pet currently eating, drinking, urinating, or defecating normally?: ",
        "Have you noticed any nasal discharge? If so, what color and consistency is it?: ",
        "Is your pet sneezing, coughing, or wheezing? If so, how frequently?: ",
        "Does your pet seem to have difficulty breathing or show signs of labored breathing?: ",
        "Have you noticed any changes in your pet's voice or vocalizations (e.g., hoarseness)?: ",
        "Has your pet been lethargic or less active than usual?: ",
        "Have there been any changes in your pet's appetite or water consumption?: ",
        "Has your pet been exposed to other animals that might be sick?: ",
        "Have you tried any treatments or interventions at home (e.g., humidifier, medications)?: "
        ,"Resolution? :"
    ]
    pyperclip.copy("\n\n".join(questions))
    print("URI questions copied.")

def clipboard_rx_clientrequest_meds():
    information = [
        "What medication did the client request?: "
        "What is the quantity?: "
    ]
    pyperclip.copy("\n\n".join(information))

def clipboard_rx_pharmacyrequest_meds():
    """
    Returns a single string of pharmacy medication request questions formatted for easy copying.
    """
    questions = [
        "What is the name of the pharmacy?: ",
        "What is the name of the person I am speaking with?: ",
        "What is the name of the medication being requested?: ",
        "What is the quantity of the medication being requested?: ",
        "What is the dosage and frequency of administration?: ",
        "Has this medication been filled here previously?: ",
        "Is there a specific urgency for the medication refill?: ",
        "Is there a prescription ID or reference number for the request?: ",
        "Are there any special instructions or notes from the pharmacy?: ",
        "What is the pharmacy's contact number if a follow-up is needed?: ",
        
    ]
    pyperclip.copy("\n\n".join(questions))
    print("Pharmacy medication request questions copied.")

def clipboard_fecal_PCR_negative(boolean):
    if boolean:
        pyperclip.copy("Results - FECAL PCR - ALL NEGATIVE / LM")
    else:
        pyperclip.copy("Results - FECAL PCR - ALL NEGATIVE / SWO")
        

def clipboard_fecal_generic_call():
    """
    Copies a generic call update template to the clipboard.
    """
    message = "UPDATE: [Reason] / When it happened / Symptoms / Resolution"
    pyperclip.copy(message)
    print("Generic call update copied to clipboard.")

