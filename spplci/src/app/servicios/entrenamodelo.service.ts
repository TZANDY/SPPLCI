import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class EntrenamodeloService {


  private BASE_URL ='http://localhost:5000/entrenamiento'


  constructor(private http:HttpClient) { }
  
  getEntrenamiento():Observable<any>{
    return this.http.get(`${this.BASE_URL}/nuevo-entrenamiento`)
  }
}
