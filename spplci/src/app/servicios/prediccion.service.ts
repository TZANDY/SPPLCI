import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class PrediccionService {
  private BASE_URL ='http://localhost:5000/files/'

  private BASE_URL_IMG = 'http://localhost:5000/images'
  

  constructor(private http:HttpClient) { }

  getImagenNeuralNet():Observable<any>{
    return this.http.get(`${this.BASE_URL}/directorio-images`)
  }

  getimage(name_file:string):Observable<Blob>{
    return this.http.get(`${this.BASE_URL_IMG}/test.jpg`,{responseType: 'blob'})
  }

  getimage_indicador_val_accuracy():Observable<Blob>{
    return this.http.get(`${this.BASE_URL_IMG}/index_val_accuracy.jpg`,{responseType: 'blob'})
  }

  getimage_indicador_val_loss():Observable<Blob>{
    return this.http.get(`${this.BASE_URL_IMG}/index_val_loss.jpg`,{responseType: 'blob'})
  }

  getimage_indicador_loss():Observable<Blob>{
    return this.http.get(`${this.BASE_URL_IMG}/index_loss.jpg`,{responseType: 'blob'})
  }
  

  deleteimage(){

  }

  downloadimage(name_file:string):Observable<Blob>{
    return this.http.get(`${this.BASE_URL_IMG}/download/${name_file}`,{responseType: 'blob'})
  }
}
