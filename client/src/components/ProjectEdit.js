import React, { Component } from 'react';
import axios from 'axios'


class ProjectEdit extends Component {
    state = {
        projectedit:{
            projectid:this.props.projectid ,
            startdate: this.props.startdate,
            estimatedcompdate: this.props.estimatedcompdate,
            projectname: this.props.projectname,
            description: '',
            creationdate: this.props.creationDate,
            updatedate: this.props.updatedate,
            company: this.props.company,
            customerid: this.props.customerid,
        }
    } 
    handleChange2 = (event) => {
        let newproject = { ...this.state.projectedit }
        newproject[event.target.name] = event.target.value
        this.setState({ projectedit: newproject });
    }
    update = () =>{
       
        let newproject = {...this.state.projectedit}
        axios.put(`/api/v1/projects/${this.props.projectid}/`, newproject)
        this.props.toggleEdit()
        
    }
    render() {
        return (
            <div>
                <div><textarea   onChange={this.handleChange2} rows='3' name='description' placeholder={this.props.description} />
                <button onClick={this.update}>Update</button></div>
            </div>
        );
    }
}

export default ProjectEdit;