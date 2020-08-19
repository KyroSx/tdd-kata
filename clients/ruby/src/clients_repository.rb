class ClientsRepository
  attr_reader :clients

  def initialize(clients = [])
    @clients = clients
  end

  def get_clients_with_purchase_over(value)
    @clients.select do |client|
      client.purchase >= value
    end
  end
end
