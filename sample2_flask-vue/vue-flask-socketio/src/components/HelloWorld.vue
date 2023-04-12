<template>
    <div>
      <div class="container">
          <!-- <img src="../../assets/images/logo-icon.svg" alt="" class="mt-1"> -->
          <div class="text">Cloud Removal of Remote Sensing Image</div>
      </div>
      <div class="content">
          <div class="img-body">
              <el-upload ref="upload" class="mt-upload" action="http://127.0.0.1:5002/upload_image"
                  :on-change="handlePictureCardPreview"  :on-success="handleAvatarSuccess"
                  :show-file-list="false" list-type="picture">
                  <img :src="imgUrl" class="img-upload">
              </el-upload>
              <div>
                  <img :src="imgUrl2" class="img-upload">
              </div>
              </div>
          </div>
          <span slot="footer" class="dialog-footer">
              <el-button type="primary" @click="submitUpload">上传</el-button>
              <el-button @click="dialogVisible = false">取 消</el-button>
          </span>
        </div>
</template>



<script>
// import io from 'socket.io-client'
export default {
  data() {
      return {
          dialogVisible: false,
          fileList: [],
          imgUrl: '/uploadBg.png',
          imgUrl2: '/uploadBg.png',
      };
  },
  create() {
  },
  methods: {
      // 文件改变时勾子函数
      handlePictureCardPreview(file, fileList) {
          this.fileList = fileList
          this.imgUrl = file.url;
      },
      // 上传成功接受回传
      handleAvatarSuccess(response, file, fileList) {
          console.log(response);
          console.log(file);
          console.log(fileList);
      },
      // 点击上传
      submitUpload() {
          if (this.fileList.length > 0) {
              this.$refs.upload.submit();
          } else {
              this.$message.error("请选择文件");
          }
      },
  },
};
</script>

<style lang="less" scoped>
.el-dialog {
  background-color: rgb(240, 226, 202);
}
.el-dialog__header {
  padding: 0;
}

.container {
  .mt-1 {
      position: relative;
      left: 50%;
      transform: translate(-50%);
      width: 50px;
      height: 50px;
  }

  .text {
      text-align: center;
      font-family: 'Courier New', Courier, monospace;
      font-size: 30px;
      font-weight: 400;
  }
}

;

.content {
  .img-body {
      position: relative;
      border: 1px dashed #d9d9d9;
      border-radius: 6px;
      text-align: center;
      display: flex;
      align-items: center;
      justify-content: center;

      // margin-top: 20px;
      .img-upload {
          width: 300px;
          height: 300px;
          margin: 0 20px;
          border: 1px dashed #a77474;
      }

      .mt-upload {
          overflow: hidden;

          .avatar-uploader-icon {
              text-align: center;
              z-index: 100;
              font-size: 300px;
              color: #8c939d;
          }

          .upload__tip {
              font-size: 12px;
              text-align: center;
              z-index: 10;
          }


          .mt-upload:hover {
              border-color: #C80505;
              color: #C80505;

              .avatar-uploader-icon {
                  color: #C80505;
              }
          }


      }
  }
}
</style>