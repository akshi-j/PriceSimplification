import React, {Component} from 'react';
import './App.css';
import axios from 'axios';

const enteredSKU = prompt('Please enter the SKU')

const api = axios.create({
  baseURL: "https://akshi.pythonanywhere.com/"
})

class App extends Component {
  state = {
    product : "",
    errorMsg: '',
  }
  constructor () {
    super();
    api.get(`/product/` + enteredSKU).then(res => {
      console.log(res.data)
      this.setState({ product : res.data})
    }).catch(err => {
      this.setState({errorMsg: "Oops! The specified SKU wasn't found."})
    })
  }
  render() {
    return (
        <div className="App">
          <header className="App-header">
            { this.state.errorMsg &&
            <h3 className="error"> { this.state.errorMsg } </h3> }
            { !this.state.errorMsg &&
            <h2>SKU: {enteredSKU}</h2> }
            { !this.state.errorMsg &&
            <h2>Price: {this.state.product.Price}</h2> }
            { !this.state.errorMsg &&
            <h2>Last Updated: {this.state.product.LastUpdated}</h2> }
          </header>
        </div>
    );
  }

}

export default App;
