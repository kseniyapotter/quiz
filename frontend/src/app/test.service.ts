import { Injectable } from '@angular/core';
import { Observable } from 'rxjs/Observable';
import { HttpClient, HttpHeaders } from '@angular/common/http';

import { Test } from './test';
import { Question } from './question';
import { Result } from './result';

@Injectable()
export class TestService {

  // URLs to web api 
  private test_list_url = 'http://localhost:8000/api/tests';  
  private test_url = 'http://localhost:8000/api/';
  private put_url = 'http://localhost:8000/api/result/';

  private questions: Question[];
  private test_list: Test[];

  private httpOptions = {
    headers: new HttpHeaders({
      'Content-Type':  'application/json',
    })
  }

  constructor(private http: HttpClient) { }

  /** GET: get the test with id=test_id from the server. */
  getTest(test_id): Observable<Question[]> {
    return this.http.get<Question[]>(this.test_url + test_id + '/?format=json');
  }

  /** GET: get the test list from the server. */
  getTestList(): Observable<Test[]> {
    return this.http.get<Test[]>(this.test_list_url)
  }


  /** PUT: put the test on the server. Returns the result. */
  sendTest(test_id, questions: Question[]): Observable<Result> {  
    return this.http.put<Result>(this.put_url + test_id + '/', questions, this.httpOptions);
  }

}

