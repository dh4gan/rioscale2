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
    
    info_content=False
    Q=0
    
    Q=ask_nature_question(Q, inputanswer=natureanswer)
    print "Q is ",Q

    Q=ask_direction_question(Q, inputanswer=directanswer)
    print "Q is ",Q

    Q_old = Q
    Q=ask_content_question(Q, inputanswer=contentanswer)
    diff = Q-Q_old
    if diff > 0.0: 
        info_content=True
    print "Q is ", Q

    Q=ask_distance_question(Q, inputanswer=distanceanswer)
    print "Q is ",Q   

    return Q, info_content


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

def ask_reanalyse_question(delta,inputanswer=None):
    
    question = "Has the signal been re-analysed by an independent team (y/n)?"
    
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
    
    question = "Has the signal been confirmed independently by another telescope/instrument (y/n)?"
    
    options = {
        "y": 2,
        "Y": 2, 
        "n": -100, 
        "N": -100, 
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

def ask_instrument_question(delta, inputanswer=None):
    
    question = "Could the signal be caused by instrumental or data analysis effects (y/n)?"
    question = question+"\n(1) Definitely Yes \n(2) Maybe Yes \n(3) Maybe No \n(4) Definitely No"

    options = {
                1:-4, # Definitely Yes
                2:-3, # Maybe Yes
                3:-2, # Maybe No
                4:0, # Definitely No
    }
    
    delta = ask_question(delta,question,options,answer=inputanswer)      
    delta = check_for_zero_delta(delta)
    
    return delta

def ask_natural_question(delta, inputanswer=None):
        
    question = "Is there a plausible natural or anthropogenic explanation?"
    question = question+"\n(1) Definitely Yes \n(2) Maybe Yes \n(3) Maybe No \n(4) Definitely No"
    
    options = {
                1:-100, # Definitely Yes
                2:1, # Maybe Yes
                3:2, # Maybe No
                4:3, # Definitely No
    }
    
    delta = ask_question(delta,question,options,answer=inputanswer)      
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

def ask_expert_question(delta,inputanswer=None):
    
    question = "Has a wide community of experts been consulted on the signal (y/n)?"
    
    options = {
        "y": 0,
        "Y": 0, 
        "n": -2, 
        "N": -2, 
    }
    
    delta = ask_yesno_question(delta,question,options,answer=inputanswer)      
    delta = check_for_zero_delta(delta)
    
    return delta

def ask_predict_question(delta,inputanswer=None):
    
    question = "Is the signal consistent with predictions for a signal from an extraterrestrial civilisation \nmade by scientists who did not make the observation?"
    
    options = {
        "y": 2,
        "Y": 2, 
        "n": -2, 
        "N": -2, 
    }
    
    delta = ask_yesno_question(delta,question,options,answer=inputanswer)      
    delta = check_for_zero_delta(delta)
    
    return delta


def ask_all_delta_questions(info_content, sourceanswer=None,analyseanswer=None,indepanswer=None,repeatanswer=None,instrumentanswer=None,naturalanswer=None,hoaxanswer=None, expertanswer=None,predictanswer=None):

    
    delta = 1
    if info_content: delta = 2
    
    delta = ask_source_question(delta, inputanswer=sourceanswer)
    if delta==0: return delta
    
    delta = ask_reanalyse_question(delta,inputanswer=analyseanswer)
    if delta==0: return delta
    
    delta = ask_indep_question(delta, inputanswer=indepanswer)
    if delta==0: return delta
    
    delta = ask_repeat_question(delta,inputanswer=repeatanswer)

    delta = ask_instrument_question(delta, inputanswer=instrumentanswer)
    if delta==0: return delta

    delta = ask_natural_question(delta, inputanswer=naturalanswer)
    if delta==0: return delta

    delta = ask_hoax_question(delta, inputanswer=hoaxanswer)

    
    delta = ask_expert_question(delta,inputanswer=expertanswer)
    if delta==0: return delta
    
    delta = ask_predict_question(delta, inputanswer=predictanswer)
    
    #delta = 0.8*pow(10,(delta-10)/2)
    delta = delta/13.0

    return delta

