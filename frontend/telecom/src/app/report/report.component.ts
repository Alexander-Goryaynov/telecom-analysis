import {Component, OnInit, Output, EventEmitter, Input} from '@angular/core';
import {Label} from 'ng2-charts';
import {ChartDataSets, ChartOptions} from 'chart.js';
import {AnalysisReportModel} from '../models/response/analysis-report-model';

@Component({
  selector: 'app-report',
  templateUrl: './report.component.html',
  styleUrls: ['./report.component.css']
})
export class ReportComponent implements OnInit {

  countByCountryLabels: Label[] = [''];
  countByCountryDataset: ChartDataSets[] = [];
  histogramOptions: ChartOptions = {
    responsive: true,
    title: {
      text: 'Кол-во поставщиков по странам',
      display: true,
      fontSize: 26
    },
    scales: {
      yAxes: [{
        ticks: {
          suggestedMin: 0
        }
      }]
    }
  };
  capByCountryLabels: Label[] = [];
  capByCountryDataset: number[] = [];
  pieChartOptions: ChartOptions = {
    title: {
      fontSize: 26,
      display: true,
      text: 'Суммарная капитализация поставщиков по странам'
    }
  };
  analysisResult: AnalysisReportModel;
  @Output()
  requestNewAnalysis = new EventEmitter<void>();

  constructor() {
  }

  ngOnInit(): void {
  }

  onNewAnalysisBtnClick(): void {
    this.requestNewAnalysis.emit();
  }

  refresh(): void {
    if (this.analysisResult !== undefined) {
      this.refreshHistogram();
      this.refreshPieChart();
    }
  }

  private refreshHistogram(): void {
    this.countByCountryDataset = [];
    for (const countryInfo of this.analysisResult.companiesCountByCountry) {
      this.countByCountryDataset.push({
        data: [countryInfo.companiesCount],
        label: countryInfo.countryName
      });
    }
    this.setHistogramYAxisMinValue();
  }

  private refreshPieChart(): void {
    this.capByCountryDataset = [];
    this.capByCountryLabels = [];
    for (const i of this.analysisResult.totalCapByCountry) {
      this.capByCountryLabels.push(i.countryName);
      this.capByCountryDataset.push(this.roundMoney(i.totalCap));
    }
  }

  private setHistogramYAxisMinValue(): void {
    let minCount = this.analysisResult.companiesCountByCountry[0].companiesCount;
    for (const i of this.analysisResult.companiesCountByCountry) {
      if (i.companiesCount < minCount) {
        minCount = i.companiesCount;
      }
    }
    minCount -= 1;
    this.histogramOptions.scales.yAxes[0].ticks.suggestedMin = minCount;
  }

  private roundMoney(value: number): number {
    return Number(value.toFixed(2));
  }

}
