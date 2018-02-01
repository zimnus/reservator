class ServiceGroup extends React.Component {
    constructor() {
      super();
      this.state = {
        error: null,
        items: []
      }
    }
    loadService() {
      $.ajax({
        url: '/api/services/1/',
      })
      .done((result) => {
        this.setState({items: result})
      })
      .fail(() => {
        this.setState({error})
      })
    }
    componentDidMount() {
      let groups = document.getElementById('group');
      console.log(groups);
      this.loadService();
    }
    render() {
      const { error, items } = this.state;
      if (error) {
        return <div className="alert alert-info">Service not found!</div>
      } else {
        return (
          <div className="client-list">
            <h2>Service</h2>
            <div className="table-responsive">
              <table className="table table-striped table-hover">
                <tbody>
                  {items.map(item => (
                    <tr key={item.id}>
                      <td><span className="label label-primary">Active</span></td>
                      <td>
                        <span className="client-link">{item.title}</span><br />
                        Staffs: {item.staff.length}
                      </td>
                      <td>
                        <button className="btn btn-default"><span className="fa fa-eye"></span></button>
                        <button className="btn btn-default"><span className="fa fa-trash"></span></button>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>
        );
    }
  }

}

ReactDOM.render(
    <ServiceGroup />,
    document.getElementById('service-group')
)
