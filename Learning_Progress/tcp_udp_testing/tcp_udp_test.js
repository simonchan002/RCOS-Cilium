import { check } from 'k6';
import udp from 'k6/x/udp'; // k6 extension for UDP
import tcp from 'k6/x/tcp'; // k6 extension for TCP

export default function () {
    // TCP Test
    const tcpClient = new tcp.Client('tcp-echo-service-ip', 9000);
    tcpClient.connect();
    tcpClient.write("Hello, TCP Server!");
    const tcpResponse = tcpClient.read();
    check(tcpResponse, {
        'TCP response received': (res) => res.includes("Hello from TCP Server"),
    });
    tcpClient.close();

    // UDP Test
    const udpClient = new udp.Client('udp-echo-service-ip', 9001);
    udpClient.write("Hello, UDP Server!");
    const udpResponse = udpClient.read();
    check(udpResponse, {
        'UDP response received': (res) => res.includes("Hello from UDP Server"),
    });
}
