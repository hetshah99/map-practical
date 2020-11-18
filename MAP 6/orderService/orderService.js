const orders = require('restana')({
    disableResponseEvent : true
});
const orderRoutes = require('./api/orders');


orders.use('/',orderRoutes);

orders.start(6000).then( function(){
    console.log('order service running 6000');
});

/**
 * get    - /
 * post   - /
 * get    - /{orderid}
 * delete - /{orderid}
 * 
 */

