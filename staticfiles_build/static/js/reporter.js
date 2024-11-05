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
    console.log("reception table");
  } );