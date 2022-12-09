import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class HistoricosService {

  private BASE_URL ='http://localhost:5000/files'

  constructor(private http:HttpClient) { }

  getHistoricoModelo():Observable<any>{
    return this.http.get(`${this.BASE_URL}/directorio-modelo`)
  }

  getHistoricoMuestra():Observable<any>{
    return this.http.get(`${this.BASE_URL}/directorio-muestra`)
  }

  getHistoricoGraficas():Observable<any>{
    return this.http.get(`${this.BASE_URL}/directorio-images`)
  }
}
