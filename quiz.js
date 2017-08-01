
var Q_questions = [{
    text:"What is the distance to the signal?",
    answers: ["in the solar system",
              "less than a light year",
              "less than 100 light years",
              "further than 100 light years"],
    values: [4, 3, 2, 1],
    qtype:"multichoice"
                   },
                   
                   {
    text: "Have They seen us?",
    answers: ["yes", "no"],
    values: [2,1],
    qtype:"y/n"
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
    
    function askNextMultiChoice(question){

clearBox("answersbox");
//  Set question text
    document.getElementById("ask").innerHTML = question.text;
    
// Create radio buttons for possible answers
for (i=0; i< question.answers.length; i++){
    

    var choiceLabel = document.createElement('label')
    var choiceRadioButton = document.createElement('input');
    choiceRadioButton.setAttribute('type', 'radio')
    choiceRadioButton.setAttribute('name', 'choice')
    
    choiceLabel.appendChild(choiceRadioButton);
    choiceLabel.appendChild(document.createTextNode(question.answers[i]));
    choiceLabel.appendChild(document.createElement('br'));
    
    document.getElementById("answersbox").appendChild(choiceLabel);
}

        }

function getQuestionAnswer()
{
    document.getElementById("confirm").innerHTML = "Answered"
    
}

askNextMultiChoice(Q_questions[0]);
askNextMultiChoice(Q_questions[1]);

