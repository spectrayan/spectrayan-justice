import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { MatStepper } from '@angular/material/stepper';

@Component({
  selector: 'app-lex-predict',
  templateUrl: './lex-predict.component.html',
  styleUrls: ['./lex-predict.component.scss'],
  standalone: false
})
export class LexPredictComponent implements OnInit {
  caseFormGroup: FormGroup;
  lawyerFormGroup: FormGroup;
  juryFormGroup: FormGroup;
  evidenceFormGroup: FormGroup;
  reviewFormGroup: FormGroup;

  isLinear = true;

  constructor(private _formBuilder: FormBuilder) {
    this.caseFormGroup = this._formBuilder.group({})
    this.lawyerFormGroup = this._formBuilder.group({})
    this.juryFormGroup = this._formBuilder.group({})
    this.evidenceFormGroup = this._formBuilder.group({})
    this.reviewFormGroup = this._formBuilder.group({})
  }

  ngOnInit(): void {
    this.caseFormGroup = this._formBuilder.group({
      caseCtrl: ['', Validators.required]
    });

    this.lawyerFormGroup = this._formBuilder.group({
      defenseCtrl: ['', Validators.required],
      prosecutorCtrl: ['', Validators.required]
    });

    this.juryFormGroup = this._formBuilder.group({
      juryCtrl: ['', Validators.required]
    });

    this.evidenceFormGroup = this._formBuilder.group({
      evidenceCtrl: ['', Validators.required]
    });

    this.reviewFormGroup = this._formBuilder.group({
      reviewCtrl: ['', Validators.required]
    });
  }

  submitPrediction(): void {
    console.log('Prediction submitted');
    // Here we would submit the data to the backend for prediction
  }
}
