import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
    vus: 1,
    duration: '30s',
    thresholds: {
        'http_req_duration': ['p(95)<500']
    },
    insecureSkipTLSVerify: true  // Skip TLS certificate verification
};

const BASE_URL = 'https://192.168.49.2:32213';  // Changed to HTTPS

export default function() {
    const params = {
        insecureSkipTLSVerify: true  // Skip TLS certificate verification for requests
    };

    const response = http.get(`${BASE_URL}/health`, params);
    
    check(response, {
        'status is 200': (r) => r.status === 200,
    });

    sleep(1);
}