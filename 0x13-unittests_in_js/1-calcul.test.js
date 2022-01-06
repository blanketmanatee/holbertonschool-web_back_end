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

describe('calculateNumber', () => {
    describe('when type is DIVIDE', () => {
      it('it round the first argument', () => {
          assert.equal(calculateNumber('DIVIDE', 10.0, 2), 5);
          assert.equal(calculateNumber('DIVIDE', 10.3, 2), 5);
          assert.equal(calculateNumber('DIVIDE', 10.7, 2), 5.5);
      });
      
      it('it round the second argument', () => {
          assert.equal(calculateNumber('DIVIDE', 10, 1.0), 10);
          assert.equal(calculateNumber('DIVIDE', 10, 1.3), 10);
          assert.equal(calculateNumber('DIVIDE', 10, 1.7), 5);
      });
      
      it('it should return the right number', () => {
          assert.equal(calculateNumber('DIVIDE', 10.3, 2), 5);
          assert.equal(calculateNumber('DIVIDE', 10, 1.2), 10);
          assert.equal(calculateNumber('DIVIDE', 10.3, 1.3), 10);
          assert.equal(calculateNumber('DIVIDE', 10.7, 1.2), 11);
          assert.equal(calculateNumber('DIVIDE', 10.3, 1.8), 5);
          assert.equal(calculateNumber('DIVIDE', 10.6, 1.8), 5.5);
      });
  
      it('it should return Error if b is equal to 0', () => {
          assert.equal(calculateNumber('DIVIDE', 10.3, 0).toLowerCase(), 'error');
          assert.equal(calculateNumber('DIVIDE', 10.7, 0).toLowerCase(), 'error');
          assert.equal(calculateNumber('DIVIDE', 10.3, 0.3).toLowerCase(), 'error');
          assert.equal(calculateNumber('DIVIDE', 10.7, 0.2).toLowerCase(), 'error');
      });
    });
  });