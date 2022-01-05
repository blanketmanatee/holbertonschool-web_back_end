'use strict';
const assert = require('assert');
const calculateNumber = require('./1-calcul');

describe('calculateNumber type == SUM', () => {
    it('checks output for SUM', () => {
        assert.strictEqual(calculateNumber('SUM', 1.4, 4.5), 6);
        assert.strictEqual(calculateNumber('SUM', 1, 3), 4);
    });
});

describe('calculateNumber type == SUBTRACT', () => {
    it('checks output of SUBTRACT', () => {
        assert.strictEqual(calculateNumber('SUBTRACT', 4, 3), 1);
        assert.strictEqual(calculateNumber('SUBTRACT', 2, 4.5), -3);
    });
});

describe('calculateNumber type == DIVIDE', () => {
    it('checks output for DIVIDE', () => {
        assert.strictEqual(calculateNumber('DIVIDE', 0.0, 2), 0);
        assert.strictEqual(calculateNumber('DIVIDE', -1, 1), -1);
        assert.equal(calculateNumber('DIVIDE', 10.3, 1.3), 10);
        assert.equal(calculateNumber('DIVIDE', 10.7, 1.2), 11);
        assert.strictEqual(calculateNumber('DIVIDE', 1, 0), 'Error');
    });
});