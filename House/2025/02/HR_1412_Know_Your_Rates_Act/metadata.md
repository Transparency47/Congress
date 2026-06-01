# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1412?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1412
- Title: Know Your Rates Act
- Congress: 119
- Bill type: HR
- Bill number: 1412
- Origin chamber: House
- Introduced date: 2025-02-18
- Update date: 2026-03-19T08:06:44Z
- Update date including text: 2026-03-19T08:06:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-02-18: Introduced in House
- 2025-02-18 - IntroReferral: Introduced in House
- 2025-02-18 - IntroReferral: Introduced in House
- 2025-02-18 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-02-18: Introduced in House

## Actions

- 2025-02-18 - IntroReferral: Introduced in House
- 2025-02-18 - IntroReferral: Introduced in House
- 2025-02-18 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-18",
    "latestAction": {
      "actionDate": "2025-02-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1412",
    "number": "1412",
    "originChamber": "House",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "G000583",
        "district": "5",
        "firstName": "Josh",
        "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
        "lastName": "Gottheimer",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "Know Your Rates Act",
    "type": "HR",
    "updateDate": "2026-03-19T08:06:44Z",
    "updateDateIncludingText": "2026-03-19T08:06:44Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-18",
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
      "actionDate": "2025-02-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-18",
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
          "date": "2025-02-18T18:00:35Z",
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
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-12-16",
      "state": "NY"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2026-03-18",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1412ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1412\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 18, 2025 Mr. Gottheimer introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Public Utility Regulatory Policies Act of 1978 to establish additional Federal standards that require electric and gas utilities to transmit to each of its consumers information regarding the consumption of electric energy or gas, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Know Your Rates Act .\n#### 2. Additional information to electric consumers\n##### (a) Establishment\nSection 113(b)(3) of the Public Utility Regulatory Policies Act of 1978 ( 16 U.S.C. 2623(b) ) is amended to read as follows:\n(3) Information to consumers Each electric utility shall transmit to each of its electric consumers information regarding rate schedules and consumption of electric energy in accordance with the requirements of section 115(f). .\n##### (b) Information to electric consumers\nSection 115(f) of the Public Utility Regulatory Policies Act of 1978 ( 16 U.S.C. 2625 ) is amended by adding at the end the following:\n(4) Additional information (A) Program For purposes of the standard for information to consumers established by section 113(b)(3), each covered electric utility shall establish a program under which such covered electric utility shall transmit information in accordance with this paragraph. (B) Additional billing information Each covered electric utility shall include in each billing to an electric consumer of the covered electric utility\u2014 (i) the difference between the dollar amount charged in the billing and the dollar amount charged in the previous billing period; and (ii) in dollars and in kilowatt hours, the average monthly consumption of electric energy by such electric consumer. (C) Usage notices A covered electric utility shall notify an electric consumer information relating to the average daily consumption of electric energy by such electric consumer in the following manner: (i) If within the first 9 days of a billing period the average daily consumption of electric energy by an electric consumer exceeds the average daily consumption of electric energy for the previous billing period, the relevant covered electric utility shall notify such electric consumer on the 10th day of the billing period of the excess consumption. (ii) If within the first 19 days of a billing period, or within another date an electric consumer chooses, the average daily consumption of electric energy by such electric consumer exceeds the average daily consumption of electric energy for the previous billing period, the relevant covered electric utility shall notify such electric consumer on the 20th day, or the day after the date on which the electric consumer chooses, of the excess consumption. (D) Optional notice Under the program established pursuant to subparagraph (A), a covered electric utility shall provide an option to each electric consumer to be notified by the covered electric utility in the event the electric consumer, within an active billing period, reaches a dollar amount\u2014 (i) that is based on the rate charged by a covered electric utility for providing electric service; (ii) that reflects the amount of electric energy consumed within the active billing period; and (iii) chosen by such electric consumer. (E) Covered electric utility defined In this paragraph, the term covered electric utility means an electric utility that receives funding from Federal sources, as determined by the Commission. .\n#### 3. Additional information to gas consumers\n##### (a) Establishment\nSection 303(b) of the Public Utility Regulatory Policies Act of 1978 ( 15 U.S.C. 3203(b) ) is amended by adding at the end the following:\n(7) Information to consumers Each gas utility shall transmit to each of its gas consumers information relating to the consumption of gas in accordance with section 304(c). .\n##### (b) Information to gas consumers\nSection 304 of the Public Utility Regulatory Policies Act of 1978 ( 15 U.S.C. 3204 ) is amended by adding at the end the following:\n(c) Information to consumers (1) Program For purposes of the standard for information to consumers established by section 303(b)(c), each covered gas utility shall establish a program under which such covered gas utility shall\u2014 (A) in each billing to a gas consumer of the covered gas utility, include\u2014 (i) the difference between the dollar amount charged in the billing and the dollar amount charged in the previous billing period; and (ii) in dollars and therms, the average monthly consumption of gas by such gas consumer; and (B) notify each such gas consumer information relating to the average daily consumption of gas by such gas consumer in the following manner: (i) If within the first 9 days of a billing period the average daily consumption of gas by a gas consumer exceeds the average daily consumption of gas for the previous billing period, the relevant covered gas utility shall notify such gas consumer on the 10th day of the billing period about such exceedance. (ii) If within the first 19 days of a billing period, or within another date a gas consumer chooses, the average daily consumption of gas by such gas consumer exceeds the average daily consumption of gas for the previous billing period, the relevant covered gas utility shall notify such gas consumer on the 20th day, or the day after the date on which the gas consumer chooses, of the excess consumption. (2) Optional notice Under the program established pursuant to paragraph (1), a covered gas utility shall provide an option to each gas consumer to be notified by the covered electric utility in the event the gas consumer, within an active billing period, reaches a dollar amount\u2014 (A) that is based on the rate charged by a covered gas utility for providing gas service; (B) that reflects the amount of gas consumed within the active billing period; and (C) chosen by such gas consumer. (3) Covered gas utility defined The term covered gas utility means a gas utility that receives funding from Federal sources, as determined by the Commission. .",
      "versionDate": "2025-02-18",
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
        "updateDate": "2025-03-18T15:09:29Z"
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
      "date": "2025-02-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1412ih.xml"
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
      "title": "Know Your Rates Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-17T13:08:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Know Your Rates Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-17T13:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Public Utility Regulatory Policies Act of 1978 to establish additional Federal standards that require electric and gas utilities to transmit to each of its consumers information regarding the consumption of electric energy or gas, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-17T13:03:49Z"
    }
  ]
}
```
