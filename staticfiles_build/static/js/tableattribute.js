$(document).ready(function() {
    $('#recpreptable').DataTable({
      paging: true, // Enable pagination
      searching: true, // Enable search
      ordering: true // Enable sorting
    });
  });

//   $(document).ready(function () {  
//     $('#profileform1').submit(function (e) {  
//         e.preventDefault(); // Prevent default form submission  

//         // Serialize the form data  
//         const formData = $(this).serializeArray();  
//         const data = {};  

//         // Convert the array to an object  
//         formData.forEach(function (item) {  
//             data[item.name] = item.value;  
//         });  
//         data['user']=28;

//         const profileId = $('#profileid').val(); /* retrieve the profile ID from elsewhere */;  
//         console.log(profileId);
//         $.ajax({  
//             url: `/api/profile/update/${profileId}/`,  
//             type: 'PUT',  
//             contentType: "application/json",  
//             data: JSON.stringify(data),  
//             headers: {  
//                 'X-CSRFToken': '{{ csrf_token }}' // Include CSRF token  
//             },  
//             success: function (response) {  
//                 console.log('Profile updated successfully:', response);  
//                 // Handle success - e.g., show a success message  
//             },  
//             error: function (xhr, status, error) {  
//                 console.error('Error updating profile:', error);  
//             }  
//         });  
//     });  
// });  

  