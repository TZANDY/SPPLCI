import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HomeComponent } from './componentes/home/home.component';
import { UsuariosComponent } from './componentes/usuarios/usuarios.component';
import { EntrenamientoComponent } from './componentes/entrenamiento/entrenamiento.component';
import { OperatividadComponent } from './componentes/operatividad/operatividad.component';
import { LoginComponent } from './componentes/auth/login/login.component';
import { RegisterComponent } from './componentes/auth/register/register.component';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { ConfifactorComponent } from './componentes/entrenamiento/confifactor/confifactor.component';
import { ModeloComponent } from './componentes/entrenamiento/modelo/modelo.component';


@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    UsuariosComponent,
    EntrenamientoComponent,
    OperatividadComponent,
    LoginComponent,
    RegisterComponent,
    ConfifactorComponent,
    ModeloComponent
    
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    NgbModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
