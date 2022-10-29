import { TestBed } from '@angular/core/testing';

import { EntrenamodeloService } from './entrenamodelo.service';

describe('EntrenamodeloService', () => {
  let service: EntrenamodeloService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(EntrenamodeloService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
