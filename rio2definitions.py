# Module defines the questions for the Rio Scale 2.0
# including Q, delta and R itself


######################################
# Definitions for the Q questions
######################################

def ask_question(Q_old,question,options, answer=None,text=True):
    ''' Basic framework for asking and answering multiple choice questions'''
    
    increment = None
    while increment==None:
    
        if answer==None:
            answer = input(question)
        else:
            if(text):
                print "------------------------------------------"
                print question
                print answer
        
        increment = options.get(answer, -1)
            
        if increment==None:
            answer=None
            print "Incorrect value entered, please try again"
 
    Q = Q_old+increment
   
    return Q

def ask_yesno_question(Q_old,question,options,answer=None,text=True):
    ''' Basic framework for asking and answering yes/no questions'''
    
    increment = None
    
    
    while increment==None:
    
        if answer==None:
            answer = raw_input(question)
        else:
            if(text):
                print "------------------------------------------"
                print question
                print answer
            
        increment = options.get(answer, None)
        
        if increment==None:
            answer=None
            print "Incorrect value entered, please try again"
 
    Q = Q_old+increment
   
    return Q

def ask_where_question(Q_old,inputanswer=None,text=True):

    question = "What is the estimated light travel time to the signal?\n"
    question = question+"(1) Less than a day (i.e. within the Solar System) \n"
    question = question+"(2) days to years (i.e. about as close as the nearest star) \n"
    question = question+"(3) years to decades (in the solar neighbourhood) \n"
    question = question+"(4) Centuries to millennia (in the Galaxy)"
    question = question+"(4) Longer/Unknown\n"
    
    options = {
                1:4, # Within the Solar System
                2:3, # nearest star
                3:2, # solar neighborhood
                4:1, # in the Galaxy 
                5:0, #unknown
    }
   
    return ask_question(Q_old,question,options,answer=inputanswer,text=text)
    
def ask_comm_question(Q_old,inputanswer=None,text=True):
    question = "What are the prospects for communication with the signal?"
    question = question+"(1) We are in active two way communication \n"
    question = question+"(2) We could respond using the same medium/encoding as the signal within 20 years: \n"
    question = question+"(3) We can understand the signal or we have artifacts we can study \n"
    question = question+"(4) No communication is taking place \n"
    
    options = {
                1:4, # Two way
                2:3, # could respond
                3:2, # can understand
                4:0, # no communication
    }
   
    return ask_question(Q_old,question,options,answer=inputanswer,text=text)
    
def ask_aware_question(Q_old,inputanswer=None,text=True):
    question = "Is the sender aware of humanity and its technology?"
    question = question+"(1) Yes, certainly - the signal is intended for us, specifically: \n"
    question = question+"(2) Possibly, but there is little or no evidence for this: \n"
    question = question+"(3) Almost certainly not (e.g. they are too far away):  \n"
    question = question+"(4) Senders are apparently extinct \n"
    
    options = {
                1:2, # Two way
                2:1, # could respond
                3:0, # can understand
                4:-1, # no communication
    }
   
    return ask_question(Q_old,question,options,answer=inputanswer,text=text)
    

def ask_all_Q_questions(text=True,whereanswer=None,commanswer=None,awareanswer=None):
    
    Q=0
    
    Q = ask_where_question(Q,inputanswer=whereanswer,text=text)
    Q = ask_comm_question(Q,inputanswer=commanswer,text=text)
    Q = ask_aware_question(Q,inputanswer=awareanswer,text=text)

    return Q

######################################
# Definitions for the delta questions
######################################

# 2 log(delta) +10 = J = A + B + C - 20
# delta = 10^( (J-10)/2)

##################
# Questions for A
##################

def ask_certainty_question(A, inputanswer=None,text=True):

    question = "Is there significant uncertainty about whether the phenomenon occurred or occurs at all?\n"
    question = question+"For instance, are the data corrupted, is there a significant risk of misunderstanding or transcription error? \n"
    question = question+"'Significant' here means more than 10%."

    uncertain = False
    options = {
               "y":0,
               "Y":0,
               "n":1,
               "N":1,
               }
    
    A_old = A
    
    A = ask_yesno_question(A,question,options,answer=inputanswer,text=text)
    
    if(A==A_old):
        uncertain=True
    
    return A, uncertain

def ask_amenable_question(A, inputanswer=None,text=True):

    question = "How amenable to study is the phenomenon? Award between 0-3 points based upon the repeatability of the phenomena.\n"
    question = question + "(0) 0 pts: The phenomena has been observed exactly once\n"
    question = question + "(1) 1 pt: The phenomenon has been observed a small but plural number times, either as multiple targets showing similar phenomena,\n"
    question = question + " or a single target showing multiple similar events.\n"
    question = question + "(2) 2 pts: The phenomenon has been been confirmed to be real and repeated, for instance by multiple groups using a single instrument\n"
    question = question + "to observe the phenomenon or by an additional observation with a different instrument or from a different site.\n"
    question = question + "(3) 3 pts: The phenomenon is observed routinely by different groups using different equipment.\n"
    
    options = {
               0:0,
               1:1,
               2:2,
               3:3,
               }
     
    return ask_question(A,question,options,answer=inputanswer,text=text)
     
def ask_person_question(A,inputanswer=None,text=True):
    
    question = "Is the discoverer of the phenomenon the same person/group that predicted that such a phenomenon would indicate the presence of alien intelligence?\n"
    question = question+"People are natural wishful thinkers, and often see what they want to see, \n"
    question = question+ "so it gives extra credibility to a claim if the groups doing the prediction and those doing the discovery are not the same.\n"
    question = question+ "(y) The claimants predicted the phenomenon they 'discovered'\n"
    question = question+ "(n) The claimants did not predict this phenomenon"
    options = {
               "y":-1,
               "Y":-1,
               "n":0,
               "N":0,
            }
    
    return ask_yesno_question(A,question,options,answer=inputanswer,text=text)
    
    
    
def ask_A_questions(text=True,certainty=None, amenable=None,person=None):
    
    A=6
    
    A,uncertain = ask_certainty_question(A,inputanswer=certainty,text=text)
    
    if(uncertain==False):
        A=ask_amenable_question(A,inputanswer=amenable,text=text)
        A=ask_person_question(A,inputanswer=person,text=text)
        
    return A
    
##################
# Questions for B
##################

def ask_instrument_question(B, inputanswer=None,text=True):
    
    question="Does the phenomenon look like a known instrumental or psychological effect? \n"  
    question = question + "Examples: DC channel in a filterbank file, cosmic rays in spectra, \n"
    question = question + "lens flare in photograph, known source of noise / bad data,\n"
    question = question + "reports of alien abduction, UFO sightings."
    
    instrumental = False
    options = {
               "y":0,
               "Y":0,
               "n":7,
               "N":7,
               }
    
    B_old = B
    B = ask_yesno_question(B,question,options,answer=inputanswer,text=text)
    
    if(B==B_old):
        instrumental = True
    
    return B,instrumental
    
    
def ask_builders_question(B, inputanswer=None,text=True):
    
    question = "What chances do the instrument builders / experts in the method / observers of the phenomenon give that the signal\n"
    question = question+"is not instrumental?\n"
    question = question+ "Award between 0 and 3 points\n"
    question = question + "(0) 0 pt: These experts have not weighed in at all\n"
    question = question + "(1) 1 pt: 1 point: These experts give a ~90% chance that it is instrumental (so a ~10% it is real)\n"
    question = question + "(2) 2 pts: These experts give even odds that it is instrumental\n"
    question = question + "(3) 3 points: These experts give less that 10% chance that it is instrumental\n"
  
    options = {
               0:0,
               1:1,
               2:2,
               3:3,
               }
    
    return ask_question(B,question,options,answer=inputanswer,text=text)


def ask_B_questions(instrument=None, builders=None,text=True):
    
    B = 0
    B,instrumental = ask_instrument_question(B,inputanswer=instrument,text=text)
    
    if(instrumental==False):
        B = ask_builders_question(B,inputanswer=builders,text=text)
        
    return B
    
###################
# Questions for C
###################

def ask_hoax_question(C,inputanswer=None,text=True):
    question="Is there good reason to believe the phenomenon is consistent with a hoax?"

    hoax = False
    options = {
               "y":0,
               "Y":0,
               "n":1,
               "N":1,
               }
    
    C_old = C
    C = ask_yesno_question(C,question,options,answer=inputanswer,text=text)
    
    if(C_old == C):
        hoax = True

    return C, hoax

def ask_community_question(C,inputanswer=None,text=True):
    
    question = "How does a wide community of experts assess the probability that there any known sources of natural or anthropogenic signal\n"
    question = question + "that could explain the phenomenon?\n"
    question = question + "Assign a score between 0-9 points:\n"
    question = question + "(0) 0 pt : A wide range of experts of the relevant natural or anthropogenic phenomena has not been consulted\n"
    question = question + "(1) 1 pt : It is consistent with a known phenomenon\n"
    question = question + "(3) 3 pts: It is consistent *only* with rare or poorly-understood phenomena\n"
    question = question + "(6) 6 pts: It is not consistent with any known natural or anthropogenic phenomena\n"
    question = question + "(8) 8 pts: *Only* extraterrestrial, artificial explanations make sense\n"
    question = question + "(9) 9 pts: The phenomenon contains information content of clearly intelligent design\n"
    
    
    
    options = {
               0:0,
               1:1,
               2:2,
               3:3,
               4:4,
               5:5,
               6:6,
               7:7,
               8:8,
               9:9,
               10:10,
               }
    
    C = ask_question(C,question,options,answer=inputanswer,text=text)

    return C


def ask_C_questions(hoax=None, community=None,text=True):
    
    C = 0
    Jzero=False
    C,ishoax = ask_hoax_question(C,inputanswer=hoax,text=text)
    
    if(ishoax):
        Jzero=True
    else:
        C = ask_community_question(C,inputanswer=community,text=text)
        
    return C, Jzero

def calculate_J(A,B,C):
    
    J = A+B+C-20
    
    return J

def calculate_delta(J):
    
    delta = pow(10.0,0.5*(J-10))
        
    return delta


def ask_all_delta_questions(text=True,certaintyanswer=None, amenableanswer=None,personanswer=None, instrumentanswer=None,buildersanswer=None,hoaxanswer=None,communityanswer=None):
    
    # Calculate A, B, C
    
    A = ask_A_questions(certainty=certaintyanswer,amenable=amenableanswer,person=personanswer, text=text)
    B = ask_B_questions(instrument=instrumentanswer,builders=buildersanswer,text=text)
    C,Jzero = ask_C_questions(hoax=hoaxanswer, community=communityanswer,text=text)
    
    # Calculate J
    
    if(Jzero):
        J=0
    else:
        J = calculate_J(A,B,C)

    
    if(J<0):
        J=0

    delta = calculate_delta(J)

    return A,B,C,J,delta

