import sys
# Definitions for the Q questions

def ask_question(Q_old,question,options):
    ''' Basic framework for asking and answering Q questions'''
    
    increment = -1
    
    while increment <0:
    
        argument = input(question)
        increment = options.get(argument, -1)
        print increment
        if increment<0:
            print "Incorrect value entered, please try again"
 
    Q = Q_old+increment
   
    return Q

def ask_yesno_question(Q_old,question,options):
    ''' Basic framework for asking and answering Q questions'''
    
    increment = -1
    
    while increment <0:
    
        argument = raw_input(question)
        increment = options.get(argument, -1)
        print increment
        if increment<0:
            print "Incorrect value entered, please try again"
 
    Q = Q_old+increment
   
    return Q

def ask_nature_question(Q_old):
    
    question = "What is the nature of the signal?"
    question = question+"\n(1) UFO\n(2) Artifact\n(3) Electromagnetic (light) transmission\n(4) Gravitational Wave \n(5) Physical Encounter\n"
    
    options = {
        1: 0, # UFO
        2: 1, # Artifact
        3: 2, # EM transmission
        4: 3, # GW transmission
        5: 4, # Physical encounter
    }
    
    return ask_question(Q_old,question,options)

def ask_direction_question(Q_old):

    question = "Is the signal specifically directed at Earth? (y/n)"
    
    options = {
        "y": 1,
        "Y": 1, 
        "n": 0, 
        "N": 0, 
    }
      
    return ask_yesno_question(Q_old,question,options)


def ask_content_question(Q_old):

    question = "Does the signal contain any form of encoded message or data? (y/n)"
    
    options = {
        "y": 1,
        "Y": 1, 
        "n": 0, 
        "N": 0, 
    }
      
    return ask_yesno_question(Q_old,question,options)
       
def ask_distance_question(Q_old):

    question = "What is the estimated distance to the signal?"
    question = question+"\n(1)Within the Solar System \n(2) Within 50 light years \n(3) Within the Galaxy \n(4) Outside the Galaxy \n"

    options = {
                1:4, # Within the Solar System
                2:3, # Within 50 light years
                3:2, # Within the Galaxy
                4:1, # Outside the Galaxy
    }
   
    return ask_question(Q_old,question,options)
       

# Definitions for the delta questions

def check_for_zero_delta(delta):

    if(delta==0):
        print "Credibility is zero"
        print "Final Rio Score is R = 0"
        sys.exit()


def ask_source_question(delta):
    
    question = "Is the discoverer and/or the tools used peer-reviewable - that is, are their methods and practices open to inspection and scrutiny (y/n)?"
    answer = raw_input(question)
    
    if answer=='y' or answer=='Y':
        delta = delta+1
    elif answer=='n' or answer=="N":
        delta = 0
    
    check_for_zero_delta(delta)
    
    
    return delta


def ask_indep_question(delta):
    
    question = "Has the signal been confirmed independently by another team (y/n)?"
    answer = raw_input(question)
    
    if answer=='y' or answer=='Y':
        delta = delta+5
    elif answer=='n' or answer=="N":
        delta = 0
    
    check_for_zero_delta(delta)
    
    
    return delta
        


def ask_natural_question(delta):
    question = "Is there a plausible natural or anthropogenic explanation (y/n)?"
    answer = raw_input(question)
    
    if answer=='y' or answer=='Y':
        delta = 0
    elif answer=='n' or answer=="N":
        delta = delta + 3
    
    check_for_zero_delta(delta)
    
    
    return delta


def ask_instrument_question(delta):
    
    question = "Could the signal be caused by instrumental or data analysis effects (y/n)?"
    answer = raw_input(question)
    
    if answer=='y' or answer=='Y':
        delta = delta -4
    
    return delta

def ask_repeat_questiona(delta):
    
    question = "Is the signal repeating (y/n)?"
    answer = raw_input(question)
    
    if answer=='y' or answer=='Y':
        delta = delta +2
    
    return delta

def ask_hoax_question(delta):
    
    question = "Is it plausible it could be a hoax or faked (y/n)?"
    answer = raw_input(question)
    
    if answer=='y' or answer=='Y':
        delta = delta -2
    
    return delta






