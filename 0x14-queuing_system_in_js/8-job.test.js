import { expect } from 'chai';
import kue from 'kue';
import createPushNotificationsJobs from './8-job';

const queue = kue.createQueue();
const list = [
    {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account'
    }
];

before(() => queue.testMode.enter());
afterEach(() => queue.testMode.clear());
after(() => queue.testMode.exit());

it ('jobs', () => {
    createPushNotificationsJobs(list, queue);
    expect(queue.testMode.jobs.type).to.equal(Array);
});