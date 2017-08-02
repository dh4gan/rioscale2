// For now, these are placeholders for the three question types
// (multiple choice, y/n, textbox)

var Q_questions = [{
    text:"What is the distance to the signal?",
    choices: ["in the solar system",
              "less than a light year",
              "less than 100 light years",
              "further than 100 light years"],
    values: [4, 3, 2, 1],
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

var answers = [0,0,0];
var nQ;
var qID = 0;

var currentQuestions;


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
	var choiceString = 'choice'+String(i+1);

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
    
    currentQuestion = currentQuestions[qID];
    nchoices = currentQuestion.choices.length;
    
    console.log("getting question answer");
    qtype = currentQuestion.qtype;
    choice = -1;
    
    
    // If question multichoice, then obtain which radio button was ticked
    if(qtype=="multichoice")
    {
	for (i=0; i < nchoices; i++)
	{
        console.log(qID, i,currentQuestion.choices.length);
	    var ischecked = document.getElementsByName("choice"+String(i+1))[0].checked;	
	    console.log(ischecked)
	    if(ischecked) choice = i;
	}

	answers[qID] = currentQuestion.values[choice];
    }
    
    else if(qtype=="textbox")
    {
        answers[qID] = parseFloat(document.getElementsByName("box")[0].value);// Get value of textbox
    }
    


    console.log("Answer is "+answers[qID]);
    
    // Update the question ID and ask the next question
    qID++;
    
    if(qID <nQ)
    {
        askQuestion(currentQuestions);
        
    // Unless we have run out of questions
    }
    
    else
    {
        console.log("We have asked all the questions");
        calculateTotal();
        
    }
 
}

function calculateTotal()

{
    var total = 0;
    
    for (i=0; i<answers.length; i++)
    {
        console.log(i, total,answers[i]);
        total = total+answers[i];
        
    }
    console.log("Total is ",total);
}

function askAllQQuestions()
{
    qID = 0;
    currentQuestions = Q_questions;
    nQ = currentQuestions.length;
    askQuestion(currentQuestions);
    
}




askAllQQuestions();
