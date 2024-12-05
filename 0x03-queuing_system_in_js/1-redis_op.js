import { createClient, print } from 'redis';

const client = createClient();
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err.message}`);
});

/**
 * 
 *
 * @param {string} school - =============
 * @param {string} value - ==============
 */

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, print); 
}

/**
 * =============
 *
 * @param {string} schoolName - key name
 */

function displaySchoolValue(schoolName) {
  client.get(schoolName, (err, reply) => {
    if (err) {
      console.error(err);
    } else {
      console.log(reply);
    }
  });
}



displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
