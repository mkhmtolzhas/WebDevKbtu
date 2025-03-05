import { Component } from '@angular/core';
import { SpacexService } from '../../services/spacex.service';
import { SpacexRocketsComponent } from "../spacex-rockets/spacex-rockets.component";
import { NgFor } from '@angular/common';
import { Rocket } from '../../models/rockets';


@Component({
  selector: 'app-spacex-launcher',
  imports: [SpacexLauncherComponent, NgFor],
  templateUrl: './spacex-launcher.component.html',
  styleUrl: './spacex-launcher.component.css'
})
export class SpacexLauncherComponent {
  rockets: Rocket[] = [];

  constructor(
    private spacexService: SpacexService
  ) {}

  async ngOnInit() {
    await this.getRockets();
    console.log(this.rockets);
  }
  
  
  async getRockets() {
    this.rockets = await this.spacexService.getRockets();
  }
}
