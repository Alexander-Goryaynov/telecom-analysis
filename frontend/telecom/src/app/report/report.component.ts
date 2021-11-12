import {Component, OnInit} from '@angular/core';
import {Label} from 'ng2-charts';
import {ChartDataSets, ChartOptions} from 'chart.js';

@Component({
  selector: 'app-report',
  templateUrl: './report.component.html',
  styleUrls: ['./report.component.css']
})
export class ReportComponent implements OnInit {

  public countByCountryLabels: Label[] = [''];
  public countByCountryDataset: ChartDataSets[] = [
    {data: [65], label: 'USA'},
    {data: [59], label: 'Germany'},
    {data: [80], label: 'France'},
    {data: [81], label: 'Russia'},
    {data: [56], label: 'Sweden'},
    {data: [55], label: 'UK'},
    {data: [40], label: 'Japan'},
    {data: [53], label: 'Italy'},
  ];
  public histogramOptions: ChartOptions = {
    responsive: true,
    title: {
      text: 'Кол-во поставщиков по странам',
      display: true,
      fontSize: 26
    },
    scales: {
      yAxes: [{
        ticks: {
          suggestedMin: 0   // TODO устанавливать при получении датасета
        }
      }]
    }
  };
  public capByCountryLabels: Label[] = ['USA', 'Germany', 'France', 'Russia', 'Sweden', 'UK', 'Japan', 'Italy'];
  public capByCountryDataset: number[] = [65.50, 59.40, 80.10, 81.60, 56.80, 55.70, 40.40, 53.00];
  public pieChartOptions: ChartOptions = {
    title: {
      fontSize: 26,
      display: true,
      text: 'Суммарная капитализация поставщиков по странам'
    }
  };

  constructor() {
  }

  ngOnInit(): void {
  }

}
