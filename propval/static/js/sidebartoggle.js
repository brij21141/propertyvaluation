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
     console.log(data.data[4]);
    //  navprofileimg.src='/propval/static/img/OIP.jpg';
    //  navmenuprofileimg.src='/propval/static/img/OIP.jpg';
    if(data.data[4]) {
    navprofileimg.setAttribute('src',data.data[4]);
     navmenuprofileimg.setAttribute('src',data.data[4]);
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





 
