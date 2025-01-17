const ctxchart = document.getElementById("userChart");
const repchart = document.getElementById("repChart");
const engchart = document.getElementById("engChart");

//console.log(ctxchart);
// console.log("datatableconnected");
// const hamburgers = document.querySelector("#myChart");
// console.log(hamburgers);

fetch('/api/rolewiseuser')
  .then(res =>res.json())
  .then(data => {
    new Chart(ctxchart, {
      type: 'bar',
      data: {
        labels: ['Admin', 'Receptionsit', 'Engineer', 'Reporter'],
        datasets: [{
          label: '# of Users',
          data: data.data,
          backgroundColor: [
        'rgba(255, 99, 132, 0.2)',
        'rgba(255, 159, 64, 0.2)',
        'rgba(75, 192, 192, 0.2)',
        'rgba(54, 162, 235, 0.2)',
      ],
      borderColor: [
        'rgb(255, 99, 132)',
        'rgb(255, 159, 64)',
        'rgb(75, 192, 192)',
        'rgb(54, 162, 235)',
        ],
          borderWidth: 1
        }]
      },
      options: {  
        responsive: true,  
        scales: {  
          y: {  
            beginAtZero: true,  // Ensure that the y-axis starts at 0  
            ticks: {  
              stepSize: 1       // Set step size to 1  
            }  
          }  
        }  
      }
    });

  });

  fetch('/api/reporterreportstatus/0')
  .then(res =>res.json())
  .then(data =>{ 
    new Chart(repchart, {
      type: 'line',
      data: {
        labels: ['Total', 'pending', 'Inprogress','Hold', 'completed'],
        datasets: [{
          label: '# of reporter Jobs',
          data: data.data,
          backgroundColor: [
        
        'rgba(54, 162, 235, 0.2)',    
        'rgba(255, 99, 132, 0.2)',
        'rgba(75, 192, 192, 0.2)',
        'rgba(255, 159, 64, 0.2)',
        'rgba(75, 192, 192, 0.2)',
        ],
      borderColor: [
        
        'rgb(54, 162, 235)',
        'rgb(255, 99, 132)',
        'rgb(54, 162, 235)',
        'rgb(255, 159, 64)',
        'rgb(75, 192, 192)',
        ],
          borderWidth: 1
        }]
      },
      options: {  
        responsive: true,  
        scales: {  
          y: {  
            beginAtZero: true,  // Ensure that the y-axis starts at 0  
            ticks: {  
              stepSize: 1       // Set step size to 1  
            }  
          }  
        }  
      }
    });

  });
  fetch('/api/engreportstatus/a/0')
  .then(res =>res.json())
  .then(data =>{ 
    new Chart(engchart, {
      type: 'line',
      data: {
        labels: ['Total', 'pending', 'Inprogress','Hold', 'completed'],
        datasets: [{
          label: '# of engineer Jobs',
          data: data.data,
          backgroundColor: [
        
        'rgba(54, 162, 235, 0.2)',    
        'rgba(255, 99, 132, 0.2)',
        'rgba(75, 192, 192, 0.2)',
        'rgba(255, 159, 64, 0.2)',
        'rgba(75, 192, 192, 0.2)',
        ],
      borderColor: [
        
        'rgb(54, 162, 235)',
        'rgb(255, 99, 132)',
        'rgb(54, 162, 235)',
        'rgb(255, 159, 64)',
        'rgb(75, 192, 192)',
        ],
          borderWidth: 1
        }]
      },
      options: {  
        responsive: true,  
        scales: {  
          y: {  
            beginAtZero: true,  // Ensure that the y-axis starts at 0  
            ticks: {  
              stepSize: 1       // Set step size to 1  
            }  
          }  
        }  
      }
    });

  });


  function addimpdoc() {
    addbtn=document.getElementById("addimpdoc");
    impdocaddbtn=document.getElementById("impdocaddbtn");
    // impdocsave=document.getElementById("impdocsave");
    // impdoccancel=document.getElementById("impdoccancel");
    impdocaddbtn.disabled = true;
    addbtn.style.display="block";
  }
  function addoptionvalue(label,id) {
    // console.log(label,id);
    document.getElementById("dummyid").value = id;
    addopbtn=document.getElementById("addoptions");
    addbtn=document.getElementById("addimpdoc");
    dropdownname=document.getElementById("dropdownname");
    dropdownname.innerHTML=label;
    addbtn.style.display="none";
    addopbtn.style.display="block";
  }
  function addsuboptionvalue(label,id) {
     console.log(label,id);
    document.getElementById("dummysubid").value = id;
    addsubopbtn=document.getElementById("addsuboptions");
    addbtn=document.getElementById("addimpdoc");
    dropdownname=document.getElementById("dropsuboption");
    dropdownname.innerHTML=label;
    addbtn.style.display="none";
    addsubopbtn.style.display="block";
    const selectElement = document.getElementById('subopt');
    selectElement.innerHTML = '';

    options.forEach(opt => {
      if (opt.eng_dynamic_field_id === id) {
          const option = document.createElement('option');
          option.value = opt.id;
          option.textContent = opt.opt_value;
          selectElement.appendChild(option);
      }
  });
  }
  function addimpdoccancel() {
    addopbtn=document.getElementById("addimpdoc");
    addopbtn.style.display="none";
  }
  function addoptioncancel() {
    addopbtn=document.getElementById("addoptions");
    addsubopbtn=document.getElementById("addsuboptions");
    addopbtn.style.display="none";
    addsubopbtn.style.display="none";
  }
  document.getElementById("addoptionvalbtn").onclick = function() {
    // $(document).on('click', '.addoptionvalbtn', function(event) {   
    console.log("clclick");
    var newRow = document.createElement("div");  
    newRow.className = "row mb-2";
  
    var optionsvaldiv = document.createElement("div");  
    optionsvaldiv.className = "col-md-6 d-flex align-items-center";  
    
    var optionvalInput = document.createElement("input");  
    optionvalInput.type = "text";  
    optionvalInput.name = "optionval[]";
    optionvalInput.className = "form-control col-md-6";  
    optionvalInput.placeholder = "Add options";  
    
    // var removeBtn = document.createElement("button");
    // removeBtn.className = "btn btn-danger btn-sm ms-2";
    // removeBtn.innerHTML = "-";
    // removeBtn.onclick = function() {
    //     newRow.remove();
    // };
    var removeLink = document.createElement("a");
    removeLink.className = "btn btn-danger btn-sm ms-2 circle";
    // removeLink.innerHTML = '<i class="fa-solid fa-circle-minus"></i>';
    removeLink.innerHTML = '<b>-</b>'
    removeLink.href = "#";
    removeLink.onclick = function(event) {
        event.preventDefault();
        newRow.remove();
    };
    optionsvaldiv.appendChild(optionvalInput); 
    optionsvaldiv.appendChild(removeLink); 
    newRow.appendChild(optionsvaldiv); 
     
    document.getElementById("optioncontainer").appendChild(newRow);  
  };
  document.getElementById("addsuboptionvalbtn").onclick = function() {
    console.log("clclick");
    var newRow = document.createElement("div");  
    newRow.className = "row mb-2";
  
    var optionsvaldiv = document.createElement("div");  
    optionsvaldiv.className = "col-md-6 d-flex align-items-center";  
    
    var optionvalInput = document.createElement("input");  
    optionvalInput.type = "text";  
    optionvalInput.name = "suboptionval[]";
    optionvalInput.className = "form-control col-md-6";  
    optionvalInput.placeholder = "Add sub options";  
    
    var removeLink = document.createElement("a");
    removeLink.className = "btn btn-danger btn-sm ms-2 circle";
    removeLink.innerHTML = '<b>-</b>'
    removeLink.href = "#";
    removeLink.onclick = function(event) {
        event.preventDefault();
        newRow.remove();
    };
    optionsvaldiv.appendChild(optionvalInput); 
    optionsvaldiv.appendChild(removeLink); 
    newRow.appendChild(optionsvaldiv); 
     
    document.getElementById("suboptioncontainer").appendChild(newRow);  
  };
  // function makeEditable(cell) {  
  //   console.log(cell)
  //   var input = document.createElement("input");  
  //   input.value = cell.innerText;  
  //   cell.innerText = '';  
  //   cell.appendChild(input);  
    
  //   input.addEventListener('blur', function() {  
  //     cell.innerText = input.value;  
  //   });  
    
  //   input.focus();  
  //   if(cell.id == 'doclink') {
      
  //   }
  //   console.log(cell.id);
  // } 

  

  // fetch('/api/rolewiseuser')
  // .then(res =>res.json())
  // .then(data => {
  //   new Chart(engrepchart, {
  //     type: 'bar',
  //     data: {
  //       labels: ['Reception', 'Engineer', 'Reporter'],
  //       datasets: [{
  //         label: '# of Users',
  //         data: data.data,
  //         backgroundColor: [
  //       'rgba(255, 99, 132, 0.2)',
  //       'rgba(255, 159, 64, 0.2)',
  //       'rgba(75, 192, 192, 0.2)',
  //       'rgba(54, 162, 235, 0.2)',
  //     ],
  //     borderColor: [
  //       'rgb(255, 99, 132)',
  //       'rgb(255, 159, 64)',
  //       'rgb(75, 192, 192)',
  //       'rgb(54, 162, 235)',
  //       ],
  //         borderWidth: 1
  //       }]
  //     },
  //     options: {
  //       responsive: true,
  //       scales: {
  //         y: {
  //           // suggestedMin: 1,
  //           // beginAtZero: true,
  //           stepSize: 1,
            
  //         }
  //       }
  //     }
  //   });

  // });


  // window.onload=function(){
  //   alert()
  // }
  //activating and deactivating user
  $(document).ready(function() {
    $('.activein').click(function(event) {
        event.preventDefault();
        var button = $(this);
        var url = button.data('url');
        //console.log(button.text());
        //console.log(url);
        $.ajax({
            url: url,
            type: 'GET',
            data: {
                csrfmiddlewaretoken: '{{ csrf_token }}'
            },
            success: function(response) {
                if (response.success) {
                    // button.closest('tr').remove();
                    if((button.text()).trim()=="InActive"){
                      button.html('<i class="fa-solid fa-user"></i> Active');
                      }else{
                      button.html('<i class="fa-solid fa-user-slash"></i> InActive');
                      }
                  } else {
                    alert('Error: ' + response.error);
                }
            }
        });
    });
});
// delete user home
$(document).ready(function() {
  $('.delet').click(function(event) {
      event.preventDefault();
      var button = $(this);
      var url = button.data('url');
      swal({  
        title: "Are you sure?",  
        text: "You will not be able to recall this user!",  
        icon: "warning",  
        buttons: true,  
        dangerMode: true,  
    }).then((willDelete) => {  
        if (willDelete) {  
            // If confirmed, redirect to the delete URL  
           // window.location.href = deleteUrl;  
           $.ajax({
            url: url,
            type: 'GET',
            data: {
                csrfmiddlewaretoken: '{{ csrf_token }}'
            },
            success: function(response) {
                if (response.success) {
                  button.closest('tr').remove();
                } else {
                    alert('Error: ' + response.error);
                }
            }
        });
        } else {  
            // Optionally do something when cancelled  
            swal("User is safe!");  
        }  
    });   
     // console.log(url);
     
  });
});





//   $(document).ready(function() {
//     console.log("jQuery is loaded");
// });
// $.ajax({
//   url: "https://jsonplaceholder.typicode.com/todos/1",
//   type: "GET",
//   success: function(response) {
//       console.log("Success:", response);
//   },
//   error: function(xhr, status, error) {
//       console.error("Error:", error);
//   }
// });
//   $(document).ready(function(){
//     console.log("active");
//     $("#active").click(function(event){
//         event.preventDefault(); // Prevent the default action
//         console.log("Anchor clicked");
//         $.ajax({
//             url: '/activeateuser/22', // Replace with your API endpoint
//             method: 'GET',
//             success: function(response) {
//                 // Handle the response data
//                 console.log(response);

//                 // Redirect to the URL after the AJAX call is successful
//                 // window.location.href = $("#myLink").attr("href");
//             },
//             error: function(error) {
//                 console.error('Error:', error);
//             }
//         });
//     });
// });



  const data = document.currentScript.dataset;
  const userdata =data.username;
  //  console.log(data);
  //  console.log(userdata);
  const userdatatable = document.getElementById("userTable");
// const userlist = [];
// if (data)
//     {
//         for (u in data){
            
//         }
//         //userlist.push([user.])
//     // console.log(user.)
//     };

$(document).ready(function() {
  
  $('#usertable').DataTable({
    //disable sorting on last column
    pageLength: 5,
    "columnDefs": [
      { "orderable": false, "targets": 8 }
      
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
  console.log("reception table");
} );
$(document).ready(function() {
  
  $('#banktable').DataTable({
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
  console.log("bank table");
} );


