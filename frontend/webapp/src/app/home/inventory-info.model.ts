export class InventoryInfo{
    name: string;
    itemCount: number;
    lastUpdate: Date;

    constructor(name: string, itemCount: number, lastUpdate: Date){
        this.name = name;
        this.itemCount = itemCount;
        this.lastUpdate = lastUpdate;
    }
}