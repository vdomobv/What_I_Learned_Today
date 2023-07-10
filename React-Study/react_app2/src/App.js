import "./App.css";
import React, { useState, useEffect } from "react";

function App() {
  return (
    <div className="container">
      <h1>Hello World</h1>
      <FuncComp initNumber={2}></FuncComp>
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
    console.log('%cfunc ==> useEffect (compononetDidMount & componentDidUpdate)' + (++funcId), "color:blue")
    document.title = number + ' : ' + _date
  })

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
