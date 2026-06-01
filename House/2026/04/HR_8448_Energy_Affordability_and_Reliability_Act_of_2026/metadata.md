# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8448?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8448
- Title: Energy Affordability and Reliability Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8448
- Origin chamber: House
- Introduced date: 2026-04-22
- Update date: 2026-04-28T15:09:36Z
- Update date including text: 2026-04-28T15:09:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-22: Introduced in House
- 2026-04-22 - IntroReferral: Introduced in House
- 2026-04-22 - IntroReferral: Introduced in House
- 2026-04-22 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2026-04-22: Introduced in House

## Actions

- 2026-04-22 - IntroReferral: Introduced in House
- 2026-04-22 - IntroReferral: Introduced in House
- 2026-04-22 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-22",
    "latestAction": {
      "actionDate": "2026-04-22",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8448",
    "number": "8448",
    "originChamber": "House",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "L000599",
        "district": "17",
        "firstName": "Michael",
        "fullName": "Rep. Lawler, Michael [R-NY-17]",
        "lastName": "Lawler",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "Energy Affordability and Reliability Act of 2026",
    "type": "HR",
    "updateDate": "2026-04-28T15:09:36Z",
    "updateDateIncludingText": "2026-04-28T15:09:36Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-22",
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
      "actionDate": "2026-04-22",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-22",
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
          "date": "2026-04-22T15:03:20Z",
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
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8448ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8448\nIN THE HOUSE OF REPRESENTATIVES\nApril 22, 2026 Mr. Lawler (for himself and Mr. Gottheimer ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo establish an Office of Energy Affordability within the Department of Energy, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Energy Affordability and Reliability Act of 2026 .\n#### 2. Establishment of Office of Energy Affordability\n##### (a) Establishment\nNot later than 180 days after the date of the enactment of this Act, the Secretary of Energy shall establish within the Office of Policy of the Department of Energy an office to be known as the Office of Energy Affordability (in this section referred to as the Office ).\n##### (b) Duties\nThe duties of the Office shall be to\u2014\n**(1)**\nreview each proposed regulation or policy of the Department of Energy that would require, or otherwise relates to, a transition between types of energy or sources of energy, to determine whether such regulation or policy\u2014\n**(A)**\nincorporates transparent and rigorous analysis of the short-term and long-term effects of such regulation or policy on energy affordability and on related economic costs;\n**(B)**\nincludes strategies to ensure that such regulation or policy does not negatively affect energy affordability and that related economic costs are mitigated; and\n**(C)**\nsupports reliable access to energy by consumers and promotes cost-effective energy solutions; and\n**(2)**\nprovide advice and guidance based on the results of such review.\n##### (c) Timely review; no prevention of issuance\nIn carrying out the duties under subsection (b), the Office\u2014\n**(1)**\nshall complete the review of each proposed regulation or policy pursuant to such subsection by not later than 30 days after the date on which the Office receives notice of such proposed regulation or policy; and\n**(2)**\nmay not prevent the issuance of any regulation or policy.\n##### (d) Annual reports\nOn an annual basis, the Office shall submit to the appropriate congressional committees a report containing, with respect to any regulation or policy specified in subsection (b) proposed to be issued or issued during the year covered by such report\u2014\n**(1)**\nan analysis of the effects specified in subsection (b)(1)(A); and\n**(2)**\nrecommendations for the strategies specified in subsection (b)(1)(B).\n##### (e) Report on effectiveness of Office\nNot later than 5 years after the date on which the Office is established under subsection (a), the Secretary of Energy shall submit to the appropriate congressional committees a report on the effectiveness of the Office.\n##### (f) Definitions\nIn this section\u2014\n**(1) Appropriate congressional committees**\nThe term appropriate congressional committees means\u2014\n**(A)**\nthe Committee on Energy and Commerce and the Committee on Appropriations of the House of Representatives; and\n**(B)**\nthe Committee on Energy and Natural Resources and the Committee on Appropriations of the Senate.\n**(2) Energy affordability**\nThe term energy affordability means the cost of energy transmitted to a residential, commercial, or industrial consumer proportional to the income or operational costs of such consumer.",
      "versionDate": "2026-04-22",
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
        "updateDate": "2026-04-28T15:09:35Z"
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
      "date": "2026-04-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8448ih.xml"
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
      "title": "Energy Affordability and Reliability Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-23T09:38:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Energy Affordability and Reliability Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-23T09:38:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish an Office of Energy Affordability within the Department of Energy, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-23T09:33:27Z"
    }
  ]
}
```
