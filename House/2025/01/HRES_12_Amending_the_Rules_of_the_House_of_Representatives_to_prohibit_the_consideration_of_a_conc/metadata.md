# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/12?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/12
- Title: Stay on Schedule (S.O.S.) Resolution
- Congress: 119
- Bill type: HRES
- Bill number: 12
- Origin chamber: House
- Introduced date: 2025-01-03
- Update date: 2025-11-20T09:06:42Z
- Update date including text: 2025-11-20T09:06:42Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-03: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on Rules.
- 2025-01-03 - Committee: Submitted in House
- 2025-01-03 - IntroReferral: Submitted in House
- Latest action: 2025-01-03: Submitted in House

## Actions

- 2025-01-03 - IntroReferral: Referred to the House Committee on Rules.
- 2025-01-03 - Committee: Submitted in House
- 2025-01-03 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-03",
    "latestAction": {
      "actionDate": "2025-01-03",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/12",
    "number": "12",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "W000804",
        "district": "1",
        "firstName": "Robert",
        "fullName": "Rep. Wittman, Robert J. [R-VA-1]",
        "lastName": "Wittman",
        "party": "R",
        "state": "VA"
      }
    ],
    "title": "Stay on Schedule (S.O.S.) Resolution",
    "type": "HRES",
    "updateDate": "2025-11-20T09:06:42Z",
    "updateDateIncludingText": "2025-11-20T09:06:42Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-03",
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
      "text": "Referred to the House Committee on Rules.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H12100",
      "actionDate": "2025-01-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "Committee"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-01-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
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
          "date": "2025-01-03T16:17:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Rules Committee",
      "systemCode": "hsru00",
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
      "bioguideId": "O000177",
      "district": "3",
      "firstName": "Robert",
      "fullName": "Rep. Onder, Robert F. [R-MO-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Onder",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-10-08",
      "state": "MO"
    },
    {
      "bioguideId": "K000399",
      "district": "2",
      "firstName": "Jennifer",
      "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Kiggans",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-11-19",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres12ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 12\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 3, 2025 Mr. Wittman submitted the following resolution; which was referred to the Committee on Rules\nRESOLUTION\nAmending the Rules of the House of Representatives to prohibit the consideration of a concurrent resolution to provide for a recess of the House after July 31 of any year unless the House has approved each regular appropriation bill for the next fiscal year.\n#### 1. Short title\nThis resolution may be cited as the Stay on Schedule (S.O.S.) Resolution .\n#### 2. Prohibiting recess during August until approval of all regular appropriation bills\nRule XXI of the Rules of the House of Representatives is amended by adding at the end the following new clause:\nConcurrent resolution providing for adjournment during August 13. If by July 31 of any calendar year the House has not passed each of the regular appropriation bills for the fiscal year which begins on October 1 of that calendar year, it shall not be in order to consider a concurrent resolution to provide that the House stand adjourned during any day occurring during August of that calendar year until the House has passed each such bill. For purposes of this clause, term regular appropriation bill means any annual appropriation bill which is under the jurisdiction of a single subcommittee of the Committee on Appropriations of the House of Representatives (as may be provided under the Rules for the fiscal year involved). .",
      "versionDate": "2025-01-03",
      "versionType": "IH"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": {
        "item": [
          {
            "name": "Appropriations",
            "updateDate": "2025-02-24T19:50:31Z"
          },
          {
            "name": "Congressional operations and organization",
            "updateDate": "2025-02-24T19:50:31Z"
          },
          {
            "name": "House of Representatives",
            "updateDate": "2025-02-24T19:50:31Z"
          },
          {
            "name": "Legislative rules and procedure",
            "updateDate": "2025-02-24T19:50:31Z"
          }
        ]
      },
      "policyArea": {
        "name": "Congress",
        "updateDate": "2025-02-18T20:29:26Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-03",
    "originChamber": "House",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119hres12",
          "measure-number": "12",
          "measure-type": "hres",
          "orig-publish-date": "2025-01-03",
          "originChamber": "HOUSE",
          "update-date": "2025-02-25"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres12v00",
            "update-date": "2025-02-25"
          },
          "action-date": "2025-01-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Stay on Schedule (S.O.S.) Resolution</strong></p><p>This resolution prevents the House of Representatives from adjourning in August until it has passed regular appropriations legislation for the fiscal year beginning in October.\u00a0</p><p>The resolution specifies that it is out of order for the House to consider a concurrent resolution for its adjournment during any day in August until the House has passed all of the regular appropriations bills.</p>"
        },
        "title": "Stay on Schedule (S.O.S.) Resolution"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres12.xml",
    "summary": {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Stay on Schedule (S.O.S.) Resolution</strong></p><p>This resolution prevents the House of Representatives from adjourning in August until it has passed regular appropriations legislation for the fiscal year beginning in October.\u00a0</p><p>The resolution specifies that it is out of order for the House to consider a concurrent resolution for its adjournment during any day in August until the House has passed all of the regular appropriations bills.</p>",
      "updateDate": "2025-02-25",
      "versionCode": "id119hres12"
    },
    "title": "Stay on Schedule (S.O.S.) Resolution"
  },
  "summaries": [
    {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Stay on Schedule (S.O.S.) Resolution</strong></p><p>This resolution prevents the House of Representatives from adjourning in August until it has passed regular appropriations legislation for the fiscal year beginning in October.\u00a0</p><p>The resolution specifies that it is out of order for the House to consider a concurrent resolution for its adjournment during any day in August until the House has passed all of the regular appropriations bills.</p>",
      "updateDate": "2025-02-25",
      "versionCode": "id119hres12"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres12ih.xml"
        }
      ],
      "type": "IH"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Stay on Schedule (S.O.S.) Resolution",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-07T14:38:47Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Amending the Rules of the House of Representatives to prohibit the consideration of a concurrent resolution to provide for a recess of the House after July 31 of any year unless the House has approved each regular appropriation bill for the next fiscal year.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-07T14:38:47Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Stay on Schedule (S.O.S.) Resolution",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-01-06T13:23:14Z"
    }
  ]
}
```
