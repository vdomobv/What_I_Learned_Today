import React, { Component } from "react";

class WithoutRedux extends Component {

  red() {
    const fire = function () {
      document.querySelector("#component_red").style.backgroundColor = "red"
      document.querySelector("#component_green").style.backgroundColor = "red"
      document.querySelector("#component_blue").style.backgroundColor = "red"
    }
    
    return (
      <div className="container" id="component_red">
        <h1>Red</h1>
        <input type="button" value="fire" onClick={fire}></input>
      </div>
      
      );
    }
    
    green() {
      const fire = function () {
        document.querySelector("#component_red").style.backgroundColor = "green"
        document.querySelector("#component_green").style.backgroundColor = "green"
        document.querySelector("#component_blue").style.backgroundColor = "green"
    }

    return (
      <div className="container" id="component_green">
        <h1>green</h1>
        <input type="button" value="fire" onClick={fire}></input>
      </div>
    );
  }

  blue() {
    const fire = function () {
      document.querySelector("#component_red").style.backgroundColor = "blue"
      document.querySelector("#component_green").style.backgroundColor = "blue"
      document.querySelector("#component_blue").style.backgroundColor = "blue"
    }

    return (
      <div className="container" id="component_blue">
        <h1>green</h1>
        <input type="button" value="fire" onClick={fire}></input>
      </div>
    );
  }
  render() {
    return (
      <div>
        <div id="red"></div>
        <div id="green"></div>
        <div id="blue"></div>
        {this.red()}
        {this.green()}
        {this.blue()}
      </div>
    );
  }
}

export default WithoutRedux;