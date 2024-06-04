import { Component } from '@angular/core';
import { RouterLink } from '@angular/router';
import { StoreService } from '../../services/store.service';
import { Product } from '../../model/productos';

@Component({
  selector: 'app-product',
  standalone: true,
  imports: [RouterLink],
  templateUrl: './product.component.html',
  styleUrl: './product.component.css'
})
export class ProductComponent {

  products: Product[] = [];
  constructor(private storeService: StoreService) { }

  ngOnInit(): void {
    this.getProducts();
  };

  getProducts() {
    this.storeService.getAllProducts().subscribe((data) => {
      return this.products = data;

    })
  }
  addToCart(product: Product) {

    this.storeService.addProduct(product)
  }

}
