import { EntrenamodeloService } from './../../servicios/entrenamodelo.service';
import { LoadsampleService } from './../../servicios/loadsample.service';
import { Component, OnInit } from '@angular/core';
import { MatDialogModule } from '@angular/material/dialog';
import * as XLSX from 'xlsx';






@Component({
  selector: 'app-entrenamiento',
  templateUrl: './entrenamiento.component.html',
  styleUrls: ['./entrenamiento.component.css']
})



export class EntrenamientoComponent implements OnInit {
  ExcelData:any;

  private fileTmp:any;
  
  constructor(private LoadsampleService:LoadsampleService,private EntrenamodeloService:EntrenamodeloService) {
    
  }

  ngOnInit(): void {
  }
  
  sendFile():void{

    const body = new FormData();
    body.append('myFile', this.fileTmp.fileRaw,this.fileTmp.fileName)

    this.LoadsampleService.sendPost(body)
    .subscribe(res => console.log(res))
  }

  ReadExcel(event:any){
    
    // PARA IMPORTAR LA MUESTRA AL BACKEND
    const [file] = event.target.files;
    console.log(file);

    this.fileTmp={
      fileRaw:file,
      fileName:file.name
    }
    
    // PARA VACIAR EN LA TABLA DE MUESTRA
    const target:DataTransfer = <DataTransfer> (event.target);
    if(target.files.length !==1) throw new Error('No se pueden usar varios archivos');

    const fileReader:FileReader = new FileReader();

    fileReader.onload = (e:any)=>{
      const bstr: string = e.target.result;

      const workBook:XLSX.WorkBook = XLSX.read(bstr,{type:'binary'});
      
      var sheetNames:string = workBook.SheetNames[0];

      const ws:XLSX.WorkSheet = workBook.Sheets[sheetNames];
      //console.log(ws);

      this.ExcelData = (XLSX.utils.sheet_to_json(ws,{header:1}));
      //console.log(this.ExcelData);
      let registro = [];
      registro = this.ExcelData;
      console.log(registro);

    }

    fileReader.readAsBinaryString(target.files[0]);

  }

  entrenar():void{
    this.EntrenamodeloService.getEntrenamiento()
    .subscribe(resp => console.log(resp))
    
  }
  nuevo():void{
    this.EntrenamodeloService.getNuevoEntrenamiento()
    .subscribe(resp => console.log(resp))
  }



  
}
