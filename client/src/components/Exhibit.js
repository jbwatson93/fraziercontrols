import React, { Component } from 'react';
import axios from 'axios'


class Exhibit extends Component {
    state={
        exhibit: {
             },
        
    }
    componentDidMount(){
        this.getExhibit()
       
    }
    getExhibit = () => {
        axios.get(`/api/v1/exhibits/${this.props.match.params.id}`)
            .then((res) => {
                 this.setState({ exhibit: res.data })
            })
    }
    render() {
        return (
            <div>
                <h1>{this.state.exhibit.exhibitName}</h1>
                <p>{this.state.exhibit.description}</p>
            </div>
        );
    }
}

export default Exhibit;