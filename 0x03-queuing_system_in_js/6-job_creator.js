const kue = require('kue');
const queue = kue.createQueue();

const jobData = {
    phoneNumber: '1234567890',
    message: 'Hello, this is a notification message!',
};

const job = queue.create('push_notification_code', jobData).save((err) => {
    if (!err) {
	console.log(`Notification job created: ${job.id}`);
    } else {
	console.error(`Error creating notification job: ${err}`);
    }
});

job.on('complete', () => {
    console.log('Notification job completed');
});

job.on('failed', () => {
    console.log('Notification job failed');
});
