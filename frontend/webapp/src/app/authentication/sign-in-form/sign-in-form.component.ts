import { Component, OnInit, ViewChild } from '@angular/core';
import { AbstractControl, FormControl, NgForm, ValidationErrors, ValidatorFn } from '@angular/forms';

@Component({
  selector: 'app-sign-in-form',
  templateUrl: './sign-in-form.component.html',
  styleUrls: ['./sign-in-form.component.css']
})
export class SignInFormComponent implements OnInit {
  @ViewChild("form") form!: NgForm;
  passwordFieldType: string = "password";
  error: string | null = "";


  constructor() { }

  ngOnInit(): void {
  }

  changePasswordVisibility(){
    if(this.passwordFieldType === "password"){
      this.passwordFieldType = "text";
    } else if(this.passwordFieldType === "text"){
      this.passwordFieldType = "password";
    } else{
      throw Error(`passwordFieldType has entered an invalid state. passwordFieldType=${this.passwordFieldType}`);
    }
  }

  onSubmit(form: NgForm){
    let email = form.value.email;
    let password = form.value.password;

    console.log(`email=${email}, password=${password}`); // Todo: Den Log raus und dafür die Request-Logik rein.

    form.reset();
  }

}
