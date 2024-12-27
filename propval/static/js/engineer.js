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
                        // console.log("red "+response.msg)
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
    // console.log(url);
    
    const id = url.split('/').pop();
    const parts = url.split('/');
    const status = parts[parts.length - 2];
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value; // Get CSRF token  
    // console.log(id);
    // console.log(status);
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

//   $(document).ready(function() { console.log("abcd");
//     $('.reportassign').click(function(event) {  console.log("abcd clicked");
//         event.preventDefault();
//         var button = $(this);
//         var url = button.data('url');
//         //console.log(button.text());
//         console.log(url);
//         $.ajax({
//             url: url,
//             type: 'GET',
//             data: {
//                 csrfmiddlewaretoken: '{{ csrf_token }}'
//             },
//             success: function(response) {
//                 if (response.success) {
//                     // button.closest('tr').remove();
//                     if(response.msg.trim()=="assigned"){
//                         button.html('<i class="fas fa-tasks fa-2x" style="color: green;"></i>' );
//                     }else{
//                         button.html('<i class="fas fa-tasks fa-2x" style="color: gray;"></i>');
//                       }
//                       alert('Success: ' + response.message);
//                     //   $('#totreq').text(response.tot);
//                     //   $('#pending').text(response.pend);
//                     //   $('#inprogress').text(response.inprog);
//                     //   $('#hold').text(response.hold);
//                     //   $('#compreq').text(response.com);
//                   } else {
//                     alert('Error: ' + response.error);
//                 }
//             }
//         });
//     });
// });

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



//   document.getElementById("engeditedbutton").onclick = function(event) { 
$(document).on('click', '.engeditedbutton', function(event) {  
// $(document).ready(function() {

// $('.engeditedbutton').click(function(event) { 
    // $('#engeditpop').modal('show') 
    event.preventDefault();
            var button = $(this);
            var url = button.data('url');
            console.log(url);
    // var fullApiUrl = apiBaseUrl + 'engineereditedview/';
    // console.log("fullApiUrl");
    fetch(url)  
        .then(response => response.json())  
        .then(data => {  
            let tableBody = document.querySelector('#engeditdataTable tbody');  
            tableBody.innerHTML = ''; // Clear existing data 
            let i=1;  
            console.log(data.data[0].dynamicfields);
            // console.log(data.data);
            const headerRow = document.querySelector('#editheader tr'); 
            const dynamicHeaders = headerRow.querySelectorAll('.dynamic-header');  
            dynamicHeaders.forEach(header => {  
                headerRow.removeChild(header);  
            }); 
            // var Header17th = headerRow.children[17]; 
            data.data[0].dynamicfields.forEach(field =>{ 
            const newTh = document.createElement('th');
            newTh.textContent = field.input_field__label;  
            newTh.classList.add('dynamic-header');
            headerRow.appendChild(newTh);  
        })
            data.data.forEach(item => { 
                let floorCellStyle = '';
                td = "";   
                j=0;
                // console.log(item.floors[0].floorname);          
                for (const fl of data.data[i-1].floors) {   
                    if(fl.floorname || fl.floordetail || fl.floorarea){   
                        td += fl.floorname + '/' + fl.floordetail + '/' + fl.floorarea + '<br><hr>'; 
                     } 
                    if(item.floors[i] && i>1){
                        if(data.data[0].floors[j]){
                            if ((fl.floorname != data.data[0].floors[j].floorname) ||(fl.floordetail != data.data[0].floors[j].floordetail)||(fl.floorarea != data.data[0].floors[j].floorarea)) {
                                floorCellStyle =  'style="background-color: yellow;"'; 
                            } 
                        }  else{
                            floorCellStyle = 'style="background-color: yellow;"';
                        }
                }  
                
                j++;      
                }
                if(data.data[i-1].floors.length!=data.data[0].floors.length && i>1){
                    floorCellStyle = 'style="background-color: yellow;"';
                }
                // print(tdd)
                let nameCellStyle = '';  

                if (item.name != data.data[0].name) {
                    nameCellStyle = 'style="background-color: yellow;"'; 
                }  
                let presenceCellStyle = '';  
                if (item.visitinpresence != data.data[0].visitinpresence) {
                    presenceCellStyle = 'style="background-color: yellow;"'; 
                }  
                let caseCellStyle = '';  
                if (item.casetype != data.data[0].casetype) {
                    caseCellStyle = 'style="background-color: yellow;"'; 
                } 
                let add1CellStyle = '';  
                if (item.add1 != data.data[0].add1 || item.add2 != data.data[0].add2 || item.city != data.data[0].city || item.region != data.data[0].region || item.country != data.data[0].country || item.zip != data.data[0].zip) {
                    add1CellStyle = 'style="background-color: yellow;"'; 
                } 
                // let add2CellStyle = '';  
                // if (item.add2 != data.data[0].add2) {
                //     add2CellStyle = 'style="background-color: yellow;"'; 
                // } 
                // let cityCellStyle = '';  
                // if (item.city != data.data[0].city) {
                //     cityCellStyle = 'style="background-color: yellow;"'; 
                // } 
                // let regionCellStyle = '';  
                // if (item.region != data.data[0].region) {
                //     regionCellStyle = 'style="background-color: yellow;"'; 
                // } 
                // let zipCellStyle = '';  
                // if (item.zip != data.data[0].zip) {
                //     zipCellStyle = 'style="background-color: yellow;"'; 
                // } 
                // let countryCellStyle = '';  
                // if (item.country != data.data[0].country) {
                //     countryCellStyle = 'style="background-color: yellow;"'; 
                // } 
                let eastCellStyle = '';  
                if (item.east != data.data[0].east) {
                    eastCellStyle = 'style="background-color: yellow;"'; 
                } 
                let westCellStyle = '';  
                if (item.west != data.data[0].west) {
                    westCellStyle = 'style="background-color: yellow;"'; 
                } 
                let northCellStyle = '';  
                if (item.north != data.data[0].north) {
                    northCellStyle = 'style="background-color: yellow;"'; 
                } 
                let southCellStyle = '';  
                if (item.south != data.data[0].south) {
                    southCellStyle = 'style="background-color: yellow;"'; 
                } 
                // let floorCellStyle = '';  
                // if (item.propertyage != data.data[0].propertyage) {
                //     // floorCellStyle = 'id ="floor" style="width:200px;"'; 
                //     floorCellStyle = 'style="background-color: yellow;"'; 
                // } 
                let propageCellStyle = '';  
                if (item.propertyage != data.data[0].propertyage) {
                    propageCellStyle = 'style="background-color: yellow;"'; 
                } 
                let landrateCellStyle = '';  
                if (item.landrate != data.data[0].landrate) {
                    landrateCellStyle = 'style="background-color: yellow;"'; 
                } 
                let occupantCellStyle = '';  
                if (item.Occupant != data.data[0].Occupant) {
                    occupantCellStyle = 'style="background-color: yellow;"'; 
                } 
                let rentedCellStyle = '';  
                if (item.rented != data.data[0].rented) {
                    rentedCellStyle = 'style="background-color: yellow;"'; 
                } 
                let landmarkCellStyle = '';  
                if (item.landmark != data.data[0].landmark) {
                    landmarkCellStyle = 'style="background-color: yellow;"'; 
                } 
                let roadwidthCellStyle = '';  
                if (item.roadwidth != data.data[0].roadwidth) {
                    roadwidthCellStyle = 'style="background-color: yellow;"'; 
                } 
                let hightensionCellStyle = '';  
                if (item.hightensionline != data.data[0].hightensionline) {
                    hightensionCellStyle = 'style="background-color: yellow;"'; 
                } 
                let railwayCellStyle = '';  
                if (item.railwayline != data.data[0].railwayline) {
                    railwayCellStyle = 'style="background-color: yellow;"'; 
                } 
                let nalaCellStyle = '';  
                if (item.nala != data.data[0].nala) {
                    nalaCellStyle = 'style="background-color: yellow;"'; 
                } 
                let riverCellStyle = '';  
                if (item.river != data.data[0].river) {
                    riverCellStyle = 'style="background-color: yellow;"'; 
                } 
                let pahadCellStyle = '';  
                if (item.pahad != data.data[0].pahad) {
                    pahadCellStyle = 'style="background-color: yellow;"'; 
                } 
                let roadbindingCellStyle = '';  
                if (item.roadcomesunderroadbinding != data.data[0].roadcomesunderroadbinding) {
                    roadbindingCellStyle = 'style="background-color: yellow;"'; 
                } 
                let accessissueCellStyle = '';  
                if (item.propertyaccessissue != data.data[0].propertyaccessissue) {
                    accessissueCellStyle = 'style="background-color: yellow;"'; 
                } 
                let othercheckCellStyle = '';  
                if (item.othercheck != data.data[0].othercheck) {
                    othercheckCellStyle = 'style="background-color: yellow;"'; 
                } 
                let othersCellStyle = '';  
                if (item.others != data.data[0].others) {
                    othersCellStyle = 'style="background-color: yellow;"'; 
                } 
                let remarkCellStyle = '';  
                if (item.remark != data.data[0].remark) {
                    remarkCellStyle = 'style="background-color: yellow;"'; 
                } 
                console.log(data.data[0].dynamicfields.length)
                
                let dyncellStyle = ''; 
                let dyntd="";
                let k=0;
                item.dynamicfields.forEach(dynval=>{
                    if (i==1){
                    dyntd+=`<td >${dynval.value}</td>`;
                    }else{
                        if(dynval.value!=data.data[0].dynamicfields[k].value)
                        dyncellStyle = 'style="background-color: yellow;"';
                        dyntd+=`<td ${dyncellStyle}>${dynval.value}</td>`;
                        k++;
                    }
                });
                // let td1=`<td >${item.applicationnumber}</td>`;
                // console.log(dyntd, item.applicationnumber) 
                let spc="  ";    
                let row = `<tr>  
                    <td>${i}</td>  
                    <td >${item.applicationnumber}</td> 
                    <td ${nameCellStyle}>${item.name}</td>  
                    <td ${presenceCellStyle}>${item.visitinpresence}</td>  
                    <td >${item.bankname}</td>  
                    <td ${caseCellStyle}>${item.casetype}</td>  
                    <td ${add1CellStyle} >${item.add1}${spc}${item.add2}${spc}${item.city}${spc}${item.region}${spc}${item.country}${spc}${item.zip}</td>  
                    <td ${eastCellStyle}>${item.east}</td>  
                    <td ${westCellStyle}>${item.west}</td>  
                    <td ${northCellStyle}>${item.north}</td>  
                    <td ${southCellStyle}>${item.south}</td>  
                    <td ${floorCellStyle}>${td}</td>
                    <td ${propageCellStyle}>${item.propertyage}</td>  
                    <td ${landrateCellStyle}>${item.landrate}</td>  
                    <td ${occupantCellStyle}>${item.Occupant}</td>  
                    <td ${rentedCellStyle}>${item.rented}</td>  
                    <td ${landmarkCellStyle}>${item.landmark}</td>  
                    <td ${roadwidthCellStyle}>${item.roadwidth}</td> 
                    
                    <td ${hightensionCellStyle}>${item.hightensionline}</td>  
                    <td ${railwayCellStyle}>${item.railwayline}</td>  
                    <td ${nalaCellStyle}>${item.nala}</td>  
                    <td ${riverCellStyle}>${item.river}</td>  
                    <td ${pahadCellStyle}>${item.pahad}</td>  
                    <td ${roadbindingCellStyle}>${item.roadcomesunderroadbinding}</td>  
                    <td ${accessissueCellStyle}>${item.propertyaccessissue}</td>  
                    <td ${othercheckCellStyle}>${item.othercheck}</td>  
                    <td ${othersCellStyle}>${item.others}</td>  
                    <td ${remarkCellStyle}>${item.remark}</td>  
                    ${dyntd}
                   
                </tr>`;  
                tableBody.innerHTML += row;  
                // i=i+1;
                i++;
            });  
            $('#engeditpop').modal('show') 
            // document.getElementById("dataModal").style.display = "block"; // Show modal  
        });  
        // let floorCell = document.getElementById('floor');  
        // console.log(floorCell);
        // let floorCellStyle = 'background-color: red; width: 200px;';   
        // floorCell.setAttribute('style', floorCellStyle);  
// });  
});  

//   }



