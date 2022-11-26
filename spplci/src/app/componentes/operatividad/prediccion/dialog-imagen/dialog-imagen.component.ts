import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-dialog-imagen',
  templateUrl: './dialog-imagen.component.html',
  styleUrls: ['./dialog-imagen.component.css']
})
export class DialogImagenComponent implements OnInit {
  imageToShow: any;

  constructor() { }

  ngOnInit(): void {
  }

  createImageFromBlob(image: Blob) {
    let reader = new FileReader();
    reader.addEventListener("load", () => {
      this.imageToShow = reader.result;
    }, false);
    if (image) {
      reader.readAsDataURL(image);
    }
   }

}
