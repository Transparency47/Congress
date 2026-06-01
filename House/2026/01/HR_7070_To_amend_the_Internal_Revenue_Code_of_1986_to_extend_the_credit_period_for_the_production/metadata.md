# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7070?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7070
- Title: To amend the Internal Revenue Code of 1986 to extend the credit period for the production of refined coal, and for other purposes.
- Congress: 119
- Bill type: HR
- Bill number: 7070
- Origin chamber: House
- Introduced date: 2026-01-14
- Update date: 2026-04-28T08:06:49Z
- Update date including text: 2026-04-28T08:06:49Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-01-14: Introduced in House
- 2026-01-14 - IntroReferral: Introduced in House
- 2026-01-14 - IntroReferral: Introduced in House
- 2026-01-14 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2026-01-14: Introduced in House

## Actions

- 2026-01-14 - IntroReferral: Introduced in House
- 2026-01-14 - IntroReferral: Introduced in House
- 2026-01-14 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-14",
    "latestAction": {
      "actionDate": "2026-01-14",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7070",
    "number": "7070",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "M001205",
        "district": "1",
        "firstName": "Carol",
        "fullName": "Rep. Miller, Carol D. [R-WV-1]",
        "lastName": "Miller",
        "party": "R",
        "state": "WV"
      }
    ],
    "title": "To amend the Internal Revenue Code of 1986 to extend the credit period for the production of refined coal, and for other purposes.",
    "type": "HR",
    "updateDate": "2026-04-28T08:06:49Z",
    "updateDateIncludingText": "2026-04-28T08:06:49Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-14",
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
      "actionDate": "2026-01-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-14",
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
          "date": "2026-01-14T15:04:20Z",
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
      "bioguideId": "G000568",
      "district": "9",
      "firstName": "H.",
      "fullName": "Rep. Griffith, H. Morgan [R-VA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Griffith",
      "middleName": "Morgan",
      "party": "R",
      "sponsorshipDate": "2026-04-27",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7070ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7070\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 14, 2026 Mrs. Miller of West Virginia introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to extend the credit period for the production of refined coal, and for other purposes.\n#### 1. Extension of credit period for refined coal production\n##### (a) In general\nSection 45(e)(8)(A) of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nin clause (i), by striking during the 10-year period beginning on the date the facility was originally placed in service and inserting before January 1, 2033 , and\n**(2)**\nin clause (ii), by amending subclause (II) to read as follows:\n(II) before January 1, 2033, and during such taxable year. .\n##### (b) Conforming amendments\n**(1)**\nSection 45(e)(8)(D) of such Code is amended\u2014\n**(A)**\nin clause (ii)\u2014\n**(i)**\nby striking subclause (II), and\n**(ii)**\nby redesignating subclause (III) as subclause (II),\n**(B)**\nby striking clause (iii), and\n**(C)**\nby redesignating clause (iv) as clause (iii).\n**(2)**\nSection 45(d)(8)(A) of such Code is amended by inserting which allows such facility to produce steel industry fuel after any modification to a facility .\n##### (c) Effective date\nThe amendments made by this section shall apply to refined coal produced and sold after December 31, 2025.",
      "versionDate": "2026-01-14",
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
        "actionDate": "2026-03-17",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "4112",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "A bill to amend the Internal Revenue Code of 1986 to extend the credit period for the production of refined coal, and for other purposes.",
      "type": "S"
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
        "updateDate": "2026-02-04T22:58:34Z"
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
      "date": "2026-01-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7070ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to extend the credit period for the production of refined coal, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-03T11:03:56Z"
    },
    {
      "title": "To amend the Internal Revenue Code of 1986 to extend the credit period for the production of refined coal, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-15T09:06:22Z"
    }
  ]
}
```
