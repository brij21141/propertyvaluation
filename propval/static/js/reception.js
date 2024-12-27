$(document).ready(function() {
    $('.priorit').click(function(event) {
        event.preventDefault();
        var button = $(this);
        var url = button.data('url');
        $.ajax({
            url: url,
            type: 'GET',
            data: {
                csrfmiddlewaretoken: '{{ csrf_token }}'
            },
            success: function(response) {
                if (response.success) {
                        var currentColor = button.css('color');
                        if(currentColor==='rgb(0, 128, 0)'){
                            console.log('Current colour:', currentColor);
                            button.css('color', 'red');
                            button.closest('tr').css('color','red');
                            var row = button.closest('tr');
                            row.addClass('table-danger');
                            if (response.success) {
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
                        }
                        }else{
                            console.log('Current color:', currentColor);
                            button.css('color', 'green');
                            var row = button.closest('tr');
                            row.removeClass('table-danger');
                            row.addClass('');
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
                        }
                      }  
                   else {
                    alert('Error: ' + response.error);
                }
            }
          
        });
    });
});

function toggleFunction(isChecked,recid) {  
  var fullApiUrl = apiBaseUrl + 'recepreportnpa/'+recid;
  console.log(fullApiUrl); 
  var row = $('#row-' + recid);
  $.ajax({
  url: fullApiUrl,
  type: 'GET',
  data: {
      csrfmiddlewaretoken: '{{ csrf_token }}'
  },
  success: function(response) {
    // var row = document.getElementById('row-' + recid);  
      
      if (response.success) {
        if (response.npacase) {
        row.addClass('table-warning');
        }
        else {
          row.removeClass('table-warning');
        }
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
        } else {
          alert('Error: ' + response.error);
      }
  }
});
   
} 

fetch('/api/engreportstatus/a/0')
  .then(res =>res.json())
  .then(data =>{ 
  console.log(data);
  $('#comp').text(data.com);
  $('#pend').text(data.pend);
  $('#inprog').text(data.inprog);
  $('#engcom').text(data.com);
//   console.log(data.com*100/(data.inprog+data.pend+data.com));
  let wd=Math.round(data.com*100/(data.inprog+data.pend+data.com+data.hold))+"%";
  $('#engper').text(wd);
//   console.log(wd);
  $(".progress-bar").css("width", wd);
});

fetch('/api/reporterreportstatus/0')
  .then(res =>res.json())
  .then(data =>{ 
  console.log(data);
  $('#rcomp').text(data.com);
  $('#rpend').text(data.pend);
  $('#rinprog').text(data.inprog);
  $('#rtot').text(data.tot);
  $('#rhold').text(data.hold);
  $('#recom').text(data.com);
  $('#rtotreq').text(data.tot);
  
  // console.log(data.com*100/(data.inprog+data.pend+data.com));
  let rwd=Math.round(data.com*100/(data.inprog+data.pend+data.com+data.hold))+"%";
  $('#repper').text(rwd);
  console.log(rwd);
  $(".progress-bara").css("width", rwd);
});
$(document).ready(function() {
    $('.recdelete').click(function(event) {
        event.preventDefault();
        var button = $(this);
        var url = button.data('url');
        swal({  
          title: "Are you sure?",  
          text: "You will not be able to recall this record!",  
          icon: "warning",  
          buttons: true,  
          dangerMode: true,  
      }).then((willDelete) => {  
          if (willDelete) {  
        $.ajax({
            url: url,
            type: 'GET',
            data: {
                csrfmiddlewaretoken: '{{ csrf_token }}'
            },
            success: function(response) {
                if (response.success) {
                  button.closest('tr').remove();
                  console.log(response.total + response.message);
                  $('#totrecrep').text('');
                  $('#totrecrep').text(response.total);
                } else {
                  $('#totrecrep').text('');
                  $('#totrecrep').text(response.total);
                  swal({  
              
                    text: response.message,  
                    
                    button: "Okay",  
                });
                  // alert('Error: ' + response.message);
                }
            }
        });
      } else {  
        // Optionally do something when cancelled  
        swal("Record is safe!");  
    }  
});  
    });
  });

  $(document).ready(function() {
  
    $('#receptiontable').DataTable({
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
    // console.log("reception table");
  } );
  $(document).ready(function() {
  
    $('#impdoctable').DataTable({
      //disable sorting on last column
      pageLength: 5,
      "columnDefs": [
        { "orderable": false, "targets": 4 }
        
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
// eye view of reception dasboard modal heading fix here modhead---->modal head
  let modhead=document.getElementById('modhead');  
  let repmodhead=document.getElementById('repmodhead');
  let engspinner=document.getElementById('engspinner');
  $(document).ready(function() {
    $('#engcomp').click(function(event) {
        var fullApiUrl = apiBaseUrl + 'engineer/engineercomjob/';
       var engArray=[];
        $.ajax({
            url: fullApiUrl,
            type: 'GET',
            data: {
                csrfmiddlewaretoken: '{{ csrf_token }}'
            },
            success: function(response) {
                if (response.success) {
                  engArray=response.data;  
                  engspinner.classList.add('spinnervisibility') 
                  console.log('spinnervisibility')
                  buildtable(engArray);  
                  modhead.innerHTML='Completed by Engineers'; 
                } else {
                    alert('Error: ' + response.error);
                }
            }
        });
    });
});

$(document).ready(function() {
  $('#engpend').click(function(event) {
    // console.log("Clicked on " );
    //   event.preventDefault();
    //   var button = $(this);
    //   var url = button.data('url');
      var fullApiUrl = apiBaseUrl + 'engineer/engineerpendjob/';
      // console.log(fullApiUrl);
     

      // Perform an AJAX request (example)
      
     // console.log(url);
     var engArray=[];
      $.ajax({
          url: fullApiUrl,
          type: 'GET',
          
          data: {
              csrfmiddlewaretoken: '{{ csrf_token }}'
              
          },
          
          success: function(response) {
            // console.log(response.data);
              if (response.success) {
                // console.log(response.data);
                engArray=response.data;  
                buildpendinprogtable(engArray);  
                engspinner.classList.add('spinnervisibility')
                modhead.innerHTML='Pending Jobs';
              } else {
                  alert('Error: ' + response.error);
              }
          }
      });
  });
});

$(document).ready(function() {
  $('#enginprog').click(function(event) {
      var fullApiUrl = apiBaseUrl + 'engineer/engineerinprogjob/';
     var engArray=[];
    //  let modhead=document.getElementById('modhead');
      $.ajax({
          url: fullApiUrl,
          type: 'GET',
          data: {
              csrfmiddlewaretoken: '{{ csrf_token }}'
          },
          success: function(response) {
              if (response.success) {
                engArray=response.data;  
                engspinner.classList.add('spinnervisibility')
                buildpendinprogtable(engArray);  
                modhead.innerHTML='Inprogress Jobs';
              } else {
                  alert('Error: ' + response.error);
              }
          }
      });
  });
});
function buildtable(data) {
  
var table =  document.getElementById('engcomptable');
var row=`<tr></tr>`
table.innerHTML = row
for (var i=0; i<data.length; i++) {
  var row = `<tr>
  <td scope="row">${i+1}</td>
  <td scope="col">${data[i].applicationnumber}</td>
  <td scope="col">${data[i].name}</td>
  <td scope="col">${data[i].visitinpresence}</td>
  <td scope="col">${data[i].bankname}</td>
  <td scope="col">${data[i].casetype}</td>
  <td scope="col">${data[i].receptionid.visitingpersonname}</td>
  <td><a href="../../reception/engcompreportpdf/${data[i].id}" id="" type="" target="_blank"> <i class="fa-regular fa-eye"></i></a></td>
  </tr>`
  table.innerHTML += row
  }
}
function buildpendinprogtable(data) {
  
var table =  document.getElementById('engcomptable');
var row=`<tr></tr>`
table.innerHTML = row
for (var i=0; i<data.length; i++) {
  var row = `<tr>
  <td scope="row">${i+1}</td>
  <td scope="col">${data[i].applicationnumber}</td>
  <td scope="col">${data[i].name}</td>
  <td scope="col">N/A</td>
  <td scope="col">${data[i].bankname}</td>
  <td scope="col">${data[i].bankvertical}</td>
  <td scope="col">${data[i].visitingpersonname}</td>
  </tr>`
  table.innerHTML += row
  }
}

   
// $(document).ready(function() {
  function repview(id){
    // console.log(id)
  // $('#reppend').click(function(event) {
    reportspinner=document.getElementById('reportspinner');
  if (id=='rephold') {
    var fullApiUrl = apiBaseUrl + 'reporter/reporterholdjob/';
  }else if(id=='reppend') {
     var fullApiUrl = apiBaseUrl + 'reporter/reporterpendjob/';
  }else if(id=='repinprog'){
    var fullApiUrl = apiBaseUrl + 'reporter/reporterinprogjob/';
  }else if(id=='repcomp'){
    var fullApiUrl = apiBaseUrl + 'reporter/reportercomjob/';
  }else if(id=='reqrecrep'){
    var fullApiUrl = apiBaseUrl + 'reporter/reporterrecjob/';
    // console.log(fullApiUrl, "home");
  }

     var engArray=[];
      $.ajax({
          url: fullApiUrl,
          type: 'GET',
          
          data: {
              csrfmiddlewaretoken: '{{ csrf_token }}'
              
          },
          
          success: function(response) {
            // console.log(response.data);
              if (response.success) {
                console.log(response.data);
                repArray=response.data; 
                reportspinner.classList.add('spinnervisibility') 
                buildreppendinprogtable(repArray,id);  
                
              } else {
                  alert('Error: ' + response.error);
              }
          }
      });
  };
// });

function buildreppendinprogtable(data,id) {
  // console.log(id);
  var table =  document.getElementById('reptable');
  var reptableheader =  document.getElementById('reptableheader');
 
  if (id=='rephold'){
    repmodhead.innerHTML='Reporter hold Jobs';
    var tabhead = `<tr>
    <th scope="col">#</th>
                    <!-- <th scope="col">APP.DATE</th> -->
                    <th scope="col">APP.NO.</th>
                    <th scope="col">NAME</th>
                    <th scope="col">Visit in presence</th>
                    <th scope="col">BANK NAME</th>
                    <th  scope="col">Engineer</th>
                    <th  scope="col">Completed by Engineer on</th>
                    <th scope="col">Reporter</th>
                    <th scope="col">Hold Cause</th>
    </tr>`  
  } else if (id=='reppend' || id=='repinprog' || id=='reqrecrep'){
    // console.log(table);
    // console.log(reptableheader);
  var tabhead = `<tr>
  <th scope="col">#</th>
                  <!-- <th scope="col">APP.DATE</th> -->
                  <th scope="col">APP.NO.</th>
                  <th scope="col">NAME</th>
                  <th scope="col">Visit in presence</th>
                  <th scope="col">BANK NAME</th>
                  <th scope="col">Case type</th>
                  <th  scope="col">Engineer</th>
                  <th  scope="col">Completed by Engineer on</th>
                  <th scope="col">Reporter</th>
  </tr>`
  }else if (id=='repcomp'){
    var tabhead = `<tr>
  <th scope="col">#</th>
                  <th scope="col">Inspection DATE</th>
                  <th scope="col">APP.NO.</th>
                  <th scope="col">NAME</th>
                  <th scope="col">Property type</th>
                  <th  scope="col">Engineer</th>
                  <th  scope="col">Completed by Engineer on</th>
                  <th scope="col">Reporter</th>
                  <th scope="col">Valuation Result</th>
                  <th scope="col">Completed by Reporter on</th>
                  <th scope="col">View</th>
  </tr>`
  }
  reptableheader.innerHTML=tabhead
  var row=`<tr> </tr>`
  table.innerHTML = row
  if (id=='reppend' || id=='repinprog' || id=='reqrecrep'){
      if (id=='repinprog'){
        repmodhead.innerHTML='Reporter In progress Jobs';
      }else if (id=='reppend'){
      repmodhead.innerHTML='Reporter Pending Jobs';
      }else if(id=='reqrecrep'){
        repmodhead.innerHTML='Reporter received Jobs';
      }
  for (var i=0; i<data.length; i++) {
    var row = `<tr>
    <td scope="row">${i+1}</td>
    <td scope="col">${data[i].applicationnumber}</td>
    <td scope="col">${data[i].name}</td>
    <td scope="col">${data[i].visitinpresence}</td>
    <td scope="col">${data[i].bankname}</td>
    <td scope="col">${data[i].casetype}</td>
    <td scope="col">${data[i].receptionid.visitingpersonname}</td>
    <td>${moment((data[i].updated_at).split('T')[0]).format('DD-MM-YYYY')}</td>
    <td scope="col">${data[i].receptionid.reportpersonname}</td>
    </tr>`
    table.innerHTML += row
    }
  }else if (id=='rephold'){
    for (var i=0; i<data.length; i++) {
      var row = `<tr>
      <td scope="row">${i+1}</td>
      <td scope="col">${data[i].applicationnumber}</td>
      <td scope="col">${data[i].name}</td>
      <td scope="col">${data[i].visitinpresence}</td>
      <td scope="col">${data[i].bankname}</td>
      <td scope="col">${data[i].receptionid.visitingpersonname}</td>
      <td>${moment((data[i].updated_at).split('T')[0]).format('DD-MM-YYYY')}</td>
      <td scope="col">${data[i].receptionid.reportpersonname}</td>
      <td scope="col">${data[i].casetype}</td> 
      
      </tr>`
      table.innerHTML += row
    }
  }else if (id=='repcomp'){
    repmodhead.innerHTML='Reporter Completed Jobs';
    for (var i=0; i<data.length; i++) {
      var row = `<tr>
      <td scope="row">${i+1}</td>
      <td>${moment((data[i].inspectiondate).split('T')[0]).format('DD-MM-YYYY')}</td>
      <td scope="col">${data[i].applicationnumber}</td>
      <td scope="col">${data[i].name}</td>
      <td scope="col">${data[i].propertytype}</td> 
      <td scope="col">${data[i].receptionid.visitingpersonname}</td>
      <td>${moment((data[i].updated_at).split('T')[0]).format('DD-MM-YYYY')}</td>
      <td scope="col">${data[i].receptionid.reportpersonname}</td>
      <td scope="col">${data[i].valuationresult}</td>
      <td>${moment((data[i].updated_at).split('T')[0]).format('DD-MM-YYYY')}</td>
      <td><a href="../../reception/repcompreportpdf/${data[i].id}" id="" type="" target="_blank"> <i class="fa-regular fa-eye"></i></a></td>
      </tr>`
      table.innerHTML += row
    }
  }
  }

  //   global search for home and reception
$(document).ready(function() {  
  $.fn.dataTable.ext.errMode = 'throw'; // Optional, to throw descriptive errors  
  if ($.fn.dataTable.isDataTable('#globalsearchengineertable')) {  
      $('#globalsearchengineertable').DataTable().clear().destroy();  
  } 
  var globalengtable = $('#globalsearchengineertable').DataTable({
    // pageLength: 5,
    paginate:false,
    "columnDefs": [
      { "orderable": false, "targets": 5 }
      
    ],
      "lengthChange": false
  });  
  $('#globalsearchengineertable_filter').hide(); 
  $('#searchquery').on('keyup', function() { 
    // $('#globalsearchmodal').modal('show')
    window.scrollTo({  
      top: 0,   
      behavior: 'smooth'   
  });
      var searchValue = this.value;
      // if (searchValue.length > 0) {  
          document.getElementById("globalengtablediv").style.display = "block"; 
          document.getElementById('globalengtablediv').scrollIntoView({ behavior: 'smooth' }); 
      // } else {  
      //     document.getElementById("globalengtablediv").style.display = "none";
      // }  
      // document.getElementById("")
      $('#homedatefilter').click(function(event) {
        const input1 = document.getElementById("stdate").value;  
        const input2 = document.getElementById("endate").value;
        console.log("homedatefilter clicked"+input1+" "+input2);
          var fullApiUrl = apiBaseUrl + 'homedatefilter/';
          var homedatefilter=[];
          // var globalengtable = $('#globalsearchengineertable').DataTable();
          $.ajax({
              url: fullApiUrl,
              
              data: {
                  'startdate': input1,
                  'enddate': input2
              },
              success: function(response) {
                  if (response.success) {
                    homedatefilter = response.data;
                    homedatefiltertable(homedatefilter,globalengtable);
      
    //   $('#searchquery').on('keyup', function() {
    //     document.getElementById("globalengtablediv").style.display = "block"; 
    //     globalengtable.search(this.value).draw();
    // });
                    // $('#homedatefilt').html(data); // Update table body with new data  
                  } else {
                      alert('Error: ' + response.error);
                  }
              }
          });
      });
      $('#clearhomedatefilter').click(function(event) {
        document.getElementById("stdate").value ="";  
        document.getElementById("endate").value="";
        const input1 = document.getElementById("stdate").value;  
        const input2 = document.getElementById("endate").value;
          var fullApiUrl = apiBaseUrl + 'homedatefilter/';
          var homedatefilter=[];
          $.ajax({
              url: fullApiUrl,
              
              data: {
                  'startdate': input1,
                  'enddate': input2
              },
              success: function(response) {
                  if (response.success) {
                    homedatefilter = response.data;
                    homedatefiltertable(homedatefilter,globalengtable);
      
                  } else {
                      alert('Error: ' + response.error);
                  }
              }
          });
      });
      
      globalengtable.search(this.value).draw();  
  });  
  
});
function clearsearch() {
  document.getElementById('searchquery').value = '';
  document.getElementById("globalengtablediv").style.display = "none";
}

$(document).ready(function() {
  $('.impdocdelete').click(function(event) {
    console.log("impdocdelete clicked");
      event.preventDefault();
      var button = $(this);
      var url = button.data('url');
      swal({  
        title: "Are you sure?",  
        text: "You will not be able to recall this record!",  
        icon: "warning",  
        buttons: true,  
        dangerMode: true,  
    }).then((willDelete) => {  
        if (willDelete) {  
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
                swal({  
            
                  text: response.message,  
                  
                  button: "Okay",  
              });
                // alert('Error: ' + response.message);
              }
          }
      });
    } else {  
      // Optionally do something when cancelled  
      swal("Record is safe!");  
  }  
});  
  });
});

$(document).ready(function() {
  $('.edit-btn').on('click', function() {
      var $row = $(this).closest('tr');
      let i=0;
      $row.find('td').each(function() {
        i=i+1 ;
          var $cell = $(this);
          if ($cell.hasClass('docnarration') || $cell.hasClass('doclink')) {
            if ($cell.hasClass('docnarration')){
              document.getElementById("editnarration").value=$cell.text();  
            }else{
              document.getElementById("editlink").value=$cell.text();
            }
            
              var content = $cell.text();
              var cellClass = $cell.attr('class');
              var cellid = $cell.attr('id');
              if(cellid=='doctype'){
                $cell.html('<select class="' + cellClass + '" id="select-' + i + '" onchange="syncText(this)">' +
                  '<option value="text" >Text</option>' +
                  '<option value="number" >Number</option>' +
                  '<option value="date" >Date</option>' +
                  '<option value="email" >Email</option>' +
                  '</select>');
              }
              else{
              $cell.html('<input type="text" value="' + content + '" onkeyup="syncText(this)" class="' + cellClass + '" id="input-' + i + '">');
            }
                  
              console.log(cellid);
          }
      });
      
      // $(this).removeClass('edit-btn').addClass('save-btn');
      // $(this).addClass('save-btn');
      $(this).hide();
      $row.find('.save-btn').show();
      $row.find('.cancel-btn').show();
  });


});
function syncText(cell) {  
  console.log(cell.id);
  // var text = cell.text();
if(cell.id =='input-2') {
  document.getElementById("editnarration").value = cell.value; 
} else {
  document.getElementById("editlink").value = cell.value;  
}
console.log(cell.value);
}  

function updateimpdoc(recid){ 
   
  const input1 = document.getElementById("editnarration").value;  
  const input2 = document.getElementById("editlink").value;  
  
  apiBaseUrl = apiBaseUrl.replace('/api/', '/');
  var fullApiUrl = apiBaseUrl + 'propval/impdocupdate/'+recid;
  const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
  fetch(fullApiUrl, {  
      method: 'PUT',  
      headers: {  
          'Content-Type': 'application/json',  
          'X-CSRFToken': csrfToken  
      },  
      body: JSON.stringify({ narration: input1, linkurl: input2 })  
  })  
  .then(response => response.json())
      
  // .then(data => console.log(data.message))  
  .then(data =>(data.success
     ?  swal({  
      title: "Confirmation", 
      text: data.message ,  
      icon: "success",  
      button: "Okay",  
  }).then((willReload) => {  
    if (willReload) {  
        location.reload();  // This will reload the current page 
        // window.location.href = apiBaseUrl+'impdoc';  
           
    }  
})
      : alert(data.message)
  )

)  
  .catch((error) => console.error('Error:', error));  
  
}  
function engdynamicfieldupdate(recid){ 
  
  const input1 = document.getElementById("editnarration").value;  
  const input2 = document.getElementById("editlink").value; 
  console.log(input1);  
  apiBaseUrl = apiBaseUrl.replace('/api/', '/');
  var fullApiUrl = apiBaseUrl + 'propval/engdynamicfieldupdate/'+recid;
  const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
  fetch(fullApiUrl, {  
      method: 'PUT',  
      headers: {  
          'Content-Type': 'application/json',  
          'X-CSRFToken': csrfToken  
      },  
      body: JSON.stringify({ label: input1, input_type: input2 })  
  })  
  .then(response => response.json())
      
  // .then(data => console.log(data.message))  
  .then(data =>(data.success
     ?  swal({  
      title: "Confirmation", 
      text: data.message ,  
      icon: "success",  
      button: "Okay",  
  }).then((willReload) => {  
    if (willReload) {  
        location.reload();  // This will reload the current page 
        // window.location.href = apiBaseUrl+'impdoc';  
           
    }  
})
      : alert(data.message)
  )

)  
  .catch((error) => console.error('Error:', error));  
  
}  

$(document).ready(function() {
  // document.getElementById("globalengtablediv").style.display = "block"; 
//   $('#homedatefilter').click(function(event) {
//     const input1 = document.getElementById("stdate").value;  
//     const input2 = document.getElementById("endate").value;
//     console.log("homedatefilter clicked"+input1+" "+input2);
//       var fullApiUrl = apiBaseUrl + 'homedatefilter/';
//       var homedatefilter=[];
//       var globalengtable = $('#globalsearchengineertable').DataTable();
//       $.ajax({
//           url: fullApiUrl,
          
//           data: {
//               'startdate': input1,
//               'enddate': input2
//           },
//           success: function(response) {
//               if (response.success) {
//                 homedatefilter = response.data;
//                 homedatefiltertable(homedatefilter,globalengtable);
  
//   $('#searchquery').on('keyup', function() {
//     document.getElementById("globalengtablediv").style.display = "block"; 
//     globalengtable.search(this.value).draw();
// });
//                 // $('#homedatefilt').html(data); // Update table body with new data  
//               } else {
//                   alert('Error: ' + response.error);
//               }
//           }
//       });
//   });
});
function homedatefiltertable(data,gltable) {
gltable.clear().draw(); // Clear existing data 
var table =  document.getElementById('homedatefilt');
console.log(table);
var row=`<tr></tr>`
table.innerHTML = row
for (var i=0; i<data.length; i++) { console.log(data[i].id);
  var engineerStatus;  
if (data[i].engineer === "Submitted") {  
    engineerStatus = "Completed";  
} else if (data[i].engineer === null) {  
    engineerStatus = "Pending";  
} else {  
    engineerStatus = data[i].engineer;  
}
var archive = data[i].archive? 'Yes' : 'No';
//   var row = `<tr>
//   <td scope="row">${i+1}</td>
//   <td>${moment((data[i].applicationdate).split('T')[0]).format('DD-MM-YYYY')}</td>
//   <td scope="col">${data[i].applicationnumber}</td>
//   <td scope="col">${data[i].name}</td>
//   <td scope="col">${data[i].bankname}</td>
//   <td scope="col">${data[i].bankvertical}</td>
//   <td scope="col">${data[i].phonenumber}</td>
//   <td scope="col">${data[i].visitingpersonname}</td>
//   <td >${engineerStatus}</td>
//   <td >${archive}</td>
//  <td scope="col">${data[i].reporterholdcause}</td>
//   </tr>`
//   table.innerHTML += row
gltable.row.add([
  i + 1,
  moment((data[i].applicationdate).split('T')[0]).format('DD-MM-YYYY'),
  data[i].applicationnumber,
  data[i].name,
  data[i].bankname,
  data[i].bankvertical,
  data[i].phonenumber,
  data[i].visitingpersonname,
  engineerStatus,
  archive,
  data[i].reporterholdcause
]).draw(false);
  }
  
}

