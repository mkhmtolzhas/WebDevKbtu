import { Component, inject } from '@angular/core';
import { ProductService } from '../../services/product.service';
import { Product } from '../../model/product';
import { ProductCardComponent } from '../product-card/product-card.component';
import { CommonModule } from '@angular/common';


@Component({
  selector: 'app-products',
  imports: [ProductCardComponent, CommonModule],
  templateUrl: './products.component.html',
  styleUrl: './products.component.css'
})
export class ProductsComponent {
  productsService = inject(ProductService);
  products: Product[] = [];
  page: number = 1;
  limit: number = 12;

  async ngOnInit() {
    this.products = await this.productsService.getProducts(this.page, this.limit) ?? [];
  }

  async loadMore() {
    this.page++;
    const newProducts = await this.productsService.getProducts(this.page, this.limit) ?? [];
    this.products = [...this.products, ...newProducts];
  }
}
