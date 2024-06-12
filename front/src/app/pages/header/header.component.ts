import { Component } from '@angular/core';
import { StoreService } from '../../services/store.service';
import { RouterLink } from '@angular/router';
import { CommonModule } from '@angular/common';
import { ServicesComponent } from '../services/services.component';

@Component({
  selector: 'app-header',
  standalone: true,
  imports: [RouterLink, CommonModule, ServicesComponent],
  templateUrl: './header.component.html',
  styleUrl: './header.component.css'
})
export class HeaderComponent {
  viewCart: boolean = false;
  myCart$ = this.storeService.myCart$;




  constructor(private storeService: StoreService) { }

  onToggleCart() {
    this.viewCart = !this.viewCart
  };

}



