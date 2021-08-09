const socket = new WebSocket('ws://localhost:3000');

const $data = document.getElementById('data');

const sendMsg = () => socket.send('hello');

socket.addEventListener('open', (e) => {
  console.log('Connected');
});
socket.addEventListener('close', (e) => {
  console.log('Disconnected');
});
socket.addEventListener('message', (e) => {
  console.log(`Received: ${e.data}`);
  // $data.appendChild(`<div>${e.data}</div>`);
});
