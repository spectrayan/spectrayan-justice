import { Component, Input, OnInit } from '@angular/core';
import {FormBuilder, FormGroup} from '@angular/forms';
import { HttpClient } from '@angular/common/http';
import {Lawyer, LawyerType} from '../../../../../generated';

@Component({
  selector: 'app-lawyer-selection',
  templateUrl: './lawyer-selection.component.html',
  styleUrls: ['./lawyer-selection.component.scss'],
  standalone: false
})
export class LawyerSelectionComponent implements OnInit {
  @Input() formGroup: FormGroup ;

  lawyers: Lawyer[] = [];
  defenseLawyers: Lawyer[] = [];
  prosecutorLawyers: Lawyer[] = [];

  constructor(private http: HttpClient, private fb: FormBuilder) {
    this.formGroup = this.fb.group({}) as FormGroup
  }

  ngOnInit(): void {
    // Load sample lawyer data
    this.http.get<Lawyer[]>('assets/data/lawyers.json').subscribe(
      data => {
        this.lawyers = data;
        // Filter lawyers by type
        this.defenseLawyers = this.lawyers.filter(lawyer =>
          lawyer.type === LawyerType.Defense ||
          lawyer.type === LawyerType.Defense
        );
        this.prosecutorLawyers = this.lawyers.filter(lawyer =>
          lawyer.type === LawyerType.Prosecutor ||
          lawyer.type === LawyerType.Prosecutor
        );
      },
      error => {
        console.error('Error loading lawyer data:', error);
      }
    );
  }
}
