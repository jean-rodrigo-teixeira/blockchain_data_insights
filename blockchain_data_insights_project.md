# Blockchain Data Insights

## Project Objective

The primary objective of this project is to measure and analyze key performance indicators (KPIs) related to blockchain data, specifically focusing on Ethereum. The KPIs to be tracked are:

### KPIs:
1. **Transaction Volume**: Total number of transactions over a given period.
2. **Transaction Value**: Total value of transactions over a given period.
3. **Active Wallets**: Number of unique wallets making transactions.
4. **Gas Fees**: Total gas fees spent on the Ethereum network.
5. **Token Transfers**: Number of transfers of various tokens.
6. **Smart Contract Interactions**: Number of interactions with smart contracts, including DeFi protocols and NFT platforms.
7. **Mining/Validator Data**: Information on mining rewards or validator performance in Ethereum's proof-of-stake system.
8. **DeFi Metrics**: Various metrics related to decentralized finance protocols, such as total value locked (TVL), borrow rates, and liquidity.
9. **NFT Metrics**: Total sales, volume, and minting of NFTs.

---

## Project Scope

The project will be executed in several phases, each consisting of specific tasks, along with the tools and technologies used in each phase.

### Phase 1: Data Collection

#### Tasks:
1. **Identify Data Sources**:
   - On-chain data from Ethereum blockchain (smart contract data, transactions, etc.)
   - Off-chain data (price feeds, NFT data, etc.)
   - **Tools**: Flipside Crypto API, Snowflake, public blockchain APIs (Etherscan, etc.)

2. **Set Up Data Pipeline**:
   - Use **dbt** for transforming and modeling the data.
   - Set up an ETL process to pull data from blockchain sources and load into Snowflake.

3. **Data Integration**:
   - Integrate on-chain and off-chain data to create comprehensive data models.
   - **Tools**: Snowflake, dbt

---

### Phase 2: Data Modeling

#### Tasks:
1. **Design Data Models**:
   - Build dimensional models (Star Schema) using **dbt** to structure the data for efficient analysis.
   - Focus on creating fact tables (transactions, token transfers, etc.) and dimension tables (wallets, tokens, smart contracts, etc.).

2. **Model DeFi Metrics**:
   - Design models to track DeFi protocol activity, including liquidity, staking, borrowing, lending, etc.

3. **Model NFT Metrics**:
   - Create models to analyze NFT transactions, minting, and sales.

4. **Data Aggregation and Cleaning**:
   - Clean, filter, and aggregate raw data into usable formats.
   - **Tools**: dbt, SQL

---

### Phase 3: Data Analysis

#### Tasks:
1. **Define KPIs**:
   - Set up specific metrics, such as total transaction volume, gas fees, active wallets, and DeFi metrics.
   
2. **Run Queries**:
   - Execute SQL queries on Snowflake to calculate KPIs and track blockchain activities.
   - Use **dbt** to automate transformations and scheduling.

3. **Data Validation**:
   - Validate the consistency and accuracy of data through automated checks.

---

### Phase 4: Data Visualization and Reporting

#### Tasks:
1. **Design Dashboards**:
   - Create interactive dashboards to visualize KPIs and metrics.
   - **Tools**: Tableau (for public sharing of reports)

2. **Publish Dashboards**:
   - Use Tableau to publish dashboards and allow public access.
   - Monitor performance and user interactions with dashboards.

---

### Phase 5: Documentation and Maintenance

#### Tasks:
1. **Create Documentation**:
   - Write clear documentation detailing the data models, KPIs, and data analysis processes.
   - **Tools**: Markdown, GitHub for version control

2. **Ongoing Monitoring**:
   - Continuously monitor the performance of the data pipeline and dashboards.
   - Ensure data is refreshed regularly and models are updated as needed.

---

## Tools & Technologies

- **Data Collection**: Flipside Crypto API, Snowflake, public blockchain APIs (Etherscan)
- **Data Modeling**: dbt, Snowflake
- **Data Visualization**: Tableau
- **Version Control & Documentation**: GitHub, Markdown