import { Component, Input, OnInit } from '@angular/core';
import {FormBuilder, FormGroup} from '@angular/forms';
import { Case, Lawyer, Juror, Evidence } from '../../../../../generated';

@Component({
  selector: 'app-review',
  templateUrl: './review.component.html',
  styleUrls: ['./review.component.scss'],
  standalone: false
})
export class ReviewComponent implements OnInit {
  @Input() formGroup: FormGroup;

  caseData: Case | undefined;
  defenseLawyer: Lawyer | undefined;
  prosecutorLawyer: Lawyer | undefined;
  jurors: Juror[] = [];
  evidences: Evidence[] = [];

  predictionResult: string = '';
  isLoading: boolean = false;

  constructor(private fb: FormBuilder) {
    this.formGroup = this.fb.group({})

  }

  ngOnInit(): void {
    // Subscribe to form value changes to update the review
    this.formGroup.valueChanges.subscribe(formValue => {
      this.updateReviewData(formValue);
    });

    // Initial update
    this.updateReviewData(this.formGroup.value);
  }

  private updateReviewData(formValue: any): void {
    if (formValue) {
      // Extract data from the form
      this.caseData = formValue.caseCtrl?.case;
      this.defenseLawyer = formValue.lawyerCtrl?.defense;
      this.prosecutorLawyer = formValue.lawyerCtrl?.prosecutor;
      this.jurors = formValue.juryCtrl?.jurors || [];
      this.evidences = formValue.evidenceCtrl?.evidences || [];
    }
  }

  getPrediction(): void {
    this.isLoading = true;
    this.predictionResult = '';

    // Simulate API call for prediction
    setTimeout(() => {
      // Generate a random prediction result for demonstration
      const outcomes = [
        'Defendant found guilty with 85% probability',
        'Defendant found not guilty with 72% probability',
        'Case likely to be dismissed with 65% probability',
        'Hung jury predicted with 58% probability',
        'Settlement recommended with 90% probability'
      ];

      this.predictionResult = outcomes[Math.floor(Math.random() * outcomes.length)];
      this.isLoading = false;
    }, 2000);
  }
}
