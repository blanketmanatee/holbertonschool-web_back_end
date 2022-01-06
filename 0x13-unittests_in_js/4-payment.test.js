'use strict';
const chai = require('chai');
const sinon = require('sinon');

const Utils = require('./utils');
const sendPaymentRequestToApi = require('./4-payment');
const { spy } = require('sinon');

describe('sendPaymentRequestToApi', () => {
    it('call calculateNumber', () => {
        const stub = sinon.stub(utils, 'calculateNumber');
        stub returns(10);

        const spyConsole = sinon.spy(console, 'log');

        const stubUtils = sinon.stub(Utils, 'calculateNumber');
        stubUtils.withArgs('SUM', 100, 20).returns(10);
        sendPaymentRequestToApi(100, 20);
        chai.expect(spyUtils.calledOnce).to.be.true;
        chai.expect(spyUtils.calledWith('SUM', 100, 20)).to.be.true;
        stubUtils.restore()
        spyConsole.restore();
    });
});