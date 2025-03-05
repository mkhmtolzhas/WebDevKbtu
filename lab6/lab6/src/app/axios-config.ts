import axios from 'axios';

const rockets = axios.create({
  baseURL: 'https://api.spacexdata.com/v3',
});


export { rockets };