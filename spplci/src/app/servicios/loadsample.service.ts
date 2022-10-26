import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class LoadsampleService {

  private BASE_URL ='http://localhost:5000'

  constructor(private http:HttpClient) { }

  sendPost(body:FormData):Observable<any>{
    return this.http.post(`${this.BASE_URL}/upload`,body)
  }
}
