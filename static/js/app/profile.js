class Profile extends React.Component {
    constructor() {
        super();
        this.state = {
            data: [],
            isLoading: false,
            data_url: 'http://localhost:8000/api/enterprise/',
            user_request_id: $('#hidden_id').val()
        }
    }

    loadData() {
        let data_url = this.state.data_url;
        let user_request_id = this.state.user_request_id;
        console.log('Full path: => ' + data_url + user_request_id);
        fetch(data_url + user_request_id)
            .then(response => response.json())
            .then(data => {
                this.setState({data: data, isLoading: false});
                console.log(data)
            })
            .catch(err => console.error(this.props.url, err.toString()))
    }

    componentDidMount() {
        this.loadData();
        this.setState({isLoading: true})
    }

    render() {
        let data_url = this.state.data_url;
        let user_request_id = this.state.user_request_id;
        if (this.state.isLoading) {
            return <div className="alert alert-info">Loading...</div>
        }
        if (this.state.data === []) {
            return (
                <div className="alert alert-danger">
                    <p>Data not found</p>
                </div>
            )
        }
        return (
            <div className='row'>
                <div className='col-md-12'>
                    <div className="card">
                        <div className="card-header">
                            <h1 className="cart-title">
                                My enterprise list
                            </h1>
                        </div>
                    </div>
                    <EnterprisePost data_url={data_url} user_request_id={user_request_id}/>
                </div>
                {
                    this.state.data.map((item, i) => {
                        return (
                            <div className='col-sm' key={i}>
                                <div className="card">
                                    <div className="card-header">
                                        <h1 className='cart-title'>{item.title}</h1>
                                    </div>
                                    <img src={item.logo} className='card-img-top' alt={item.title}/>
                                    <div className="card-body">
                                        <p className='card-text'>
                                            {item.short_descr}
                                        </p>
                                    </div>
                                    <div className="card-footer">
                                        <span>Services</span>
                                    </div>
                                </div>
                            </div>
                        );
                    })
                }
            </div>
        )
    }
}

class EnterprisePost extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            data_url: this.props.data_url,
            user_request_id: this.props.user_request_id
        }
    }

    addEnterprise = (e) => {
        e.preventDefault();
        console.log(e.target.input);

    };
    newEnterprise = () =>
        <div>
            <h1>New enterprise</h1>
            <form onSubmit={this.addEnterprise} className="form-group">
                <fieldset>
                    <div className="row">
                        <div className="col-sm-2">
                            <label htmlFor="">Title:</label>
                        </div>
                        <div className="col-sm-10">
                            <input type="text" name="title" />
                        </div>
                    </div>
                    <button type="submit" className="btn btn-dark">Post</button>
                </fieldset>
            </form>
        </div>;

    render() {
        return (
            <div>
                {this.newEnterprise()}
            </div>
        )
    }
}

ReactDOM.render(
    <Profile/>,
    document.getElementById('profile')
);
