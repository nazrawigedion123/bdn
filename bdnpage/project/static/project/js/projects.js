document.querySelectorAll('.card').forEach(card => {
    card.addEventListener('click', function() {
        const modal = document.getElementById('projectModal');
        const modalImage = modal.querySelector('.modal-image');
        const modalTitle = modal.querySelector('.modal-title');
        const modalDescription = modal.querySelector('.modal-description');
        const modalDate = modal.querySelector('.modal-date');
        const shareOptions = modal.querySelector('.share-options');
        const likeButton = modal.querySelector('.like-button');
        const likeCounter = modal.querySelector('.like-counter');

        // Get project data
        const title = this.getAttribute('data-title');
        const description = this.getAttribute('data-description');
        const date = this.getAttribute('data-date');
        const images = JSON.parse(this.getAttribute('data-images'));
        
        let currentImageIndex = 0;

        // Display first image
        modalImage.src = images[currentImageIndex];

        // Set project details
        modalTitle.textContent = title;
        modalDescription.textContent = description;
        modalDate.textContent = `Date: ${date}`;

        // Show modal
        modal.classList.add('active');

        // Handle carousel navigation
        const prevButton = modal.querySelector('.prev');
        const nextButton = modal.querySelector('.next');

        prevButton.onclick = () => {
            currentImageIndex = (currentImageIndex - 1 + images.length) % images.length;
            modalImage.src = images[currentImageIndex];
        };

        nextButton.onclick = () => {
            currentImageIndex = (currentImageIndex + 1) % images.length;
            modalImage.src = images[currentImageIndex];
        };

        // Toggle share options
        const shareButton = modal.querySelector('.share-button');
        shareButton.addEventListener('click', () => {
            shareOptions.classList.toggle('active');
        });

        // Like button functionality
        let likes = parseInt(likeCounter.textContent);
        likeButton.addEventListener('click', () => {
            likes += 1;
            likeCounter.textContent = likes;
        });
    });
});

// Close modal when clicking the close button
document.querySelector('.modal .close').addEventListener('click', function() {
    document.getElementById('projectModal').classList.remove('active');
});
