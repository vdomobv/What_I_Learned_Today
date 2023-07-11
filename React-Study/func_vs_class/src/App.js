import "./App.css";
import React, { useState, useEffect } from "react";

function App() {
  var [funcShow, setFuncShow ] = useState(true);

  return (
    <div className="container">
      <h1>Hello World</h1>
      <input type="button" value="remove func" onClick={function () {
        setFuncShow(false);
      }}></input>
      { funcShow ? <FuncComp initNumber={2}></FuncComp> : null}
      <ClassComp initNumber={2}></ClassComp>
    </div>
  );
}

var funcId = 0;
function FuncComp(props) {
  var numberState = useState(props.initNumber);
  var number = numberState[0];
  var setNumber = numberState[1];
  
  var [ _date, setDate] = useState((new Date()).toString());

  useEffect(function () {
    console.log('%cfunc ==> useEffect number (compononetDidMount)' + (++funcId), "color:blue")
    document.title = number + ' : ' + _date
    return function(){
      console.log('%cfunc => useEffect number return (componentWillUnMount)' + (++funcId), "color:blue")
    }
  }, [])

  useEffect(function () {
    console.log('%cfunc ==> useEffect number (compononetDidMount & componentDidUpdate)' + (++funcId), "color:blue")
    document.title = number + ' : ' + _date
    return function(){
      console.log('%cfunc => useEffect number return (compononetDidMount & componentDidUpdate)' + (++funcId), "color:blue")
    }
  }, [number])

  // useEffect(function () {
  //   console.log('%cfunc ==> useEffect date (compononetDidMount & componentDidUpdate)' + (++funcId), "color:blue")
  //   document.title =  _date
  //   return function(){
  //     console.log('%cfunc => useEffect date return (compononetDidMount & componentDidUpdate)' + (++funcId), "color:blue")
  //   }
  // }, [_date])

  console.log('%cfunc ==> render' + (++funcId), "color:blue")
  return (
    <div className="container">
      <h2>function style component</h2>
      <p>Number : {number}</p>
      <p>Date : { _date }</p>
      <input
        type="button"
        value="random"
        onClick={function () {
          setNumber(Math.random());
        }}
      ></input>
      <input
        type="button"
        value="date"
        onClick={function () {
          setDate((new Date()).toString())
        }}
      ></input>
    </div>
  );
}

class ClassComp extends React.Component {
  state = {
    number: this.props.initNumber,
    date : (new Date()).toString()
  };

  // componentWillMount(){
  //   console.log('%cclass ==> componentWillMount', 'color:red')
  // }
  
  componentDidMount(){
    console.log('%cclass ==> componentDidMount', 'color:red')
  }

  shouldComponentUpdate(nextPrps, nextState) {
    console.log('%cclass ==> shouldComponentUpdate', 'color:red')
    return true;
  }

  // componentWillUpdate(nextProps, nextState){
  //   console.log('%cclass ==> componentWillUpdate', 'color:red')
  // }

  componentDidUpdate(nextProps, nextState){
    console.log('%cclass ==> componentDidUpdate', 'color:red')
  }

  render() {
    console.log('%cclass ==> render', 'color:red')
    return (
      <div className="container">
        <h2>class style component</h2>
        <p>Number : {this.state.number}</p>
        <p>Date : {this.state.date}</p>
        <input
          type="button"
          value="random"
          onClick={function () {
            this.setState({ number: Math.random() });
          }.bind(this)}
        ></input>
        <input
          type="button"
          value="date"
          onClick={function () {
            this.setState({ date: (new Date()).toString() });
          }.bind(this)}
        ></input>
      </div>
    );
  }
}
export default App;
