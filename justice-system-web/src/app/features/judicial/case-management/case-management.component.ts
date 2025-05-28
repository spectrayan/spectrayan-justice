import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-case-management',
  templateUrl: './case-management.component.html',
  styleUrls: ['./case-management.component.scss'],
  standalone: false
})
export class CaseManagementComponent implements OnInit {
  displayedColumns: string[] = ['caseNumber', 'title', 'type', 'status', 'date', 'actions'];

  // Sample data for demonstration
  cases = [
    { caseNumber: 'JC-2023-001', title: 'State vs. Smith', type: 'Criminal', status: 'Active', date: '2023-05-15' },
    { caseNumber: 'JC-2023-002', title: 'Johnson vs. City', type: 'Civil', status: 'Pending', date: '2023-06-20' },
    { caseNumber: 'JC-2023-003', title: 'Family Matter - Jones', type: 'Family', status: 'Closed', date: '2023-04-10' },
    { caseNumber: 'JC-2023-004', title: 'Property Dispute - Brown', type: 'Civil', status: 'Active', date: '2023-07-05' },
    { caseNumber: 'JC-2023-005', title: 'State vs. Williams', type: 'Criminal', status: 'Active', date: '2023-05-22' }
  ];

  constructor() { }

  ngOnInit(): void {
  }

  viewCase(caseNumber: string): void {
    console.log(`Viewing case: ${caseNumber}`);
    // Navigate to case details page
  }

  editCase(caseNumber: string): void {
    console.log(`Editing case: ${caseNumber}`);
    // Navigate to case edit page
  }
}
