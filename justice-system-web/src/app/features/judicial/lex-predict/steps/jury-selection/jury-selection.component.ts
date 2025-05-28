import { Component, Input, OnInit } from '@angular/core';
import { FormArray, FormBuilder, FormGroup, Validators } from '@angular/forms';
import {
  Juror,
  Identity,
  Personality,
  PhysicalTraits,
  EmotionalIntelligence,
  SocialBehavior,
  Disability,
  getIdentityForm,
  getPersonalityForm,
  getPhysicalTraitsForm,
  getEmotionalIntelligenceForm,
  getSocialBehaviorForm,
  getDisabilityForm, JurorFormType, getJurorForm
} from '../../../../../generated';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-jury-selection',
  templateUrl: './jury-selection.component.html',
  styleUrls: ['./jury-selection.component.scss'],
  standalone: false
})
export class JurySelectionComponent implements OnInit {
  @Input() formGroup!: FormGroup;

  jurors: Juror[] = [];
  selectedJurors: Juror[] = [];

  constructor(private http: HttpClient, private fb: FormBuilder) {
    // FormGroup will be provided by parent component via @Input
  }

  ngOnInit(): void {
    // Initialize the jurors form array if it doesn't exist
    const juryCtrl = this.formGroup.get('juryCtrl');
    if (!juryCtrl) {
      this.formGroup.setControl('juryCtrl', this.fb.group({
        jurors: this.fb.array([])
      }));
    } else if (!juryCtrl.get('jurors')) {
      // Check if juryCtrl is a FormGroup before calling setControl
      if (juryCtrl instanceof FormGroup) {
        juryCtrl.setControl('jurors', this.fb.array([]));
      } else {
        // If juryCtrl is not a FormGroup, recreate it properly
        this.formGroup.setControl('juryCtrl', this.fb.group({
          jurors: this.fb.array([])
        }));
      }
    }

    // Load sample juror data
    this.http.get<Juror[]>('assets/data/jurors.json').subscribe(
      data => {
        this.jurors = data;
      },
      error => {
        console.error('Error loading juror data:', error);
      }
    );
  }

  get jurorsArray(): FormArray<JurorFormType> {
    return this.formGroup.get('juryCtrl')?.get('jurors') as FormArray || null;
  }

  // Helper method to get a juror form as FormGroup (for type safety)
  getJurorFormGroup(index: number): JurorFormType {
    return this.jurorsArray?.at(index);
  }

  addJuror(): void {
    const jurorForm: JurorFormType = getJurorForm();

    // Initialize jurors array if it doesn't exist
    if (!this.jurorsArray) {
      const juryCtrl = this.formGroup.get('juryCtrl');
      if (!juryCtrl) {
        this.formGroup.setControl('juryCtrl', this.fb.group({
          jurors: this.fb.array([jurorForm])
        }));
      } else {
        // Check if juryCtrl is a FormGroup before calling setControl
        if (juryCtrl instanceof FormGroup) {
          juryCtrl.setControl('jurors', this.fb.array([jurorForm]));
        } else {
          // If juryCtrl is not a FormGroup, recreate it properly
          this.formGroup.setControl('juryCtrl', this.fb.group({
            jurors: this.fb.array([jurorForm])
          }));
        }
      }
    } else {
      this.jurorsArray.push(jurorForm);
    }
  }

  removeJuror(index: number): void {
    if (this.jurorsArray) {
      this.jurorsArray.removeAt(index);
    }
  }

  selectExistingJuror(juror: Juror, index: number): void {
    // Update the form with the selected juror's data
    const jurorForm = this.getJurorFormGroup(index);
    if (jurorForm) {
      jurorForm.patchValue({
        identity: juror.identity,
        personality: juror.personality,
        physicalTraits: juror.physicalTraits,
        emotionalIntelligence: juror.emotionalIntelligence,
        socialBehavior: juror.socialBehavior,
        disability: juror.disability
      });

      this.selectedJurors[index] = juror;
    }
  }
}
