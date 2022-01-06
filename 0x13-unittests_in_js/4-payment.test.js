'use strict';
const chai = require('chai');
const sinon = require('sinon');

const Utils = require('./utils');
const sendPaymentRequestToApi = require('./4-payment');
const { spy } = require('sinon');

describe('sendPaymentRequestToApi function', () => {
    const spyConsole = sinon.spy(console, 'log');

    it('validate usage of Utils', () => {
        const stubUtils = sinon.stub(Utils, 'calculateNumber');
        stubUtils.withArgs('SUM', 100, 20).returns(10);
        sendPaymentRequestToApi(100, 20);
        chai.expect(spyUtils.calledOnce).to.be.true;
        chai.expect(spyUtils.calledWith('SUM', 100, 20)).to.be.true;
        stubUtils.restore()
        spyConsole.restore();
    });
});