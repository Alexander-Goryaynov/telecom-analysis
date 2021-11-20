import {Injectable} from '@angular/core';
import {apiUrl} from '../../environments/environment';
import {HttpClient} from '@angular/common/http';
import {FileBindingModel} from '../models/request/file-binding-model';
import {Observable} from 'rxjs';
import {AnalysisReportModel} from '../models/response/analysis-report-model';

@Injectable({
  providedIn: 'root'
})
export class AnalysisService {

  private fileUploadUrl = `${apiUrl}/upload`;

  constructor(private httpClient: HttpClient) {
  }

  getAnalysisResult(file: FileBindingModel): Observable<AnalysisReportModel> {
    return this.httpClient.post<AnalysisReportModel>(this.fileUploadUrl, file);
  }

}
