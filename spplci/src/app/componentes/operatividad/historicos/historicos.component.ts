import { Component, OnInit,ViewChild } from '@angular/core';
import {MatPaginator} from '@angular/material/paginator';
import {MatSort} from '@angular/material/sort';
import {MatTableDataSource} from '@angular/material/table';
import { HistoricosService } from '../../../servicios/historicos.service';

@Component({
  selector: 'app-historicos',
  templateUrl: './historicos.component.html',
  styleUrls: ['./historicos.component.css']
})
export class HistoricosComponent implements OnInit {
  displayedColumns: string[] = ['ord', 'nombre', 'fechaC', 'fechaU','size'];
  dataSource!: MatTableDataSource<any>;

  @ViewChild(MatPaginator) paginator!: MatPaginator;
  @ViewChild(MatSort) sort!: MatSort;

  constructor(private HistoricosService:HistoricosService) { }

  ngOnInit(): void {
    //this.listarModelos();
  }

  applyFilter(event: Event) {
    const filterValue = (event.target as HTMLInputElement).value;
    this.dataSource.filter = filterValue.trim().toLowerCase();

    if (this.dataSource.paginator) {
      this.dataSource.paginator.firstPage();
    }
  }

  listarModelos(){
    try{
      this.HistoricosService.getHistoricoModelo()
      .subscribe({
        next:(res)=>{
          console.log(res);
          this.dataSource = new MatTableDataSource(res.data);
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

  listarMuestras(){
    try{
      this.HistoricosService.getHistoricoMuestra()
      .subscribe({
        next:(res)=>{
          console.log(res);
          this.dataSource = new MatTableDataSource(res.data);
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

  listarGraficas(){
    try{
      this.HistoricosService.getHistoricoGraficas()
      .subscribe({
        next:(res)=>{
          console.log(res);
          this.dataSource = new MatTableDataSource(res.data);
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

}
