import React, { Component } from "react";


class WithRedux extends Component {
  red() {
    return (
      <div className="container" id="component_red">
        <h1>Red</h1>
        <input type="button" value="fire"></input>
      </div>

    );
  }

  render() {
    return (
      <div>
        <div id="red">
          <div className="container" id="component_red">
            <h1>red</h1>
            <input type="button" value="fire"></input>
          </div>
        </div>
        <div id="green">
          <div className="container" id="component_green">
            <h1>green</h1>
            <input type="button" value="fire"></input>
          </div>
        </div>
        <div id="blue">
          <div className="container" id="component_blue">
            <h1>blue</h1>
            <input type="button" value="fire"></input>
          </div>
        </div>
      </div>
    );
  }
}

export default WithRedux;