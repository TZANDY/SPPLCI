
import { OperatividadComponent } from './componentes/operatividad/operatividad.component';
import { EntrenamodeloService } from './servicios/entrenamodelo.service';
import { NgModule } from '@angular/core';
import { FormsModule, ReactiveFormsModule } from '@angular/forms'
import { ScrollingModule } from '@angular/cdk/scrolling';

import { BrowserModule } from '@angular/platform-browser';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HomeComponent } from './componentes/home/home.component';
import { UsuariosComponent } from './componentes/usuarios/usuarios.component';
import { EntrenamientoComponent } from './componentes/entrenamiento/entrenamiento.component';
import { LoginComponent } from './componentes/auth/login/login.component';
import { RegisterComponent } from './componentes/auth/register/register.component';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { ConfifactorComponent } from './componentes/entrenamiento/confifactor/confifactor.component';
import { ModeloComponent } from './componentes/entrenamiento/modelo/modelo.component';
import { PrediccionComponent } from './componentes/operatividad/prediccion/prediccion.component';
import { RequerimientoComponent } from './componentes/operatividad/requerimiento/requerimiento.component';
import { SolicitudesComponent } from './componentes/operatividad/solicitudes/solicitudes.component';
import { CalificacionesComponent } from './componentes/operatividad/calificaciones/calificaciones.component';
import { HistoricosComponent } from './componentes/operatividad/historicos/historicos.component';


// Import the module from the SDK
import { AuthModule } from '@auth0/auth0-angular';
import { UsuarioService } from './servicios/usuario.service';
import { HttpClientModule } from '@angular/common/http';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MatDialogModule } from '@angular/material/dialog';
import { MatButtonModule } from '@angular/material/button';
import { MatIconModule} from '@angular/material/icon';
import { MatInputModule} from '@angular/material/input';
import { MatFormFieldModule} from '@angular/material/form-field';
import { MatCheckboxModule } from '@angular/material/checkbox';
import { MatTableModule} from '@angular/material/table';
import { PrediccionService } from './servicios/prediccion.service';
import { DialogComponent } from './componentes/operatividad/requerimiento/dialog/dialog.component';
import { MatSelectModule} from '@angular/material/select';
import { MatDatepickerModule} from '@angular/material/datepicker';
import { MatNativeDateModule } from '@angular/material/core';
import { MatRadioModule} from '@angular/material/radio';
import { RequerimientService } from './servicios/requerimient.service';
import { MatPaginatorModule} from '@angular/material/paginator';
import { MatProgressSpinnerModule} from '@angular/material/progress-spinner';
import { MatListModule} from '@angular/material/list';
import { MatGridListModule} from '@angular/material/grid-list';
import { MatCardModule} from '@angular/material/card';


import { MatSortModule} from '@angular/material/sort';






@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    UsuariosComponent,
    EntrenamientoComponent,
    LoginComponent,
    RegisterComponent,
    ConfifactorComponent,
    ModeloComponent,
    OperatividadComponent,
    PrediccionComponent,
    RequerimientoComponent,
    SolicitudesComponent,
    CalificacionesComponent,
    HistoricosComponent,
    DialogComponent

  ],
  imports: [
    BrowserModule,
    FormsModule,
    BrowserAnimationsModule,
    AppRoutingModule,
    ScrollingModule,
    MatDialogModule,
    MatButtonModule,
    MatCheckboxModule,
    HttpClientModule,
    NgbModule,
    MatIconModule,
    MatInputModule,
    MatFormFieldModule,
    MatTableModule,
    MatSelectModule,
    MatDatepickerModule,
    MatNativeDateModule,
    MatRadioModule,
    MatPaginatorModule,
    MatSortModule,
    MatProgressSpinnerModule,
    MatCardModule,
    MatListModule,
    MatGridListModule,
    ReactiveFormsModule,
        
    // Import the module into the application, with configuration
    AuthModule.forRoot({
      domain: 'dev-nl9rk7s9.us.auth0.com',
      clientId: 'Y9SWgTQKobsUXR6v5ihnw3Vn6daybaPr',
      cacheLocation:'localstorage',
      useRefreshTokens:true
    }),
    BrowserAnimationsModule,
  ],
  providers: [UsuarioService,EntrenamodeloService,PrediccionService,RequerimientService],
  bootstrap: [AppComponent]
})
export class AppModule { 
  
}
