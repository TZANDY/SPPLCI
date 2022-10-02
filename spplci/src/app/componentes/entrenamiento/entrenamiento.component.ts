import { Component, OnInit } from '@angular/core';
import {NgbModal} from '@ng-bootstrap/ng-bootstrap';
import * as XLSX from 'xlsx';

@Component({
  selector: 'app-entrenamiento',
  templateUrl: './entrenamiento.component.html',
  styleUrls: ['./entrenamiento.component.css']
})
export class EntrenamientoComponent implements OnInit {
  ExcelData:any;
  
  constructor(public modal:NgbModal) {
    
   }

  ngOnInit(): void {
  }

  ReadExcel(event:any){
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
      console.log(this.ExcelData);
    }

    fileReader.readAsBinaryString(target.files[0]);

    

  }

  
}
