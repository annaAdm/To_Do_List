document.addEventListener('DOMContentLoaded', function() {
    // Get all checkboxes with the class 'single_todo_checkbox'
    var checkboxes = document.querySelectorAll('.single_todo_checkbox');

    // Iterate over each checkbox and add a click event listener
    checkboxes.forEach(function(checkbox) {
        checkbox.addEventListener('click', function() {
                // Make a request to your server
                // Replace 'your_server_endpoint' with the actual endpoint you want to send the request to
                fetch("/update" ,  {
                    method: 'POST', // Send a POST request
                    body: JSON.stringify({ id: this.id }), // Send the checkbox id to the server
                    headers: {
                        'Content-Type': 'application/json'
                    }
                })
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Network response was not ok');
                    }
                    //refresh the page
                    location.reload();
                })
                .catch(error => {
                    // Handle errors
                    console.error('There was a problem with the fetch operation:', error);
                });
        });
    });
});
