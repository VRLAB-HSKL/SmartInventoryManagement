import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import { SignUpFormComponent } from './authentication/sign-up-form/sign-up-form.component';

@NgModule({
  declarations: [
    AppComponent,
    SignUpFormComponent
  ],
  imports: [
    BrowserModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
