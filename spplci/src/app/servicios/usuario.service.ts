import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class UsuarioService {

  private BASE_URL ='http://localhost:5000/usuarios'

  constructor(private http:HttpClient) { 


  }

  getUsuarios():Observable<any>{
    return this.http.get(`${this.BASE_URL}/listar-usuarios`)
  }
}

