import { Component } from '@angular/core';
import { RouterLink } from '@angular/router';
import { ProductComponent } from '../product/product.component';

@Component({
  selector: 'app-services',
  standalone: true,
  imports: [RouterLink, ProductComponent],
  templateUrl: './services.component.html',
  styleUrl: './services.component.css'
})
export class ServicesComponent {

}
