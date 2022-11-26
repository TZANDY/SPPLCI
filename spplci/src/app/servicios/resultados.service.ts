import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';


@Injectable({
  providedIn: 'root'
})
export class ResultadosService {
  private BASE_URL ='http://localhost:5000'

  constructor(private http:HttpClient) { }

  getResultPredict():Observable<any>{
    return this.http.get(`${this.BASE_URL}/resultados`);
  }
}
