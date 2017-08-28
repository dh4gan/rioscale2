/* Javascript to run the Rio 2.0 Questionnaire
* Written by dh4gan (01-Aug-2017)
* Runs the quiz, and records all answers along with Q, J, delta and R
*/


// Variables to hold the question data //
var questionset;
var currentQuestions;
var answers;
var nQ;
var qID;

var questionsets = ["Q", "A", "B","C"]


// Q question variables
var Q_questions = [{
                   text:"Q1) What is the light travel time to the signal?",
                   choices: ["Less than a day (i.e. in the Solar System)",
                             "Days to years (i.e. about as close as the nearest star)",
                             "Years to decades (in the solar neighbourhood)",
                             "Centuries to millennia (good fraction of the galactic radius)",
                             "Longer/unknown"],
                   values: [4, 3, 2, 1,0],
                   qtype:"multichoice",
		   explainertext:""
    },
                   
                   {
                   text: "Q2) What are the prospects for communication with the source of the signal?",
                   choices: ["We are in active two way communication",
                             "We could respond using the same medium/encoding as the signal in the near future",
                             "We can understand the signal or we have artifacts we can study",
                             "No communication is taking place"],
                   values: [4,3,2,1],
                   qtype:"multichoice",
		   explainertext:""
                   },
                   {
                   text: "Q3) Is the sender aware of humanity and its technology?",
                   choices:["Yes, certainly—the signal is intended for us, specifically",
                            "Possibly, but there is little or no evidence for this",
                            "Almost certainly not (e.g. they are too far away)",
                            "Senders are apparently extinct"],
                   values:[2,1,0,-1],
                   qtype:"multichoice",
		   explainertext:""
		   }];


var Q_answers = [0,0,0];
var Q_total = 0.0;

var Q_dictionary = {
    3:"Philosophically ground-breaking, but of limited immediate scientific impact. The prospects for understanding ETIs remain unclear.",
    5:"Scientifically revolutionary, but of no everyday consequence. Prospects for understanding ETIs remain decades in the future.",
    7:"SETI becomes the study of ETI. There are good prospects for near-future, limited understanding of ETI.",
    9:"the making of an epoch; the future direction of humanity is changed.",
    10:"Revolutionary. Everyday life on Earth will change forever."
}
    
    
    Q_dictionary[0] = Q_dictionary[3];
Q_dictionary[1] = Q_dictionary[3];
Q_dictionary[2] = Q_dictionary[3];
Q_dictionary[4] = Q_dictionary[5];
Q_dictionary[6] = Q_dictionary[7];
Q_dictionary[8] = Q_dictionary[9];

// delta question variables

// A first

var A_questions = [{
                   text: "A1) Is there significant uncertainty about whether the phenomenon occurred/occurs at all?",
                   choices: ["yes","no"],
                   values: [6,7],
                   skipvalue:[6],
                   qtype:"multichoice",
		   explainertext:"Examples of significant uncertainty: <br>reports of sighting of a UFO or aliens, <br>interpretation of ancient art, <br>telescopic data from amateurs, <br>interpreting other people’s data with little or no documentation or metadata"
    },
                   {
                   text:"A2) How amenable to study is the phenomenon? Award up to 3 points based on the repeatability of the phenomenon. <br><br>&nbsp0: The phenomenon has been observed exactly once, <br>&nbsp1: The phenomenon has been observed a small but plural number times, either as multiple targets showing similar phenomena, or a single target showing multiple similar events. <br>&nbsp2: The phenomenon has been been confirmed to be real and repeated, for instance by multiple groups using a single instrument to observe the phenomenon or by an additional observation with a different instrument or from a different site. <br>&nbsp3: The phenomenon is observed routinely by different groups using different equipment.",
                   minimum:0,
                   maximum:3,
                   qtype:"textbox",
		   explainertext:""
                   },
                   {
                   text:"A3) Is the discoverer of phenomenon the same person/group that predicted that such a phenomenon would indicate the presence of alien intelligence?",
                   choices:["yes, the claimants predicted this 'discovery'","no, the claimants have identified a new phenomenon, or one predicted by others"],
                   values:[-1,0],
                   qtype:"multichoice",
		   explainertext:"(People are natural wishful thinkers, and often see what they want to see, so it gives extra credibility to a claim if the groups doing the prediction and those doing the discovery are not the same)"
                   }];
var A_answers = [0,0,0];
var A_total = 0.0;


// Now B

var B_questions = [{
                   text:"B1) Does the phenomenon look like a known instrumental or psychological effect?",
                   choices:["yes", "no"],
                   values:[0,7],
                   skipvalue:[0],
                   qtype:"multichoice",
		   explainertext:"Examples of known instrumental effects:<br> DC channel in a filterbank file, cosmic rays in spectra, lens flare in photograph, other known sources of noise / bad data<br><br>Examples of known psychological effects: Reports of alien abduction, UFO sightings; subjective, qualitative interpretations of apparent correlations in noisy data."
                   },
                   {
                   text:"B2) What chances do the instrument builders / experts in the method / observers of the phenomenon give that the signal is not instrumental? Award between 0-3 points:<br><br>&nbsp0: These experts have not weighed in at all<br>&nbsp1: These experts give roughly 90% chance that it is instrumental (i.e. 10% chance it is real)<br>&nbsp2: These experts give a 50% chance that it is instrumental<br>&nbsp3: These experts give a less than 10% chance that it is instrumental",
                   minimum:0,
                   maximum:3,
                   qtype:"textbox",
		   explainertext:""
                   }]

var B_answers = [0,0];
var B_total = 0.0;


// Finally C

var C_questions = [{
                   text:"C1) Is there good reason to think the phenomenon is a hoax?",
                   choices:["yes","no"],
                   values:[0,1],
                   skipvalue:[0],
                   qtype:"multichoice",
		   explainertext:"",
                   },
                   {
                   text: "C2) How does a wide community of experts assess the probability that there any known sources of natural or anthropogenic signal that could explain the phenomenon? Award between 0-9 points<br><br>&nbsp0 points: A wide range of experts of the relevant natural or anthropogenic phenomena has not been consulted<br>&nbsp1 point: It is consistent with a common phenomenon<br>&nbsp3 points: It is consistent only with rare or poorly-understood phenomena<br>&nbsp6 points: It is not consistent with any known natural or anthropogenic phenomena<br>&nbsp8 points: Only extraterrestrial, artificial explanations make sense (all natural and anthropogenic explanations have been ruled out).<br>&nbsp9 points: The phenomenon contains information content of clearly intelligent design (i.e. it contains a message; or is an obviously artificial and alien artifact available for close (perhaps robotic) inspection).",
                   minimum:0,
                   maximum:9,
                   qtype:"textbox",
		   explainertext:""
                   }];
var C_answers = [0,0];
var C_total = 0.0;




// Dictionary for J

var J_dictionary = {
    0: "No interest warranted",
    1: "SETI interest potentially warranted; no press interest warranted",
    2: "SETI interest potentially warranted; no press interest warranted",
    3: "SETI interest potentially warranted; no press interest warranted",
    4: "SETI interest potentially warranted; no press interest warranted",
    5: "SETI interest probably warranted; technical popular press interest potentially warranted",
    6: "SETI interest probably warranted; technical popular press interest potentially warranted",
    7: "SETI interest definitely warranted; technical popular press interest probably warranted; possible off-beat news item for general press, if expressed with appropriate caveats. If not aliens, still very interesting",
    8: "SETI interest definitely warranted; technical popular press interest probably warranted; possible off-beat news item for general press, if expressed with appropriate caveats. If not aliens, still very interesting",
    9: "Significant mainstream press interest warranted, heavy coverage by technical popular press. Broad agreement that the signal could be due to aliens",
    10: "Aliens. Front page of every major newspaper."
}


var R_dictionary = {
    10: "Extraordinary",
    9:  "Outstanding",
    8:  "Far-reaching",
    7:  "High",
    6:  "Noteworthy",
    5:  "Intermediate",
    4:  "Moderate",
    3:  "Minor",
    2:  "Low",
    1:  "Insignificant",
    0:  "Nil"
}


// Function that drives the quiz


startQuiz();



/*
 *
 * Function definitions
 *
 */


function startQuiz() {
    /*
     * Begins the quiz
     */
    
    questionset= "Q";
    askQuestionSet();
}


function askQuestionSet() {
    /*
     * Decides which question set is next, and asks the first question
     */
    console.log("Asking all " +questionset+ " questions");
    
    
    
    switch(questionset){
	
    case "Q":
	currentQuestions = Q_questions;
	answers = Q_answers;
	break;
        
    case "A":
	currentQuestions = A_questions;
	answers = A_answers;
	break;
        
    case "B":
	currentQuestions = B_questions;
	answers = B_answers;
	break;
        
    case "C":
	currentQuestions = C_questions;
	answers = C_answers;
	break;
    default:
	document.getElementById("confirm").innerHTML = "Error: question set not found";
	return;
    }
    
    qID = 0;
    nQ = currentQuestions.length;
    askQuestion(currentQuestions);
}


function askQuestion() {
    /*
     * Asks a question - decides which type to ask
     */
    
    question = currentQuestions[qID];
    // Clear previous question
    clearBox("answersbox");
    
    // Set new question text
    document.getElementById("ask").innerHTML = question.text;
    
    // Get either radio buttons for multiple choice or text box
    if (question.qtype=='multichoice')
	{
	    askMultiChoice(question);
	}
    
    else if (question.qtype =='textbox')
	{
	    askTextBox(question);
	}

    document.getElementById("explainbox").innerHTML = question.explainertext;
    
}


function askMultiChoice(question){
    /*
     * sets up a multiple choice question
     */
    
    // Create radio buttons for possible choices
    for (i=0; i< question.choices.length; i++){
	
	
	var choiceLabel = document.createElement('label');
	choiceLabel.setAttribute('name', 'label'+String(i+1));
	var choiceRadioButton = document.createElement('input');
	var choiceString = 'multichoice';
	
	choiceRadioButton.setAttribute('type', 'radio');
	choiceRadioButton.setAttribute('name', choiceString);
	
	choiceLabel.appendChild(choiceRadioButton);
	choiceLabel.appendChild(document.createTextNode(question.choices[i]));
	choiceLabel.appendChild(document.createElement('br'));
	
	document.getElementById("answersbox").appendChild(choiceLabel);
    }
}

function askTextBox(question){
    /*
     * Sets up a question with a text box for answering
     */
    
    // Create text box for answer
    var choiceLabel = document.createElement('label');
    var textBox = document.createElement('input');
    
    var boxString = "tbox";
    textBox.setAttribute('type', 'text');
    textBox.setAttribute('name', boxString);
    textBox.setAttribute('id',boxString);
    textBox.setAttribute('value', 0);
    
    document.getElementById("answersbox").appendChild(textBox);
}


function getQuestionAnswer(){
    /*
     * Interrogates page for question answer
     * Either sets up next question
     * Or calculates total from this question set
     */
    
    document.getElementById("confirm").innerHTML = "";
    currentQuestion = currentQuestions[qID];
    
    
    console.log("getting question answer");
    
    qtype = currentQuestion.qtype;
    choice = -1;
    
    
    // If question multichoice, then obtain which radio button was ticked
    if(qtype=="multichoice")
	{
	    nchoices = currentQuestion.choices.length;
	    var buttonList = document.getElementsByName("multichoice");
	    choice = -10;
	    for (i=0; i < nchoices; i++)
		{
		    
		    var ischecked = buttonList[i].checked;
		    if(ischecked) choice = i;
		}
	    
        updateLog(choice,qtype);
        
	    if(choice==-10)
		{
		    document.getElementById("confirm").innerHTML = "Please select an option before continuing"
			return;
		}
	    answers[qID] = currentQuestion.values[choice];
	}
    
    // Else if question textbox, obtain value from textbox and check it for veracity
    else if(qtype=="textbox")
	{
	    try
		{
		    answers[qID] = Number(document.getElementById("tbox").value);// Get value of textbox
		    
		    if (isNaN(answers[qID])) throw "Not a valid number - try again";
		    if (answers[qID]<currentQuestion.minimum) throw "Number too low - try again";
		    if (answers[qID]>currentQuestion.maximum) throw "Number too high - try again"
														}
	    catch(err)
		{
		    if(err!="TypeError")
			{
			    document.getElementById("confirm").innerHTML = err;
			    return;
			}
		}
        
        updateLog(answers[qID],qtype);
	    
	}
    
    
    
    console.log("Answer is "+answers[qID]);
    
    // Check to see if answer demands we skip the rest of the question set
    if(answers[qID]==currentQuestion.skipvalue)
	{
	    // If we're skipping
	    document.getElementById("confirm").innerHTML = "Previous answer resulted in skipping questions";
	    qID =nQ;
	}
    else
	{
	    
	    // If not, update the question ID
	    qID++;
	}
    
    
    // If we haven't run out of questions, ask the next one
    if(qID <nQ)
	{
	    askQuestion();
	    
	    // Otherwise, calculate the total from this section and move on
	}
    
    else
	{
	    console.log("We have asked all the questions in this section");
	    calculateTotal();
	    
	}
    
}


function goBack()
{
    /*
     * Goes back a question
     */


    // Don't go back if we're at the first question

    if (qID==0){
	return;
    }
    
    // Set question ID back one

    qID--;

    // Delete current answer value
    answers[qID]=0.0;

    
    // Remove previous line from the answer log

    // Split log text by carriage returns
    var logtext = document.getElementById("logbox").innerHTML;
    var loglines = logtext.split('<br><br>');

    // Find index of line to delete and delete it
    var delIndex = loglines.length-2;
    
    loglines[delIndex] = "";


    // Rewrite the log
    document.getElementById("logbox").innerHTML = "";

    for (i=0; i<loglines.length; i++)
    {
	if(loglines[i]!="")
	{
	    document.getElementById("logbox").innerHTML = document.getElementById("logbox").innerHTML + loglines[i] + "<br><br>";
	}
    }

    // Ask this question
    askQuestion(qID);

}


function updateLog(choice,qtype){
    
    /*
     * Updates the answer log with the selected answer and its value
     */
    
    var qtext = currentQuestion.text.split("<br>")[0];
    
    if (qtype=="multichoice")
    {
        
        document.getElementById("logbox").innerHTML = document.getElementById("logbox").innerHTML + qtext+"&nbsp &nbsp"+currentQuestion.choices[choice]+"  ("+currentQuestion.values[choice]+")<br><br>" ;
    }
    else if(qtype="textbox")
    {
        document.getElementById("logbox").innerHTML = document.getElementById("logbox").innerHTML + qtext+"&nbsp &nbsp("+choice+")<br><br>";
    }
}


function calculateTotal(){
    /*
     * Calculates the total from this question set
     * Asks the next set of questions
     */
    
    
    var total = 0;
    
    for (i=0; i<answers.length; i++)
	{
	    total = total+answers[i];
	}
    console.log("Total is ",total);
    
    if(questionset=="Q")
	{
	    console.log("Q questions answered");
	    questionset = "A";
	    Q_total = total;
        if(Q_total < 0.0)
        {
            Q_total = 0.0;
        }
	    
	    // Update header to show new question set
	    
	    document.getElementById("quizname").innerHTML = "Questions to determine &#948";
	    document.getElementById("quizsub").innerHTML = "Section A) How real and amenable to study is the phenomenon?";
	    askQuestionSet();
	    
	}
    
    else if(questionset=="A")
	{
	    console.log("A questions answered");
	    questionset="B";
	    A_total = total;
	    
	    // Update header to show new question set
	    
	    document.getElementById("quizsub").innerHTML = "Section B) How certain are we that the phenomenon is not instrumental?";
	    
	    askQuestionSet();
	    
	}
    
    else if(questionset=="B")
	{
	    console.log("B questions answered");
	    questionset="C";
	    B_total = total;
	    
	    // Update header to show new question set
	    
	    document.getElementById("quizsub").innerHTML = "Section C) How certain are we that the phenomenon is not natural or anthropogenic?";
	    
	    askQuestionSet();
	}
    
    else if(questionset=="C")
	{
	    C_total = total;
	    // If this is the end of the quiz, delete quiz elements and calculate final scores
	    
	    console.log("Quiz complete");
	    
	    clearBox("ask");
	    clearBox("confirm");
	    clearBox("answersbox");
	    clearBox("quizsub");
	    clearBox("explainbox");
	    
	    document.getElementById("submitbutton").style.visibility = "hidden";
	    document.getElementById("quizname").innerHTML = "Quiz complete ("+Date()+")";
	    
	    finalAnswer();
	    
	}
    
}


function finalAnswer(){
    /*
     * Returns the final Rio score
     */
    
    
    console.log("A="+A_total);
    console.log("B="+B_total);
    console.log("C="+C_total);
    
    var J=0.0;
    // J only non-zero if not a hoax (C>0)
    if(C_total > 1.0e-10) J = A_total + B_total +C_total - 20.0;
    
    if(J<0.0) J=0.0;
    console.log("J="+J);
    
    var delta = Math.pow(10.0, (J-10.0)/2.0);
    
    var prob_A = 100.0*Math.pow(10.0, (A_total-10.0)/2.0);
    var prob_B = 100.0*Math.pow(10.0, (B_total-10.0)/2.0);
    var prob_C = 100.0* Math.pow(10.0, (C_total-10.0)/2.0);
    
    var Rio = Q_total*delta;
    
    // Get explainer text for Q

    var Q_explainer = Q_dictionary[Math.round(Q_total)];
    var J_explainer = J_dictionary[Math.round(J)];

    var A_explainer = "Chance phenomenon is real is "+getChance(prob_A);
    var B_explainer = "Chance phenomenon is not instrumental/psychological is "+getChance(prob_B);
    var C_explainer = "Chance phenomenon is not natural/anthropogenic is "+getChance(prob_C);
    var R_explainer = R_dictionary[Math.round(Rio)]

    
    document.getElementById("spaces").innerHTML = "";
    document.getElementById("buttonarray").innerHTML = "";
    document.getElementById("answersbox").innerHTML = "";
    document.getElementById("ask").innerHTML = "";
    document.getElementById("quizsub").innerHTML = "";
    
    document.getElementById("resultheader").style.visibility = "visible";
    document.getElementById("Qbox").innerHTML = "(Q = "+Q_total+"): <b>If signal is from extraterrestrial intelligence</b>...<br>"+Q_explainer;
    document.getElementById("Abox").innerHTML = "(A = "+A_total+"): "+A_explainer;
    document.getElementById("Bbox").innerHTML = "(B = "+B_total+"): "+B_explainer;
    document.getElementById("Cbox").innerHTML = "(C = "+C_total+"): "+C_explainer;
    document.getElementById("Jbox").innerHTML = "(J = "+J+"): "+J_explainer;
    document.getElementById("deltabox").innerHTML = "&#948 = "+delta.toPrecision(1);
    document.getElementById("Rbox").innerHTML = "Rio Score: R = Q x &#948 =  "+Math.round(Rio,3)+"<br>Rating: "+R_explainer;
    
    
    // Show buttons to print results, refresh quiz
    
    document.getElementById("printbutton").style.visibility="visible";
    document.getElementById("refreshlower").style.visibility="visible";
    
    
}

function clearBox(elementID)
{ 
    // Simple helper function to empty HTML elements
    document.getElementById(elementID).innerHTML = "";
}

function getChance(prob)
{
    var chance = "";
	if (prob<10.0)
	    {
		chance = "very low";
	    }
	
	else if (prob>=10.0 && prob<30.0)
	    {
		chance = "low";
	    }
	else if (prob>=30.0 && prob<50.0)
	    {
		chance = "moderate";
	    }
	else if (prob>=50.0 && prob<70.0)
	    {
	    chance = "high";
	    }
	else
	    {
	    chance =  "very high";
	    }

    return chance;
}
