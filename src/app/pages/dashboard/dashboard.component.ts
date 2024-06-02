import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { StoreService } from '../../services/store.service';
import { RouterLink } from '@angular/router';
import { ProductComponent } from '../product/product.component';
import { HeaderComponent } from '../header/header.component';


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
  imports: [CommonModule, RouterLink, ProductComponent, HeaderComponent],
  templateUrl: './dashboard.component.html',
  styleUrl: './dashboard.component.css'
})
export class DashboardComponent {
  myCart$ = this.storeService.myCart$;

  viewCart: boolean = false;

  constructor(private storeService: StoreService) { }

  updateUnits(operation: string, id: string) {

    const product = this.storeService.findProductById(id)
    if (product) {
      if (operation === 'minus' && product.cantidad > 0) {
        product.cantidad = product.cantidad - 1;
      }
      if (operation === 'add') {
        product.cantidad = product.cantidad + 1;

      }
      if (product.cantidad === 0) {
        this.deleteProduct(id)
      }
    }


}

totalProduct(price: number, units: number) {
  return price * units
}
deleteProduct(id: string) {
  console.log(`Delete product ID: ${id}`);
  this.storeService.deleteProduct(id);

}
totalCart() {
  const result = this.storeService.totalCart();
  return result;
}

}
