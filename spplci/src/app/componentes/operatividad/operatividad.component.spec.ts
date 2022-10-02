import { ComponentFixture, TestBed } from '@angular/core/testing';

import { OperatividadComponent } from './operatividad.component';

describe('OperatividadComponent', () => {
  let component: OperatividadComponent;
  let fixture: ComponentFixture<OperatividadComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ OperatividadComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(OperatividadComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
