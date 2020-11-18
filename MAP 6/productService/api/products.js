const express = require('express');
const router = express.Router();

router.get('/', (req, res, next) => {
    res.send({
        message: 'Handling GET requests to /products',
        method: 'GET'
    },200);
   
});

router.post('/', (req, res, next) => {
    res.send({
        message: 'Handling POST requests to /products',
        method: 'POST'
    },201);
});

router.get('/:productId', (req, res, next) => {
    const id = req.params.productId;
    if (id === 'special') {
        res.send({
            message: 'You discovered the special ID',
            id: id,
            method:'GET'
        },200);
    } else {
        res.send({
            message: 'You passed an ID',
            method: 'GET'
        },200);
    }
});

router.patch('/:productId', (req, res, next) => {
    res.send({
        message: 'Updated product!',
        method: 'PATCH'
    },200);
});

router.delete('/:productId', (req, res, next) => {
    res.send({
        message: 'Deleted product!',
        method: 'DELETE'
    },200);
});

module.exports = router;