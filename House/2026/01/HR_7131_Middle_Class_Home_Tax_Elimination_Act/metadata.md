# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7131?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7131
- Title: Middle Class Home Tax Elimination Act
- Congress: 119
- Bill type: HR
- Bill number: 7131
- Origin chamber: House
- Introduced date: 2026-01-16
- Update date: 2026-02-06T16:03:01Z
- Update date including text: 2026-02-06T16:03:01Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-01-16: Introduced in House
- 2026-01-16 - IntroReferral: Introduced in House
- 2026-01-16 - IntroReferral: Introduced in House
- 2026-01-16 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2026-01-16: Introduced in House

## Actions

- 2026-01-16 - IntroReferral: Introduced in House
- 2026-01-16 - IntroReferral: Introduced in House
- 2026-01-16 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-16",
    "latestAction": {
      "actionDate": "2026-01-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7131",
    "number": "7131",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "F000471",
        "district": "5",
        "firstName": "Scott",
        "fullName": "Rep. Fitzgerald, Scott [R-WI-5]",
        "lastName": "Fitzgerald",
        "party": "R",
        "state": "WI"
      }
    ],
    "title": "Middle Class Home Tax Elimination Act",
    "type": "HR",
    "updateDate": "2026-02-06T16:03:01Z",
    "updateDateIncludingText": "2026-02-06T16:03:01Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-16",
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
      "actionDate": "2026-01-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-16",
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
          "date": "2026-01-16T20:00:20Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7131ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7131\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 16, 2026 Mr. Fitzgerald introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to eliminate the dollar limitations on the exclusion of gain from sales of principal residences, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Middle Class Home Tax Elimination Act .\n#### 2. Elimination of dollar limitations on exclusion of gain from sales of principal residences\n##### (a) In general\nSection 121(b) of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nby striking paragraphs (1), (2), and (4), and\n**(2)**\nby redesignating paragraphs (3) and (5) as paragraphs (1) and (2), respectively.\n##### (b) Conforming amendments\nSection 121(c) of such Code is amended\u2014\n**(1)**\nin paragraph (1), by striking , and subsection (b)(3) and all that follows through 2 years and inserting , and subsection (b)(1), shall not apply , and\n**(2)**\nin paragraph (2)(A)(ii), by striking subsection (b)(3) and inserting subsection (b)(1) .\n##### (c) Effective date\nThe amendments made by this section shall apply to sales and exchanges after the date of the enactment of this Act.",
      "versionDate": "2026-01-16",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2026-01-13",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "7034",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "To amend the Internal Revenue Code of 1986 to eliminate the dollar limitations on the exclusion of gain from sales of principal residences, and for other purposes.",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2026-01-21",
        "actionTime": "16:48:50",
        "text": "ASSUMING FIRST SPONSORSHIP - Mr. Alford asked unanimous consent that he may hereafter be considered as the first sponsor of H.R. 4327, a bill originally introduced by Representative Greene (GA), for the purpose of adding cosponsors and requesting reprintings pursuant to clause 7 of rule XII. Agreed to without objection."
      },
      "number": "4327",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "No Tax on Home Sales Act",
      "type": "HR"
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
        "name": "Taxation",
        "updateDate": "2026-02-04T22:59:34Z"
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
      "date": "2026-01-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7131ih.xml"
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
      "title": "Middle Class Home Tax Elimination Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-03T12:53:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Middle Class Home Tax Elimination Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-03T12:53:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to eliminate the dollar limitations on the exclusion of gain from sales of principal residences, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-03T12:48:34Z"
    }
  ]
}
```
