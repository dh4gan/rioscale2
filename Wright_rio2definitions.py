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
        #else:
            #print question
            #print answer
            
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

# 2 log(delta) +10 = J = A + B + C - 20
# delta = 10^( (A + B + C - 30)/2)


# Questions to find A

def ask_hypothesis_question(A, inputanswer=None):

    question= " Does the ETI hypothesis have explanatory power for the phenomenon?"
    options = {
               "y":6,
               "Y":6,
               "n":0,
               "N":0,
               }
    
    return ask_yesno_question(A,question,options,answer=inputanswer)


def ask_certainty_question(A, inputanswer=None):

    question= " Is there significant uncertainty about whether the phenomenon occurred or occurs at all?  \nFor instance, are the data corrupted, is there a significant risk of misunderstanding or transcription error?  \n'Significant' here means more than 10%."

    options = {
               "y":0,
               "Y":0,
               "n":1,
               "N":1,
               }
    
    return ask_yesno_question(A,question,options,answer=inputanswer)
    
    
def ask_multiple_question(A,inputanswer=None):
    question = "Has the phenomenon been observed more than once \n(different times, or different instruments, (including towards different targets))?."
    
    options = {
               "y":1,
               "Y":1,
               "n":0,
               "N":0,
               }
    
    return ask_yesno_question(A,question,options,answer=inputanswer)
    
    
def ask_multiplegroup_question(A,inputanswer=None):
    question = "Has the phenomenon been confirmed to be real and repeated, \nfor instance by multiple groups using a single instrument to observe the phenomenon for many instances \nor by observations of multiple instances from multiple instruments?"

    options = {
               "y":1,
               "Y":1,
               "n":0,
               "N":0,
               }
    
    return ask_yesno_question(A,question,options,answer=inputanswer)

def ask_routine_question(A,inputanswer=None):
    
    question = "Is the phenomenon observed routinely by different groups using different equipment?"

    options = {
               "y":1,
               "Y":1,
               "n":0,
               "N":0,
               }
    
    return ask_yesno_question(A,question,options,answer=inputanswer)
    
    
    
# Questions for B

def ask_instrument_question(B, inputanswer=None):
    
    question="Does the phenomenon look like a known instrumental or psychological effect?  \nExamples: DC channel in a filterbank file, cosmic rays in spectra, lens flare in photograph, known source of noise / bad data, reports of alien abduction, UFO sightings."
    
    options = {
               "y":0,
               "Y":0,
               "n":7,
               "N":7,
               }
    
    return ask_yesno_question(B,question,options,answer=inputanswer)
    
    
def ask_builders_question(B, inputanswer=None):
    
    question ="Have the instrument builders / experts in the method / observers of the phenomenon been consulted about the signal, \nand do they agree there is at least a reasonable chance it is real and not terrestrial? \n(10% confidence that the signal is astrophysical)"
     
    options = {
               "y":1,
               "Y":1,
               "n":0,
               "N":0,
               }
    
    return ask_yesno_question(B,question,options,answer=inputanswer)

    
def ask_50_question(B,inputanswer=None):
    
    question="Do the instrument builders / experts in the method / observers of the phenomenon \ngive at least even odds that it is astrophysical? (50% confidence)"
    
    options = {
               "y":1,
               "Y":1,
               "n":0,
               "N":0,
               }
    
    return ask_yesno_question(B,question,options,answer=inputanswer)

    
def ask_astrophysics_question(B,inputanswer=None):
    
    question ="Is the phenomenon unambiguously astrophysical?  \nFor instance, is there essentially no chance of instrumental/psychological error, \nAND is it clearly associated with an astrophysical source or otherwise clearly originating well beyond the atmosphere?"

    options = {
               "y":1,
               "Y":1,
               "n":0,
               "N":0,
               }
    
    return ask_yesno_question(B,question,options,answer=inputanswer)


# Questions for C

def hoax_question(C,inputanswer=None):
    question="Is the phenomenon consistent with a hoax?"

    options = {
               "y":0,
               "Y":0,
               "n":1,
               "N":1,
               }
    
    return ask_yesno_question(C,question,options,answer=inputanswer)
    
def anthropogenic_question(C,inputanswer=None):
    question= "Is the phenomenon consistent with a known and well understood natural or anthrophogenic phenomenon?"
    
    options = {
               "y":0,
               "Y":0,
               "n":2,
               "N":2,
               }
    
    return ask_yesno_question(C,question,options,answer=inputanswer)

def rare_question(C,inputanswer=None):
    
    question = "Is the phenomenon consistent with known but rare or poorly understood natural phenomena?"
    
    options = {
               "y":0,
               "Y":0,
               "n":3,
               "N":3,
               }
    
    return ask_yesno_question(C,question,options,answer=inputanswer)

def community_question(C,inputanswer=None):
    
    question="Has a wide community of experts in the relevant scientific field been engaged to determine \nwhat natural phenomena could be at play?"
    
    options = {
               "y":1,
               "Y":1,
               "n":0,
               "N":0,
               }
    
    return ask_yesno_question(C,question,options,answer=inputanswer)


def artificial_question(C,inputanswer=None):
    
    question = "Do only artificial explanations (that is, those requiring design and engineering) make sense?"
    
    options = {
               "y":2,
               "Y":2,
               "n":0,
               "N":0,
               }
    
    return ask_yesno_question(C,question,options,answer=inputanswer)
    
def message_question(C,inputanswer=None):
    
    question = "Is the phenomenon a communicated signal with clear intelligent content, or a physical object available for close (perhaps robotic) inspection?"
    
    options = {
               "y":1,
               "Y":1,
               "n":0,
               "N":0,
               }
    
    return ask_yesno_question(C,question,options,answer=inputanswer)


def calculate_J(A,B,C):
    
    J = A+B+C-20
    
    return J

def J_question(J,inputanswer=None):
    
    question="Is the phenomenon consistent with a prediction of the observable consequences of alien civilizations made by scientists other than the observers of the phenomenon? "

    options = {
               "y":0,
               "Y":0,
               "n":-1,
               "N":-1,
               }
    
    return ask_yesno_question(J,question,options,answer=inputanswer)

def calculate_delta(J):
    
    delta = pow(10.0,0.5*(J-10))
        
    
    return delta


def ask_all_delta_questions(hypothesisanswer=None, certainanswer=None,multanswer=None,groupanswer=None,routineanswer=None,instrumentanswer=None,buildersanswer=None, fiftyanswer=None, astrophysicsanswer=None, hoaxanswer=None, anthroanswer=None,rareanswer=None,communityanswer=None,artificialanswer=None, messageanswer=None, Janswer=None):

    A = 0
    B = 0
    C = 0

    Jzero = False
    
    # Calculate A
    
    
    A = ask_hypothesis_question(A,inputanswer=hypothesisanswer)
    
    if(A==0):
        Jzero=True
    
    if(A>0):
        A = ask_certainty_question(A, inputanswer=certainanswer)
    
        if(A>6):
            A = ask_multiple_question(A,inputanswer=multanswer)
        if(A>7):
            A = ask_multiplegroup_question(A,inputanswer=groupanswer)
            if(A>8):
                A = ask_routine_question(A,inputanswer=routineanswer)

    # Calculate B

    if(Jzero==False):
        B = ask_instrument_question(B, inputanswer=instrumentanswer)
        if(B>0):
            B = ask_builders_question(B, inputanswer=buildersanswer)
            if(B>7):
                B = ask_50_question(B,inputanswer=fiftyanswer)
                if(B>8):
                    B = ask_astrophysics_question(B,inputanswer=astrophysicsanswer)
    
    # Calculate C
    
    if(Jzero==False):
        C = hoax_question(C,inputanswer=hoaxanswer)
        if(C>0):
            C = anthropogenic_question(C,inputanswer=anthroanswer)
        else:
            Jzero = True
            
        if(Jzero==False):
            if(C>2):
                C = rare_question(C,inputanswer=rareanswer)
                if(C>5):
                    C = community_question(C,inputanswer=communityanswer)
                    if(C>6):
                        C = artificial_question(C,inputanswer=artificialanswer)
                        if(C>8):
                            C = message_question(C,inputanswer=messageanswer)
    
    # Calculate J
    
    if(Jzero):
        J=0
    else:
        J = calculate_J(A,B,C)
        J = J_question(J,inputanswer=Janswer)
    
    if(J<0):
        J=0
    delta = calculate_delta(J)

    return A,B,C,J,delta

