document.getElementById('contact-form').addEventListener('submit', function(event) {
    var nameInput = document.getElementById('name').value.trim();
    var emailInput = document.getElementById('email').value.trim();
    var messageInput = document.getElementById('message').value.trim();
    var emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/; // Simple email regex pattern

    if (nameInput === '') {
        alert('Please enter your name.');
        event.preventDefault();
    } else if (!emailPattern.test(emailInput)) {
        alert('Please enter a valid email address.');
        event.preventDefault();
    } else if (messageInput === '') {
        alert('Please enter your message.');
        event.preventDefault();
    }
});