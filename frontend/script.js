function sendNotification() {
    const message = document.getElementById("message").value;

    fetch("https://TU-BACKEND-URL/send-notification", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ message: message })
    })
    .then(response => response.json())
    .then(data => alert("Notificación enviada: " + data.status));
}
