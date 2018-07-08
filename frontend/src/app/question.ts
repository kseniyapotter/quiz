import { Answer } from './answer'

export class Question {

	constructor(
	  public id: number,
	  public name: string,
	  public text: string,
	  public time_second: number,
	  public answers: Answer[]
	) {}
}