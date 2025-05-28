import { Component, Input, OnInit } from '@angular/core';
import {FormBuilder, FormGroup} from '@angular/forms';
import { Case, CaseType, CaseStatus } from '../../../../../generated';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-case-info',
  templateUrl: './case-info.component.html',
  styleUrls: ['./case-info.component.scss'],
  standalone: false
})
export class CaseInfoComponent implements OnInit {
  @Input() formGroup: FormGroup ;

  caseTypes: CaseType[] = Object.values(CaseType);
  caseStatuses: CaseStatus[] = Object.values(CaseStatus);
  cases: Case[] = [];

  constructor(private http: HttpClient, private fb: FormBuilder) {
    this.formGroup = this.fb.group({}) as FormGroup
  }

  ngOnInit(): void {
    // Load sample case data
    this.http.get<Case[]>('assets/data/cases.json').subscribe(
      data => {
        this.cases = data;
      },
      error => {
        console.error('Error loading case data:', error);
      }
    );
  }
}
