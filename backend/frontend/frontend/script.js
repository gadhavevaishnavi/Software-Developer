document.getElementById('registrationForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const registrationData = {
        name: document.getElementById('name').value,
        email: document.getElementById('email').value,
        date_of_birth: document.getElementById('dateOfBirth').value,
        phone_number: document.getElementById('phoneNumber').value,
        address: document.getElementById('address').value
    };

    fetch('/registrations', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(registrationData)
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
        alert('Registration successful!');
    })
    .catch((error) => {
        console.error('Error:', error);
        alert('Registration failed!');
    });
});
