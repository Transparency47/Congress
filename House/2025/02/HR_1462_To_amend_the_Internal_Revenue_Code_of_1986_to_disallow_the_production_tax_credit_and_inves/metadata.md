# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1462?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/1462
- Title: To amend the Internal Revenue Code of 1986 to disallow the production tax credit and investment tax credit for offshore wind facilities placed in service in the inland navigable waters of the United States or the coastal waters of the United States.
- Congress: 119
- Bill type: HR
- Bill number: 1462
- Origin chamber: House
- Introduced date: 2025-02-21
- Update date: 2025-05-09T14:20:57Z
- Update date including text: 2025-05-09T14:20:57Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-02-21: Introduced in House
- 2025-02-21 - IntroReferral: Introduced in House
- 2025-02-21 - IntroReferral: Introduced in House
- 2025-02-21 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-02-21: Introduced in House

## Actions

- 2025-02-21 - IntroReferral: Introduced in House
- 2025-02-21 - IntroReferral: Introduced in House
- 2025-02-21 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-21",
    "latestAction": {
      "actionDate": "2025-02-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/1462",
    "number": "1462",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "F000246",
        "district": "4",
        "firstName": "Pat",
        "fullName": "Rep. Fallon, Pat [R-TX-4]",
        "lastName": "Fallon",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "To amend the Internal Revenue Code of 1986 to disallow the production tax credit and investment tax credit for offshore wind facilities placed in service in the inland navigable waters of the United States or the coastal waters of the United States.",
    "type": "HR",
    "updateDate": "2025-05-09T14:20:57Z",
    "updateDateIncludingText": "2025-05-09T14:20:57Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-21",
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
      "actionDate": "2025-02-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-21",
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
          "date": "2025-02-21T20:30:35Z",
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
      "bioguideId": "G000589",
      "district": "5",
      "firstName": "Lance",
      "fullName": "Rep. Gooden, Lance [R-TX-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Gooden",
      "party": "R",
      "sponsorshipDate": "2025-02-21",
      "state": "TX"
    },
    {
      "bioguideId": "G000603",
      "district": "26",
      "firstName": "Brandon",
      "fullName": "Rep. Gill, Brandon [R-TX-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Gill",
      "party": "R",
      "sponsorshipDate": "2025-02-24",
      "state": "TX"
    },
    {
      "bioguideId": "H001096",
      "district": "0",
      "firstName": "Harriet",
      "fullName": "Rep. Hageman, Harriet M. [R-WY-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Hageman",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-03-06",
      "state": "WY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1462ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1462\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 21, 2025 Mr. Fallon (for himself and Mr. Gooden ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to disallow the production tax credit and investment tax credit for offshore wind facilities placed in service in the inland navigable waters of the United States or the coastal waters of the United States.\n#### 1. Disallowance of investment tax credit and clean electricity production credit for certain offshore wind facilities\n##### (a) Investment tax credit\nSection 48(a)(5) of the Internal Revenue Code of 1986 is amended by striking subparagraph (F).\n##### (b) Renewable resources production tax credit\nSection 45(d)(1) of such Code is amended by striking the period at the end and inserting , or any facility which is located in the inland navigable waters of the United States or in the coastal waters of the United States .\n##### (c) Clean electricity production tax credit\nSection 45Y(b)(1) of such Code is amended by adding at the end the following new subparagraph:\n(E) Certain offshore wind facilities not treated as qualified facilities (i) In general The term qualified facility shall not include any disqualified offshore wind facility. (ii) Disqualified offshore wind facility For purposes of this subparagraph, the term disqualified offshore wind facility means an offshore wind facility which is located in the inland navigable waters of the United States or in the coastal waters of the United States. .\n##### (d) Effective date\nThe amendment made by this section shall apply to energy produced and property placed in service after December 31, 2025.",
      "versionDate": "2025-02-21",
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
        "actionDate": "2025-03-18",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "2187",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "To amend the Internal Revenue Code of 1986 to disallow the production tax credit and investment tax credit for offshore wind facilities placed in service in the inland navigable waters of the United States or the coastal waters of the United States.",
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
        "updateDate": "2025-05-07T14:01:43Z"
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
      "date": "2025-02-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1462ih.xml"
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
      "title": "To amend the Internal Revenue Code of 1986 to disallow the production tax credit and investment tax credit for offshore wind facilities placed in service in the inland navigable waters of the United States or the coastal waters of the United States.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-17T12:48:27Z"
    },
    {
      "title": "To amend the Internal Revenue Code of 1986 to disallow the production tax credit and investment tax credit for offshore wind facilities placed in service in the inland navigable waters of the United States or the coastal waters of the United States.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-22T09:06:26Z"
    }
  ]
}
```
