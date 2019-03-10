const upComingLatestOverlay = () => {
    const videoPlay = document.querySelectorAll('.achievement-one');
    const videoOverlay = document.querySelector('.content-overlay');
    const closeVideoOverlay = document.querySelector('.close-content-overlay');
    videoPlay.forEach( (pos) => {
        pos.addEventListener('click', () => {
            videoOverlay.classList.add('active-content-overlay');
        });
    });
    closeVideoOverlay.addEventListener('click', () => {
        videoOverlay.classList.remove('active-content-overlay');
    });
}

upComingLatestOverlay();