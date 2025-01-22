document.addEventListener('DOMContentLoaded', () => {  
  const container = document.getElementById('scrollContainer');  
  const items = Array.from(container.children);  
  
  // Clone the items to create an infinite scrolling effect  
  items.forEach(item => {  
      const clone = item.cloneNode(true);  
      container.appendChild(clone);  
  });  
  
  let scrollPosition = 0; // Initial scroll position  
  const scrollSpeed = 1; // Pixels to scroll per interval  
  const scrollInterval = 20; // Milliseconds between scrolls  

  function autoScroll() {  
      // Scroll by `scrollSpeed` pixels  
      scrollPosition += scrollSpeed;   
      container.scrollTop = scrollPosition;  

      // If we've scrolled past the original content height, reset to the top  
      if (scrollPosition >= container.scrollHeight / 2) {  
          scrollPosition = 0; // Reset scroll position  
      }  
  }  
  function startScrolling() {  
    // Start auto-scrolling at defined intervals  
    intervalId = setInterval(autoScroll, scrollInterval);  
}  

function stopScrolling() {  
    // Clear the interval to stop scrolling  
    clearInterval(intervalId);  
}

  // Start auto-scrolling at defined intervals  
  // setInterval(autoScroll, scrollInterval); 
  startScrolling(); 

  container.addEventListener('mouseover', stopScrolling);  
    container.addEventListener('mouseout', startScrolling);  
});

const hamburger = document.querySelector("#toggle-btn");
console.log("sidebar connected");
hamburger.addEventListener("click",function(){
    document.querySelector("#sidebar").classList.toggle("expand");
});

let navbarname=document.getElementById("topnavbarmenuusername");
let topnavbarname=document.getElementById("topnavbarusername");
let topnavbaremail=document.getElementById("topnavbaremail");
let navprofileimg=document.getElementById("navprofileimg");
let navmenuprofileimg = document.getElementById("navmenuprofileimg");
fetch('/api/currentuser')
  .then(res =>res.json())
//   .then(data => (console.log(data.data[1])));
  .then(data =>{ 
     navbarname.textContent=data.data[1];
     topnavbarname.textContent=data.data[1]+" ("+ data.data[3]+" )";
     topnavbaremail.textContent=data.data[2];
    //  console.log(data.data[3]);
    //  navprofileimg.src='/propval/static/img/OIP.jpg';
    //  navmenuprofileimg.src='/propval/static/img/OIP.jpg';
    if(data.data[4]) {
    navprofileimg.setAttribute('src',data.data[4]);
     navmenuprofileimg.setAttribute('src',data.data[4]);
    }
    if(data.data[3]=='Engineer') {
      // engspinner.classList.add('spinnervisibility') document.getElementById("globalengtablediv").style.display = "none";
      document.getElementById("dashboard").style.display = "none";
      document.getElementById("reception").style.display = "none";
      document.getElementById("sidebar").style.display = "none";
      // document.getElementById("engineer").style.display = "none";
      document.getElementById("reporter").style.display = "none";
      document.getElementById("bankmgmt").style.display = "none";
      document.getElementById("compprofile").style.display = "none";
      document.getElementById("genbill").style.display = "none";
      document.getElementById("administration").style.display = "none";
      document.getElementById("repinitiate").style.display = "none";
      document.querySelectorAll('.engedit').forEach(function(element) {  
        element.style.display = 'none';  
    }); 
    }else if(data.data[3]=='Reporter') {
      document.getElementById("dashboard").style.display = "none";
      document.getElementById("reception").style.display = "none";
      document.getElementById("engineer").style.display = "none";
      // document.getElementById("reporter").style.display = "none";
      document.getElementById("bankmgmt").style.display = "none";
      document.getElementById("compprofile").style.display = "none";
      document.getElementById("genbill").style.display = "none";
      document.getElementById("administration").style.display = "none";
      document.querySelectorAll('.repedit').forEach(function(element) {  
        element.style.display = 'none';  
    }); 
      
    }
    else if(data.data[3]=='Reception') {
      document.getElementById("dashboard").style.display = "none";
      // document.getElementById("reception").style.display = "none";
      document.getElementById("engineer").style.display = "none";
      document.getElementById("reporter").style.display = "none";
      document.getElementById("bankmgmt").style.display = "none";
      document.getElementById("compprofile").style.display = "none";
      // document.getElementById("genbpythonill").style.display = "none";
      document.getElementById("administration").style.display = "none";
      document.getElementById("repinitiate").style.display = "none";
      document.querySelectorAll('.recedit').forEach(function(element) {  
        element.style.display = 'none';  
    }); 
    }
    else if(data.data[3]=='Admin') {
      
    }
    let pageTitle = document.title;  
    console.log(pageTitle);
    if(pageTitle=="Home" || pageTitle=="Reception" || pageTitle=="Site Engineer" || pageTitle=="Reporter"){
      document.getElementById("globsearch").style.display = "inline-block";
    }  
});

let submenu =document.getElementById("submenu");
function toggleMenu(){
  submenu.classList.toggle("open-menu");
}

$(document).ready(function() {
  console.log("log table");
  $('#userlogtable').DataTable({
    //disable sorting on last column
    pageLength: 5,
    "columnDefs": [
      { "orderable": false, "targets": 6 }
      
    ],
    
    language: {
      //customize pagination prev and next buttons: use arrows instead of words
      'paginate': {
        'previous': '<span class="fa fa-chevron-left"></span>',
        'next': '<span class="fa fa-chevron-right"></span>'
      },
      //customize number of elements to be displayed
      "lengthMenu": 'Display <select class="form-control input-sm">'+
      '<option value="5">5</option>'+
      '<option value="10">10</option>'+
      '<option value="20">20</option>'+
      '<option value="-1">All</option>'+
      '</select> results'
    }
  })  
  console.log("log table");
} );


const img = document.querySelector('#profileimaged');
document.getElementById('profileimage').onchange = function(event) {
  const file = event.target.files[0];
  console.log(file);
  if (file) {
  const reader = new FileReader();
  reader.addEventListener('load',function(){
    img.setAttribute('src',reader.result);
    
  });
  reader.readAsDataURL(file)
  }
};


  function cancelAction() {  
    // Get the last accessed URL from localStorage  
    const lastUrl = localStorage.getItem('last_accessed_url') || '/default-url/';  
    
    // Redirect to the last accessed URL  
    window.location.href = lastUrl;  
}  
//   function addmorerows() {  
//     document.getElementById("tf").style.display = "inline-block";
//     document.getElementById("frf").style.display = "inline-block";
//     document.getElementById("fvf").style.display = "inline-block";
//     document.getElementById("sxf").style.display = "inline-block";
//     document.getElementById('addmorerows').disabled = true;  
// }  


 
