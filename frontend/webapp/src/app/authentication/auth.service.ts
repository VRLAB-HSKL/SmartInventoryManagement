import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { shareReplay, tap } from 'rxjs';
import { environment } from "../../environments/environment"


interface AuthResponseData {
  userId: number,
  token: string,
  refresh_token: string,
  expires_in: number,
}


@Injectable({
  providedIn: 'root'
})
export class AuthService {

  constructor(private http: HttpClient) { }

  signin(email: string, password: string){
    return this.http.post<AuthResponseData>(`${environment.restApiUrl}/sign-in`,
      {
        email: email,
        password: password,
      }
    ).pipe(tap(authResponseData => this.setSession), shareReplay());//Todo: nochmal mit RXJS auseinandersetzen und dann diese Line hier nochmal überprüfen
  }


  private setSession(authResponseData: AuthResponseData){
    const expiresAt_utc = new Date().getTime()+ authResponseData.expires_in*1000;

    localStorage.setItem("token", authResponseData.token);
    localStorage.setItem("expiresAt_utc", expiresAt_utc.toString());
  }

  logout(){
    localStorage.removeItem("token");
    localStorage.removeItem("expiresAt_utc");
  }


  isLoggedIn(){
    const expiresAt_utc = Number(localStorage.getItem("expiresAt_utc"));
    const token = localStorage.getItem("token");
    if(expiresAt_utc && token){
      return new Date().getTime() < expiresAt_utc;   
    }
    
    return false;
  }

  isLoggedOut(){
    return !this.isLoggedIn();
  }

}
