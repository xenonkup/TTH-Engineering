// static/js/about.js
document.addEventListener('DOMContentLoaded', (event) => {
    const video = document.getElementById('myVideo');

    // Unmute the video after user interaction
    document.body.addEventListener('click', () => {
        video.muted = false;
        video.play().catch(error => {
            console.error('Error attempting to play the video:', error);
        });
    });
});
