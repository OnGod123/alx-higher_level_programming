const net = require('net');

// Create a TCP/IP socket
const client = new net.Socket();

// Connect to the server
const serverPort = 12345;
client.connect(serverPort, 'localhost', () => {
    console.log('Connected to the server');

    // Send data to the server
    client.write('Hello from the client!');
});

// Receive data from the server
client.on('data', (data) => {
    console.log('Received:', data.toString());
    
    // Close the connection after receiving the response
    client.destroy();
});

// Handle connection closure
client.on('close', () => {
    console.log('Connection closed');
});

