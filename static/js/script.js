// Qidiruv maydonini tozalash uchun JavaScript
        const searchInput = document.getElementById('searchInput');
        const clearButton = document.getElementById('clearSearch');

        // Matn kiritilganda tozalash tugmasini ko'rsatish/yashirish
        searchInput.addEventListener('input', () => {
            if (searchInput.value.length > 0) {
                clearButton.classList.add('visible');
            } else {
                clearButton.classList.remove('visible');
            }
        });

        // Tozalash tugmasini bosganda matnni o'chirish
        clearButton.addEventListener('click', () => {
            searchInput.value = '';
            clearButton.classList.remove('visible');
            searchInput.focus();
        });
        
        // Smooth scrolling for anchor links
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {
                    target.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            });
        });