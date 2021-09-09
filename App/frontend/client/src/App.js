import './App.css';
import { Switch,BrowserRouter as Router,Route } from 'react-router-dom'
import MainPage from './components/MainPage';
import "antd/dist/antd.css";
import DataLabels from './components/DataLabels';
import HtmlLoader from './components/HtmlLoader'

function App() {
  console.disableYellowBox = true
  return (
    <div className="App">
      <Router>
      <MainPage />
          <Switch>
            <Route exact path="/" component={DataLabels}/>
            {/* <Route exact path="/Analysis" component={HtmlLoader}/> */}
          </Switch>
      </Router>
    </div>
  );
}

export default App;
