import { Component, OnInit,Inject } from '@angular/core';
import { FormGroup, FormControl, Validators, FormBuilder } from '@angular/forms';
import { MatDialogRef,MAT_DIALOG_DATA } from '@angular/material/dialog';
import { Requerimiento } from 'src/app/modelos/requerimiento';
import { RequerimientService } from 'src/app/servicios/requerimient.service';


@Component({
  selector: 'app-dialog',
  templateUrl: './dialog.component.html',
  styleUrls: ['./dialog.component.css']
})
export class DialogComponent implements OnInit {
  
  hide = true;
  actionBtn:string ="Aceptar"
  email = new FormControl('', [Validators.required, Validators.email]);
  requerimientoForm !: FormGroup;
  estadoRequerimiento: string[] = ['Aprobado', 'Pendiente', 'Rechazado'];
  requerimientoArray: Requerimiento[]=[];
  id!:string;
 


  constructor(private formBuilder:FormBuilder,
    private requerimentService:RequerimientService,
    @Inject(MAT_DIALOG_DATA) public editData:any,
    private dialogRef: MatDialogRef<DialogComponent>) { }

  ngOnInit(): void {
    this.requerimientoForm = this.formBuilder.group({
      id:[''],
      nombreInsumo:['',Validators.required],
      categoriaInsumo:['',Validators.required],
      fecha:['',Validators.required],
      cantidad:['',Validators.required],
      unidad:['',Validators.required],
      email:['',[Validators.required,Validators.email]],
      monto:['',Validators.required],
      comentario:['',Validators.required],
      estado:['']      
    });
    console.log(this.editData);

    if(this.editData){
      this.actionBtn = "Actualizar";
      this.requerimientoForm.controls['id'].setValue(this.editData._id);
      this.requerimientoForm.controls['nombreInsumo'].setValue(this.editData.nombreInsumo);
      this.requerimientoForm.controls['categoriaInsumo'].setValue(this.editData.categoriaInsumo);
      this.requerimientoForm.controls['fecha'].setValue(this.editData.fecha);
      this.requerimientoForm.controls['cantidad'].setValue(this.editData.cantidad);
      this.requerimientoForm.controls['unidad'].setValue(this.editData.unidad);
      this.requerimientoForm.controls['email'].setValue(this.editData.email);
      this.requerimientoForm.controls['monto'].setValue(this.editData.monto);
      this.requerimientoForm.controls['estado'].setValue(this.editData.estado);
      this.requerimientoForm.controls['comentario'].setValue(this.editData.comentario);
      console.log(this.editData._id);
    }
  }
  
  getErrorMessage() {
    if (this.email.hasError('required')) {
      return 'Debe ingresar un correo válido';
    }
    return this.email.hasError('email') ? 'Not a valid email' : '';
  }

  nuevoRequerimiento(){
    if(!this.editData){
      this.requerimientoArray=this.requerimientoForm.value;
      if(this.requerimientoForm.valid){
        this.requerimentService.postRequeriment(this.requerimientoArray)
        .subscribe({
          next:(res)=>{
            alert("Requerimiento generado con éxito");
            console.log(res);
            this.requerimientoForm.reset();
            this.dialogRef.close('save')
          },
          error:()=>{
            alert("Error mientras se registraba el requerimiento")
          }
        })
      }else{
        alert("Hay campos vacios")
      }
    }else{
      this.actualizarRequerimiento()
    }
  }

  actualizarRequerimiento(){
    this.requerimentService.updateRequeriment(this.requerimientoForm.value,this.editData._id)
    .subscribe({
      next:(res)=>{
        alert("Producto Actualizado correctamente")
        this.requerimientoForm.reset();
        this.dialogRef.close('update');
      },
      error:()=>{
        alert("Error mientras se actualizaba el registro")
      }
    })

  }

}
