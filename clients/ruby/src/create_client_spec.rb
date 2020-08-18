require_relative 'client'

class CreateClient
  def create(name, purchase)
    raise Exception if (name === '') || (purchase <= 0)

    Client.new name, purchase
  end

  def create_many(client_list)
    client_list.map! do |client|
      create client[:name], client[:purchase]
    end
  end
end

describe 'Client Creation' do
  before(:each) do
    @sut = CreateClient.new

    @client_name = 'Any Name'
    @client_purchase = 42.0
  end

  context 'single client' do
    it 'should be able to create if data is valid' do
      client = @sut.create @client_name, @client_purchase

      expect(client.name).to eql(@client_name)
      expect(client.purchase).to eql(@client_purchase)
    end

    it 'should throw if data is invalid' do
      expect { @sut.create '', -1 }.to raise_error(Exception)
    end
  end

  context 'multiple clients' do
    it 'should be able to create multiple clients if data is valid' do
      client_list = @sut.create_many [
        { name: @client_name, purchase: @client_purchase },
        { name: @client_name, purchase: @client_purchase },
        { name: @client_name, purchase: @client_purchase }
      ]

      client_list.each do |client|
        expect(client.name).to eql(@client_name)
        expect(client.purchase).to be(@client_purchase)
      end
    end

    it 'should throw if data is invalid' do
      data_list = [
        { name: @client_name, purchase: @client_purchase },
        { name: '', purchase: @client_purchase },
        { name: @client_name, purchase: -1 }
      ]

      expect { @sut.create_many data_list }.to raise_error(Exception)
    end
  end
end
