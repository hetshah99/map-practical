
const products = require('restana')({
    disableResponseEvent : true
});
const productRoutes = require('./api/products');


products.use('/',productRoutes);

products.start(4000).then( function(){
    console.log('Product service running 4000');
});

/**
 * get    - /
 * post   - /
 * get    - /{productid}
 * patch  - /{productid}
 * delete - /{productid}
 * 
 */
