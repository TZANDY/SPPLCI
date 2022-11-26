import { Component, OnInit,ViewChild } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Imagenes } from 'src/app/modelos/imagenes';
import { PrediccionService } from 'src/app/servicios/prediccion.service';
import { MatPaginator} from '@angular/material/paginator';
import { MatSort} from '@angular/material/sort';
import { MatTableDataSource} from '@angular/material/table';
import { ResultadosService } from 'src/app/servicios/resultados.service';

@Component({
  selector: 'app-prediccion',
  templateUrl: './prediccion.component.html',
  styleUrls: ['./prediccion.component.css']
})
export class PrediccionComponent implements OnInit {
  form:FormGroup;
  imagenesarray:Imagenes[] =[];
  imageToShow: any;
  panelOpenState = false;

  multi!: any[];
  view: [number,number] = [700, 300];

  // options
  legend: boolean = true;
  showLabels: boolean = true;
  animations: boolean = true;
  xAxis: boolean = true;
  yAxis: boolean = true;
  showYAxisLabel: boolean = true;
  showXAxisLabel: boolean = true;
  xAxisLabel: string = 'Dias de la semana';
  yAxisLabel: string = 'Cantidad';
  timeline: boolean = true;

  colorScheme = {
    domain: ['#5AA454', '#E44D25', '#CFC0BB', '#7aa3e5', '#a8385d', '#aae3f5']
  };

  
  onSelect(data:any): void {
    console.log('Item clicked', JSON.parse(JSON.stringify(data)));
  }

  onActivate(data:any): void {
    console.log('Activate', JSON.parse(JSON.stringify(data)));
  }

  onDeactivate(data:any): void {
    console.log('Deactivate', JSON.parse(JSON.stringify(data)));
  }
  

  displayedColumns: string[] = ['no', 'diaSemana','valor','valorkg', 'action'];
  dataSource!: MatTableDataSource<any>; 
  @ViewChild(MatPaginator) paginator!: MatPaginator;
  @ViewChild(MatSort) sort!: MatSort; 

  constructor(private PrediccionService:PrediccionService,private fb:FormBuilder,private ResultadosService:ResultadosService) { 
    this.form = this.fb.group({
      nombre:['',Validators.required]
    })
    //Object.assign(this,{multi});
    
    //this.nombrearchivo = this.nombre.toString();
  }

  createImageFromBlob(image: Blob) {
   let reader = new FileReader();
   reader.addEventListener("load", () => {
    this.imageToShow = reader.result;
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
      this.ResultadosService.getResultPredict().subscribe({
        next:(res)=>{
          console.log(res);
          this.dataSource = new MatTableDataSource(res.res);
          this.dataSource.paginator = this.paginator;
          this.dataSource.sort=this.sort;
        }
        

      })

    }catch{

    }

  }
  

  verImagen(row:any){

  }
  generarReporte(row:any){

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
    }catch{}
  }

  

  

  ngOnInit(): void { 
    this.listarResultadoPrediccion();
    this.getimage()

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
