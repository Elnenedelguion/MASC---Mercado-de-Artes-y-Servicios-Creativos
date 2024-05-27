import { Component } from '@angular/core';
import { AboutUsService } from '../../services/about-us.service';

@Component({
  selector: 'app-about-us',
  standalone: true,
  imports: [],
  templateUrl: './about-us.component.html',
  styleUrl: './about-us.component.css'
})
export class AboutUsComponent {
 profesionalList:any;

constructor(private AboutUsService:AboutUsService)
{
  this.profesionalList=AboutUsService.obtenerProfesionales().subscribe({
    next: (profesionalList) => {
      this.profesionalList=this.profesionalList;
    },
    error: (error) => {
      console.error(error)
    }
  });
}

}
