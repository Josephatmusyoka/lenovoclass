document.addEventListener("DOMContentLoaded", function() {
    const videoContainer = document.getElementById("video-container");
    const participantList = document.getElementById("participant-list");
    const chatBox = document.getElementById("chat-box");

    // Function to send a chat message
    const sendMessageButton = document.getElementById("send-message");
    sendMessageButton.addEventListener("click", function() {
        const messageInput = document.getElementById("message-input");
        const messageText = messageInput.value.trim();
        if (messageText !== "") {
            const message = document.createElement("div");
            message.innerText = `You: ${messageText}`;
            chatBox.appendChild(message);
            messageInput.value = "";
        }
    });

    // Function to initiate screen sharing
    const shareScreenButton = document.getElementById("share-screen");
    shareScreenButton.addEventListener("click", function() {
        navigator.mediaDevices.getDisplayMedia({ video: true })
            .then(stream => {
                // Display the shared screen in the video container
                const sharedScreen = document.createElement("video");
                sharedScreen.srcObject = stream;
                sharedScreen.autoplay = true;
                videoContainer.appendChild(sharedScreen);
            })
            .catch(error => {
                console.error("Error sharing screen:", error);
            });
    });

    // Function to toggle camera
    const toggleCameraButton = document.getElementById("toggle-camera");
    toggleCameraButton.addEventListener("click", function() {
        console.log("Toggle Camera");
        // Add logic to toggle camera
    });

    // Function to toggle microphone
    const toggleMicrophoneButton = document.getElementById("toggle-microphone");
    toggleMicrophoneButton.addEventListener("click", function() {
        console.log("Toggle Microphone");
        // Add logic to toggle microphone
    });

    // Function to record session
    const recordSessionButton = document.getElementById("record-session");
    recordSessionButton.addEventListener("click", function() {
        console.log("Record Session");
        // Add logic to start/stop recording session
    });
});
