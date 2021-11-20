import {Component, OnInit, ViewChild} from '@angular/core';
import {SwalComponent} from '@sweetalert2/ngx-sweetalert2';
import {AnalysisService} from '../services/analysis.service';
import {FileBindingModel} from '../models/request/file-binding-model';
import {AnalysisReportModel} from '../models/response/analysis-report-model';
import {ReportComponent} from '../report/report.component';

@Component({
  selector: 'app-analysis',
  templateUrl: './analysis.component.html',
  styleUrls: ['./analysis.component.css']
})
export class AnalysisComponent implements OnInit {

  isFileUploadHidden = false;
  isReportHidden = true;
  @ViewChild('serverErrorSweetAlert')
  serverErrorSweetAlert: SwalComponent;
  @ViewChild(ReportComponent)
  reportComponent: ReportComponent;

  constructor(private analysisService: AnalysisService) { }

  ngOnInit(): void {
  }

  onFileUpload(content: string): void {
    this.analysisService
      .getAnalysisResult(new FileBindingModel(content))
      .subscribe(
        (data: AnalysisReportModel) => {
          this.isFileUploadHidden = true;
          this.isReportHidden = false;
          this.reportComponent.analysisResult = data;
          this.reportComponent.refresh();
        },
        (error: any) => this.serverErrorSweetAlert.fire()
      );
  }

  onNewAnalysisRequest(): void {
    this.isReportHidden = true;
    this.isFileUploadHidden = false;
  }

}
