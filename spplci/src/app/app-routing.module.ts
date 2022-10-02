import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './componentes/home/home.component';
import { UsuariosComponent } from './componentes/usuarios/usuarios.component';
import { EntrenamientoComponent } from './componentes/entrenamiento/entrenamiento.component';
import { ConfifactorComponent } from './componentes/entrenamiento/confifactor/confifactor.component';
import { ModeloComponent } from './componentes/entrenamiento/modelo/modelo.component';


//Crear una constante
const routes: Routes = [

  //crear rutas o path's
  {path:'home',component:HomeComponent},
  {path:'',redirectTo:'home',pathMatch:'full'},
  {path:'usuarios',component:UsuariosComponent},
  {path:'entrenamiento',component:EntrenamientoComponent},
  {path:'entrenamiento/confifactor',component:ConfifactorComponent},
  {path:'entrenamiento/modelo',component:ModeloComponent},

  

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
