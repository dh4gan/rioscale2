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

var A_questions = Q_questions
var A_answers = Q_answers;
var A_total = 0.0;


var B_questions = Q_questions
var B_answers = Q_answers;
var B_total = 0.0;


var C_questions = Q_questions
var C_answers = Q_answers;
var C_total = 0.0;



/*var delta_questions = [{
                       text:"This is a delta question",
                       choices: ["Yup", "Narp"],
                       values: [0,1],
                       qtype:"multichoice",
                       skipvalue:[0],
                       },
                       {
                       text:"So's this ",
                       choices: ["y", "n"],
                       values: [0,1],
                       qtype:"multichoice",
                       }];

var delta_answers = [0,0];
var delta_total = 0.0*/




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
    textBox.setAttribute('value', 71);
		
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
        askAllQuestions();
        
    }
    
    else if(questionset=="A")
    {
        console.log("A questions answered");
        questionset="B";
        A_total = total;
        
        document.getElementById("quizsub").innerHTML = "B) How certain are we that the phenomenon is not instrumental?";
        
        askAllQuestions();
        
    }
    
    else if(questionset=="B")
    {
        console.log("B questions answered");
    questionset="C";
    B_total = total;
    
    document.getElementById("quizsub").innerHTML = "C) How certain are we that the phenomenon is not natural or anthropogenic?";
    
    askAllQuestions();
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
    
    var J = A_total + B_total +C_total - 20.0;
    var delta = Math.pow(10, (J-10.0)/2.0);
    
    Rio = Q_total*delta_total;
    
    document.getElementById("Qbox").innerHTML = "Q = "+Q_total;
    document.getElementById("Abox").innerHTML = "A= "+A_total+", B = "+B_total, ", C = "+C_total;
    document.getElementById("Jbox").innerHTML = "J = "+J;
    document.getElementById("deltabox").innerHTML = "delta = "+delta_total;
    document.getElementById("Rbox").innerHTML = "Rio Score: R = "+Rio;
    
}

function askAllQuestions()
{
    
    
    
    if(questionset=="Q")
    {
        console.log("Asking Q Questions");
    currentQuestions = Q_questions;
    answers = Q_answers;
    }
    
    else if(questionset=="delta")
    {
        console.log("Asking delta questions");
        currentQuestions=delta_questions;
        answers = delta_answers;
    
    }
    
    else if(questionsets.indexOf(questionset)<0)
    {
        console.log("Error - question set not found");
        return;
    }
    
    qID = 0;
    nQ = currentQuestions.length;
    askQuestion(currentQuestions);
}



questionset= "Q";
askAllQuestions();
