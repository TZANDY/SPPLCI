import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EntrenamientoComponent } from './entrenamiento.component';
import {NgbModal} from '@ng-bootstrap/ng-bootstrap';

describe('EntrenamientoComponent', () => {
  let component: EntrenamientoComponent;
  let fixture: ComponentFixture<EntrenamientoComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ EntrenamientoComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(EntrenamientoComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
