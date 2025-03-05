import { Injectable } from '@angular/core';
import { rockets } from '../axios-config';
import { Rocket } from '../models/rockets';

@Injectable({
  providedIn: 'root'
})
export class SpacexService {
  constructor() { }

  async getRockets(): Promise<Rocket[]> {
    return await rockets.get('/rockets');
  }

}

