const chai = require('chai');
const expect = chai.expect;
const calculateNumber = require('./2-calcul_chai');

describe('calculateNumber type == SUM', () => {
    it('checks output for SUM', () => {
        expect(calculateNumber('SUM', 1.4, 4.5)).to.equal(6);
        expect(calculateNumber('SUM', 1, 3)).to.equal(4);
    });
});

describe('calculateNumber type == SUBTRACT', () => {
    it('checks output of SUBTRACT', () => {
        expect(calculateNumber('SUBTRACT', 4, 3)).to.equal(1);
        expect(calculateNumber('SUBTRACT', 2, 4.5)).to.equal(-3);
    });
});

describe('calculateNumber type == DIVIDE', () => {
    it('checks output for DIVIDE', () => {
        expect(calculateNumber('DIVIDE', 10.0, 2)).to.equal(5);
        expect(calculateNumber('DIVIDE', 10.3, 2)).to.equal(5);
        expect(calculateNumber('DIVIDE', 10.7, 2)).to.equal(5.5);
        expect(calculateNumber('DIVIDE', 10, 1.0)).to.equal(10);
        expect(calculateNumber('DIVIDE', 10, 1.3)).to.equal(10);
        expect(calculateNumber('DIVIDE', 10, 1.7)).to.equal(5);
        expect(calculateNumber('DIVIDE', 10.3, 2)).to.equal(5);
        expect(calculateNumber('DIVIDE', 10, 1.2)).to.equal(10);
        expect(calculateNumber('DIVIDE', 10.3, 1.3)).to.equal(10);
        expect(calculateNumber('DIVIDE', 10.7, 1.2)).to.equal(11);
        expect(calculateNumber('DIVIDE', 10.3, 1.8)).to.equal(5);
        expect(calculateNumber('DIVIDE', 10.6, 1.8)).to.equal(5.5);
        expect(calculateNumber('DIVIDE', 1, 0)).to.equal('Error');
    });
});