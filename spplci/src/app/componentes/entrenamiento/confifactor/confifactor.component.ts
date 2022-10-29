import { Factor } from './../../../modelos/factor';
import { Component, OnInit } from '@angular/core';
import {ThemePalette} from '@angular/material/core';




export interface Task {
  name: string;
  completed: boolean;
  color: ThemePalette;
  subtasks?: Task[];
}

@Component({
  selector: 'app-confifactor',
  templateUrl: './confifactor.component.html',
  styleUrls: ['./confifactor.component.css']
})
export class ConfifactorComponent implements OnInit {

  task: Task = {
    name: 'Estaciones astronómica',
    completed: false,
    color: 'primary',
    subtasks: [
      {name: 'Invierno', completed: true, color: 'accent'},
      {name: 'Primavera', completed: false, color: 'accent'},
      {name: 'Verano', completed: false, color: 'accent'},
      {name: 'Otoño', completed: true, color: 'accent'},
    ],
  };

  setClase(){
    const factor = new Factor();
    factor.nombre = this.task.name;
    console.log(factor);
  }

  allComplete: boolean = false;

  updateAllComplete() {
    this.allComplete = this.task.subtasks != null && this.task.subtasks.every(t => t.completed);
  }

  someComplete(): boolean {
    if (this.task.subtasks == null) {
      return false;
    }
    return this.task.subtasks.filter(t => t.completed).length > 0 && !this.allComplete;
  }

  setAll(completed: boolean) {
    this.allComplete = completed;
    if (this.task.subtasks == null) {
      return;
    }
    this.task.subtasks.forEach(t => (t.completed = completed));
  }

  constructor() { }

  ngOnInit(): void {
    
  }

}
