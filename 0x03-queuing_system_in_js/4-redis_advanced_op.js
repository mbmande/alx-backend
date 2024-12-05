import { createClient, print } from 'redis';
const client = createClient();
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err.message}`);
});

function createHash() {
  const schools = {
    Portland: 50,
    Seattle: 80,
    'New York': 20,
    Bogota: 20,
    Cali: 40,
    Paris: 2,
  };

  for (const [city, value] of Object.entries(schools)) {
    client.hset('HolbertonSchools', city, value, print);
  }
}

function displayHash() {
  client.hgetall('HolbertonSchools', (err, object) => {
    if (err) {
      console.error(err);
    } else {
      console.log(object);
    }
  });
}


createHash();
displayHash();
