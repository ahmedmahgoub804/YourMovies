const movies = document.querySelectorAll(".movie");
movies.forEach((movie)=>{
    let img = movie.firstElementChild
    let a = movie.lastElementChild;
    movie.addEventListener("mouseover",
        (e)=>
        {
        img.style.filter = "blur(3px)";
        a.style.display = "block"
        }
    )

    movie.addEventListener("mouseout",
        (e)=>
        {
        img.style.filter = "none";
        a.style.display = "none"
        }
    )
})

const movieg = document.querySelectorAll(".inside-body");
movieg.forEach((movie)=>{
    let img = movie.firstElementChild.firstElementChild
    let button = movie.querySelector(".moviebutton")
    movie.addEventListener("mouseover",(e)=>{
        img.style.filter = "grayscale(90%)";
        img.style.transform= "scale(1.3)";
        if(button){
        button.style.backgroundColor = "#198754"}
        movie.style.backgroundColor = " #198754"
        
        })

    movie.addEventListener("mouseout",(e)=>{
        img.style.filter = "none";
        img.style.transform= "scale(1)";
        if(button){
        button.style.backgroundColor = "#212529"}
        movie.style.backgroundColor = "#f8f9fa26"
    })
})

