# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4112?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/4112
- Title: Congressional Review Reform Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 4112
- Origin chamber: House
- Introduced date: 2025-06-24
- Update date: 2025-07-21T15:25:29Z
- Update date including text: 2025-07-21T15:25:29Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-24: Introduced in House
- 2025-06-24 - IntroReferral: Introduced in House
- 2025-06-24 - IntroReferral: Introduced in House
- 2025-06-24 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-06-24 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-06-24: Introduced in House

## Actions

- 2025-06-24 - IntroReferral: Introduced in House
- 2025-06-24 - IntroReferral: Introduced in House
- 2025-06-24 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-06-24 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-24",
    "latestAction": {
      "actionDate": "2025-06-24",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/4112",
    "number": "4112",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "S001228",
        "district": "2",
        "firstName": "Derek",
        "fullName": "Rep. Schmidt, Derek [R-KS-2]",
        "lastName": "Schmidt",
        "party": "R",
        "state": "KS"
      }
    ],
    "title": "Congressional Review Reform Act of 2025",
    "type": "HR",
    "updateDate": "2025-07-21T15:25:29Z",
    "updateDateIncludingText": "2025-07-21T15:25:29Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-24",
      "committees": {
        "item": {
          "name": "Rules Committee",
          "systemCode": "hsru00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-24",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-24",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-24",
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
          "date": "2025-06-24T14:01:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Rules Committee",
      "systemCode": "hsru00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-06-24T14:01:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "H001096",
      "district": "0",
      "firstName": "Harriet",
      "fullName": "Rep. Hageman, Harriet M. [R-WY-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Hageman",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-06-24",
      "state": "WY"
    },
    {
      "bioguideId": "B001302",
      "district": "5",
      "firstName": "Andy",
      "fullName": "Rep. Biggs, Andy [R-AZ-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2025-06-24",
      "state": "AZ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4112ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4112\nIN THE HOUSE OF REPRESENTATIVES\nJune 24, 2025 Mr. Schmidt (for himself, Ms. Hageman , and Mr. Biggs of Arizona ) introduced the following bill; which was referred to the Committee on the Judiciary , and in addition to the Committee on Rules , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend chapter 8 of title 5, United States Code, to provide for additional time for Congress to disapprove of rules.\n#### 1. Short title\nThis Act may be cited as the Congressional Review Reform Act of 2025 .\n#### 2. Amendments to the Congressional Review Act\nChapter 8 of title 5, United States Code, is amended as follows:\n**(1)**\nIn section 801\u2014\n**(A)**\nby striking subsection (d); and\n**(B)**\nby redesignating subsections (e) through (g) as subsections (d) through (f), respectively.\n**(2)**\nIn section 802\u2014\n**(A)**\nin subsection (a), to read as follows:\n(a) For purposes of this section, the term joint resolution means only a joint resolution introduced after the report referred to in section 801(a)(1)(A) is received by Congress, the matter after the resolving clause of which is as follows: That Congress disapproves the rule submitted by the ____ relating to ____, and such rule shall have no force or effect. (The blank spaces being appropriately filled in). ;\n**(B)**\nby striking subsection (e); and\n**(C)**\nby redesignating subsections (f) and (g) as subsections (e) and (f), respectively.",
      "versionDate": "2025-06-24",
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
        "name": "Congress",
        "updateDate": "2025-07-21T15:25:29Z"
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
      "date": "2025-06-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4112ih.xml"
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
      "title": "Congressional Review Reform Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-08T07:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Congressional Review Reform Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-08T07:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend chapter 8 of title 5, United States Code, to provide for additional time for Congress to disapprove of rules.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-08T07:18:49Z"
    }
  ]
}
```
