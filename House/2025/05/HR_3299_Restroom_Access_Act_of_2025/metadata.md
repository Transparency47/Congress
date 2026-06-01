# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3299?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3299
- Title: Restroom Access Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3299
- Origin chamber: House
- Introduced date: 2025-05-08
- Update date: 2026-02-24T06:26:19Z
- Update date including text: 2026-02-24T06:26:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-08: Introduced in House
- 2025-05-08 - IntroReferral: Introduced in House
- 2025-05-08 - IntroReferral: Introduced in House
- 2025-05-08 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-05-08 - IntroReferral: Sponsor introductory remarks on measure. (CR E403)
- Latest action: 2025-05-08: Introduced in House

## Actions

- 2025-05-08 - IntroReferral: Introduced in House
- 2025-05-08 - IntroReferral: Introduced in House
- 2025-05-08 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-05-08 - IntroReferral: Sponsor introductory remarks on measure. (CR E403)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-08",
    "latestAction": {
      "actionDate": "2025-05-08",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3299",
    "number": "3299",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "N000147",
        "district": "",
        "firstName": "Eleanor",
        "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
        "lastName": "Norton",
        "party": "D",
        "state": "DC"
      }
    ],
    "title": "Restroom Access Act of 2025",
    "type": "HR",
    "updateDate": "2026-02-24T06:26:19Z",
    "updateDateIncludingText": "2026-02-24T06:26:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-08",
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
      "actionDate": "2025-05-08",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "B00100",
      "actionDate": "2025-05-08",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Sponsor introductory remarks on measure. (CR E403)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-08",
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
          "date": "2025-05-08T13:00:40Z",
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
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-06-02",
      "state": "MI"
    },
    {
      "bioguideId": "R000617",
      "district": "3",
      "firstName": "Delia",
      "fullName": "Rep. Ramirez, Delia C. [D-IL-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Ramirez",
      "middleName": "C.",
      "party": "D",
      "sponsorshipDate": "2025-06-03",
      "state": "IL"
    },
    {
      "bioguideId": "M001229",
      "district": "10",
      "firstName": "LaMonica",
      "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
      "isOriginalCosponsor": "False",
      "lastName": "McIver",
      "party": "D",
      "sponsorshipDate": "2025-06-04",
      "state": "NJ"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-10-31",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3299ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3299\nIN THE HOUSE OF REPRESENTATIVES\nMay 8, 2025 Ms. Norton introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo provide an individual with an eligible medical condition access to employee restroom facilities of a retail establishment under certain conditions, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Restroom Access Act of 2025 .\n#### 2. Medically necessary restroom access\n##### (a) In general\nAny retail establishment that has a restroom facility that is not usually accessible to the public shall allow a customer to use that facility during business hours of such retail establishment if\u2014\n**(1)**\nthe customer suffers from an eligible medical condition;\n**(2)**\nthe customer presents an identification card as described by subsection (b);\n**(3)**\ntwo or more employees of the retail establishment are working at the time the customer requests use of the restroom facility;\n**(4)**\nthe restroom facility is not located in an area where providing access would create an obvious health or safety risk to the customer; and\n**(5)**\na public restroom is not available to the customer at the time at which they seek to use such restroom.\n##### (b) Identification card\nNot later than 180 days after the date of the enactment of this Act, the Secretary of Labor shall establish a system to create and distribute an identification card to an individual for whom a medical professional has certified has an eligible medical condition.\n##### (c) Definitions\nIn this section:\n**(1) Customer**\nThe term customer means an individual who is lawfully on the premises of a retail establishment.\n**(2) Eligible medical condition**\nThe term eligible medical condition means\u2014\n**(A)**\nany inflammatory bowel disease, including Crohn\u2019s disease, ulcerative colitis or irritable bowel syndrome;\n**(B)**\nthe use of an ostomy device; or\n**(C)**\nany other diagnosed medical condition, including pregnancy, that would require immediate access to a restroom facility.\n**(3) Medical professional**\nThe term medical professional means a physician, naturopathic physician, physician assistant, nurse, or nurse practitioner qualified to diagnose an eligible medical condition.\n**(4) Retail establishment**\nThe term retail establishment means a place of business open to the public for the sale of goods or services moving in or affecting interstate commerce.",
      "versionDate": "2025-05-08",
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
        "name": "Health",
        "updateDate": "2025-05-22T17:10:09Z"
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
      "date": "2025-05-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3299ih.xml"
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
      "title": "Restroom Access Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-18T04:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Restroom Access Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-18T04:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide an individual with an eligible medical condition access to employee restroom facilities of a retail establishment under certain conditions, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-18T04:18:17Z"
    }
  ]
}
```
