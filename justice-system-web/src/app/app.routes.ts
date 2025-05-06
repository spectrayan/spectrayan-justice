import { Routes } from '@angular/router';

export const routes: Routes = [
  {
    path: 'judicial',
    loadChildren: () => import('./features/judicial/judicial.module').then(m => m.JudicialModule)
  },
  {
    path: '',
    redirectTo: 'judicial',
    pathMatch: 'full'
  }
];
