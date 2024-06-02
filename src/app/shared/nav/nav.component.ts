import { Component } from '@angular/core';
import { RouterLink } from '@angular/router';
import { StoreService } from '../../services/store.service';
import { AsyncPipe } from '@angular/common';
import { ProductComponent } from '../../pages/product/product.component';

@Component({
  selector: 'app-nav',
  standalone: true,
  imports: [RouterLink, AsyncPipe, ProductComponent],
  templateUrl: './nav.component.html',
  styleUrl: './nav.component.css'
})
export class NavComponent {
  viewCart: boolean = false;
  myCart$ = this.storeService.myCart$;




  constructor(private storeService: StoreService) { }

  onToggleCart() {
    this.viewCart = !this.viewCart

  };

}
