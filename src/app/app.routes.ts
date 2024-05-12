import { Routes } from '@angular/router';
import { HomeComponent } from './pages/home/home.component';
import { AboutUsComponent } from './pages/about-us/about-us.component';
import { ContactComponent } from './pages/contact/contact.component';
import { DashboardComponent } from './pages/dashboard/dashboard.component';

export const routes: Routes = [
    {path: 'home', component: HomeComponent},
    {path:'about-us', component:AboutUsComponent},
    {path:'contact', component:ContactComponent},
    {path:'dashboard', component:DashboardComponent},
    {path: '', redirectTo: '/home', pathMatch: 'full'},
];
