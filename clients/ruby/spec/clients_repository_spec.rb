require_relative '../src/clients_repository'
require_relative '../src/client'

describe '::Clients Repository' do
  before(:each) do
    @client_list = [
      Client.new('Any Name', 42.0),
      Client.new('Any Name', 42.0),
      Client.new('Any Name', 42.0)
    ]

    @sut = ClientsRepository.new @client_list
  end

  context 'sut.init' do
    it 'should have clients as [] by default on sut.init' do
      @sut = ClientsRepository.new

      expect(@sut.clients).to eq([])
    end

    it 'should be able to inject client list on init' do
      @sut = ClientsRepository.new @client_list

      expect(@sut.clients).to eq(@client_list)
    end
  end

  context 'get clients with purchase over' do
    it 'should return all clients' do
      clients_with_over_value = @sut.get_clients_with_purchase_over 20.0

      expect(clients_with_over_value).to eq(@client_list)
    end

    it 'should return [] if no client has overvalue' do
      @client_list = [
        Client.new('Any Name', 10.11),
        Client.new('Any Name', 9.3),
        Client.new('Any Name', 13.5)
      ]

      @sut = ClientsRepository.new @client_list

      clients_with_over_value = @sut.get_clients_with_purchase_over 20.0

      expect(clients_with_over_value).to eq([])
    end
  end
end
