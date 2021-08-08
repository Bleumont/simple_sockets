const socket = new WebSocket('ws://localhost:3000');

socket.addEventListener('open', (e) => {
  console.log('Connected');
});
socket.addEventListener('close', (e) => {
  console.log('Disconnected');
});
socket.addEventListener('message', (e) => {
  console.log(`Received: ${e.data}`);
});

const sendMsg = () => socket.send('KeyorSomething');
