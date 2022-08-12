export class ApiResponse {
  status: string | undefined
  error: string | undefined
  data: any | undefined
}

class BaseObject {
  id: number | undefined
  name: string

  constructor(name: string) {
    this.name = name;
  }
}

export class Place extends BaseObject {
  available_times: string[]

  constructor(name: string, available_times:string[]) {
    super(name);
    this.available_times = available_times

  }
}

export class Team extends BaseObject {
  
}
