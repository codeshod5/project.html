let userscore = 0;
let compscore = 0;
const msg = document.querySelector("#msg");

const choices = document.querySelectorAll(".choice");

const gencompchoice = () => {
    const options = ["rock", "paper", "scissors"];
    const ranindx = Math.floor(Math.random() * 3);
    return options[ranindx];
};

const drawgame = () => {
    msg.innerText = "draw";
};

const showwinner = (userwin, userchoice, compchoice) => {
    if (userwin) {
        msg.innerText = `You win! ${userchoice} beats ${compchoice}`;
    } else {
        msg.innerText = `You lose! ${compchoice} beats ${userchoice}`;
    }
    updatescores(userwin,userscoree,compscoree);
};

const userscoree = document.querySelector("#userscore")
const compscoree = document.querySelector("#compscore")
// const scoreconatiner = document.querySelector(".scoreconatiner")
const updatescores = (userwin, userscoree, compscoree) => {
    if (userwin) {
        userscoree.textContent = ++userscore;
    } else {
        compscoree.textContent = ++compscore;
    }
};



const playgame = (userchoice) => {
    console.log("userchoice", userchoice);
    const compchoice = gencompchoice();
    console.log("comp choice", compchoice);
    if (userchoice === compchoice) {
        drawgame();
    } else {
        let userwin = true;
        if (userchoice === "rock") {
            userwin = compchoice === "paper" ? false : true;
        } else if (userchoice === "paper") {
            userwin = compchoice === "scissors" ? false : true;
        } else {
            userwin = compchoice === "rock" ? false : true;
        }
        showwinner(userwin, userchoice, compchoice);
    }
};

choices.forEach((choice) => {
    choice.addEventListener("click", () => {
        const userchoice = choice.getAttribute("id");
        console.log("user choice", userchoice);
        playgame(userchoice);
    });
});
