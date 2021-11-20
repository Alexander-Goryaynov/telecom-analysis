import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { AnalysisComponent } from './analysis/analysis.component';
import { FileUploadComponent } from './file-upload/file-upload.component';
import { ReportComponent } from './report/report.component';
import { ChartsModule } from 'ng2-charts';
import {SweetAlert2Module} from '@sweetalert2/ngx-sweetalert2';
import {HttpClientModule} from '@angular/common/http';

@NgModule({
  declarations: [
    AppComponent,
    AnalysisComponent,
    FileUploadComponent,
    ReportComponent
  ],
    imports: [
        BrowserModule,
        AppRoutingModule,
        ChartsModule,
        HttpClientModule,
        SweetAlert2Module.forRoot()
    ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
