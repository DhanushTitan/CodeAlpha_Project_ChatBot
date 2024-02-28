function sendMessage() {
    const userInput = document.getElementById("user-input");
    const chatBox = document.getElementById("chat-box");

    const userMessage = userInput.value;
    if (userMessage.trim() === "") return;

    // Display user message in the chat box
    chatBox.innerHTML += `<div class="user-message">${userMessage}</div>`;

    // Send user message to the server for processing
    fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded",
        },
        body: `user_message=${encodeURIComponent(userMessage)}`,
    })
    .then(response => response.json())
    .then(data => {
        const botResponse = data.bot_response;
        // Display bot response in the chat box
        chatBox.innerHTML += `<div class="bot-message">${botResponse}</div>`;
    });

    // Clear the input field
    userInput.value = "";
}
