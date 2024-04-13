const net = require('net');

function packetFilter(packet) {
    // Implement packet filtering logic here
    // For demonstration purposes, allow all packets
    return true;
}

// Create a TCP/IP socket
const server = net.createServer((connection) => {
    console.log('Connection established with', connection.remoteAddress);

    connection.on('data', (data) => {
        console.log('Received:', data.toString());

        // Packet filtering
        if (packetFilter(data)) {
            // Allow packet
            connection.write('Packet allowed by firewall');
        } else {
            // Block packet
            connection.write('Packet blocked by firewall');
        }

        // Close connection after sending response
        connection.end();
    });
});

// Start listening on port 12345
server.listen(12345, 'localhost', () => {
    console.log('Server listening on port 12345');
});

