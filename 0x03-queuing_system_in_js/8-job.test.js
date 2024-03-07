const kue = require('kue');
const createPushNotificationsJobs = require('./8-job');

describe('createPushNotificationsJobs', () => {
  let queue;

  before(() => {
    queue = kue.createQueue();
    kue.Job.rangeByType('push_notification_code_3', 'inactive', 0, -1, 'asc', (err, jobs) => {
      if (!err) {
        jobs.forEach(job => {
          job.remove();
        });
      }
    });
  });

  after(() => {
    kue.Job.rangeByType('push_notification_code_3', 'inactive', 0, -1, 'asc', (err, jobs) => {
      if (!err) {
        jobs.forEach(job => {
          job.remove();
        });
      }
    });
    queue.testMode.exit();
  });

  beforeEach(() => {
    queue.testMode.enter();
  });

  afterEach(() => {
    queue.testMode.clear();
  });

  it('should throw an error if jobs is not an array', () => {
    const invalidJobs = 'invalid';
    const queue = kue.createQueue();
    try {
      createPushNotificationsJobs(invalidJobs, queue);
    } catch (error) {
      chai.expect(error.message).to.equal('Jobs is not an array');
    }
  });

  it('should add jobs to the queue correctly', () => {
    const jobs = [
      {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account'
      },
      {
        phoneNumber: '4153518781',
        message: 'This is the code 4562 to verify your account'
      }
    ];

    createPushNotificationsJobs(jobs, queue);

    const jobIds = Object.keys(queue.testMode.jobs);
    chai.expect(jobIds).to.have.lengthOf(2);
  });
});
