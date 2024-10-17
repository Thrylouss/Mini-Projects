(function() {
    const popularContent = document.querySelector('#popular-content');
    const newContent = document.querySelector('#new-content');
    const discountContent = document.querySelector('#discount-content');
    const popularModel = document.querySelector('.popular-model');
    const newModel = document.querySelector('.new-model');
    const discountModel = document.querySelector('.discount-model');

    popularContent.addEventListener('click', () => {
        popularContent.classList.add('current-model');
        newContent.classList.remove('current-model');
        discountContent.classList.remove('current-model');
        popularModel.classList.remove('hidden');
        newModel.classList.add('hidden');
        discountModel.classList.add('hidden');
    });

    newContent.addEventListener('click', () => {
        newContent.classList.add('current-model');
        popularContent.classList.remove('current-model');
        discountContent.classList.remove('current-model');
        popularModel.classList.add('hidden');
        newModel.classList.remove('hidden');
        discountModel.classList.add('hidden');
    });

    discountContent.addEventListener('click', () => {
        discountContent.classList.add('current-model');
        newContent.classList.remove('current-model');
        popularContent.classList.remove('current-model');
        popularModel.classList.add('hidden');
        newModel.classList.add('hidden');
        discountModel.classList.remove('hidden');
    });

    function initializeCarousel() {
        const track = document.querySelector('.carousel-track');
        if (!track) return;

        const slides = Array.from(track.children);
        const nextButton = document.querySelector('#nextBtn');
        const prevButton = document.querySelector('#prevBtn');
        let currentIndex = 0;

        function updateCarousel() {
            const slideWidth = slides[0].getBoundingClientRect().width;
            track.style.transform = `translateX(-${currentIndex * slideWidth}px)`;
        }

        nextButton.addEventListener('click', () => {
            currentIndex++;
            if (currentIndex >= slides.length) {
                currentIndex = 0;
            }
            updateCarousel();
        });

        prevButton.addEventListener('click', () => {
            currentIndex--;
            if (currentIndex < 0) {
                currentIndex = slides.length - 1;
            }
            updateCarousel();
        });

        window.addEventListener('resize', updateCarousel);

        updateCarousel();
    }

    function updateContent(category) {
        document.querySelector('.carousel-track').innerHTML = ''; // Clear old slides
        const newSlides = getSlidesForCategory(category); // Get new slides based on category

        newSlides.forEach(slide => {
            document.querySelector('.carousel-track').appendChild(slide);
        });

        initializeCarousel(); // Reinitialize the carousel with new content
    }

    popularContent.addEventListener('click', () => {
        updateContent('popular');
    });

    newContent.addEventListener('click', () => {
        updateContent('new');
    });

    discountContent.addEventListener('click', () => {
        updateContent('discount');
    });

    initializeCarousel(); // Initialize carousel on page load

})();
