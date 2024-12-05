import { createClient, print } from 'redis';
import { promisify } from 'util';

const client = createClient();
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err.message}`);
});

/**
 * ====================
 *
 * @param {string} schoolName - ==========
 *
 * @param {string} value - =============
 */

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, print);
}
const getAsync = promisify(client.get).bind(client);

/**
 * Using async/await
 *
 * @param {string} schoolName -======
 */

async function displaySchoolValue(schoolName) {
  try {
    const result = await getAsync(schoolName);
    console.log(result);
  } catch (error) {
    console.error(error);
  }
}


displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
