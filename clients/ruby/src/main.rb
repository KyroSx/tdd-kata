require_relative "./client"
require_relative "./create_client"
require_relative "./clients_repository"
require_relative "./get_mean_purchase"

createClient = CreateClient.new
client_list = createClient.create_many [
  { name: 'Jhon Doe', purchases: 12.33 },
  { name: 'Marly Monroe', purchases: 24.98 },
]

clientsRepository = ClientsRepository.new client_list
clients_with_purchase_over = clientsRepository.get_clients_with_purchase_over 20.0

getMeanPurchase = GetMeanPurchase.new  clientsRepository.clients
mean = getMeanPurchase.calculate

puts client_list.inspect
puts clients_with_purchase_over.inspect
puts mean
