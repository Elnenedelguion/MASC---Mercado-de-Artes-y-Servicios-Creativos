import { ApplicationConfig, importProvidersFrom } from '@angular/core';
import { provideRouter } from '@angular/router';


import { routes } from './app.routes';
import{authInterceptor} from './interceptor/auth.interceptor'
import { provideHttpClient, withInterceptors } from '@angular/common/http';
import { provideToastr } from 'ngx-toastr';

export const appConfig: ApplicationConfig = {
  providers: [
  provideToastr(),
  provideRouter(routes),
  provideHttpClient(withInterceptors([authInterceptor])),
    
  ],
};
