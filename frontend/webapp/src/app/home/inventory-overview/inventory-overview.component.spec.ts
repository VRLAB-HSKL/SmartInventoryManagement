import { ComponentFixture, TestBed } from '@angular/core/testing';

import { InventoryOverviewComponent } from './inventory-overview.component';

describe('InventoryOverviewComponent', () => {
  let component: InventoryOverviewComponent;
  let fixture: ComponentFixture<InventoryOverviewComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ InventoryOverviewComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(InventoryOverviewComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
