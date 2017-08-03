/* Javascript to run the Rio 2.0 Questionnaire
* Written by dh4gan (01-Aug-2017)
*
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
                   text:"What is the light travel time to the signal?",
                   choices: ["less than a day (i.e. in the Solar System)",
                             "days to years (i.e. about as close as the nearest star)",
                             "years to decades (in the solar neighbourhood)",
                             "Centuries to millennia (good fraction of the galactic radius)",
                             "Longer/unknown"],
                   values: [4, 3, 2, 1,0],
                   qtype:"multichoice"},
                   
                   {
                   text: "What are the prospects for communication with the source of the signal?",
                   choices: ["We are in active two way communication",
                             "We could respond using the same medium/encoding as the signal in the near future",
                             "We can understand the signal or we have artifacts we can study",
                             "No communication is taking place"],
                   values: [4,3,2,1],
                   qtype:"multichoice"
                   },
                   {
                   text: "Is the sender aware of humanity and its technology?",
                   choices:["Yes, certainly—the signal is intended for us, specifically",
                            "Possibly, but there is little or no evidence for this",
                            "Almost certainly not (e.g. they are too far away)",
                            "Senders are apparently extinct"],
                   values:[2,1,0,-1],
                   qtype:"multichoice"
		   }];


var Q_answers = [0,0,0];
var Q_total = 0.0;


// delta question variables

// A first

var A_questions = [{
                   text: "Is there significant uncertainty about whether the phenomenon occurred/occurs at all?",
                   choices: ["yes","no"],
                   values: [0,1],
                   skipvalue:[0],
                   qtype:"multichoice"},
                   {
                   text:"How amenable to study is the phenomenon? Award up to 3 points based on the repeatability of the phenomenon. <br><br>0: The phenomenon has been observed exactly once, <br>1: The phenomenon has been observed a small but plural number times, either as multiple targets showing similar phenomena, or a single target showing multiple similar events. <br>2: The phenomenon has been been confirmed to be real and repeated, for instance by multiple groups using a single instrument to observe the phenomenon or by an additional observation with a different instrument or from a different site. <br>3: The phenomenon is observed routinely by different groups using different equipment.",
                   minimum:0,
                   maximum:3,
                   qtype:"textbox"
                   },
                   {
                   text:"Is the discoverer of phenomenon the same person/group that predicted that such a phenomenon would indicate the presence of alien intelligence? <br><br>(People are natural wishful thinkers, and often see what they want to see, so it gives extra credibility to a claim if the groups doing the prediction and those doing the discovery are not the same).",
                   choices:["yes, the claimants predicted this 'discovery'","no, the claimants have identified a new phenomenon, or one predicted by others"],
                   values:[-1,0],
                   qtype:"multichoice",
                   }];
var A_answers = [0,0,0];
var A_total = 0.0;


// Now B

var B_questions = [{
                   text:"Does the phenomenon look like a known instrumental or psychological effect?",
                   choices:["yes", "no"],
                   values:[0,7],
                   skipvalue:[0],
                   qtype:"multichoice"
                   },
                   {
                   text:"What chances do the instrument builders / experts in the method / observers of the phenomenon give that the signal is not instrumental? Award between 0-3 points:<br><br>0: These experts have not weighed in at all<br>1: These experts give roughly 90% chance that it is instrumental (i.e. 10% chance it is real)<br>2: These experts give a 50% chance that it is instrumental<br>3: These experts give a less than 10% chance that it is instrumental",
                   minimum:0,
                   maximum:3,
                   qtype:"textbox"
                   }]

var B_answers = [0,0];
var B_total = 0.0;


// Finally C

var C_questions = [{
                   text:"Is there good reason to think the phenomenon is a hoax?",
                   choices:["yes","no"],
                   values:[0,1],
                   skipvalue:[0],
                   qtype:"multichoice"
                   },
                   {
                   text: "How does a wide community of experts assess the probability that there any known sources of natural or anthropogenic signal that could explain the phenomenon? Award between 0-9 points<br><br>0 points: A wide range of experts of the relevant natural or anthropogenic phenomena has not been consulted<br>1 point: It is consistent with a common phenomenon<br>3 points: It is consistent only with rare or poorly-understood phenomena<br>6 points: It is not consistent with any known natural or anthropogenic phenomena<br>8 points: Only extraterrestrial, artificial explanations make sense (all natural and anthropogenic explanations have been ruled out).<br>9 points: The phenomenon contains information content of clearly intelligent design (i.e. it contains a message; or is an obviously artificial and alien artifact available for close (perhaps robotic) inspection).",
                   minimum:0,
                   maximum:9,
                   qtype:"textbox"
                   }]

var C_answers = [0,0];
var C_total = 0.0;

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
    var choiceLabel = document.createElement('label')
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
        if (answers[qID]<currentQuestion.minimum) throw "Number too low - try again"
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
        askQuestion(currentQuestions);
        
    // Otherwise, calculate the total from this section and move on
    }
    
    else
    {
        console.log("We have asked all the questions in this section");
        calculateTotal();
        
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
        
        // Update header to show new question set
        
        document.getElementById("quizname").innerHTML = "Questions to determine &#948";
        document.getElementById("quizsub").innerHTML = "Section A) How real and amenable to study is the phenomenon?";
        askQuestionSet();
        
    }
    
    else if(questionset=="A")
    {
        console.log("A questions answered");
        questionset="B";
        A_total = total+6.0;
        
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
        
        //document.getElementById("ask").innerHTML = "";
        document.getElementById("submitbutton").style.visibility = "hidden";
        //document.getElementById("confirm").innerHTML = "";
        document.getElementById("quizname").innerHTML = "Quiz complete";
        //document.getElementById("answersbox").innerHTML = "";
        //document.getElementById("quizsub").innerHTML = "";
        
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
    
    var delta = Math.pow(10.0, (J-10.0)/2.0);
    
    var Rio = Q_total*delta;
    
    document.getElementById("Qbox").innerHTML = "Q = "+Q_total;
    document.getElementById("Abox").innerHTML = "A= "+A_total+", B = "+B_total+", C = "+C_total;
    document.getElementById("Jbox").innerHTML = "J = "+J;
    document.getElementById("deltabox").innerHTML = "&#948 = "+delta.toPrecision(2);
    document.getElementById("Rbox").innerHTML = "Rio Score: R = Q x &#948 =  "+Rio.toPrecision(2);
    

    document.getElementById("refreshbutton").style.visibility="visible";
}

function clearBox(elementID)
{ // Simple helper function to empty HTML elements
    document.getElementById(elementID).innerHTML = "";
}
