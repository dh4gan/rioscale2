import sys
# Definitions for the Q questions

def ask_question(Q_old,question,options, answer=None):
    ''' Basic framework for asking and answering multiple choice questions'''
    
    increment = None
    
    while increment==None:
    
        if answer==None:
            answer = input(question)
        else:
            print question
            print answer
        
        increment = options.get(answer, -1)
            
        if increment==None:
            answer=None
            print "Incorrect value entered, please try again"
 
    Q = Q_old+increment
   
    return Q

def ask_yesno_question(Q_old,question,options,answer=None):
    ''' Basic framework for asking and answering yes/no questions'''
    
    increment = None
    
    while increment==None:
    
        if answer==None:
            answer = raw_input(question)
        else:
            print question
            print answer
            
        increment = options.get(answer, None)
        
        if increment==None:
            answer=None
            print "Incorrect value entered, please try again"
 
    Q = Q_old+increment
   
    return Q

def ask_nature_question(Q_old, inputanswer=None):
    
    question = "What is the nature of the signal?"
    question = question+"\n(1) UFO\n(2) Artifact\n(3) Electromagnetic (light) transmission\n(4) Gravitational Wave \n(5) Physical Encounter\n"
    
    options = {
        1: 0, # UFO
        2: 1, # Artifact
        3: 2, # EM transmission
        4: 3, # GW transmission
        5: 4, # Physical encounter
    }
    
    return ask_question(Q_old,question,options,answer=inputanswer)

def ask_direction_question(Q_old,inputanswer=None):

    question = "Is the signal specifically directed at Earth? (y/n)"
    
    options = {
        "y": 1,
        "Y": 1, 
        "n": 0, 
        "N": 0, 
    }
      
    return ask_yesno_question(Q_old,question,options,answer=inputanswer)


def ask_content_question(Q_old,inputanswer=None):

    question = "Does the signal contain any form of encoded message or data? (y/n)"
    
    options = {
        "y": 1,
        "Y": 1, 
        "n": 0, 
        "N": 0, 
    }
      
    return ask_yesno_question(Q_old,question,options,answer=inputanswer)
       
def ask_distance_question(Q_old,inputanswer=None):

    question = "What is the estimated distance to the signal?"
    question = question+"\n(1) Within the Solar System \n(2) Within 50 light years \n(3) Within the Galaxy \n(4) Outside the Galaxy \n(5) Unknown \n"

    options = {
                1:4, # Within the Solar System
                2:3, # Within 50 light years
                3:2, # Within the Galaxy
                4:1, # Outside the Galaxy
                5:1, # Unknown
    }
   
    return ask_question(Q_old,question,options,answer=inputanswer)
    
    
def ask_all_Q_questions(natureanswer=None,directanswer=None,contentanswer=None,distanceanswer=None):
    
    
    Q=0
    
    Q=ask_nature_question(Q, inputanswer=natureanswer)
    print "Q is ",Q

    Q=ask_direction_question(Q, inputanswer=directanswer)
    print "Q is ",Q

    Q=ask_content_question(Q, inputanswer=contentanswer)
    print "Q is ", Q

    Q=ask_distance_question(Q, inputanswer=distanceanswer)
    print "Q is ",Q   

    return Q


# Definitions for the delta questions

def check_for_zero_delta(delta):

    if(delta<=0):
        print "Credibility is zero"
        print "Final Rio Score is R = 0"
        delta = 0
        
    return delta


def ask_source_question(delta, inputanswer=None):
    
    question = "Is the discoverer and/or the tools used peer-reviewable - that is, are their methods and practices open to inspection and scrutiny (y/n)?"
    
    options = {
        "y": 1,
        "Y": 1, 
        "n": -100, 
        "N": -100, 
    }
    
    delta = ask_yesno_question(delta,question,options,answer=inputanswer)
        
    delta = check_for_zero_delta(delta)
    
    return delta


def ask_indep_question(delta,inputanswer=None):
    
    question = "Has the signal been confirmed independently by another team (y/n)?"
    
    options = {
        "y": 5,
        "Y": 5, 
        "n": -100, 
        "N": -100, 
    }
    
    delta = ask_yesno_question(delta,question,options,answer=inputanswer)      
    delta = check_for_zero_delta(delta)
    
    return delta


def ask_natural_question(delta, inputanswer=None):
    
    question = "Is there a plausible natural or anthropogenic explanation (y/n)?"
    options = {
        "y": -100,
        "Y": -100, 
        "n": 3, 
        "N": 3, 
    }
    
    delta = ask_yesno_question(delta,question,options,answer=inputanswer)      
    delta = check_for_zero_delta(delta)
    
    return delta


def ask_instrument_question(delta, inputanswer=None):
    
    question = "Could the signal be caused by instrumental or data analysis effects (y/n)?"
    
    options = {
        "y": -4,
        "Y": -4, 
        "n": 0, 
        "N": 0, 
    }
    
    delta = ask_yesno_question(delta,question,options,answer=inputanswer)      
    delta = check_for_zero_delta(delta)
    
    return delta

def ask_repeat_question(delta,inputanswer=None):
    
    question = "Is the signal repeating (y/n)?"
    
    options = {
        "y": 2,
        "Y": 2, 
        "n": 0, 
        "N": 0, 
    }
    
    delta = ask_yesno_question(delta,question,options,answer=inputanswer)      
    delta = check_for_zero_delta(delta)
    
    return delta

def ask_hoax_question(delta,inputanswer=None):
    
    question = "Is it plausible it could be a hoax or faked (y/n)?"
    
    options = {
        "y": -2,
        "Y": -2, 
        "n": 0, 
        "N": 0, 
    }
    
    delta = ask_yesno_question(delta,question,options,answer=inputanswer)      
    delta = check_for_zero_delta(delta)
    
    return delta


def ask_all_delta_questions(sourceanswer=None,indepanswer=None,naturalanswer=None,instrumentanswer=None,repeatanswer=None,hoaxanswer=None):

    delta = 1

    delta = ask_source_question(delta, inputanswer=sourceanswer)
    
    print "delta is ",delta
    if delta==0: return delta
    

    delta = ask_indep_question(delta, inputanswer=indepanswer)
    print "delta is ",delta
    if delta==0: return delta

    delta = ask_natural_question(delta, inputanswer=naturalanswer)
    print "delta is ",delta
    if delta==0: return delta
    
    delta = ask_instrument_question(delta, inputanswer=instrumentanswer)
    print "delta is ",delta
    if delta==0: return delta
    
    delta = ask_repeat_question(delta,inputanswer=repeatanswer)
    print "delta is ", delta

    delta = ask_hoax_question(delta, inputanswer=hoaxanswer)
    print "delta is ",delta
    
    
    delta = delta/10.0

    return delta

