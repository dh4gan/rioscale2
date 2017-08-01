// For now, these are placeholders for the three question types
// (multiple choice, y/n, textbox)

var Q_questions = [{
    text:"What is the distance to the signal?",
    answers: ["in the solar system",
              "less than a light year",
              "less than 100 light years",
              "further than 100 light years"],
    values: [4, 3, 2, 1],
    qtype:"multichoice"},
                   
                   {
		       text: "Have They seen us?",
		       answers: ["yes", "no"],
		       values: [2,1],
		       qtype:"multichoice"
                   },
                   {
		       text: "How large is it?",
		       answers: [0,100],
		       qtype:"textbox"
		   }];

                   
function clearBox(elementID)
    {
     document.getElementById(elementID).innerHTML = "";
    }
    
function askMultiChoice(question){
    
    // Create radio buttons for possible answers
    for (i=0; i< question.answers.length; i++){
	
	
	var choiceLabel = document.createElement('label');
	choiceLabel.setAttribute('name', 'label'+String(i+1));
	var choiceRadioButton = document.createElement('input');
	var choiceString = 'choice'+String(i+1);

	choiceRadioButton.setAttribute('type', 'radio');
	choiceRadioButton.setAttribute('name', choiceString);
	
	choiceLabel.appendChild(choiceRadioButton);
	choiceLabel.appendChild(document.createTextNode(question.answers[i]));
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


function askQuestion(question)
{

    // Clear previous question
    clearBox("answersbox")

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

function getQuestionAnswer(currentQuestion)
{
    
    console.log("getting question answer");
    qtype = currentQuestion.qtype;
    document.getElementById("confirm").innerHTML = qtype;
    choice = -1;
    // If question multichoice, then obtain which radio button was ticked
    if(currentQuestion.qtype=="multichoice")
    {
	for (i=0; i < currentQuestion.answers.length; i++)
	{

	    var ischecked = document.getElementsByName("choice"+String(i+1))[0].checked;	
	    console.log(ischecked)
	    if(ischecked) choice = i;
	}

	answer = currentQuestion.values[choice];
    }


    console.log(answer)
    answered=true;
return answer;
}

function askAllQQuestions()
{
    var qID = 0;
    var qnumber = Q_questions.length;

    currentQuestion = Q_questions[qID];
    askQuestion(currentQuestion);

    // Function that waits for user press

    // Function that gets answer

    answer = getQuestionAnswer(currentQuestion);
    
    answered=false;
     
}


click = false;
currentQuestion = Q_questions[0];

askAllQQuestions();
