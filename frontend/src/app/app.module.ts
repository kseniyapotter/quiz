import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';


import { AppComponent } from './app.component';
import { TestComponent } from './test/test.component';
import { AnswerComponent } from './answer/answer.component';
import { TestService } from './test.service';
import { AppRoutingModule } from './app-routing.module';
import { QuestionFormComponent } from './question-form/question-form.component'

@NgModule({
  declarations: [
    AppComponent,
    TestComponent,
    AnswerComponent,
    QuestionFormComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    AppRoutingModule,
    HttpClientModule
  ],
  providers: [TestService],
  bootstrap: [AppComponent]
})
export class AppModule { }
