'use strict';
const chai = require('chai');
const sinon = require('sinon');
const {spy, stub } = require('sinon');

const Utils = require('./utils');
const sendPaymentRequestToApi = require('./4-payment');

describe('sendPaymentRequestToApi function', () => {
    const spyUtils = sinon.spy(Utils, 'calculateNumber');

    it('validate usage of Utils', () => {
        sendPaymentRequestToApi(100, 20);
        chai.expect(spyUtils.calledOnce).to.be.true;
        chai.expect(spyUtils.calledWith('SUM', 100, 20)).to.be.true;
        spyUtils.restore()
    });
});