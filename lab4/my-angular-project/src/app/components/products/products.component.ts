import { Component, inject } from '@angular/core';
import { ProductService } from '../../services/product.service';
import { Product } from '../../model/product';
import { ProductCardComponent } from '../product-card/product-card.component';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-products',
  imports: [ProductCardComponent, CommonModule],
  templateUrl: './products.component.html',
  styleUrls: ['./products.component.css'] 
})
export class ProductsComponent {
  productsService = inject(ProductService);
  products: Product[] = [];
  favorites: Product[] = []
  page: number = 1;
  limit: number = 12;
  selectedTitle: string = 'all';

  async ngOnInit() {
    await this.fetchProducts();
  }


  async fetchProducts(reset: boolean = true) {
    if (reset) {
      this.page = 1;
      this.products = [];
    }
    
    let newProducts: Product[] = [];
    if (this.selectedTitle === 'all') {
      newProducts = await this.productsService.getProducts(this.page, this.limit) ?? [];
    } else if (this.selectedTitle === 'favorites') {
      newProducts = this.favorites
    } else {
      newProducts = await this.productsService.getProductByTitle(this.selectedTitle, this.page, this.limit) ?? [];
    }
    this.products = reset ? newProducts : [...this.products, ...newProducts];
  }

  async loadMore() {
    this.page++;
    await this.fetchProducts(false);
  }

  async filterProducts(category: string) {
    this.selectedTitle = category;
    await this.fetchProducts(true);
  }

  addToFavorite(product: Product) {
    this.favorites.push(product)
    console.log("added product")
  }


}
