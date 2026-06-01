# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2579?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2579
- Title: Reduce Duplication and Improve Access to Work Act
- Congress: 119
- Bill type: HR
- Bill number: 2579
- Origin chamber: House
- Introduced date: 2025-04-01
- Update date: 2026-02-04T04:26:31Z
- Update date including text: 2026-02-04T04:26:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-01: Introduced in House
- 2025-04-01 - IntroReferral: Introduced in House
- 2025-04-01 - IntroReferral: Introduced in House
- 2025-04-01 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-04-01: Introduced in House

## Actions

- 2025-04-01 - IntroReferral: Introduced in House
- 2025-04-01 - IntroReferral: Introduced in House
- 2025-04-01 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-01",
    "latestAction": {
      "actionDate": "2025-04-01",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2579",
    "number": "2579",
    "originChamber": "House",
    "policyArea": {
      "name": "Social Welfare"
    },
    "sponsors": [
      {
        "bioguideId": "S001199",
        "district": "11",
        "firstName": "Lloyd",
        "fullName": "Rep. Smucker, Lloyd [R-PA-11]",
        "lastName": "Smucker",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "Reduce Duplication and Improve Access to Work Act",
    "type": "HR",
    "updateDate": "2026-02-04T04:26:31Z",
    "updateDateIncludingText": "2026-02-04T04:26:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-01",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-04-01",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-01",
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
          "date": "2025-04-01T14:01:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "bioguideId": "V000134",
      "district": "24",
      "firstName": "Beth",
      "fullName": "Rep. Van Duyne, Beth [R-TX-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Duyne",
      "party": "R",
      "sponsorshipDate": "2025-04-01",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2579ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2579\nIN THE HOUSE OF REPRESENTATIVES\nApril 1, 2025 Mr. Smucker (for himself and Ms. Van Duyne ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend part A of title IV of the Social Security Act to allow States to transfer a limited amount of funds provided under the program of block grants to States for temporary assistance for needy families, for use under title I of the Workforce Innovation and Opportunity Act.\n#### 1. Short title\nThis Act may be cited as the Reduce Duplication and Improve Access to Work Act .\n#### 2. Allowing transfers to support workforce development\n##### (a) In general\nSection 404(d) of the Social Security Act ( 42 U.S.C. 604(d) ) is amended\u2014\n**(1)**\nin paragraph (1), by adding at the end the following:\n(C) Title I of the Workforce Innovation and Opportunity Act. ;\n**(2)**\nin paragraph (2)\u2014\n**(A)**\nin the heading, by striking subtitle 1 and inserting subtitle a ; and\n**(B)**\nin subparagraph (A), by striking subtitle 1 and inserting subtitle A ; and\n**(3)**\nin paragraph (3)\u2014\n**(A)**\nin subparagraph (B)\u2014\n**(i)**\nin the heading, by striking 1 of title xx and inserting a of title xx and title i of WIOA ; and\n**(ii)**\nby striking 1 of title XX and inserting A of title XX or title I of the Workforce Innovation and Opportunity Act ; and\n**(B)**\nby adding at the end the following:\n(C) Funds transferred to title I of WIOA program (i) Limitation on reservation of funds In the case of funds transferred under paragraph (1)(C) of this subsection, not more than 15 percent of the funds shall be reserved for statewide workforce investment activities referred to in section 128(a)(1) of the Workforce Innovation and Opportunity Act. (ii) Submission of combined State plan under WIOA If a State intends to transfer funds under paragraph (1)(C) of this subsection, the State shall\u2014 (I) submit to the Secretary and the Secretary of Labor a combined State plan pursuant to section 103 of the Workforce Innovation and Opportunity Act that covers the State program to be carried out pursuant to this part; and (II) in doing so, apply section 102(c)(3) of such Act to the programs referred to in section 103(a)(2)(B) of such Act covered by the combined plan. .\n##### (b) Effective date\nThe amendments made by subsection (a) shall take effect on October 1, 2026.",
      "versionDate": "2025-04-01",
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
        "name": "Social Welfare",
        "updateDate": "2025-04-08T16:30:27Z"
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
      "date": "2025-04-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2579ih.xml"
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
      "title": "Reduce Duplication and Improve Access to Work Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-08T10:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Reduce Duplication and Improve Access to Work Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-08T10:53:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend part A of title IV of the Social Security Act to allow States to transfer a limited amount of funds provided under the program of block grants to States for temporary assistance for needy families, for use under title I of the Workforce Innovation and Opportunity Act.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-08T10:48:19Z"
    }
  ]
}
```
