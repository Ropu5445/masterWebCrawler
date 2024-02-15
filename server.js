const config = require('./config');
const express = require('express');

const app = express();
const port = config.server.port;
const host = config.server.host;

app.use(express.static(__dirname + '/public'));

app.route('/')
    .get((req, res) => {
        res.sendFile(__dirname + '/public/index.html');
    })
    .all((req, res) => {
        res.sendStatus(405)
    })

// Start the server
app.listen(port, () => {
    console.log(`Server listening at http://${host}:${port}`);
});

app.once('error', function(err) {
    if (err.code === 'EADDRINUSE') {
        console.log(`Port ${port} already in use`);
        process.exit();
    }
});