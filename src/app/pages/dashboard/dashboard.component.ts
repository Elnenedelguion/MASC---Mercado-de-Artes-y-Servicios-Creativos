import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';


interface Artist {
  id: number;
  name: string;
  genre: string;
  imageUrl: string;
  price: number;
}

@Component({
  selector: 'app-dashboard',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './dashboard.component.html',
  styleUrl: './dashboard.component.css'
})
export class DashboardComponent {}