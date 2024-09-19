const sendButton = document.querySelector('.send-button');
const recipientForm = document.querySelector('.recipient-form');
const submitButton = document.querySelector('.submit-button');
const recipientName = document.querySelector('.recipient-name');
const recipientEmail = document.querySelector('.recipient-email');

sendButton.addEventListener('click', () => {
	recipientForm.style.display = 'block';
	sendButton.style.display = 'none';
});

submitButton.addEventListener('click', () => {
	const name = recipientName.value;
	const email = recipientEmail.value;
	const message = `Dear ${name},<br><br>H