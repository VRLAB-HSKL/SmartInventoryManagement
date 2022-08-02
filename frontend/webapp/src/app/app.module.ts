import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http'

import { AppComponent } from './app.component';
import { SignUpFormComponent } from './authentication/sign-up-form/sign-up-form.component';
import { SignInFormComponent } from './authentication/sign-in-form/sign-in-form.component';
import { HomeComponent } from './home/home.component';
import { RouterModule, Routes } from '@angular/router';
import { LandingPageComponent } from './landing-page/landing-page.component';
import { AuthGuard } from './authentication/auth.guard';
import { InventoryOverviewComponent } from './home/inventory-overview/inventory-overview.component';

const appRoutes: Routes = [
  {path: '', component: LandingPageComponent},
  {path: 'home', component: HomeComponent, canActivate: [AuthGuard]},
  {path: 'signup', component: SignUpFormComponent},
  {path: 'signin', component: SignInFormComponent},
]

@NgModule({
  declarations: [
    AppComponent,
    SignUpFormComponent,
    SignInFormComponent,
    HomeComponent,
    LandingPageComponent,
    InventoryOverviewComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpClientModule,
    RouterModule.forRoot(appRoutes),
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
