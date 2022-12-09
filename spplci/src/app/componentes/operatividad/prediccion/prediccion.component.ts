import { Component, OnInit,ViewChild } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Imagenes } from 'src/app/modelos/imagenes';
import { PrediccionService } from 'src/app/servicios/prediccion.service';
import { MatPaginator} from '@angular/material/paginator';
import { MatSort} from '@angular/material/sort';
import { MatTableDataSource} from '@angular/material/table';
import { ResultadosService } from 'src/app/servicios/resultados.service';
import { Prediccion } from '../../../modelos/prediccion';

@Component({
  selector: 'app-prediccion',
  templateUrl: './prediccion.component.html',
  styleUrls: ['./prediccion.component.css']
})
export class PrediccionComponent implements OnInit {
  form:FormGroup;
  imagenesarray:Imagenes[] =[];
  imageToShow: any;
  imageToShowIndex1:any;
  imageToShowIndex2:any;
  imageToShowIndex3:any;
  panelOpenState = false;

  ELEMENT_DATA:Prediccion[]=[];
  

  displayedColumns: string[] = ['ord', 'codigo','descripcion','valor', 'action'];
  dataSource!: MatTableDataSource<any>; 
  @ViewChild(MatPaginator) paginator!: MatPaginator;
  @ViewChild(MatSort) sort!: MatSort; 

  constructor(private PrediccionService:PrediccionService,private fb:FormBuilder,private ResultadosService:ResultadosService) { 
    this.form = this.fb.group({
      nombre:['',Validators.required]
    })
  }

  ngOnInit(): void { 
    try {
      this.listarResultadoPrediccion();
      this.getimage();
      this.getimage_Index_val_accuracy();
      this.getimage_Index_val_loss();
      this.getimage_Index_loss();
    } catch (error) {
      console.log(error);
      alert("Hubo un error en la muestra de resultados");
    }
  }

  createImageFromBlob(image: Blob) {
   let reader = new FileReader();
   reader.addEventListener("load", () =>{
    this.imageToShow = reader.result;
    
  }, false);
  if (image) {
    reader.readAsDataURL(image);
   }
  }

  createImageFromBlob1(image: Blob) {
    let reader = new FileReader();
    reader.addEventListener("load", () =>{
     this.imageToShowIndex1=reader.result;
   }, false);
   if (image) {
     reader.readAsDataURL(image);
    }
   }
   createImageFromBlob2(image: Blob) {
    let reader = new FileReader();
    reader.addEventListener("load", () =>{
     this.imageToShowIndex2=reader.result;
   }, false);
   if (image) {
     reader.readAsDataURL(image);
    }
   }
   createImageFromBlob3(image: Blob) {
    let reader = new FileReader();
    reader.addEventListener("load", () =>{
     this.imageToShowIndex3=reader.result;
   }, false);
   if (image) {
     reader.readAsDataURL(image);
    }
   }
  
  applyFilter(event: Event) {
    const filterValue = (event.target as HTMLInputElement).value;
    this.dataSource.filter = filterValue.trim().toLowerCase();
    if (this.dataSource.paginator) {
      this.dataSource.paginator.firstPage();
    }
  }

  obtenerPrediccionKg(row:any){
    console.log(row);
  }
  
  listarResultadoPrediccion(){
    try{
      this.ResultadosService.getResultPredict()
      .subscribe({
        next:(res)=>{
          //console.log(res);
          this.ELEMENT_DATA = res.res;
          console.log(this.ELEMENT_DATA);
          console.log(Object.values(this.ELEMENT_DATA));
          this.dataSource = new MatTableDataSource(res.res);
          this.dataSource.paginator = this.paginator;
          this.dataSource.sort=this.sort;
        },error:()=>{
          alert("Hubo un error mientras se generaba el entrenamiento");
        }
      })
    }catch{
      alert("hubo un error al mostrar la Lista de resultados")
    }
  }
  
  verImagen(row:any){}

  generarReporte(row:any){}
  
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
    }catch{
      alert("Hubo un error al mostrar el resultado *.jpg")
    }
  }

  getimage_Index_val_accuracy(){
    try{
      this.PrediccionService.getimage_indicador_val_accuracy()
      .subscribe(data => {
        this.createImageFromBlob1(data);
        //this.isImageLoading = false;
      }, error => {
        //this.isImageLoading = false;
        console.log(error);
      });
    }catch{
      alert("Hubo un error al mostrar el resultado *.jpg")
    }
  }

  getimage_Index_val_loss(){
    try{
      this.PrediccionService.getimage_indicador_val_loss()
      .subscribe(data => {
        this.createImageFromBlob2(data);
        //this.isImageLoading = false;
      }, error => {
        //this.isImageLoading = false;
        console.log(error);
      });
    }catch{
      alert("Hubo un error al mostrar el resultado *.jpg")
    }
  }
  getimage_Index_loss(){
    try{
      this.PrediccionService.getimage_indicador_loss()
      .subscribe(data => {
        this.createImageFromBlob3(data);
        //this.isImageLoading = false;
      }, error => {
        //this.isImageLoading = false;
        console.log(error);
      });
    }catch{
      alert("Hubo un error al mostrar el resultado *.jpg")
    }
  }

  
  /*
  ngOnInit(): void {
    this.PrediccionService.getImagenNeuralNet()
    .subscribe(data=>{
      console.log(data);
      this.imagenesarray = data.data;
      //this.imagenesarray.values();
    },
    error =>console.log(error))
  }
  */

  deleteimage(){}

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
    }catch{alert("Hubo un error al momento de descargar")
  }
}

}
