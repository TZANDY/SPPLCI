import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './componentes/home/home.component';
import { UsuariosComponent } from './componentes/usuarios/usuarios.component';
import { EntrenamientoComponent } from './componentes/entrenamiento/entrenamiento.component';
import { ConfifactorComponent } from './componentes/entrenamiento/confifactor/confifactor.component';
import { ModeloComponent } from './componentes/entrenamiento/modelo/modelo.component';

//import { AuthGuard } from '@auth0/auth0-angular';
import { AuthGuard } from './guards/auth.guard';
import { PrediccionComponent } from './componentes/operatividad/prediccion/prediccion.component';
import { RequerimientoComponent } from './componentes/operatividad/requerimiento/requerimiento.component';
import { SolicitudesComponent } from './componentes/operatividad/solicitudes/solicitudes.component';
import { CalificacionesComponent } from './componentes/operatividad/calificaciones/calificaciones.component';
import { HistoricosComponent } from './componentes/operatividad/historicos/historicos.component';

//Crear una constante
const routes: Routes = [

  //crear rutas o path's
  {path:'home',component:HomeComponent},
  {path:'',redirectTo:'home',pathMatch:'full'},
  {path:'usuarios',component:UsuariosComponent,canActivate:[AuthGuard]},
  {path:'entrenamiento',component:EntrenamientoComponent,canActivate:[AuthGuard]},
  {path:'entrenamiento/confifactor',component:ConfifactorComponent,canActivate:[AuthGuard]},
  {path:'entrenamiento/modelo',component:ModeloComponent,canActivate:[AuthGuard]},
  {path:'operatividad/prediccion',component:PrediccionComponent,canActivate:[AuthGuard]},
  {path:'operatividad/requerimiento',component:RequerimientoComponent,canActivate:[AuthGuard]},
  {path:'operatividad/solicitudes',component:SolicitudesComponent,canActivate:[AuthGuard]},
  {path:'operatividad/calificaciones',component:CalificacionesComponent,canActivate:[AuthGuard]},
  {path:'operatividad/historicos',component:HistoricosComponent,canActivate:[AuthGuard]}

  

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
