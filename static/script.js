const allDefaultBtn = document.querySelectorAll(".defaultBtn")
console.log(allDefaultBtn)
allDefaultBtn.forEach((e)=>{

    e.addEventListener('click',(event)=>{event.preventDefault()})


})