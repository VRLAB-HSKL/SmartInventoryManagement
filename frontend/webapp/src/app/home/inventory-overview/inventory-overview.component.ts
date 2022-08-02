import { Component, OnInit, Input } from '@angular/core';
import { InventoryInfo } from '../inventory-info.model';

@Component({
  selector: 'app-inventory-overview',
  templateUrl: './inventory-overview.component.html',
  styleUrls: ['./inventory-overview.component.css']
})
export class InventoryOverviewComponent implements OnInit {
  @Input() inventoryInfo!: InventoryInfo;

  constructor() { }

  ngOnInit(): void {
  }

}
