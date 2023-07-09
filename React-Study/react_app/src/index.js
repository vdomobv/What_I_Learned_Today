import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import reportWebVitals from './reportWebVitals';
import { BrowserRouter, Route, Switch, NavLink, useParams } from 'react-router-dom/cjs/react-router-dom.min';
import WithoutRedux from './components/without-redux';

function App() {
  return (
    <div>
      <h1>
        Hello React Router
      </h1>
      <ul>
        <li><NavLink exact to='/'>Home</NavLink></li>
        <li><NavLink to='/topics'>Topics</NavLink></li>
        <li><NavLink to='/withoutRedux'>withoutRedux</NavLink></li>
      </ul>
      <Switch>
        <Route exact path="/"><Home></Home></Route>
        <Route path="/topics"><Topics></Topics></Route>
        <Route path="/withoutRedux"><WithoutRedux></WithoutRedux></Route>
        <Route path="/">Not Found</Route>
      </Switch>
    </div>
  )
}

function Home() {
  return (
    <div>
      <h2>Home</h2>
      Home is ...
    </div>
  )
}

var contents = [
  { id: 1, title: 'HTML', description: "HTML is ..." },
  { id: 2, title: 'JS', description: "JS is ..." },
  { id: 3, title: 'REACT', description: "REACT is ..." },
]

function Topics() {
  var lis = [];
  for (const c of contents) {
    lis.push(
      <li key={c.id}><NavLink to={"/topics/" + c.id}>{c.title}</NavLink></li>
    )
  }

  return (
    <div>
      <h2>Topic</h2>
      <ul>
        {lis}
      </ul>
      <Switch>
        <Route path="/topics/:topic_id">
          <Topic></Topic>
        </Route>
      </Switch>
    </div>
  )
}

function Topic() {
  var params = useParams();
  var topic_id = params.topic_id;
  var selected_topic = {
    title: "Sorry",
    description: "Not Found"
  }
  for (const c of contents) {
    if (c.id === Number(topic_id)) {
      selected_topic = c
      break;
    }
  }
  return (
    <div>
      <h3>{selected_topic.title}</h3>
      {selected_topic.description}
    </div>
  )
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <BrowserRouter>
      <App />
    </BrowserRouter>
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
