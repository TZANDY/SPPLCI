import { NgModule } from '@angular/core';
import { ScrollingModule } from '@angular/cdk/scrolling';
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





// Import the module from the SDK
import { AuthModule } from '@auth0/auth0-angular';
import { UsuarioService } from './servicios/usuario.service';
import { HttpClientModule } from '@angular/common/http';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';



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
    ModeloComponent,
    
    
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    ScrollingModule,
    HttpClientModule,
    NgbModule,
    
    // Import the module into the application, with configuration
    AuthModule.forRoot({
      domain: 'dev-nl9rk7s9.us.auth0.com',
      clientId: 'Y9SWgTQKobsUXR6v5ihnw3Vn6daybaPr',
      cacheLocation:'localstorage',
      useRefreshTokens:true
    }),
    BrowserAnimationsModule,
  ],
  providers: [UsuarioService],
  bootstrap: [AppComponent]
})
export class AppModule { 
  
}
