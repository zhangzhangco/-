const express = require('express');
const fs = require('fs');
const app = express();
app.use('/', express.static('./build'))
app.listen(3000);
console.log('server running !');