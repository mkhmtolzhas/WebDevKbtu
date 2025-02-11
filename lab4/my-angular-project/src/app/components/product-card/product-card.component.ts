import { CommonModule } from '@angular/common';
import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-product-card',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './product-card.component.html',
  styleUrl: './product-card.component.css'
})
export class ProductCardComponent {
  @Input() title: string = '';
  @Input() price: number = 0;
  @Input() description: string = '';
  @Input() category: string = '';
  @Input() link: string = '';
  @Input() rating: number = 0;
  @Input() image: string = '';
  

  constructor() {
  }

  ngOnInit() {
  }

  get fullStars(): number[] {
    return Array(Math.floor(this.rating)).fill(0);
  }
  
  get hasHalfStar(): boolean {
    return this.rating % 1 !== 0;
  }
  
  get emptyStars(): number[] {
    return Array(5 - Math.ceil(this.rating)).fill(0);
  }
}
