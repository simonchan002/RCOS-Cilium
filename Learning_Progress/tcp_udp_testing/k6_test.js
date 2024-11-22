import http from 'k6/http';
import { check } from 'k6';

export default function () {
    // Test TCP Server through HTTP relay
    const tcpResponse = http.get('http://localhost:8080/test-tcp');
    check(tcpResponse, {
        'TCP response received': (res) => res.body.includes("Hello from TCP Server"),
    });

    // Test UDP Server through HTTP relay
    const udpResponse = http.get('http://localhost:8081/test-udp');
    check(udpResponse, {
        'UDP response received': (res) => res.body.includes("Hello from UDP Server"),
    });
}
