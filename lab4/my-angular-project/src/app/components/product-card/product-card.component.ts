import { CommonModule } from '@angular/common';
import { Component, EventEmitter, Input, Output } from '@angular/core';
import { Product } from '../../model/product';

@Component({
  selector: 'app-product-card',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './product-card.component.html',
  styleUrl: './product-card.component.css'
})
export class ProductCardComponent {
  @Input() product!: Product;
  @Output() addToFavoriteEvent = new EventEmitter<Product>();

  get fullStars(): number[] {
    return Array(Math.floor(this.product.rating)).fill(0);
  }

  get hasHalfStar(): boolean {
    return this.product.rating % 1 !== 0;
  }

  get emptyStars(): number[] {
    return Array(5 - Math.ceil(this.product.rating)).fill(0);
  }

  addToFavorite() {
    this.addToFavoriteEvent.emit(this.product);
  }
}
