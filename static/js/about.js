document.addEventListener('DOMContentLoaded', (event) => {
    const video = document.getElementById('myVideo');

    // Check if the video element is muted and play the video
    if (video.muted) {
        video.muted = true;
        video.play().catch(error => {
            console.error('Error attempting to play the video:', error);
        });
    }

    // Unmute the video after user interaction
    document.body.addEventListener('click', () => {
        video.muted = false;
        video.play().catch(error => {
            console.error('Error attempting to play the video:', error);
        });
    });
});
