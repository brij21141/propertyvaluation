function nextStep(step) {  
    
    var steps = document.querySelectorAll('.step'); 
    console.log(steps ); 
    console.log(step ); 
    steps.forEach(function(el) {  
        el.style.display = 'none';  
    });  
    document.getElementById('step' + step).style.display = 'block';  
    console.log(document.getElementById('step' + step).style.display); 
  }

  $(document).ready(function() {
  
    $('#reportertable').DataTable({
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
    // console.log("reception table");
  } );

  $(document).ready(function() {
    // console.log("reception table in reportyer js");
    $('#repunassigned').click(function(event) {
      $('#myModal').modal('show')
      // document.getElementById("assignurll").innerText =url;  
      // $('#assignurlid').val(id); 
      // console.log("reception table);");
        var fullApiUrl = apiBaseUrl + 'reception/reporterunassigned/';
       var engArray=[];
      //  let modhead=document.getElementById('modhead');
        $.ajax({
            url: fullApiUrl,
            type: 'GET',
            headers: {  
              'Authorization': 'Token ' + token // Replace 'yourToken' with the actual token variable  
          }, 
            data: {
                csrfmiddlewaretoken: '{{ csrf_token }}'
            },
            success: function(response) {
                if (response.success) {
                  engArray=response.data;  
                  engspinner.classList.add('spinnervisibility')
                  buildrepunassignedtable(engArray);  
                  // modhead.innerHTML='Inprogress Jobs';
                } else {
                    alert('Error: ' + response.error);
                }
            }
        });
    });
  });
  function buildrepunassignedtable(data) {
    
  var table =  document.getElementById('repunassignedtable');
  var row=`<tr></tr>`
  table.innerHTML = row
  for (var i=0; i<data.length; i++) { console.log(data[i].id);
    var row = `<tr>
    <td scope="row">${i+1}</td>
    <td scope="col">${data[i].applicationdate}</td>
    <td scope="col">${data[i].applicationnumber}</td>
    <td scope="col">${data[i].name}</td>
    <td scope="col">${data[i].bankname}</td>
    <td scope="col">${data[i].add1}</td>
    <td scope="col">${data[i].city}</td>
    <td scope="col">${data[i].phonenumber}</td>
    <td><a onclick="assignunassign(${data[i].id})" class="reportassign" id="reportassign" data-url="{% url 'reportassign' ${data[i].id} %}" href="#" title="Assign yourself"><i class="fas fa-tasks fa-2x" style="color: red;"></i></a></td>
    </tr>`
    table.innerHTML += row
    }
  }

  async function assignunassign(id) {
    $(document).ready(function() { console.log("abcd");
      var fullApiUrl = apiBaseUrl + 'reportassign/'+id;
    console.log(fullApiUrl,id);
          const icon = document.querySelector('#reportassign i'); // Select the <i> tag inside the anchor  
          var url=fullApiUrl;
          console.log(url);
          $.ajax({
              url: url,
              type: 'GET',
              data: {
                  csrfmiddlewaretoken: '{{ csrf_token }}'
              },
              success: function(response) {
                  if (response.success) {
                      // button.closest('tr').remove();
                      if(response.msg.trim()=="assigned"){
                          icon.style.color = 'green';
                          // location.reload();
                      }else{
                        icon.style.color = 'red';
                        // location.reload();
                        }
                        // alert('Success: ' + response.message);
                        swal({  
                          title: "Confirmation", 
                          text: response.message ,  
                          icon: "success",  
                          button: "Okay",  
                      // }).then((willReload) => {  
                      //   if (willReload) {  
                      //       location.reload();  // This will reload the current page  
                      //   }  
                    }); 
                      
                      // console.log(response);
                        $('#totunassign').text(response.tot);
                      //   $('#pending').text(response.pend);
                      //   $('#inprogress').text(response.inprog);
                      //   $('#hold').text(response.hold);
                      //   $('#compreq').text(response.com);
                    } else {
                      // alert('Error: ' + response.error);
                      swal({  
                        title: "Confirmation", 
                        text: response.msg ,  
                        icon: "error",
                        button: "Okay",  
                    });
                  }
                  // location.reload(); 
              }
          });
      });
  // });
}

function reportrefresh(){
  location.reload();
  // window.location.href = "/propval/report/";
} 