import {CompanyResultModel} from './company-result-model';

export class AnalysisReportModel {
  marketCap: {
    max: CompanyResultModel;
    min: CompanyResultModel;
    median: CompanyResultModel;
    avg: number
  };
  stockPrice: {
    max: CompanyResultModel;
    min: CompanyResultModel;
    median: CompanyResultModel;
    avg: number
  };
  dailyLossGain: {
    gain: {
      max: CompanyResultModel;
      avg: number;
    };
    loss: {
      max: CompanyResultModel;
      avg: number;
    }
  };
  totalCapByCountry: {countryName: string; totalCap: number}[];
  companiesCountByCountry: {countryName: string; companiesCount: number}[];
}
