import { Component, OnInit } from '@angular/core';

import { Test } from '../test';
import { TestService } from '../test.service'
import { Question } from '../question'
import { Answer } from '../answer'
import { QuestionFormComponent } from '../question-form/question-form.component'

@Component({
  selector: 'app-test',
  templateUrl: './test.component.html',
  styleUrls: ['./test.component.css']
})
export class TestComponent implements OnInit {

  questions: Question[];
  test_list: Test[];
  test_id: Number;

  constructor(private testService: TestService) { }

  ngOnInit() {
    this.testService.getTestList().subscribe(test_list => this.test_list = test_list)
  }

  getTest(test_id): void {
    this.testService.getTest(test_id)
      .subscribe(questions => this.questions = questions)
  }

  onClickMe(test_id): void {
    this.test_id = test_id;
    this.getTest(test_id); 
  }

}