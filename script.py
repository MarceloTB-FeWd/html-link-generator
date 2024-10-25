import webbrowser
import os

# Dados dos tokens e sites extraídos do arquivo
tokens = [
    {
        "nome": "CRO",
        "contratos": [
            {
                "endereco": "0xa0b73e1ff0b80914ab6fe0444e65848c4c34450b",
                "sites_especificos": ["Etherscan", "Dex Screener", "Token Sniffer"]
            },
            {
                "endereco": "DvjMYMVeXgKxaixGKpzQThLoG98nc7HSU7eanzsdCboA",
                "sites_especificos": ["Solscan", "Dex Screener", "Token Sniffer"]
            }
        ],
        "ucid": 3635,
        "id_api": "crypto-com-chain",
        "conta": "@cryptocom"
    },
    {
        "nome": "DRACE",
        "contratos": [
            {
                "endereco": "0xa6c897caaca3db7fd6e2d2ce1a00744f40ab87bb",
                "sites_especificos": ["BscScan", "Dex Screener", "Token Sniffer"]
            }
        ],
        "ucid": 11682,
        "id_api": "deathroad",
        "conta": "@DeathRoad_io"
    },
    {
        "nome": "DOME",
        "contratos": [
            {
                "endereco": "0x475bfaa1848591ae0e6ab69600f48d828f61a80e",
                "sites_especificos": ["BscScan", "Dex Screener", "Token Sniffer"]
            }
        ],
        "ucid": 16432,
        "id_api": "everdome",
        "conta": "@Everdome_io"
    },
    {
        "nome": "FYN",
        "contratos": [
            {
                "endereco": "0x3B56a704C01D650147ADE2b8cEE594066b3F9421",
                "sites_especificos": ["Polygonscan", "Dex Screener", "Token Sniffer"]
            }
        ],
        "ucid": 17073,
        "id_api": "affyn",
        "conta": "@AffynOfficial"
    },
    {
        "nome": "HELLO",
        "contratos": [
            {
                "endereco": "0x411099C0b413f4fedDb10Edf6a8be63BD321311C",
                "sites_especificos": ["Etherscan", "Dex Screener", "Token Sniffer"]
            },
            {
                "endereco": "0x0f1cbed8efa0e012adbccb1638d0ab0147d5ac00",
                "sites_especificos": ["BscScan", "Dex Screener", "Token Sniffer"]
            },
            {
                "endereco": "4h49hPGphLNJNDRyiBwzvKoasR3rw1WJCEv19PhUbSS4",
                "sites_especificos": ["Solscan", "Dex Screener", "Token Sniffer"]
            }
        ],
        "ucid": 22320,
        "id_api": "hello-labs",
        "conta": "@thehellolabs"
    },
    {
        "nome": "HERO",
        "contratos": [
            {
                "endereco": "0xD40bEDb44C081D2935eebA6eF5a3c8A31A1bBE13",
                "sites_especificos": ["BscScan", "Dex Screener", "Token Sniffer"]
            }
        ],
        "ucid": 10778,
        "id_api": "metahero",
        "conta": "@Metahero_io"
    },
    {
        "nome": "HTD",
        "contratos": [
            {
                "endereco": "0x5E2689412Fae5c29BD575fbe1d5C1CD1e0622A8f",
                "sites_especificos": ["BscScan", "Dex Screener", "Token Sniffer"]
            }
        ],
        "ucid": 14422,
        "id_api": "heroes-td",
        "conta": "@heroes_td"
    },
    {
        "nome": "MATIC",
        "contratos": [
            {
                "endereco": "0x7D1AfA7B718fb893dB30A3aBc0Cfc608AaCfeBB0",
                "sites_especificos": ["Etherscan", "Dex Screener", "Token Sniffer"]
            },
            {
                "endereco": "0xcc42724c6683b7e57334c4e856f4c9965ed682bd",
                "sites_especificos": ["BscScan", "Dex Screener", "Token Sniffer"]
            },
            {
                "endereco": "0x0000000000000000000000000000000000001010",
                "sites_especificos": ["Polygonscan", "Dex Screener", "Token Sniffer"]
            },
            {
                "endereco": "C7NNPWuZCNjZBfW5p6JvGsR8pUdsRpEdP1ZAhnoDwj7h",
                "sites_especificos": ["Solscan", "Dex Screener", "Token Sniffer"]
            }
        ],
        "ucid": 3890,
        "id_api": "matic-network",
        "conta": "@0xPolygon"
    },
    {
        "nome": "MIST",
        "contratos": [
            {
                "endereco": "0x68E374F856bF25468D365E539b700b648Bf94B67",
                "sites_especificos": ["BscScan", "Dex Screener", "Token Sniffer"]
            }
        ],
        "ucid": 9218,
        "id_api": "mist",
        "conta": "@MistNft"
    },
    {
        "nome": "MTS",
        "contratos": [
            {
                "endereco": "0x496cC0b4ee12Aa2AC4c42E93067484e7Ff50294b",
                "sites_especificos": ["BscScan", "Dex Screener", "Token Sniffer"]
            }
        ],
        "ucid": 16033,
        "id_api": "metastrike",
        "conta": "@MetastrikeHQ"
    },
    {
        "nome": "TLM",
        "contratos": [
            {
                "endereco": "0x888888848B652B3E3a0f34c96E00EEC0F3a23F72",
                "sites_especificos": ["Etherscan", "Dex Screener", "Token Sniffer"]
            },
            {
                "endereco": "0x2222227e22102fe3322098e4cbfe18cfebd57c95",
                "sites_especificos": ["BscScan", "Dex Screener", "Token Sniffer"]
            }
        ],
        "ucid": 9119,
        "id_api": "alien-worlds",
        "conta": "@AlienWorlds"
    },
    {
        "nome": "UFO",
        "contratos": [
            {
                "endereco": "0x249e38ea4102d0cf8264d3701f1a0e39c4f2dc3b",
                "sites_especificos": ["Etherscan", "Dex Screener", "Token Sniffer"]
            },
            {
                "endereco": "GWdkYFnXnSJAsCBvmsqFLiPPe2tpvXynZcJdxf11Fu3U",
                "sites_especificos": ["Solscan", "Dex Screener", "Token Sniffer"]
            }
        ],
        "ucid": 10729,
        "id_api": "ufo-gaming",
        "conta": "@TheUFOtoken"
    }
]

sites = [
    {"nome": "BscScan", "url": "https://bscscan.com/"},
    {"nome": "Dex Screener", "url": "https://dexscreener.com/"},
    {"nome": "Etherscan", "url": "https://etherscan.io/"},
    {"nome": "Polygonscan", "url": "https://polygonscan.com/"},
    {"nome": "Solscan", "url": "https://solscan.io/"},
    {"nome": "Token Sniffer", "url": "https://tokensniffer.com/"},
    {"nome": "TweetScout", "url": "https://app.tweetscout.io/search?q="}
]

# Função para gerar URLs do CoinMarketCap e CoinGecko
def generate_coin_urls(token):
    urls = []
    # Gerar URL para CoinMarketCap
    cmc_url = f"https://coinmarketcap.com/currencies/{token['id_api']}/"
    urls.append({"site": "CoinMarketCap", "url": cmc_url})
    
    # Gerar URL para CoinGecko
    coingecko_url = f"https://www.coingecko.com/en/coins/{token['id_api']}"
    urls.append({"site": "CoinGecko", "url": coingecko_url})
    
    return urls

def search_by_contract(token):
    results = []

    for contrato in token['contratos']:
        sites_a_pesquisar = contrato['sites_especificos']
        for site in sites:
            if site['nome'] in sites_a_pesquisar:
                if "scan" in site['url']:
                    search_url = f"{site['url']}token/{contrato['endereco']}"
                elif "dexscreener" in site['url']:
                    search_url = f"{site['url']}?q={contrato['endereco']}"
                elif "tokensniffer" in site['url']:
                    search_url = f"{site['url']}/token/{contrato['endereco']}"
                results.append({"site": site['nome'], "url": search_url})

    # Adicionar URLs de CoinMarketCap e CoinGecko
    coin_urls = generate_coin_urls(token)
    results.extend(coin_urls)

    return results

# Função para gerar URLs do Twitterscore
def search_by_account(token):
    username = token['conta'].lstrip('@')  # Remove o '@' do início
    twitter_url = f"https://twitterscore.io/twitter/{username}/overview/"
    tweetscout_url = f"https://app.tweetscout.io/search?q=@{username}"
    
    return [
        {"site": "Twitterscore", "url": twitter_url},
        {"site": "TweetScout", "url": tweetscout_url}
    ]

def main():
    all_results = []
    for token in tokens:
        contract_results = search_by_contract(token)
        twitter_results = search_by_account(token)
        combined_results = contract_results + twitter_results
        if combined_results:
            all_results.append({"token": token['nome'], "results": combined_results})

    html_content = "<html><body><h1>Resultados</h1><ul>"
    for token_data in all_results:
        html_content += f"<li><strong>{token_data['token']}</strong><ul>"
        for result in token_data['results']:
            html_content += f"<li>{result['site']}: <a href='{result['url']}' target='_blank'>{result['url']}</a></li>"
        html_content += "</ul></li>"
    html_content += "</ul></body></html>"

    html_filename = "index.html"
    with open(html_filename, "w", encoding='utf-8') as html_file:
        html_file.write(html_content)

    webbrowser.open(f"file://{os.path.abspath(html_filename)}")

if __name__ == "__main__":
    main()
