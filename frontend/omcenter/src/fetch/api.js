import axios from 'axios'
import sha1 from 'sha1'
import {store} from '../store'
import router from '../router'
// axios 配置
axios.defaults.timeout = 3000;
axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded;charset=UTF-8';
axios.defaults.baseURL = '/ams';

//POST传参序列化
axios.interceptors.request.use((config) => {
  if(config.url==="/ams/account/preWithDraw.do"){
//
  } else {
    store.$emit('showLoading', true);
  }
  if (config.method === 'post') {
    config.headers.token = localStorage.token;
    //
  }
  return config;
}, (error) => {
  return Promise.reject(error);
});

//返回状态判断
axios.interceptors.response.use((res) => {
  store.$emit('showLoading', false);
  if (!res.data.status) {
    return Promise.reject(res);
  }
  return res;
}, (res) => {
  store.$emit('showLoading', false);
  if (res.response.data.status === 120) {
    localStorage.username = '';
    localStorage.token = "";
    router.replace({
      path: 'login',
      query: {redirect: router.currentRoute.fullPath}
    });
    return Promise.reject(res.response.data.message);
  } else {
    return Promise.reject(res.message);
  }
});

export function fetch(url, params) {
  return new Promise((resolve, reject) => {
    axios.post(url, params)
      .then(response => {
        resolve(response.data);
      }, err => {
        reject(err);
      })
      .catch((error) => {
        reject(error)
      })
  })
}

export function get(url, params) {
  return new Promise((resolve, reject) => {
    axios.get(url, params)
      .then(response => {
        resolve(response.data);
      }, err => {
        reject(err);
      })
      .catch((error) => {
        reject(error)
      })
  })
}

//参数签名
export function toSHA1(param) {
  let array = [];
  for (let key in param) {
    array.push(key);
  }
  array.sort();

  // 拼接有序的参数名-值串
  let paramArray = [];
  for (let index in array) {
    let key = array[index];
    paramArray.push(key + param[key]);
  }

  let shaSource = paramArray.join("");
  return sha1(shaSource).toUpperCase();
}

export default {
  DateFormat(date) {
    const tmpDate = new Date();
    tmpDate.setTime(date);
    return tmpDate.getFullYear() + "-" + (tmpDate.getMonth() + 1) + "-" + tmpDate.getDate();
  },
  Login(params) {
    // params.sign = toSHA1(params.param);
    return fetch('login/login.do', params)
  },
  Logout(params) {
    return fetch('login/logout.do', params)
  },
  Register(params) {
    // params.sign = toSHA1(params.param);
    return fetch('login/doRegister.do', params)
  },
  GetVerificationCode() {
    return get('login/captcha.do', '')
  },
  Test(params) {
    params.sign = toSHA1(params.param);
    return fetch('test/sign.do', params)
  },
  QueryIdentity(params) {
    return fetch('companyBackstage/queryIdentity.do', params)
  },
  GetRoles() {
    return fetch('companyBackstage/getRoles.do', '')
  },
  SetProxy(params) {
    return fetch('agent/accredit.do', params)
  },
  GetProxy(params) {
    return fetch('userInfo/agentUser.do', params)
  },
  ModifyPassword(params) {
    return fetch('agentBackstage/modifyPassword.do', params)
  },
  GetIncome(params) {
    return fetch('agentBackstage/getIncome.do', params)
  },
  GetPayment(params) {
    return fetch('agentBackstage/getPayment.do', params)
  },
  GetNoSettlement(params) {
    return fetch('agentBackstage/getNoSettlement.do', params)
  },
  GetWithdrawLog(params) {
    return fetch('agentBackstage/getWithdrawLog.do', params)
  },
  QueryRelation(params) {
    return fetch('agentBackstage/queryRelation.do', params)
  },
  GetMyPlayers(params) {
    return fetch('agent/myPlayers.do', params)
  },
  GetMyPlayersTotal(params) {
    return fetch('agent/myPlayersTotal.do', params)
  },
  GetIncomeChart(params) {
    return fetch('agentBackstage/getIncomeChart.do', params)
  },
  GetPaymentChart(params) {
    return fetch('agentBackstage/getPaymentChart.do', params)
  },
  TodayIndex(params) {
    return fetch('agentBackstage/todayIndex.do', params)
  },
  Pay(params) {
    return fetch('account/pay.do', params)
  },
  PayState(params) {
    return fetch('account/payState.do', params)
  },
  GetUserInfo(params) {
    return fetch('companyBackstage/userInfo.do', params)
  },
  SelectAgentDirectPlayerPayment(params) {
    return fetch('agentBackstage/selectAgentDirectPlayerPayment.do', params)
  },
  MyAgentTotal(params) {
    return fetch('agent/myAgentTotal.do', params)
  },
  QueryHehuorenRechargeTotal(params) {
    return fetch('agent/queryHehuorenRechargeTotal.do ', params)
  },
  QueryTuijianRechargeTotal(params) {
    return fetch('agent/queryTuijianRechargeTotal.do ', params)
  },
  QueryHehuorenRecharge(params) {
    return fetch('agent/queryHehuorenRecharge.do', params)
  },
  QueryTuijianrenRecharge(params) {
    return fetch('agent/queryTuijianrenRecharge.do', params)
  },
  GetMyCard(params) {
    return fetch('agent/myCard.do', params)
  },
  QueryContCards(params) {
    return fetch('agent/queryContCards.do', params)
  },
  GetMyAgents(params) {
    return fetch('agent/myAgents.do', params)
  },
  preWithDraw(params) {
    return fetch('account/preWithDraw.do', params)
  },
  withDraw(params) {
    return fetch('account/withDraw.do', params)
  },
  mcode(params) {
    return fetch('login/mcode.do', params)
  },
  GetAuthCode(params) {
    return fetch('account/authCode.do', params)
  }
}
