import { Component, Input, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Imagenes } from 'src/app/modelos/imagenes';
import { PrediccionService } from 'src/app/servicios/prediccion.service';

@Component({
  selector: 'app-prediccion',
  templateUrl: './prediccion.component.html',
  styleUrls: ['./prediccion.component.css']
})
export class PrediccionComponent implements OnInit {
  form:FormGroup;
  imagenesarray:Imagenes[] =[];
  imageToShow: any;

  createImageFromBlob(image: Blob) {
   let reader = new FileReader();
   reader.addEventListener("load", () => {
    this.imageToShow = reader.result;
  }, false);
  if (image) {
    reader.readAsDataURL(image);
   }
}
getimage(){
  try{
    const nombre = this.form.value.nombre;
    console.log(nombre);
    this.PrediccionService.getimage(nombre)
    .subscribe(data => {
      this.createImageFromBlob(data);
      //this.isImageLoading = false;
    }, error => {
      //this.isImageLoading = false;
      console.log(error);
    });      
  }
  catch{
  }
}

  

  constructor(private PrediccionService:PrediccionService,private fb:FormBuilder) { 
    this.form = this.fb.group({
      nombre:['',Validators.required]
    })
    //this.nombrearchivo = this.nombre.toString();
  }

  ngOnInit(): void {
    this.PrediccionService.getImagenNeuralNet()
    .subscribe(data=>{
      console.log(data);
      this.imagenesarray = data.data;
      //this.imagenesarray.values();
    },
    error =>console.log(error))
    
  }

  

  deleteimage(){

  }
  downloadimage(){
    try{
      const nombre = this.form.value.nombre;
      console.log(nombre);
      this.PrediccionService.downloadimage(nombre)
    .subscribe(data => {
      this.createImageFromBlob(data);
      //this.isImageLoading = false;
    }, error => {
      //this.isImageLoading = false;
      console.log(error);
    });    
    }
    catch{
    }

  }
  


}
