'use strict';
import redis from 'redis';
const { promisify } = require("util");
const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);


client.on("error", (error) => {
    if (error) console.log(`Redis client not connected to the server: ${error}`)
}).on('ready', () => {
    console.log('Redis client connected to the server');
});

function setNewSchool(schoolName, value) {
    client.set(schoolName, value, redis.print);
}

async function displaySchoolValue(schoolName) {
    const foundValue = client.get(schoolName, redis.print);
    console.log(foundValue);
}

(async function main() {
await displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
await displaySchoolValue('HolbertonSanFrancisco');
}());
