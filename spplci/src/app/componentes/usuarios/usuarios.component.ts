import { Component, OnInit } from '@angular/core';
import { Usuarios } from '../../modelos/usuarios';
import { UsuarioService } from '../../servicios/usuario.service';

@Component({
  selector: 'app-usuarios',
  templateUrl: './usuarios.component.html',
  styleUrls: ['./usuarios.component.css']
})


export class UsuariosComponent implements OnInit {
  usuarioArray: Usuarios[]=[];

  constructor(private UsuarioService:UsuarioService) { }

  ngOnInit(): void {
    this.UsuarioService.getUsuarios()
    .subscribe(data=>{
      console.log(data);
      this.usuarioArray = data.data;
    },
    error =>console.log(error))
  }

}
