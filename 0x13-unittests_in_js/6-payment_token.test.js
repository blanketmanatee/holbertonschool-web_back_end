'use strict';
const chai = require('chai');
const getPaymentTokenFromAPI = require('./6-payment_token');

describe('getPaymentTokenFromAPI', () => {
    it('async tests', (done) => {
        getPaymentTokenFromAPI(true)
        .then((res) => {
            chai.expect(res).to.include({ data: 'Successful response from the API' });
            done();
        })
        .catch((error) => done(error));
    });
});