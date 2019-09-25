/* import React, { Component, Fragment } from 'react'
import ReactDOM from 'react-dom'
import Header from './layout/Header'
import Dashboard from './catalog/Dashboard'
class App extends Component {
    render() {
        return (
            <h1>test</h1>
            
                        <Fragment>
                            <Header />
                            <div className="container">
                                <Dashboard />
                            </div>
            
                        </Fragment> 
        )
    }
}
ReactDOM.render(<App />, document.getElementById('app'));0
 */

import React from "react";
import ReactDOM from "react-dom";
import DataProvider from "./DataProvider";
import Table from "./Table";

const App = () => (
    <DataProvider endpoint="api/author/"
        render={data => <Table data={data} />} />
);

const wrapper = document.getElementById("app");

wrapper ? ReactDOM.render(<App />, wrapper) : null;