const allDefaultBtn = document.querySelectorAll(".defaultBtn")
console.log(allDefaultBtn)
let onanimate = false
allDefaultBtn.forEach((e)=>{

    e.addEventListener('click',(event)=>{event.preventDefault()})


})
const banner = document.getElementById("banner")
const nextItemBtn = document.getElementById("next--item")
const prevItemBtn = document.getElementById("prev--item")

nextItemBtn.addEventListener("click",(e)=>{
    if (!onanimate){
        onanimate=true
        let width = window.innerWidth
        let index = (banner.scrollLeft/width + 1)
        let target = (index * width)-9
        console.log(index)
        e.preventDefault()
        console.log("next")
        const animate = setInterval(()=>{
            console.log("Animate ,", target," > ", banner.scrollLeft)
            console.log(banner.scrollLeft <= target)
            banner.scrollLeft <= target? banner.scrollLeft +=10 : (onanimate=false,clearInterval(animate))
        },1)
    
    }
})
prevItemBtn.addEventListener("click",(e)=>{
    if(!onanimate){
        onanimate = true
        let width = window.innerWidth
        let index = (banner.scrollLeft/width - 1)
        let target = (index * width)+9
        console.log(index)
        e.preventDefault()
        console.log("next")
        const animate = setInterval(()=>{
            console.log("Animate ,", target," > ", banner.scrollLeft)
            console.log(banner.scrollLeft <= target)
            banner.scrollLeft >= target? banner.scrollLeft -=10 : (onanimate=false,clearInterval(animate))
        },1)
    }

})