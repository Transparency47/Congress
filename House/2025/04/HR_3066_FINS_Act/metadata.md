# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3066?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/3066
- Title: FINS Act
- Congress: 119
- Bill type: HR
- Bill number: 3066
- Origin chamber: House
- Introduced date: 2025-04-29
- Update date: 2025-05-21T12:05:29Z
- Update date including text: 2025-05-21T12:05:29Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-04-29: Introduced in House
- 2025-04-29 - IntroReferral: Introduced in House
- 2025-04-29 - IntroReferral: Introduced in House
- 2025-04-29 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2025-04-29: Introduced in House

## Actions

- 2025-04-29 - IntroReferral: Introduced in House
- 2025-04-29 - IntroReferral: Introduced in House
- 2025-04-29 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-29",
    "latestAction": {
      "actionDate": "2025-04-29",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/3066",
    "number": "3066",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "H001101",
        "district": "10",
        "firstName": "Pat",
        "fullName": "Rep. Harrigan, Pat [R-NC-10]",
        "lastName": "Harrigan",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "FINS Act",
    "type": "HR",
    "updateDate": "2025-05-21T12:05:29Z",
    "updateDateIncludingText": "2025-05-21T12:05:29Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-29",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Financial Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-04-29",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-29",
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
          "date": "2025-04-29T14:03:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3066ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3066\nIN THE HOUSE OF REPRESENTATIVES\nApril 29, 2025 Mr. Harrigan introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo enhance financial oversight of commercial wire transfer companies and prevent illicit money transfers by criminal organizations, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Financial Integrity for National Security Act or the FINS Act .\n#### 2. Findings\n##### (a) Findings\nThe Congress finds the following:\n**(1)**\nInternational criminal organizations, including cartels and terrorist groups, exploit unregulated commercial wire transfer services, such as Western Union, Ria, and XE, to facilitate human trafficking, drug trade, and terrorism.\n**(2)**\nUnlike institutional banks, these wire transfer companies operate with minimal regulatory oversight, creating vulnerabilities in financial crime enforcement.\n**(3)**\nStrengthening oversight of wire transfers will enhance national security and align non-bank financial institutions with established anti-money laundering laws and the Bank Secrecy Act.\n#### 3. Requirements for wire transfer service providers\n##### (a) In general\nSection 5312(a) of title 31, United States code is amended\u2014\n**(1)**\nin paragraph (2)\u2014\n**(A)**\nby redesignating subparagraphs (Y) and (Z) as subparagraphs (Z) and (AA), respectively; and\n**(B)**\nby inserting after paragraph (X) the following:\n(Y) wire transfer service providers; ; and\n**(2)**\nby adding at the end the following:\n(7) Wire transfer service provider The term wire transfer service provider means an entity that engages in the electronic transfer of funds on behalf of consumers or businesses, either domestically or across international borders, including but not limited to services such as Western Union, Ria, MoneyGram, XE, and digital remittance platforms (we recommend against calling out specific companies as they change over time). .\n##### (b) Rulemaking\nThe Secretary of the Treasury shall, not later than 180 days after the date of the enactment of this Act, issues such rules as the Secretary of the Treasury determines necessary to carry out the amendments made by this section.\n##### (c) Effective date\nThe amendments made by this section shall take effect 1 year after the date of the enactment of this section.",
      "versionDate": "2025-04-29",
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
        "name": "Finance and Financial Sector",
        "updateDate": "2025-05-21T12:05:29Z"
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
      "date": "2025-04-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3066ih.xml"
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
      "title": "FINS Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-13T05:23:29Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "FINS Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-13T05:23:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Financial Integrity for National Security Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-13T05:23:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To enhance financial oversight of commercial wire transfer companies and prevent illicit money transfers by criminal organizations, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-13T05:18:51Z"
    }
  ]
}
```
