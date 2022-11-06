import { TestBed } from '@angular/core/testing';

import { RequerimientService } from './requerimient.service';

describe('RequerimientService', () => {
  let service: RequerimientService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(RequerimientService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
