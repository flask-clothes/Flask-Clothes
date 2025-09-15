const bannerInner = document.getElementById("banner-inner");

if (bannerInner) {
    const prevBtn = document.getElementById("prev-btn");
    const nextBtn = document.getElementById("next-btn");
    const bannerItems = document.querySelectorAll(".banner--item");
    let currentIndex = 0;

    function updateBanner() {
        const itemWidth = bannerItems[0].clientWidth;
        bannerInner.style.transform = `translateX(${-currentIndex * itemWidth}px)`;
    }

    nextBtn.addEventListener("click", () => {
        currentIndex = (currentIndex + 1) % bannerItems.length;
        updateBanner();
    });

    prevBtn.addEventListener("click", () => {
        currentIndex = (currentIndex - 1 + bannerItems.length) % bannerItems.length;
        updateBanner();
    });

    window.addEventListener('load', updateBanner);
    window.addEventListener('resize', updateBanner);
}