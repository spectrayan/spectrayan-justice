import { Component, Input, OnInit } from '@angular/core';
import { FormArray, FormBuilder, FormGroup, Validators } from '@angular/forms';
import { HttpClient } from '@angular/common/http';
import {Evidence, EvidenceType} from '../../../../../generated';

@Component({
  selector: 'app-evidence',
  templateUrl: './evidence.component.html',
  styleUrls: ['./evidence.component.scss'],
  standalone: false
})
export class EvidenceComponent implements OnInit {
  @Input() formGroup: FormGroup;

  evidences: Evidence[] = [];
  evidenceTypes = Object.values(EvidenceType);
  selectedFiles: File[] = [];

  constructor(private http: HttpClient, private fb: FormBuilder) {
    this.formGroup = this.fb.group({}) as FormGroup
  }

  ngOnInit(): void {
    // Initialize the evidences form array if it doesn't exist
    if (!this.formGroup.get('evidenceCtrl')) {
      this.formGroup.addControl('evidenceCtrl', this.fb.group({
        evidences: this.fb.array([])
      }));
    }

    // Load sample evidence data
    this.http.get<Evidence[]>('assets/data/evidences.json').subscribe(
      data => {
        this.evidences = data;
      },
      error => {
        console.error('Error loading evidence data:', error);
      }
    );
  }

  get evidencesArray(): FormArray {
    return this.formGroup.get('evidenceCtrl.evidences') as FormArray;
  }

  // Helper method to get an evidence form as FormGroup (for type safety)
  getEvidenceFormGroup(index: number): FormGroup {
    return this.evidencesArray.at(index) as FormGroup;
  }

  addEvidence(): void {
    const evidenceForm = this.fb.group({
      title: ['', Validators.required],
      description: [''],
      evidenceType: ['', Validators.required],
      fileUrl: [''],
      credibilityLevel: [''],
      isAdmissible: [true]
    });

    this.evidencesArray.push(evidenceForm);
  }

  removeEvidence(index: number): void {
    this.evidencesArray.removeAt(index);
    this.selectedFiles.splice(index, 1);
  }

  onFileSelected(event: Event, index: number): void {
    const input = event.target as HTMLInputElement;
    if (input.files && input.files.length) {
      const file = input.files[0];
      this.selectedFiles[index] = file;

      // Update the form with the file name
      const evidenceForm = this.getEvidenceFormGroup(index);
      evidenceForm.patchValue({
        fileUrl: file.name
      });
    }
  }

  selectExistingEvidence(evidence: Evidence, index: number): void {
    // Update the form with the selected evidence's data
    const evidenceForm = this.getEvidenceFormGroup(index);
    evidenceForm.patchValue({
      description: evidence.description,
      evidenceType: evidence.type,
      fileUrl: evidence.filePaths,

    });
  }
}
