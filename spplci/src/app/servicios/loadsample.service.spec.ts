import { TestBed } from '@angular/core/testing';

import { LoadsampleService } from './loadsample.service';

describe('LoadsampleService', () => {
  let service: LoadsampleService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(LoadsampleService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
