import { Component, OnInit } from '@angular/core';
import { InventoryInfo } from './inventory-info.model';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
  inventoryInfos: InventoryInfo[] = [
    new InventoryInfo("Fridge 1", 20, new Date(2022, 3, 12)),
    new InventoryInfo("Vorratsraum 2", 55, new Date(2014, 6, 22)),
    new InventoryInfo("Fridge 1", 20, new Date(2022, 3, 12)),
    new InventoryInfo("Vorratsraum 2", 55, new Date(2014, 6, 22)),
    new InventoryInfo("Fridge 1", 20, new Date(2022, 3, 12)),
    new InventoryInfo("Vorratsraum 2", 55, new Date(2014, 6, 22)),
    new InventoryInfo("Vorratsraum 2", 55, new Date(2014, 6, 22)),
    new InventoryInfo("Vorratsraum 2", 55, new Date(2014, 6, 22))
  ];
  constructor() { }

  ngOnInit(): void {
  }

}
