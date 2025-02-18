import { Injectable } from '@angular/core';
import { api } from '../../axios-config';

@Injectable({
  providedIn: 'root'
})
export class ProductService {

  constructor() { }

  async getProducts(page: number = 1, limit: number = 10) {
    try {
      const response = await api.get('/products', {
        params: {
          page,
          limit
        }
      });
      return response.data.product;
    } catch (error) {
      console.error(error);
      return null;
    }
  }

  async getProductByTitle(title: string, page: number = 1, limit: number = 10) {
    try {
      const response = await api.get(`/products/search/`, {
        params: {
          title,
          page, 
          limit
        }
      });
      return response.data.product;
    } catch (error) {
      console.error(error);
      return null;
    }
  }
}
