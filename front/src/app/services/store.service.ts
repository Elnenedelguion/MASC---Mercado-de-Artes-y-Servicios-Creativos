import { Injectable } from '@angular/core';
import { BehaviorSubject, Observable } from 'rxjs';
import { HttpClient } from '@angular/common/http';
import { Product } from '../model/productos';
@Injectable({
  providedIn: 'root'
})
export class StoreService {

 
  baseUrl: string = 'http://localhost:8000/api/productos/'

  //lista carrito
  private myList: Product[] = [];

  //carrito observable
  private myCart = new BehaviorSubject<Product[]>([]);
  myCart$ = this.myCart.asObservable();

  constructor(private httpClient: HttpClient) { }

  getAllProducts(): Observable<Product[]> {
    const response = this.httpClient.get<Product[]>(`${this.baseUrl}`);
    // console.log(response);
    return response
  }
  //con promesa
  // getPromise(): Promise<any[]> {
  //   return lastValueFrom(this.httpClient.get<any[]>(`${this.baseUrl}products`))
  // }

  //añado producto al carrito
  addProduct(product: Product) {

    // debugger;
    if (this.myList.length === 0) {
      product.cantidad = 1;
      this.myList.push(product);
      //emito la lista para los que estén escuchando
      this.myCart.next(this.myList);

    } else {
      const productMod = this.myList.find((element) => {
        return element.codigodeBarras === product.codigodeBarras
      })
      if (productMod) {
        productMod.cantidad = productMod.cantidad + 1;
        this.myCart.next(this.myList);
      } else {
        product.cantidad = 1;
        this.myList.push(product);
        //ojo hay que emitir la lista!!
        this.myCart.next(this.myList);
      }

    }
  }

  findProductById(id: number) {
    return this.myList.find((element) => {
      return element.codigodeBarras === id
    })

  }

  deleteProduct(id: number) {

    this.myList = this.myList.filter((product) => {
      return product.codigodeBarras != id
    })
    this.myCart.next(this.myList);


  }
  totalCart() {
    const total = this.myList.reduce(function (acc, product) { return acc + (product.cantidad * product.precio); }, 0)
    return total
  }
}


