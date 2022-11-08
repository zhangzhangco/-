const express = require('express');
const app = express();
app.use(function(req,res){
   res.end('hello,node!');
});
app.listen(3000);
console.log('server running !');
