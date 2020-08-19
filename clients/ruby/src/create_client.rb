require_relative 'client'

class CreateClient
  def create(name, purchase)
    raise Exception if (name === '') || (purchase <= 0)

    Client.new name, purchase
  end

  def create_many(client_list)
    client_list.map do |client|
      name, purchase = client.values
      create name, purchase
    end
  end
end
