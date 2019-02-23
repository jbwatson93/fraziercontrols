import React, { Component } from 'react';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom'
import ProjectList from './components/ProjectList'
import Homepage from './components/Homepage'
import SingleProject from './components/SingleProject'
import Newproject from './components/Newproject'

class App extends Component {
  render() {
    return (
      <Router>
      <div>
        
        <Switch>
          <Route exact path="/" component={Homepage}/>
          <Route exact path="/projects/" component={ProjectList}/>
          <Route exact path="/projects/:id" component={SingleProject}/>
          <Route exact path="/newproject" component={Newproject}/>
        </Switch>
      </div>
    </Router>
    );
  }
}

export default App;
