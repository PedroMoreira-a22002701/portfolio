const startButton = document.getElementById('start-btn')
const nextButton = document.getElementById('next-btn')

const questionContainerElement = document.getElementById('question-container')
const questionElement = document.getElementById('question')
const answerButtonsElement = document.getElementById('answers-buttons')

let shuffledQuestions, currectQuestionIndex;
let quizScore = 0;

startButton.addEventListener('click', startGame())

nextButton.addEventListener('click',() => {
    currectQuestionIndex++;
    setNextQuestion()
} )

function startGame() {
    startButton.classList.add('hide')
    shuffledQuestions=questions.sort(() => Math.random() -0.5)
    currectQuestionIndex=0;
    questionContainerElement.classList.remove('hide')
    setNextQuestion()
    quizScore=0
}

function setNextQuestion()  {
    resetState();
    showQuestion(shuffledQuestions[currectQuestionIndex])
}


function showQuestion(question) {
    questionElement.innerText = question.question;
    question.answers.forEach((answers) =>{
        const button = document.createElement('button')
        button.innerText = answer.text;
        button.classList.add('btn')
        if(answer.correct){
            button.dataset.correct = answer.correct
        }
        button.addEventListener('click', selectAwswer)
        answerButtonsElement.appendChild(button)
    })
}

function resetState(){
    clearStatusClass(document.body)
    nextButton.classList.add('hide')
    while(answerButtonsElement.firstChild) {
        answerButtonsElement.removeChild(answerButtonsElement.firstChild)
    }
}

function selectAwswer(e) {
    const selectedButton=e.target
    const correct = selectedButton.dataset.correct

    setStatusClass(document.body, correct)
    Array.from(answerButtonsElement.children).forEach((button)=>{
        setStatusClass(button, button.dataset.correct)
    })
    if(shuffledQuestions.length > currectQuestionIndex +1){
        nextButton.classList.remove("hide")
    } else {
        startButton.innerText = "restart"
        startButton.classList.remove("hide")
    }
    if(selectedButton.dataset = correct) {
        quizScore++
    }
    document.getElementById('right-answers').innerText=quizScore
}


function setStatusClass(element, correct){
    clearStatusClass(element)
    if(correct){
        element.classList.add("correct")
    }else{
        element.classList.add("wrong")
    }

}


function clearStatusClass(element){
    element.classList.remove('correct')
    element.classList.remove('wrong')
}

const questions = [
    {
        question: 'Pergunta 1',
        answers: [
            {text: '1', correct: false},
            {text: '2', correct: false},
            {text: '3', correct: false},
            {text: '4', correct: true}
        ],
    },
    {
        question: 'Pergunta 2',
        answers: [
            {text: '1', correct: false},
            {text: '2', correct: false},
            {text: '3', correct: false},
            {text: '4', correct: true}
        ],
    },
    {
        question: 'Pergunta 3',
        answers: [
            {text: '1', correct: false},
            {text: '2', correct: false},
            {text: '3', correct: false},
            {text: '4', correct: true}
        ],
    },

]


