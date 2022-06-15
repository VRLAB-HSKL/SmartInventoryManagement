import { Component, OnInit, ViewChild } from '@angular/core';
import { FormControl, NgForm } from '@angular/forms';
import { AuthService } from '../auth.service';

@Component({
  selector: 'app-sign-up-form',
  templateUrl: './sign-up-form.component.html',
  styleUrls: ['./sign-up-form.component.css']
})
export class SignUpFormComponent implements OnInit {
  @ViewChild("form") form!: NgForm;
  @ViewChild("password") password!: FormControl;
  @ViewChild("confirmPassword") confirmPassword!: FormControl;
  passwordFieldType: string = "password";
  error: string | null = "";


  constructor(private authService: AuthService) { }

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
    let nickname: string | null = form.value.nickname;
    let email = form.value.email;
    let password = form.value.password;
    
    this.authService.signUp(nickname, email, password).subscribe(
      () => {
        console.log("User signed up");
        // Todo: Zur Home-Seite (Logged-in) weiterleiten
      }   
    )

    form.reset();
  }

  checkIfPasswordsMatch(){
    const passwordsMatch: boolean = this.password.value === this.confirmPassword.value;
    if(passwordsMatch){
      this.form.controls['confirmPassword'].setErrors(null);
    } else{
      this.form.controls['confirmPassword'].setErrors({'incorrect': true});
    }
  }

}

