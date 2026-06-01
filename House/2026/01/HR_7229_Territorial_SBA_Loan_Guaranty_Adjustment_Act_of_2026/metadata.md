# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7229?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7229
- Title: Territorial SBA Loan Guaranty Adjustment Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7229
- Origin chamber: House
- Introduced date: 2026-01-22
- Update date: 2026-03-06T09:07:08Z
- Update date including text: 2026-03-06T09:07:08Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-01-22: Introduced in House
- 2026-01-22 - IntroReferral: Introduced in House
- 2026-01-22 - IntroReferral: Introduced in House
- 2026-01-22 - IntroReferral: Referred to the House Committee on Small Business.
- Latest action: 2026-01-22: Introduced in House

## Actions

- 2026-01-22 - IntroReferral: Introduced in House
- 2026-01-22 - IntroReferral: Introduced in House
- 2026-01-22 - IntroReferral: Referred to the House Committee on Small Business.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-22",
    "latestAction": {
      "actionDate": "2026-01-22",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7229",
    "number": "7229",
    "originChamber": "House",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "M001219",
        "district": "",
        "firstName": "James",
        "fullName": "Del. Moylan, James C. [R-GU-At Large]",
        "lastName": "Moylan",
        "party": "R",
        "state": "GU"
      }
    ],
    "title": "Territorial SBA Loan Guaranty Adjustment Act of 2026",
    "type": "HR",
    "updateDate": "2026-03-06T09:07:08Z",
    "updateDateIncludingText": "2026-03-06T09:07:08Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-22",
      "committees": {
        "item": {
          "name": "Small Business Committee",
          "systemCode": "hssm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Small Business.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-01-22",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-22",
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
          "date": "2026-01-22T14:01:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Small Business Committee",
      "systemCode": "hssm00",
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
      "bioguideId": "K000404",
      "district": "0",
      "firstName": "Kimberlyn",
      "fullName": "Del. King-Hinds, Kimberlyn [R-MP-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "King-Hinds",
      "party": "R",
      "sponsorshipDate": "2026-01-22",
      "state": "MP"
    },
    {
      "bioguideId": "H001103",
      "district": "0",
      "firstName": "Pablo",
      "fullName": "Rescom. Hern\u00e1ndez, Pablo Jose [D-PR-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Hern\u00e1ndez",
      "middleName": "Jose",
      "party": "D",
      "sponsorshipDate": "2026-02-02",
      "state": "PR"
    },
    {
      "bioguideId": "R000600",
      "district": "0",
      "firstName": "Aumua Amata",
      "fullName": "Del. Radewagen, Aumua Amata Coleman [R-AS-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Radewagen",
      "middleName": "Coleman",
      "party": "R",
      "sponsorshipDate": "2026-03-05",
      "state": "AS"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7229ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7229\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 22, 2026 Mr. Moylan (for himself and Ms. King-Hinds ) introduced the following bill; which was referred to the Committee on Small Business\nA BILL\nTo amend the Small Business Act to provide for loan guarantees to certain small businesses, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Territorial SBA Loan Guaranty Adjustment Act of 2026 .\n#### 2. Loan guarantees for covered territory businesses\n##### (a) In general\nSection 7(a)(2) of the Small Business Act ( 15 U.S.C. 636(a)(2) ) is amended by adding at the end the following:\n(G) Participation in loan to covered territory business (i) In general Except as provided in clause (ii), in an agreement to participate in a loan to a covered territory business on a deferred basis under this subsection, the participation by the Administration shall be 90 percent. (ii) Exceptions Clause (i) shall not apply with respect to a loan under paragraph (9), (14)(A), (16), (31), or (34), or under a pilot program carried out pursuant to paragraph (25). .\n##### (b) Conforming amendment\nSection 7(a)(2)(A) of such Act is amended by striking and (F) and inserting (F), and (G) .",
      "versionDate": "2026-01-22",
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
        "name": "Commerce",
        "updateDate": "2026-02-12T15:26:36Z"
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
      "date": "2026-01-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7229ih.xml"
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
      "title": "Territorial SBA Loan Guaranty Adjustment Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-06T03:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Territorial SBA Loan Guaranty Adjustment Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-06T03:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Small Business Act to provide for loan guarantees to certain small businesses, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-06T03:18:25Z"
    }
  ]
}
```
