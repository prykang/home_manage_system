const envConfig = {
  dev: {
    //  apiPrefix: 'http://10.40.20.62:8080'
    // apiPrefix: 'http://localhost:8000'
    // apiPrefix: 'http://10.14.8.172:8000'
    // apiPrefix: 'http://192.168.199.102:8000'
    apiPrefix: 'http://10.14.9.127:8000'
    // apiPrefix: 'http://192.168.199.102:8000'
  },
  prod: {
    // apiPrefix: 'http://llcs-manage-api-tran.ql.corp:8081'
    apiPrefix: 'http://10.40.20.62:8080'
  }
};

const curEnvConfig = envConfig[process.env.ENV];

export default curEnvConfig;
