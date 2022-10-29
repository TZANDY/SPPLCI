import { Component } from '@angular/core';
import { AuthService } from '@auth0/auth0-angular';
import { MatDialog } from '@angular/material/dialog';
import { MatCheckboxModule } from '@angular/material/checkbox'


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})

export class AppComponent {
  title = 'spplci';
  //usuarioArray: Usuarios[]=[];
  

  
  constructor(public auth:AuthService,public dialog:MatDialog){}

  loginWithRedirect(){
    this.auth.loginWithRedirect();
  }

  logout(){
    this.auth.logout();
  }

  

  /*
  ngOnInit(): void{
    this.UsuarioService.getUsuarios()
    .subscribe(data=>{
      console.log(data);
      this.usuarioArray = data.data;
    },
    error =>console.log(error))

  }*/

 
}
