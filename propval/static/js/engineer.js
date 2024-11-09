$(document).ready(function() {
    
    $('.reporterstatusupdate').click(function(event) {
        event.preventDefault();
        var button = $(this);
        var url = button.data('url');
        const id = url.split('/').pop(); 
        // console.log('p'+id.trim());
        // const ii="p"+id.trim();
        // console.log(url);
        // var idd=document.getElementById(ii);
        // console.log(idd);
        var buttonId = button.attr('id');  
        // console.log("Button ID:", buttonId); 
        // var iddd=document.getElementById(buttonId);
        // console.log(iddd);
   
        // var element = document.querySelector('#p' + id.tostring());
        // console.log(element);
       // var buttonClass = button.attr('class');
        var currentColor = button.find('i').css('color') ;
          console.log(currentColor);              
        if(currentColor==='rgb(0, 128, 0)'){
            $(document).ready(function() {
                // function openmodal(url){
            // document.getElementById('reporterstatus').addEventListener('click', reporterhold);
            $('#holdcausepopup').modal('show')
            document.getElementById("urll").innerText =url;  
            $('#urlid').val(id);  
            // console.log(document.getElementById("urll").innerText)
        // }   
        // openmodal(url);
            });
           
        }else{
            $.ajax({
                url: url,
                type: 'GET',
                data: {
                    csrfmiddlewaretoken: '{{ csrf_token }}'
                },
                success: function(response) {
                    if (response.success) {
                        console.log("red "+response.msg)
                        // button.css('color', 'green');
                            if(response.msg.trim()=="InProgress"){
                                button.html('<i class="fa-solid fa-spinner fa-2x" style="color: green;"></i>' );
                                }else if (response.msg.trim()=="Hold"){
                                    button.html('<i class="fa-solid fa-circle-pause fa-2x" style="color: red;"></i>');
                                }
                                else{
                                button.html('<i class="fa-regular fa-clock fa-2x" style="color: blue;"></i>');
                                }
                                
                                // button.removeClass('engineerstatus1');
                                // button.addClass('engineerstatus');
                                $('#totreq').text(response.tot);
                                $('#pending').text(response.pend);
                                $('#inprogress').text(response.inprog);
                                $('#hold').text(response.hold);
                                $('#compreq').text(response.com);
    
                      } else {
                        alert('Error: ' + response.error);
                    }
                }
            });
        }
       
    });
    
});

// function reporterhold(element) {
async function reporterhold() {
    // console.log($('textarea#reporterholdcause').val());
    var cause = $('textarea#reporterholdcause').val().trim();
    // console.log(cause.length);
    
    if ( cause.length==0 ) {
        alert("Hold cause is required");
        $('textarea#reporterholdcause').val("");
        // return false;  // stop the form submission if the cause is not filled out.
    }else{
    var url = document.getElementById("urll").innerText
    console.log(url);
    
    const id = url.split('/').pop();
    const parts = url.split('/');
    const status = parts[parts.length - 2];
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value; // Get CSRF token  
    console.log(id);
    console.log(status);
    // debugger;
    $('#urlid').val(id);  
            $('#holdcausepopup').modal('hide')
            if (status == 'S') {
                var button = $('.engineerstatusupdate[data-url="' + url + '"]');
            }else{
            var button = $('.reporterstatusupdate[data-url="' + url + '"]');
        }
        const response = await fetch(url, {  
            method: 'PUT',  
            headers: {  
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken ,  
            },  
            body: JSON.stringify({ cause }),  
        });  

        const data = await response.json();  
        if (response.ok) {  
            if(response.msg.trim()=="InProgress"){
                button.html('<i class="fa-solid fa-spinner fa-2x" style="color: green;"></i>' );
                }else{
                button.html('<i class="fa-solid fa-circle-pause fa-2x" style="color: red;"></i>');
                
                } 
                $('#totreq').text(response.tot);
                $('#pending').text(response.pend);
                $('#inprogress').text(response.inprog);
                $('#hold').text(response.hold);
                $('#compreq').text(response.com);
            // alert("Item updated successfully!");  
        } else {  
            alert("Error: " + data.error);  
        }  
    
}
 


}

$(document).ready(function() {
    $('.engineerstatusupdate').click(function(event) {
        event.preventDefault();
        var button = $(this);
        var url = button.data('url');
        const id = url.split('/').pop(); 
        //console.log(button.text());
        var currentColor = button.find('i').css('color') ;
          console.log(currentColor);
        console.log(url);
        if(currentColor==='rgb(0, 128, 0)'){
            $(document).ready(function() {
            $('#holdcausepopup').modal('show')
            document.getElementById("urll").innerText =url;  
            $('#urlid').val(id);  
            });
        }else{    
        $.ajax({
            url: url,
            type: 'GET',
            data: {
                csrfmiddlewaretoken: '{{ csrf_token }}'
            },
            success: function(response) {
                if (response.success) {
                    // button.closest('tr').remove();
                    console.log(response)
                    if(response.msg.trim()=="InProgress"){
                        button.html('<i class="fa-solid fa-spinner fa-2x" style="color: green;"></i>' );
                    }else if (response.msg.trim()=="Hold"){
                        button.html('<i class="fa-solid fa-circle-pause fa-2x" style="color: red;"></i>');
                    }
                    else{
                        button.html('<i class="fa-regular fa-clock fa-2x" style="color: blue;"></i>');
                      }
                      $('#totreq').text(response.tot);
                      $('#pending').text(response.pend);
                      $('#inprogress').text(response.inprog);
                      $('#hold').text(response.hold);
                      $('#compreq').text(response.com);
                  } else {
                    alert('Error: ' + response.error);
                }
            }
        });
        }
    });
});

$(document).ready(function() {
  
    $('#engineertable').DataTable({
      //disable sorting on last column
      pageLength: 5,
      "columnDefs": [
        { "orderable": false, "targets": 7 }
        
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
  
    $('#engineertablecomp').DataTable({
      //disable sorting on last column
      pageLength: 5,
      "columnDefs": [
        { "orderable": false, "targets": 5 }
        
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
    $('.reportassign').click(function(event) {
        event.preventDefault();
        var button = $(this);
        var url = button.data('url');
        //console.log(button.text());
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
                        button.html('<i class="fas fa-tasks fa-2x" style="color: green;"></i>' );
                    }else{
                        button.html('<i class="fas fa-tasks fa-2x" style="color: gray;"></i>');
                      }
                      alert('Success: ' + response.message);
                    //   $('#totreq').text(response.tot);
                    //   $('#pending').text(response.pend);
                    //   $('#inprogress').text(response.inprog);
                    //   $('#hold').text(response.hold);
                    //   $('#compreq').text(response.com);
                  } else {
                    alert('Error: ' + response.error);
                }
            }
        });
    });
});

function updateLink() {  
    var select = document.getElementById("bankSelect");  
    var selectedValue = select.value; // Get the selected value  
    console.log(selectedValue);
    var link = document.getElementById("generateLink"); // Get the link element
   
    link.href = "/propval/generatebill/bills/" + selectedValue;
    // link1.href = "{% url 'bills' " + selectedValue + " %}";
    console.log(link);

  }
  function checkselect(event) {
    var select = document.getElementById("bankSelect");  
    var selectedValue = select.value; // Get the selected value  
    if(selectedValue==0) {
        event.preventDefault();
        // alert('Please select bank select'  );
        swal({  
              
            text: "Please select a bank to generate bill",  
            
            button: "Okay",  
        }); 
        // var link = document.getElementById("generateLink"); // Get the link element
        // link.href = "/propval/generatebill/";
        return false;
    }
  }

//   global search engineer and reporter
$(document).ready(function() {  
    
    var globalengtable = $('#globalsearchengineertable').DataTable({
        pageLength: 5,
        "columnDefs": [
          { "orderable": false, "targets": 5 }
          
        ],
        "lengthChange": false
    });  
    $('#globalsearchengineertable_filter').hide(); 
    $('#searchquery').on('keyup', function() { 
        
        
        var searchValue = this.value;
        if (searchValue.length > 0) {  
            // $('#myTable').show(); // Show the table 
            document.getElementById("globalengtablediv").style.display = "block";  
            // Delay scrolling to allow DOM changes  
                document.getElementById('globalengtablediv').scrollIntoView({ behavior: 'smooth' });
           } else {  
            // $('#myTable').hide(); // Hide the table  
            document.getElementById("globalengtablediv").style.display = "none";
        }  
        globalengtable.search(this.value).draw();  
    });  
    
});

function clearsearch() {
    document.getElementById('searchquery').value = '';
    document.getElementById("globalengtablediv").style.display = "none";
  }

