import { Component, OnInit, ViewChild } from '@angular/core';
import { MatDialog, MAT_DIALOG_DATA } from '@angular/material/dialog';
import { RequerimientService } from 'src/app/servicios/requerimient.service';
import { DialogComponent } from './dialog/dialog.component';
import { MatPaginator} from '@angular/material/paginator';
import { MatSort} from '@angular/material/sort';
import { MatTableDataSource} from '@angular/material/table';



@Component({
  selector: 'app-requerimiento',
  templateUrl: './requerimiento.component.html',
  styleUrls: ['./requerimiento.component.css']
})
export class RequerimientoComponent implements OnInit {

  displayedColumns: string[] = ['nombreInsumo', 'categoriaInsumo', 'fecha','cantidad','unidad','email','monto','comentario','estado','action'];
  dataSource!: MatTableDataSource<any>; 
  @ViewChild(MatPaginator) paginator!: MatPaginator;
  @ViewChild(MatSort) sort!: MatSort; 

  
  constructor(
    public dialog: MatDialog,
    private requerimentService:RequerimientService) { }

  openDialog() {
    this.dialog.open(DialogComponent,{
      width:'30%'
    }).afterClosed().subscribe(val=>{
      if(val ==='save'){
        this.listarRequerimientos();
      }
      
    });
  }

  listarRequerimientos(){
    this.requerimentService.getRequeriment().subscribe({
        next:(res)=>{
          console.log(res);
          
          this.dataSource = new MatTableDataSource(res.data);
          this.dataSource.paginator = this.paginator;
          this.dataSource.sort = this.sort;
          console.log(this.dataSource);
        },
        error:()=>{
          alert("Error mientras se registraba el requerimiento")
        }
      });
  }

  editarRequerimiento(row:any){
    this.dialog.open(DialogComponent,{
      width:'30%',
      data:row
    }).afterClosed().subscribe( val=>{
      if(val ==='update'){this.listarRequerimientos();}
    })
  }

  eliminarRequerimiento(id:any){
    this.requerimentService.deleteRequeriment(id).subscribe({
      next:(res)=>{
        alert("Registro eliminado con exito");
        this.listarRequerimientos();
      },error:()=>{
        alert("Error mientras se eliminaba el registro");
        this.listarRequerimientos();
      }
    })


  }

  applyFilter(event: Event) {
    const filterValue = (event.target as HTMLInputElement).value;
    this.dataSource.filter = filterValue.trim().toLowerCase();

    if (this.dataSource.paginator) {
      this.dataSource.paginator.firstPage();
    }
  }

  

  ngOnInit(): void {
    this.listarRequerimientos();
  }

}
