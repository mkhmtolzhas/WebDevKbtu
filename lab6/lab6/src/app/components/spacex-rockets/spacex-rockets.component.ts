import { Component, Input } from '@angular/core';
import { Rocket } from '../../models/rockets';

@Component({
  selector: 'app-spacex-rockets',
  imports: [],
  templateUrl: './spacex-rockets.component.html',
  styleUrl: './spacex-rockets.component.css'
})
export class SpacexRocketsComponent {
  @Input() rocket!: Rocket;

  constructor() {
    console.log(this.rocket);
  }
}
