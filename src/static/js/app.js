// Debounce Function for Scroll Animation  

function debounce(func, wait = 20, immediate = true) {
    var timeout;
    return function() {
      var context = this, args = arguments;
      var later = function() {
        timeout = null;
        if (!immediate) func.apply(context, args);
      };
      var callNow = immediate && !timeout;
      clearTimeout(timeout);
      timeout = setTimeout(later, wait);
      if (callNow) func.apply(context, args);
    };
}

// All Functions 

const navSlide = () => {
    var viewportWidth = window.innerWidth || document.documentElement.clientWidth;
    const body = document.querySelector('body');
    const toggle = document.querySelector('.nav-toggle');
    const nav = document.querySelector('.navs');
    const navLinks = document.querySelectorAll('ul li');

        // Toggle Nav 
    toggle.addEventListener('click', () =>{
        nav.classList.toggle('nav-active');
        body.classList.toggle('hidden');

         // Animate Link 
        navLinks.forEach((link, index) => {
            if(link.style.animation){
                link.style.animation = '';
            }else{
                link.style.animation = `navLinkFade 0.5s ease forwards ${index / 5 + 0.3}s`;
            }
        });

        toggle.classList.toggle('cros');
    })

    window.addEventListener('resize', function () {
        viewportWidth = window.innerWidth || document.documentElement.clientWidth;
        if (viewportWidth > 889) {
            if(body.classList.value == "hidden"){
                body.classList.remove('hidden');
            }
            if(nav.classList.length > 0){
                nav.classList.remove('nav-active');
                // nav.style.transition = "none";
            }

            navLinks.forEach((link, index) => {
                link.style.animation = '';
            });

            toggle.classList.remove('cros');
        }

        
    }, false);

}


const videoOverlayOpen = () => {
    const videoPlay = document.querySelector('.video-play-btn');
    const videoOverlay = document.querySelector('.video-overlay');
    const closeVideoOverlay = document.querySelector('.close-video-overlay');
    videoPlay.addEventListener('click', () => {
        videoOverlay.classList.add('active-video-overlay');
    }); 

    closeVideoOverlay.addEventListener('click', () => {
        videoOverlay.classList.remove('active-video-overlay');
    });
}


const upComingOverlay = () => {
    const videoPlay = document.querySelector('#achievement');
    const videoOverlay = document.querySelector('.content-overlay');
    const closeVideoOverlay = document.querySelector('.close-content-overlay');
    videoPlay.addEventListener('click', () => {
        videoOverlay.classList.add('active-content-overlay');
    }); 

    closeVideoOverlay.addEventListener('click', () => {
        videoOverlay.classList.remove('active-content-overlay');
    });
}



// Change Image

var i = 0; 			// Start Point
var images = [];	// Images Array
var time = 4000;	// Time Between Switch
var setImage = document.getElementsByName('slide');
	 
images[0] = "static/images/college.jpeg";
images[1] = "static/images/nasscom.jpg";

setImage.forEach((link) =>{
    link.style.opacity = "1";
    link.style.transform = "scale(1)";
});

function changeImg(){
    document.slide.src = images[i];
	// Check If Index Is Under Max
	if(i < images.length - 1){
	  // Add 1 to Index
      i++; 
      
	} else { 
		// Reset Back To O
		i = 0;
	}

	// Run function every x seconds
	setTimeout("changeImg()", time);
}



// Typing Effects 
class TypeWriter {
    constructor(txtElement, words, wait = 3000) {
      this.txtElement = txtElement;
      this.words = words;
      this.txt = '';
      this.wordIndex = 0;
      this.wait = parseInt(wait, 10);
      this.type();
      this.isDeleting = false;
    }
  
    type() {
      // Current index of word
      const current = this.wordIndex % this.words.length;
      // Get full text of current word
      const fullTxt = this.words[current];
  
      // Check if deleting
      if(this.isDeleting) {
        // Remove char
        this.txt = fullTxt.substring(0, this.txt.length - 1);
      } else {
        // Add char
        this.txt = fullTxt.substring(0, this.txt.length + 1);
      }
  
      // Insert txt into element
      this.txtElement.innerHTML = `<span class="txt">&nbsp;${this.txt}</span>`;
  
      // Initial Type Speed
      let typeSpeed = 200;
  
      if(this.isDeleting) {
        typeSpeed /= 2;
      }
  
      // If word is complete
      if(!this.isDeleting && this.txt === fullTxt) {
        // Make pause at end
        typeSpeed = this.wait;
        // Set delete to true
        this.isDeleting = true;
      } else if(this.isDeleting && this.txt === '') {
        this.isDeleting = false;
        // Move to next word
        this.wordIndex++;
        // Pause before start typing
        typeSpeed = 500;
      }
  
      setTimeout(() => this.type(), typeSpeed);
    }
  }
  
  
  // Init On DOM Load
  document.addEventListener('DOMContentLoaded', init);
  
  // Init App
  function init() {
    const txtElement = document.querySelector('.txt-type');
    const words = JSON.parse(txtElement.getAttribute('data-words'));
    const wait = txtElement.getAttribute('data-wait');
    // Init TypeWriter
    new TypeWriter(txtElement, words, wait);
  }


/* scroll Animation functions */
/* function scrollAppear(){
    const introText = document.querySelector('.home-faculties__college');

    const homeLatest = document.querySelector('.home-latest__student');
    const homeUpcoming = document.querySelector('.home-latest__upcoming');
    
    const projectSection = document.querySelectorAll('#home-projects .row div');
    const teamSection = document.querySelectorAll('#home-team .row div');



    var introPosition  = introText.getBoundingClientRect().top;
    var latestPosition  = homeLatest.getBoundingClientRect().top;
    var upcomingPosition  = homeUpcoming.getBoundingClientRect().top;

    var screePosition = window.innerHeight / 1.2;

    if (introPosition < screePosition){
        introText.style.opacity = "1";
        //introText.style.transform = "translate3d(0px, 0px, 0px)";
    }

    if (latestPosition < screePosition){
        homeLatest.style.opacity = "1";
        //homeLatest.style.transform = "translate3d(0px, 0px, 0px)";
    }

    if (upcomingPosition < screePosition){
        homeUpcoming.style.opacity = "1";
        //homeUpcoming.style.transform = "translate3d(0px, 0px, 0px)";
    }

    projectSection.forEach((pos) => {
        let projectSectionPositions = pos.getBoundingClientRect().top;
        
        if (projectSectionPositions < screePosition){
            pos.style.opacity = "1";
            //pos.style.transform = "translate3d(0px, 0px, 0px)";
        }
    });

    teamSection.forEach((pos) => {
        let projectSectionPositions = pos.getBoundingClientRect().top;
        
        if (projectSectionPositions < screePosition){
            pos.style.opacity = "1";
            //pos.style.transform = "translate3d(0px, 0px, 0px)";
        }
    });
} */

/* End of scroll animation function  */


// Function Calls 

// Run function when page loads
window.onload=changeImg;
// window.addEventListener('scroll', scrollAppear);

const app = () =>{
    navSlide();
    videoOverlayOpen();
    upComingOverlay();
}

app();


