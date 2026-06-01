# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/603?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/603
- Title: Reinforcing the Grid Against Extreme Weather Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 603
- Origin chamber: House
- Introduced date: 2025-01-22
- Update date: 2025-02-21T16:22:49Z
- Update date including text: 2025-02-21T16:22:49Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-01-22: Introduced in House
- 2025-01-22 - IntroReferral: Introduced in House
- 2025-01-22 - IntroReferral: Introduced in House
- 2025-01-22 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-01-22: Introduced in House

## Actions

- 2025-01-22 - IntroReferral: Introduced in House
- 2025-01-22 - IntroReferral: Introduced in House
- 2025-01-22 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-22",
    "latestAction": {
      "actionDate": "2025-01-22",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/603",
    "number": "603",
    "originChamber": "House",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "C001117",
        "district": "6",
        "firstName": "Sean",
        "fullName": "Rep. Casten, Sean [D-IL-6]",
        "lastName": "Casten",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "Reinforcing the Grid Against Extreme Weather Act of 2025",
    "type": "HR",
    "updateDate": "2025-02-21T16:22:49Z",
    "updateDateIncludingText": "2025-02-21T16:22:49Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-22",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-22",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-22",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    }
  ]
}
```

## API Data: committees

```json
{
  "committees": [
    {
      "activities": {
        "item": {
          "date": "2025-01-22T15:01:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
      "type": "Standing"
    }
  ]
}
```

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr603ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 603\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 22, 2025 Mr. Casten introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo direct the Federal Energy Regulatory Commission to improve interregional electricity transfer capability between immediately adjacent transmission planning regions, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Reinforcing the Grid Against Extreme Weather Act of 2025 .\n#### 2. Improving interregional electricity transfer capability\nPart II of the Federal Power Act ( 16 U.S.C. 824 et seq. ) is amended by adding at the end the following:\n224. Improving interregional electricity transfer capability (a) Rulemaking Not later than 24 months after the date of enactment of this section, the Commission shall issue regulations to establish a process for\u2014 (1) calculating existing transfer capability between each transmission planning region and its immediately adjacent transmission planning region, such that\u2014 (A) each transmission planning entity for a given transmission planning region and the transmission planning entities for any immediately adjacent transmission planning region shall use the same method to calculate the transfer capability between them; and (B) each shared method of calculation shall comply with requirements established by the Commission; (2) determining a minimum transfer capability between each transmission planning region and its immediately adjacent transmission planning region in order to\u2014 (A) ensure that each transmission planning region has sufficient electric transfer capability with immediately adjacent transmission planning regions to ensure reliability during impacts associated with weather events, physical events, or cyberattacks to the transmission planning region; and (B) optimize achievement of the transmission benefits; (3) identifying, selecting, and allocating costs for individual interregional transmission projects needed to achieve each minimum transfer capability identified pursuant to paragraph (2); and (4) preventing the disclosure of information pertaining to cyberattacks that may compromise the security of the electricity system. (b) Filing a plan (1) In general Not later than 3 years after the date of enactment of this section, and at least every 5 years thereafter, the transmission planning entities for each pair of immediately adjacent transmission planning regions shall file with the Commission, and receive approval for, a plan that, in accordance with the regulations issued under subsection (a)\u2014 (A) evaluates and selects interregional transmission projects based on consideration of the transmission benefits; and (B) achieves minimum interregional transfer capability. (2) Duty of Commission The Commission shall approve or deny a plan filed pursuant to paragraph (1) in consideration of the factors described in subsection (a)(2). (c) Report Not later than 48 months after the date on which the regulations are issued pursuant to subsection (a), and annually thereafter, the Commission shall publish in the Federal Register a report on the results of implementing this section. (d) Definitions In this section: (1) Greenhouse gas The term greenhouse gas includes each of the following: (A) Carbon dioxide. (B) Methane. (C) Nitrous oxide. (D) Sulfur hexafluoride. (E) Any hydrofluorocarbon. (F) Any perfluorocarbon. (G) Nitrogen trifluoride. (H) Any fully fluorinated linear, branched, or cyclic\u2014 (i) alkane; (ii) ether; (iii) tertiary amine; or (iv) amino ether. (I) Any perfluoropolyether. (J) Any hydrofluoropolyether. (K) Any other fluorocarbon, except for a fluorocarbon with a vapor pressure of less than 1 mm of Hg absolute at 25 degrees Celsius. (2) Transmission benefit The term transmission benefit means a broad range of economic, operational, safety, security, resilience, public policy, environmental, and other reasonably anticipated benefit of constructing, modifying, or operating a transmission facility, including any benefit realized when real-time energy prices and operational conditions differ from those anticipated in the 48-hour ahead or day-ahead time frame. Such benefits include\u2014 (A) improved reliability; (B) improved resilience; (C) improved safety; (D) reduced congestion; (E) reduced power losses; (F) greater carrying capacity; (G) reduced operating reserve requirements; (H) improved access to lower-cost electricity generation; (I) improved access to electricity generating facilities with no direct emissions of greenhouse gases; (J) improved public health from the closure of electricity generation facilities that emit harmful pollution; (K) increased competition and market liquidity in electricity markets; (L) improved energy resilience and reliability of Department of Defense installations; (M) optimizing use of existing transmission assets, including any existing rights of way; (N) other transmission costs avoided by the proposed transmission solution; and (O) other potential benefits of increasing the interconnectedness of the electric grid. (3) Transmission planning entity The term transmission planning entity means an entity responsible for planning for the deployment of electric transmission for a given transmission planning region. (4) Transmission planning region The term transmission planning region means a geographic area that the Commission finds sufficient to satisfy its requirements for the scope of regional transmission planning, as established in or in compliance with the following orders issued by the Commission: (A) Transmission Planning and Cost Allocation by Transmission Owning and Operating Public Utilities published in the Federal Register on October 12, 2012 (77 Fed. Reg. 64890); and (B) Building for the Future Through Electric Regional Transmission Planning and Cost Allocation published in the Federal Register on October 24, 2012 (77 Fed. Reg. 64890). .",
      "versionDate": "2025-01-22",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Energy",
        "updateDate": "2025-02-21T16:22:49Z"
      }
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr603ih.xml"
        }
      ],
      "type": "Introduced in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Reinforcing the Grid Against Extreme Weather Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-21T06:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Reinforcing the Grid Against Extreme Weather Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-21T06:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Federal Energy Regulatory Commission to improve interregional electricity transfer capability between immediately adjacent transmission planning regions, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-21T06:49:28Z"
    }
  ]
}
```
