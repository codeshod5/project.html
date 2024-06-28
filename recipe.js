const searchbox = document.querySelector(".searchbox");
const btn = document.querySelector(".btn");
const recipecont = document.querySelector(".recipecont")
const recipecontent = document.querySelector(".recipe-deatails-content")
const recipeclosebtn = document.querySelector(".recipe-closebtn")


const fetchdata = async(inputt)=>{
    recipecont.innerHTML = "<h2>fetching data ...</h2>"//so your images can be properly place not only that 
    const data = await fetch(`https://www.themealdb.com/api/json/v1/1/search.php?s=${inputt}`)
    const response = await data.json()
    recipecont.innerHTML = ""
     console.log(response.meals)
    response.meals.forEach(meal=>{
        const recipediv = document.createElement('div');
        recipediv.classList.add('recpie');//accesing through meal array from response.meals
        recipediv.innerHTML = `
        <img src = "${meal.strMealThumb}">
       
        <h3>${meal.strArea}</h3>
        <h5><b>${meal.strMeal}</b></h5>
        `
        const button = document.createElement('button');
        button.textContent = "view recipe";
        recipediv.appendChild(button)
//ADDING EVENLISTNER AFTER ADDING INTO RECIPEDIV TO VIEW THE RECIPES 
button.addEventListener('click',()=>{
    openpopup(meal);
})

        recipecont.appendChild(recipediv);
    })
}
const fetchIngredients = (meal) => {
    let ingredients = "";
    for (let i = 1; i <= 20; i++) {
        const ingredient = meal[`strIngredient${i}`]; // Corrected typo here
        if (ingredient) {
            const measure = meal[`strMeasure${i}`];
            ingredients += `<li>${measure} ${ingredient}</li>`;
        } else {
            break;
        }
    }
    return ingredients; // Moved return outside of the loop
}

 const openpopup =(meal)=>{
    recipecontent .innerHTML= `
    <h2 class = "recipename">${meal.strMeal}</h2>
    <h3>ingredeients</h3>
    <ul class= "ingredients">${fetchIngredients(meal)}</ul>
    <div>
    <h3>instruction</h3>
    <p class="instructions">${meal.strInstructions}</p>

    
    `
    recipecontent.parentElement.style.display = "block";
 }

 btn.addEventListener('click',(e)=>{
    e.preventDefault() //this will count the number of clicks 
    const inputt = searchbox.value.trim() //this will trim the spaces from the search box 
    fetchdata(inputt)
    // console.log("click")

 })
 recipeclosebtn.addEventListener('click',()=>{
    recipecontent.parentElement.style.display = "none";
 })
