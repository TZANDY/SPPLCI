import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class RequerimientService {
  private BASE_URL ='http://localhost:5000/requerimiento'

  constructor(private http:HttpClient) { }

  postRequeriment(data:any):Observable<any>{
    return this.http.post(`${this.BASE_URL}/crear-requerimiento2`,data);
  }
  
  getRequeriment():Observable<any>{
    return this.http.get(`${this.BASE_URL}/listar-requerimiento`);
  }

  deleteRequeriment(_id:any):Observable<any>{
    return this.http.delete(`${this.BASE_URL}/delete/${_id}`)
  }

  updateRequeriment(data:any,_id:any):Observable<any>{
    return this.http.put(`${this.BASE_URL}/update/${_id}`,data)

  }


}
