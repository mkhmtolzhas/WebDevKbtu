import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { SpacexLauncherComponent } from "./components/spacex-launcher/spacex-launcher.component";

@Component({
  selector: 'app-root',
  imports: [SpacexLauncherComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'lab6';
}
