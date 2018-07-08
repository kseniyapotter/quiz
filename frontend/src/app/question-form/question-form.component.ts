import { Component, OnChanges, OnDestroy, Input } from '@angular/core';
import { FormControl } from '@angular/forms';

import { Question } from '../question'
import { Answer } from '../answer'
import { Result } from '../result'
import { TestService } from '../test.service'


@Component({
  selector: 'app-question-form',
  templateUrl: './question-form.component.html',
  styleUrls: ['./question-form.component.css']
})
export class QuestionFormComponent implements OnChanges, OnDestroy { 

  @Input() questions: Question[];
  @Input() test_id: Number;
  keys: string[]; 
  question: Question; 
  result: Result;
  //for timer
  intervalId = 0;
  seconds = 0;
  timer_message = '';
  
  constructor(private testService: TestService) { }

  ngOnChanges(changes) {
    //first question
    if (this.questions != null && this.question == null) {
      this.keys = Object.keys(this.questions); 
      this.question = this.questions[this.keys.shift()]; 
      this.start(); //start timer
    } 
  }

  start() { 
    this.seconds = this.question.time_second;
    this.countDown(); 
  }

  clearTimer() { clearInterval(this.intervalId); }

  private countDown() {
    this.clearTimer();
    this.intervalId = window.setInterval(() => {
      this.seconds -= 1;
      if (this.seconds === 0) {
        let answer_keys = Object.keys(this.question.answers);
        // set false answers on current question becouse time is over
        for (let i=0; i<answer_keys.length; i++) {
          this.question.answers[answer_keys[i]].correct = false;
        }
        this.onSubmit();
        this.timer_message = 'Time is over';
      } 
    }, 1000);
  }

  onSubmit() { 
    this.clearTimer(); 
    let keys_answers = Object.keys(this.question.answers);
    
    if (this.keys.length) {
      //next question
      this.question = this.questions[this.keys.shift()];
      this.seconds = this.question.time_second;
      this.countDown();
    } else {
      this.sendTest();
      this.question = null;
      this.questions = null;
    }
  }

  sendTest(): void {
    this.testService.sendTest(this.test_id, this.questions)
      .subscribe(result => this.result = result);
  }

  ngOnDestroy() { 
    this.clearTimer(); 
    this.question = null;
    this.questions = null;
  }

}
