import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl, Validators, FormBuilder } from '@angular/forms';
import { MatDialogRef } from '@angular/material/dialog';
import { Requerimiento } from 'src/app/modelos/requerimiento';
import { RequerimientService } from 'src/app/servicios/requerimient.service';


@Component({
  selector: 'app-dialog',
  templateUrl: './dialog.component.html',
  styleUrls: ['./dialog.component.css']
})
export class DialogComponent implements OnInit {
  
  hide = true;
  email = new FormControl('', [Validators.required, Validators.email]);
  requerimientoForm !: FormGroup;
  estadoRequerimiento: string[] = ['Aprobado', 'Pendiente', 'Rechazado'];
  requerimientoArray: Requerimiento[]=[];


  constructor(private formBuilder:FormBuilder,private requerimentService:RequerimientService,private dialogRef: MatDialogRef<DialogComponent>) { }

  ngOnInit(): void {
    this.requerimientoForm = this.formBuilder.group({
      nombreInsumo:['',Validators.required],
      categoriaInsumo:['',Validators.required],
      fecha:['',Validators.required],
      cantidad:['',Validators.required],
      unidad:['',Validators.required],
      email:['',Validators.required],
      monto:['',Validators.required],
      estado:[''],
      comentario:['',Validators.required]
    })
  }
  
  getErrorMessage() {
    if (this.email.hasError('required')) {
      return 'Debe ingresar un correo válido';
    }

    return this.email.hasError('email') ? 'Not a valid email' : '';
  }
  nuevoRequerimiento(){
    this.requerimientoArray=this.requerimientoForm.value;
    
    if(this.requerimientoForm.valid){
      this.requerimentService.postRequeriment(this.requerimientoArray)
      .subscribe({
        next:(res)=>{
          alert("Requerimiento generado con éxito");
          this.requerimientoForm.reset();
          this.dialogRef.close()
        },
        error:()=>{
          alert("Error mientras se registraba el requerimiento")
        }
      })
    }else{
      alert("Hay campos vacios")
    }
  }

  /*nuevoRequerimiento(){
    if(this.requerimientoForm.valid){
      this.requerimentService.postRequeriment(this.requerimientoForm.value)
      .subscribe({
        next:(res)=>{
          alert("Requerimiento generado con éxito");
          this.requerimientoForm.reset();
          this.dialogRef.close()

        },
        error:()=>{
          alert("Error mientras se registraba el requerimiento")
        }
      })
      
    }
    console.log(this.requerimientoForm.value);

  }*/

}
