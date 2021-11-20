import {Component, OnInit, EventEmitter, Output, ViewChild} from '@angular/core';
import {SwalComponent} from '@sweetalert2/ngx-sweetalert2';

@Component({
  selector: 'app-file-upload',
  templateUrl: './file-upload.component.html',
  styleUrls: ['./file-upload.component.css']
})
export class FileUploadComponent implements OnInit {

  @Output()
  fileUpload = new EventEmitter<string>();
  @ViewChild('emptyFileInputSweetAlert')
  emptyFileInputSweetAlert: SwalComponent;

  constructor() { }

  ngOnInit(): void {
  }

  onBtnAnalyseClick(): void {
    const datasetFileInput = document.getElementById('dataset') as HTMLInputElement;
    if (datasetFileInput.files.length === 0) {
      this.emptyFileInputSweetAlert.fire();
      return;
    }
    const datasetFile: File = datasetFileInput.files[0];
    const fileReader: FileReader = new FileReader();
    fileReader.onloadend = (e: ProgressEvent<FileReader>) => {
      const datasetString = fileReader.result as string;
      this.fileUpload.emit(datasetString);
    };
    fileReader.readAsDataURL(datasetFile);
  }

}
