const chai = require('chai');
const expect = chai.expect;
const calculateNumber = require('./2-calcul_chai');

describe('calculateNumber type == SUM', () => {
    it('checks output for SUM', () => {
        chai.expect(calculateNumber('SUM', 1.4, 4.5), 6);
        chai.expect(calculateNumber('SUM', 1, 3), 4);
    });
});

describe('calculateNumber type == SUBTRACT', () => {
    it('checks output of SUBTRACT', () => {
        chai.expect(calculateNumber('SUBTRACT', 4, 3), 1);
        chai.expect(calculateNumber('SUBTRACT', 2, 4.5), -3);
    });
});

describe('calculateNumber type == DIVIDE', () => {
    it('checks output for DIVIDE', () => {
        chai.expect(calculateNumber('DIVIDE', 0.0, 2), 0);
        chai.expect(calculateNumber('DIVIDE', -1, 1), -1);
        chai.expect(calculateNumber('DIVIDE', 1, 0), 'Error');
    });
});