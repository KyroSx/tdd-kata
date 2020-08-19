require_relative '../src/get_mean_purchase'
require_relative '../src/client'

describe '::Get Mean Purchase' do
  before do
    @client_list = [
      Client.new('Any Name', 12.21),
      Client.new('Any Name', 34.43),
      Client.new('Any Name', 42.00)
    ]

    @sut = GetMeanPurchase.new @client_list
  end

  context 'sut.init' do
    it 'should have clients as [] by default on sut.init' do
      @sut = GetMeanPurchase.new

      expect(@sut.clients).to eq([])
    end

    it 'should be able to inject client list on init' do
      expect(@sut.clients).to eq(@client_list)
    end
  end

  context 'mean calculation' do
    it 'should calculate the mean correctly' do
      mean = @sut.calculate

      expect(mean).to eq(29.55)
    end
  end
end
