const express = require('express');
const fs = require('fs');
const app = express();
app.get('/',function(req,res){
    res.send(fs.readFileSync('I:\\WPSDrive\\259626762\\WPS网盘\\标准研究室\\mediastandards-registry-china\\build\\index.html','utf-8'));
})
app.use(function(req,res){
    res.send('hello world');
})
app.listen(3000);
console.log('server running !');