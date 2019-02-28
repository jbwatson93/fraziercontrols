import React, { Component } from 'react';
import axios from 'axios'
import { Link } from 'react-router-dom'
class Newproject extends Component {
    state={
        project:{
            company:"",
            creationdate:  Date,
            customerid:"",
            description:"",
            estimatedcompdate:Date,
            projectid: "",
            projectname:"",
            startdate:Date,
            
            
        }
    }

    // getDate = () =>{
    //     let date = Date.now()
    //     let now = {...this.state.project.creationdate}
    //     this.setState(project: date)
    // }
    handleChange = (event) => {
        let newproject = { ...this.state.project }
        newproject[event.target.name] = event.target.value
        this.setState({ project: newproject });
    }
    submitForm = (event) =>{
        event.preventDefault()
        let newproject = {...this.state.project}
        axios.post('/api/v1/projects/', newproject)
        return Promise.resolve(newproject)
    }

    render() {
        return (
            <div>
                <form onSubmit={this.submitForm} >
                <input  onChange={this.handleChange} type="text" name='projectname' placeholder="Project Name" /> <br />
                <input  onChange={this.handleChange} type="text"maxLength="5" name='projectid' placeholder="Project ID" /> <br />
                <input  onChange={this.handleChange} type="text" name='company' placeholder="Company" /> <br />
                <textarea   onChange={this.handleChange} rows='5' name='description' placeholder="Description" /> <br />
                <input  onChange={this.handleChange} type="text" name='customerid' placeholder="Customer ID" /> <br />
                Start Date: <br/>
                <input  onChange={this.handleChange} type="date" name='startdate'  /> <br />
                Estimated Completion Date: <br/>
                 <input  onChange={this.handleChange} type="date" name='estimatedcompdate'  /> <br />
                 Creation Date: <br/>
                 <input  onChange={this.handleChange} type="datetime-local" name='creationdate'  /> <br />
               
                </form>
               <Link to={'/projects/'}> <button  onClick={this.submitForm}>Submit</button></Link> 
            </div>
        );
    }
}

export default Newproject;