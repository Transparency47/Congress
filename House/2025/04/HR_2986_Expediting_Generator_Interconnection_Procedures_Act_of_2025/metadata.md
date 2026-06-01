# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2986?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2986
- Title: Expediting Generator Interconnection Procedures Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2986
- Origin chamber: House
- Introduced date: 2025-04-24
- Update date: 2026-02-04T05:06:20Z
- Update date including text: 2026-02-04T05:06:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-24: Introduced in House
- 2025-04-24 - IntroReferral: Introduced in House
- 2025-04-24 - IntroReferral: Introduced in House
- 2025-04-24 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-04-24: Introduced in House

## Actions

- 2025-04-24 - IntroReferral: Introduced in House
- 2025-04-24 - IntroReferral: Introduced in House
- 2025-04-24 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-24",
    "latestAction": {
      "actionDate": "2025-04-24",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2986",
    "number": "2986",
    "originChamber": "House",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "C001066",
        "district": "14",
        "firstName": "Kathy",
        "fullName": "Rep. Castor, Kathy [D-FL-14]",
        "lastName": "Castor",
        "party": "D",
        "state": "FL"
      }
    ],
    "title": "Expediting Generator Interconnection Procedures Act of 2025",
    "type": "HR",
    "updateDate": "2026-02-04T05:06:20Z",
    "updateDateIncludingText": "2026-02-04T05:06:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-24",
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
      "actionDate": "2025-04-24",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-24",
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
          "date": "2025-04-24T15:01:45Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "Q000023",
      "district": "5",
      "firstName": "Mike",
      "fullName": "Rep. Quigley, Mike [D-IL-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Quigley",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "IL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2986ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2986\nIN THE HOUSE OF REPRESENTATIVES\nApril 24, 2025 Ms. Castor of Florida introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo require the Federal Energy Regulatory Commission to promulgate regulations that accelerate the interconnection of electric generation and storage resources to the transmission system through more efficient and effective interconnection procedures.\n#### 1. Short title\nThis Act may be cited as the Expediting Generator Interconnection Procedures Act of 2025 .\n#### 2. Definitions\nIn this Act:\n**(1) Commission**\nThe term Commission means the Federal Energy Regulatory Commission.\n**(2) Energy storage project**\nThe term energy storage project means\u2014\n**(A)**\nany equipment that receives, stores, and delivers energy using batteries, compressed air, pumped hydropower, hydrogen storage (including hydrolysis), thermal energy storage, regenerative fuel cells, flywheels, capacitors, superconducting magnets, or other technologies identified by the Commission; and\n**(B)**\nany project for the construction or modification of equipment described in subparagraph (A) as part of an effort to build-out transmission interconnection opportunities.\n**(3) Generation project**\nThe term generation project means\u2014\n**(A)**\nany facility\u2014\n**(i)**\nthat generates or injects electricity; and\n**(ii)**\nfor which an interconnection request is subject to the jurisdiction of the Commission; and\n**(B)**\nany project for the construction or modification of a facility described in subparagraph (A).\n**(4) Interconnection customer**\nThe term interconnection customer means a person or entity that has submitted an interconnection request.\n**(5) Interconnection request**\nThe term interconnection request means a request submitted to a public utility to interconnect a new generation project or energy storage project to the electric system of a public utility for the purposes of transmission of electric energy in interstate commerce or the sale of electric energy at wholesale.\n**(6) Public utility**\nThe term public utility has the meaning given the term in section 201(e) of the Federal Power Act ( 16 U.S.C. 824(e) ).\n**(7) Transmission facility**\nThe term transmission facility means a facility that is used for the transmission of electric energy in interstate commerce.\n**(8) Transmission provider**\nThe term transmission provider means a public utility that owns, operates, or controls 1 or more transmission facilities.\n**(9) Transmission system**\nThe term transmission system means a network of transmission facilities used for the transmission of electric energy in interstate commerce.\n#### 3. Rulemaking to expedite generator interconnection procedures\n##### (a) In general\nNot later than 180 days after the date of enactment of this Act, the Commission shall initiate a rulemaking\u2014\n**(1)**\nto address the inefficiencies and ineffectiveness of existing procedures for processing interconnection requests to ensure that new generation projects and energy storage projects can interconnect quickly, cost-effectively, and reliably; and\n**(2)**\nto revise the pro forma Large Generator Interconnection Procedures and, as appropriate, the pro forma Large Generator Interconnection Agreement, promulgated pursuant to section 35.28(f) of title 18, Code of Federal Regulations (or successor regulations), to require transmission providers\u2014\n**(A)**\nto develop and employ modeling assumptions for each resource type based on actual operating abilities and practices, for the purposes of studying an interconnection request;\n**(B)**\nto study interconnection requests in a manner consistent with the risk tolerance of the interconnection customer;\n**(C)**\nto select, as appropriate, 1 or more cost-effective solutions to address network reliability needs that may be identified while studying an interconnection request;\n**(D)**\nto provide sufficient information to interconnection customers for the interconnection customers to understand how a transmission provider has implemented the assumptions and solutions described in subparagraphs (A) and (C);\n**(E)**\nto share and employ, as appropriate, queue management best practices, including with respect to the use of advanced computing technologies, automation, and standardized study criteria, in evaluating interconnection requests, in order to expedite study results; and\n**(F)**\nto implement transparency and performance-enhancing measures to ensure timely and cost-conscious construction of necessary network upgrades once an interconnection agreement has been executed.\n##### (b) Deadline for final rule\nNot later than 18 months after the date of enactment of this Act, the Commission shall promulgate a final rule to complete the rulemaking initiated under subsection (a).\n##### (c) Savings clause\nNothing in this section alters, or may be construed to alter, the allocation of costs of the transmission system pursuant to the ratemaking authority of the Commission under section 205 of the Federal Power Act ( 16 U.S.C. 824d ).",
      "versionDate": "2025-04-24",
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
        "updateDate": "2025-05-20T12:29:17Z"
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
      "date": "2025-04-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2986ih.xml"
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
      "title": "Expediting Generator Interconnection Procedures Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-07T04:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Expediting Generator Interconnection Procedures Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-07T04:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Federal Energy Regulatory Commission to promulgate regulations that accelerate the interconnection of electric generation and storage resources to the transmission system through more efficient and effective interconnection procedures.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-07T04:18:22Z"
    }
  ]
}
```
