import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SpacexRocketsComponent } from './spacex-rockets.component';

describe('SpacexRocketsComponent', () => {
  let component: SpacexRocketsComponent;
  let fixture: ComponentFixture<SpacexRocketsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [SpacexRocketsComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(SpacexRocketsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
