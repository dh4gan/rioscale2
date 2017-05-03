# Module defines the questions for the Rio Scale 2.0
# including Q, delta and R itself


######################################
# Definitions for the Q questions
######################################

def ask_question(Q_old,question,options, answer=None):
    ''' Basic framework for asking and answering multiple choice questions'''
    
    increment = None
    
    print "------------------------------------------"
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
    
    print "------------------------------------------"
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
    
    question = "What is the nature of the signal? (select one of the 7 options) \n\n"
    
    question = question+"------------------------\n"
    question = question+"Manufactured Artifact:\n"
    question = question+"------------------------\n"
    question = question+"(1) Small Probe / Pieces of Alien Technology\n"
    question = question+"(2) Spacecraft capable of carrying macroscopic organisms\n"
    question = question+"(3) Megastructure\n"
    question = question+"------------------------\n"
    question = question+"Transmission: \n"
    question = question+"------------------------\n"
    question = question+"(4) Electromagnetic (radio, visible or other form of light)\n"
    question = question+"(5) Neutrino or other high energy particle\n"
    question = question+"(6) Gravitational Waves\n"
    
    question = question+"------------------------\n"
    question = question+"Close Encounter \n"
    question = question+"------------------------\n"
    question = question+"(7)Physical Encounter with alien(s)\n"
      
    options = {
        1: 1, # Small probe / pieces of alien tech
        2: 2, # Larger spacecraft
        3: 3, # Megastructure
        4: 1, # EM transmission
        5: 2, # Neutrino transmission
        6: 3,  # GW transmission
        7: 3, # Physical encounter
    }
    
    return ask_question(Q_old,question,options,answer=inputanswer)




def ask_content_question(Q_old,inputanswer=None):

    question = "Does the signal contain clear evidence of an encoded message or data? (y/n)"
    
    options = {
        "y": 1,
        "Y": 1, 
        "n": 0, 
        "N": 0, 
    }
      
    return ask_yesno_question(Q_old,question,options,answer=inputanswer)
    
def ask_direction_question(Q_old,inputanswer=None):

    question = "Has the origin of the signal been accurately located (either on the sky, or nearby)? (y/n)"
    
    options = {
        "y": 1,
        "Y": 1, 
        "n": 0, 
        "N": 0, 
    }
      
    return ask_yesno_question(Q_old,question,options,answer=inputanswer)
       
def ask_distance_question(Q_old, inputanswer=None):
    
    question = "Has the distance to the signal been accurately determined? (y/n)"
    
    options = {
        "y": 1,
        "Y": 1, 
        "n": 0, 
        "N": 0, 
    }
      
    return ask_yesno_question(Q_old,question,options,answer=inputanswer)
           

def ask_where_question(Q_old,inputanswer=None):

    question = "What is the estimated distance to the signal?\n"
    question = question+"(1) Within the Solar System \n"
    question = question+"(2) Within the Galaxy \n"
    question = question+"(3) Beyond the Galaxy/unknown\n"
    
    options = {
                1:2, # Within the Solar System
                2:1, # Within the Galaxy
                3:0, # Outside the Galaxy/unknown
    }
   
    return ask_question(Q_old,question,options,answer=inputanswer)
    
    
def ask_all_Q_questions(natureanswer=None,directanswer=None,contentanswer=None,distanceanswer=None,whereanswer=None):
    
    Q=0
    
    Q=ask_nature_question(Q, inputanswer=natureanswer)
    Q=ask_content_question(Q, inputanswer=contentanswer)
    Q=ask_direction_question(Q, inputanswer=directanswer)
    Q=ask_distance_question(Q, inputanswer=distanceanswer)
    Q=ask_where_question(Q, inputanswer=whereanswer)

    return Q

######################################
# Definitions for the delta questions
######################################

# 2 log(delta) +10 = J = A + B + C - 20
# delta = 10^( (J-10)/2)

##################
# Questions for A
##################

def ask_certainty_question(A, inputanswer=None):

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
    
    A = ask_yesno_question(A,question,options,answer=inputanswer)
    
    if(A==A_old):
        uncertain=True
    
    return A, uncertain

def ask_amenable_question(A, inputanswer=None):

    question = "How amenable to study is the phenomenon? Award between 0-3 points based upon the repeatability of the phenomena.\n"
    question = question + "(0) 0 pts: The phenomena has been observed exactly once\n"
    question = question + "(1) 1 pt: The phenomenon has been observed a small but plural number times, either as multiple targets showing similar phenomena,\n"
    question = question + " or a single target showing multiple similar events.\n"
    question = question + "(2) 2 pts: The phenomenon has been been confirmed to be real and repeated, for instance by multiple groups using a single instrument\n"
    question = question + "to observe the phenomenon or by an additional observation with a different instrument or from a different site.\n"
    question = question + "(3) 3 pts: The phenomenon is observed routinely by different groups using different equipment.\n"
    
    options = {
               "0":0,
               "1":1,
               "2":2,
               "3":3,
               }
     
    return ask_yesno_question(A,question,options,answer=inputanswer)
     
def ask_person_question(A,inputanswer=None):
    
    question = "Is the discoverer of the phenomenon the same person/group that predicted that such a phenomenon would indicate the presence of alien intelligence?\n"
    question = question+"People are natural wishful thinkers, and often see what they want to see, \n"
    question = question+ "so it gives extra credibility to a claim if the groups doing the prediction and those doing the discovery are not the same.\n"
    question = question+ "(y) The claimants predicted the phenomenon they 'discovered'\n"
    question = question+ "(n) The claimants did not predict this phenomenon"
    options = {
               "y":0,
               "Y":0,
               "n":7,
               "N":7,
            }
    
    return ask_yesno_question(A,question,options,answer=inputanswer)
    
    
    
def ask_A_questions(certainty=None, amenable=None,person=None):
    
    A=6
    
    A,uncertain = ask_certainty_question(A,inputanswer=certainty)
    
    if(uncertain==False):
        A=ask_amenable_question(A,inputanswer=amenable)
        A=ask_person_question(A,inputanswer=person)
        
    return A
    
##################
# Questions for B
##################

def ask_instrument_question(B, inputanswer=None):
    
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
    B = ask_yesno_question(B,question,options,answer=inputanswer)
    
    if(B==B_old):
        instrumental = True
    
    return B,instrumental
    
    
def ask_builders_question(B, inputanswer=None):
    
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
    
    return ask_question(B,question,options,answer=inputanswer)


def ask_B_questions(instrument=None, builders=None):
    
    B = 0
    B,instrumental = ask_instrument_question(B,inputanswer=instrument)
    
    if(instrumental==False):
        B = ask_builders_question(B,inputanswer=builders)
        
    return B
    
###################
# Questions for C
###################

def ask_hoax_question(C,inputanswer=None):
    question="Is there good reason to believe the phenomenon is consistent with a hoax?"

    hoax = False
    options = {
               "y":0,
               "Y":0,
               "n":1,
               "N":1,
               }
    
    C_old = C
    C = ask_yesno_question(C,question,options,answer=inputanswer)
    
    if(C_old == C):
        hoax = True
    
    print C
    return C, hoax

def ask_community_question(C,inputanswer=None):
    
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
               3:3,
               6:6,
               8:8,
               9:9,
               }
    
    C = ask_question(C,question,options,answer=inputanswer)
    print C
    return C


def ask_C_questions(hoax=None, community=None):
    
    C = 0
    Jzero=False
    C,ishoax = ask_hoax_question(C,inputanswer=hoax)
    
    if(ishoax):
        Jzero=True
    else:
        C = ask_community_question(C,inputanswer=community)
        
    print C,Jzero
    return C, Jzero

def calculate_J(A,B,C):
    
    J = A+B+C-20
    
    return J

def calculate_delta(J):
    
    delta = pow(10.0,0.5*(J-10))
        
    return delta


def ask_all_delta_questions(certaintyanswer=None, amenableanswer=None,personanswer=None, instrumentanswer=None,buildersanswer=None,hoaxanswer=None,communityanswer=None):
    
    
    # Calculate A, B, C
    
    A = ask_A_questions(certainty=certaintyanswer,amenable=amenableanswer,person=personanswer)
    B = ask_B_questions(instrument=instrumentanswer,builders=buildersanswer)
    C,Jzero = ask_C_questions(hoax=hoaxanswer, community=communityanswer)
    
    # Calculate J
    
    if(Jzero):
        J=0
    else:
        J = calculate_J(A,B,C)

    
    if(J<0):
        J=0

    delta = calculate_delta(J)

    return A,B,C,J,delta

