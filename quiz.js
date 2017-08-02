// For now, these are placeholders for the three question types
// (multiple choice, y/n, textbox)

var questionset;
var currentQuestions;
var answers;
var nQ;
var qID;

var questionsets = ["Q", "A", "B","C"]


var Q_questions = [{
                   text:"What is the distance to the signal?",
                   choices: ["in the solar system",
                             "less than a light year",
                             "less than 100 light years",
                             "further than 100 light years"],
                   values: [4, 3, 2, 1],
                   skipvalue: [4],
                   qtype:"multichoice"},
                   
                   {
                   text: "Have They seen us?",
                   choices: ["yes", "no"],
                   values: [2,1],
                   qtype:"multichoice"
                   },
                   {
                   text: "How large is it?",
                   choices: [0,100],
                   qtype:"textbox"
		   }];


var Q_answers = [0,0,0];
var Q_total = 0.0;

var A_questions = [{
                   text: "Is there significant uncertainty about whether the phenomenon occurred/occurs at all?",
                   choices: ["yes","no"],
                   values: [0,1],
                   skipvalue:[0],
                   qtype:"multichoice"},
                   {
                   text:"How amenable to study is the phenomenon? Award up to 3 points based on the repeatability of the phenomenon. <br>0: The phenomenon has been observed exactly once, <br>1: The phenomenon has been observed a small but plural number times, either as multiple targets showing similar phenomena, or a single target showing multiple similar events. <br>2: The phenomenon has been been confirmed to be real and repeated, for instance by multiple groups using a single instrument to observe the phenomenon or by an additional observation with a different instrument or from a different site. <br>3: The phenomenon is observed routinely by different groups using different equipment.",
                   choices:[0,3],
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


var B_questions = [{
                   text:"Does the phenomenon look like a known instrumental or psychological effect?",
                   choices:["yes", "no"],
                   values:[0,7],
                   skipvalue:[0],
                   qtype:"multichoice"
                   },
                   {
                   text:"What chances do the instrument builders / experts in the method / observers of the phenomenon give that the signal is not instrumental? Award between 0-3 points:<br>0: These experts have not weighed in at all<br>1: These experts give roughly 90% chance that it is instrumental (i.e. 10% chance it is real)<br>2: These experts give a 50% chance that it is instrumental<br>3: These experts give a less than 10% chance that it is instrumental",
                   choices:[0,3],
                   qtype:"textbox"
                   }]

var B_answers = [0,0];
var B_total = 0.0;


var C_questions = [{
                   text:"Is there good reason to think the phenomenon is a hoax?",
                   choices:["yes","no"],
                   values:[0,1],
                   skipvalue:[0],
                   qtype:"multichoice"
                   },
                   {
                   text: "How does a wide community of experts assess the probability that there any known sources of natural or anthropogenic signal that could explain the phenomenon?<br>0 points: A wide range of experts of the relevant natural or anthropogenic phenomena has not been consulted<br>1 point: It is consistent with a common phenomenon<br>3 points: It is consistent only with rare or poorly-understood phenomena<br>6 points: It is not consistent with any known natural or anthropogenic phenomena<br>8 points: Only extraterrestrial, artificial explanations make sense (all natural and anthropogenic explanations have been ruled out).<br>9 points: The phenomenon contains information content of clearly intelligent design (i.e. it contains a message; or is an obviously artificial and alien artifact available for close (perhaps robotic) inspection).",
                   choices:[0,9],
                   qtype:"textbox"
                   }]

var C_answers = Q_answers;
var C_total = 0.0;


function clearBox(elementID)
    {
     document.getElementById(elementID).innerHTML = "";
    }
    
function askMultiChoice(question){
    
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

    // Create text box for answer
    var choiceLabel = document.createElement('label')
    var textBox = document.createElement('input');

    var boxString = 'box';
    textBox.setAttribute('type', 'text');
    textBox.setAttribute('name', boxString);
    textBox.setAttribute('value', 0);
		
    document.getElementById("answersbox").appendChild(textBox);
    }


function askQuestion()
{

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

function getQuestionAnswer()
{
    
    document.getElementById("confirm").innerHTML = "";
    currentQuestion = currentQuestions[qID];
    nchoices = currentQuestion.choices.length;
    
    console.log("getting question answer");
    
    qtype = currentQuestion.qtype;
    choice = -1;
    
    
    // If question multichoice, then obtain which radio button was ticked
    if(qtype=="multichoice")
    {
        
        var buttonList = document.getElementsByName("multichoice");
	for (i=0; i < nchoices; i++)
	{
        
        var ischecked = buttonList[i].checked;
	    if(ischecked) choice = i;
	}

	answers[qID] = currentQuestion.values[choice];
    }
    
    else if(qtype=="textbox")
    {
        // Need to throw an out of bounds exception as well (TODO)
        try
        {
        answers[qID] = Number(document.getElementsByName("box")[0].value);// Get value of textbox
        if (isNaN(answers[qID])) throw "Not a valid number - try again";
        }
        catch(err)
        {
            document.getElementById("confirm").innerHTML = err;
            return;
        }
        
    }
    


    console.log("Answer is "+answers[qID]);
    
    if(answers[qID]==currentQuestion.skipvalue)
    {
    
        document.getElementById("confirm").innerHTML = "Previous answer resulted in skipping questions";
        qID =nQ;
    }
    else
    {
    // Update the question ID and ask the next question
    qID++;
    }
    if(qID <nQ)
    {
        askQuestion(currentQuestions);
        
    // Unless we have run out of questions
    }
    
    else
    {
        console.log("We have asked all the questions in this section");
        calculateTotal();
        
    }
 
}

function calculateTotal()

{
    var total = 0;
    
    for (i=0; i<answers.length; i++)
    {
        console.log(i,answers[i],answers.length);
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
        document.getElementById("quizsub").innerHTML = "A) How real and amenable to study is the phenomenon?";
        askQuestionSet();
        
    }
    
    else if(questionset=="A")
    {
        console.log("A questions answered");
        questionset="B";
        A_total = total;
        
        document.getElementById("quizsub").innerHTML = "B) How certain are we that the phenomenon is not instrumental?";
        
        askQuestionSet();
        
    }
    
    else if(questionset=="B")
    {
        console.log("B questions answered");
    questionset="C";
    B_total = total;
    
    document.getElementById("quizsub").innerHTML = "C) How certain are we that the phenomenon is not natural or anthropogenic?";
    
    askQuestionSet();
    }
    
    else if(questionset=="C")
    {
        console.log("Quiz complete");
        
        document.getElementById("ask").innerHTML = "";
        document.getElementById("submitbutton").style.visibility = "hidden";
        document.getElementById("confirm").innerHTML = "";
        document.getElementById("quizname").innerHTML = "Quiz complete";
        document.getElementById("answersbox").innerHTML = "";
        document.getElementById("quizsub").innerHTML = "";
        
        delta_total = total;
        finalAnswer();
    
    }
    
}


function finalAnswer()
{
    
    console.log("A="+A_total);
    console.log("B="+B_total);
    console.log("C="+C_total);
    
    var J=0.0;
    // J only non-zero if not a hoax (C>0)
    if(C_total > 1.0e-10) J = A_total + B_total +C_total - 20.0;
    
    var delta = Math.pow(10, (J-10.0)/2.0);
    
    Rio = Q_total*delta_total;
    
    document.getElementById("Qbox").innerHTML = "Q = "+Q_total;
    document.getElementById("Abox").innerHTML = "A= "+A_total+", B = "+B_total+", C = "+C_total;
    document.getElementById("Jbox").innerHTML = "J = "+J;
    document.getElementById("deltabox").innerHTML = "&#948 = "+delta_total;
    document.getElementById("Rbox").innerHTML = "Rio Score: R = "+Rio;
    

    document.getElementById("refreshbutton").style.visibility="visible";
    
}

function askQuestionSet()
{
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


function startQuiz()
{
    document.getElementById("refreshbutton").style.visibility="hidden";
    questionset= "Q";
    askQuestionSet();
}

startQuiz();
