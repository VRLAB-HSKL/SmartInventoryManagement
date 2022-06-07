import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import { SignUpFormComponent } from './authentication/sign-up-form/sign-up-form.component';
import { SignInFormComponent } from './authentication/sign-in-form/sign-in-form.component';

@NgModule({
  declarations: [
    AppComponent,
    SignUpFormComponent,
    SignInFormComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
