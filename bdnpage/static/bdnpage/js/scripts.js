document.addEventListener("DOMContentLoaded", function() {
    const loadingPage = document.getElementById('loading-page');
    const mainContent = document.getElementById('main-content');

    // Simulate loading time (e.g., 2 seconds)
    setTimeout(function() {
        loadingPage.style.opacity = '0';
        loadingPage.style.transition = 'opacity 0.5s ease';

        // Once faded out, hide the loading page and show the main content
        setTimeout(function() {
            loadingPage.style.display = 'none';
            mainContent.style.display = 'block';
        }, 500);
    }, 2000); // 2 seconds delay
});



// Update scroll progress bar width based on scroll position
window.addEventListener('scroll', function() {
    var scrollTop = window.pageYOffset || document.documentElement.scrollTop;
    var scrollHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
    var scrollPercentage = (scrollTop / scrollHeight) * 100;
    document.querySelector('.scroll-progress-inner').style.width = scrollPercentage + '%';
  });

  


  typing_effect(['Hello World', 'Website Developer', 'Graphics Designer', 'Digital Marketer', 'Branding'],
    ['#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF']);

function typing_effect(words, colors) {

var cursor = document.getElementById('cursor'); //cursor
var text = document.getElementById('text') //text

var blink = true;
var wait = false;
var letters_count = 1;
var temp = 1;

text.style.color = colors[0]
window.setInterval(function () { //wait between words when it starts writting
if (letters_count === 0 && wait === false) {
  wait = true;

  text.innerHTML = '' // leave a blank
  window.setTimeout(function () {
    var usedColor = colors.splice(0, 1)[0] //remove first element and get it as str
    colors.push(usedColor);
    var usedWord = words.splice(0, 1)[0]
    words.push(usedWord);
    temp = 1;
    text.style.color = colors[0]
    letters_count += temp;
    wait = false;
  }, 1000)
} else if (letters_count === words[0].length + 1 && wait === false) {
  wait = true;
  window.setTimeout(function () { //wait a bit until words finished and start deleting
    temp = -1;
    letters_count += temp;
    wait = false;
  }, 1000)
} else if (wait === false) { //write words                    
  text.innerHTML = words[0].substr(0, letters_count)
  letters_count += temp;
}
}, 120)
window.setInterval(function () {
if (blink) {
  cursor.style.opacity = "0";
  blink = false;
} else {
  cursor.style.opacity = "1";
  blink = true;
}
}, 400)
}

  