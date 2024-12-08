import http from 'k6/http';
import { check } from 'k6';

export let options = {
  stages: [
    { duration: '30s', target: 50 }, // Ramp-up to 50 users in 30 seconds
    { duration: '1m', target: 50 },  // Hold at 50 users for 1 minute
    { duration: '30s', target: 0 },  // Ramp-down to 0 users in 30 seconds
  ],
};

export default function () {
  let res = http.get('http://<minikube-ip>:<node-port>');
  check(res, {
    'status was 200': (r) => r.status === 200,
    'response time < 200ms': (r) => r.timings.duration < 200,
  });
}
