class GetMeanPurchase
  attr_reader :clients

  def initialize(client_list = [])
    @clients = client_list
  end

  def calculate
    total_clients = @clients.count

    purchases_list = @clients.map do |client|
      client.purchase
    end

    total_sum = purchases_list.reduce :+

    mean = total_sum / total_clients

    round_float mean
  end

  private

  def round_float(float)
    (float * 100).round / 100.0
  end
end
