import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SpacexLauncherComponent } from './spacex-launcher.component';

describe('SpacexLauncherComponent', () => {
  let component: SpacexLauncherComponent;
  let fixture: ComponentFixture<SpacexLauncherComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [SpacexLauncherComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(SpacexLauncherComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
