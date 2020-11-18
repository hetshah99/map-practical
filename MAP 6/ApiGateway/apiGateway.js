

const gateway = require('fast-gateway');

const server = gateway({
    routes:[{

        prefix:'/products',
        target: 'http://localhost:4000'
    },{
        prefix:'/orders',
        target: 'http://127.0.1:6000'
    },{
        prefix:'/library',
        target: 'http://localhost:5000'
    },{
        prefix:'/movies',
        target: 'http://localhost:7000'
    }]
})
server.start(3000);
console.log("Server running port 3000");

