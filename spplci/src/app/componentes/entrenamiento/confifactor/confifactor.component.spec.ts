import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ConfifactorComponent } from './confifactor.component';

describe('ConfifactorComponent', () => {
  let component: ConfifactorComponent;
  let fixture: ComponentFixture<ConfifactorComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ConfifactorComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ConfifactorComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
