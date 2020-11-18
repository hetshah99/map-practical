const express = require('express');
const router = express.Router();

// Handle incoming GET requests to /orders
router.get('/', (req, res, next) => {
    res.send({
        message: 'Orders were fetched',
        method: 'GET'
    },200);
});

router.post('/', (req, res, next) => {
    res.send({
        message: 'Order was created',
        method: 'POST'
    },201);
});

router.get('/:orderId', (req, res, next) => {
    res.send({
        message: 'Order details',
        orderId: req.params.orderId,
        method: 'GET'
    },200);
});

router.delete('/:orderId', (req, res, next) => {
    res.send({
        message: 'Order deleted',
        orderId: req.params.orderId,
        method:'DELETE'
    },200);
});

module.exports = router;