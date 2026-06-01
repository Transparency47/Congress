# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/11?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hres/11
- Title: Fair Representation Amendment
- Congress: 119
- Bill type: HRES
- Bill number: 11
- Origin chamber: House
- Introduced date: 2025-01-03
- Update date: 2025-01-30T13:09:31Z
- Update date including text: 2025-01-30T13:09:31Z
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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hres/11",
    "number": "11",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "D000626",
        "district": "8",
        "firstName": "Warren",
        "fullName": "Rep. Davidson, Warren [R-OH-8]",
        "lastName": "Davidson",
        "party": "R",
        "state": "OH"
      }
    ],
    "title": "Fair Representation Amendment",
    "type": "HRES",
    "updateDate": "2025-01-30T13:09:31Z",
    "updateDateIncludingText": "2025-01-30T13:09:31Z"
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
          "date": "2025-01-03T16:15:50Z",
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
      "bioguideId": "G000565",
      "district": "9",
      "firstName": "Paul",
      "fullName": "Rep. Gosar, Paul A. [R-AZ-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Gosar",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres11ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 11\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 3, 2025 Mr. Davidson submitted the following resolution; which was referred to the Committee on Rules\nRESOLUTION\nAuthorizing and directing certain authorizing committees to review laws within their jurisdiction and submit to the Committee on Oversight and Government Reform changes in such laws necessary to eliminate excessive Executive Branch discretion in the application of those laws.\n#### 1. Short title\nThis resolution may be cited as the Fair Representation Amendment .\n#### 2. Authorizing committee actions\n##### (a) In general\nWithin 6 months after the date of adoption of this resolution, the committees listed in subsection (b) shall review laws within their jurisdiction and submit to the Committee on Oversight and Government Reform changes in those laws sufficient to eliminate excessive Executive Branch discretion in the application of those laws.\n##### (b) Committees subject to subsection (a)\nThe following committees shall comply with subsection (a):\n**(1)**\nCommittee on Agriculture.\n**(2)**\nCommittee on Armed Services.\n**(3)**\nCommittee on the Budget.\n**(4)**\nCommittee on Energy and Commerce.\n**(5)**\nCommittee on Education and the Workforce.\n**(6)**\nCommittee on Financial Services.\n**(7)**\nCommittee on Foreign Affairs.\n**(8)**\nCommittee on the Judiciary.\n**(9)**\nCommittee on Natural Resources.\n**(10)**\nCommittee on Oversight and Government Reform.\n**(11)**\nCommittee on Science, Space, and Technology.\n**(12)**\nCommittee on Small Business.\n**(13)**\nCommittee on Transportation and Infrastructure.\n**(14)**\nCommittee on Veterans Affairs.\n**(15)**\nCommittee on Ways and Means.\n**(16)**\nPermanent Select Committee on Intelligence.\n#### 3. Legislative procedure\nUpon receiving all the recommendations made pursuant to section 1, the Committee on Oversight and Government Reform shall expeditiously report legislation carrying out all such recommendations without any substantive revision. The short title of this legislation shall be the Article One Restoration Act.",
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
            "name": "Congressional committees",
            "updateDate": "2025-01-15T18:56:06Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-01-15T18:56:16Z"
          },
          {
            "name": "Congressional-executive branch relations",
            "updateDate": "2025-01-15T18:56:21Z"
          },
          {
            "name": "House Committee on Agriculture",
            "updateDate": "2025-01-15T18:56:26Z"
          },
          {
            "name": "House Committee on Appropriations",
            "updateDate": "2025-01-15T18:56:35Z"
          },
          {
            "name": "House Committee on Armed Services",
            "updateDate": "2025-01-15T18:56:52Z"
          },
          {
            "name": "House Committee on Education and Workforce",
            "updateDate": "2025-01-30T13:09:31Z"
          },
          {
            "name": "House Committee on Energy and Commerce",
            "updateDate": "2025-01-15T18:57:04Z"
          },
          {
            "name": "House Committee on Financial Services",
            "updateDate": "2025-01-15T18:57:17Z"
          },
          {
            "name": "House Committee on Foreign Affairs",
            "updateDate": "2025-01-15T18:57:23Z"
          },
          {
            "name": "House Committee on Natural Resources",
            "updateDate": "2025-01-15T18:57:35Z"
          },
          {
            "name": "House Committee on Oversight and Government Reform",
            "updateDate": "2025-01-15T18:57:41Z"
          },
          {
            "name": "House Committee on Science, Space, and Technology",
            "updateDate": "2025-01-15T18:57:46Z"
          },
          {
            "name": "House Committee on Small Business",
            "updateDate": "2025-01-15T18:57:52Z"
          },
          {
            "name": "House Committee on Transportation and Infrastructure",
            "updateDate": "2025-01-15T18:57:57Z"
          },
          {
            "name": "House Committee on Veterans' Affairs",
            "updateDate": "2025-01-15T18:58:02Z"
          },
          {
            "name": "House Committee on Ways and Means",
            "updateDate": "2025-01-15T18:58:08Z"
          },
          {
            "name": "House Committee on the Budget",
            "updateDate": "2025-01-15T18:56:58Z"
          },
          {
            "name": "House Committee on the Judiciary",
            "updateDate": "2025-01-15T18:57:29Z"
          },
          {
            "name": "House Permanent Select Committee on Intelligence",
            "updateDate": "2025-01-15T18:58:13Z"
          },
          {
            "name": "Legislative rules and procedure",
            "updateDate": "2025-01-15T18:58:18Z"
          }
        ]
      },
      "policyArea": {
        "name": "Congress",
        "updateDate": "2025-01-08T18:50:42Z"
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
          "measure-id": "id119hres11",
          "measure-number": "11",
          "measure-type": "hres",
          "orig-publish-date": "2025-01-03",
          "originChamber": "HOUSE",
          "update-date": "2025-01-16"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres11v00",
            "update-date": "2025-01-16"
          },
          "action-date": "2025-01-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Fair Representation Amendment</strong></p><p>This resolution directs specified House committees to conduct a comprehensive review of laws within their jurisdiction and to recommend changes to eliminate excessive executive branch discretion in the application of those laws. Thereafter, the Committee on Oversight and Government Reform must report legislation containing all such recommendations with the short title<em>\u00a0Article One Restoration Act</em>.</p><p>The requirement applies to the following House committees:</p><p>Agriculture<br/>Armed Services<br/>Budget<br/>Education and Workforce<br/>Energy and Commerce<br/>Financial Services<br/>Foreign Affairs<br/>Judiciary<br/>Natural Resources<br/>Oversight and Government Reform<br/>Science, Space, and Technology<br/>Small Business<br/>Transportation and Infrastructure<br/>Veterans\u2019 Affairs<br/>Ways and Means<br/>Permanent Select Committee on Intelligence</p>"
        },
        "title": "Fair Representation Amendment"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres11.xml",
    "summary": {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Fair Representation Amendment</strong></p><p>This resolution directs specified House committees to conduct a comprehensive review of laws within their jurisdiction and to recommend changes to eliminate excessive executive branch discretion in the application of those laws. Thereafter, the Committee on Oversight and Government Reform must report legislation containing all such recommendations with the short title<em>\u00a0Article One Restoration Act</em>.</p><p>The requirement applies to the following House committees:</p><p>Agriculture<br/>Armed Services<br/>Budget<br/>Education and Workforce<br/>Energy and Commerce<br/>Financial Services<br/>Foreign Affairs<br/>Judiciary<br/>Natural Resources<br/>Oversight and Government Reform<br/>Science, Space, and Technology<br/>Small Business<br/>Transportation and Infrastructure<br/>Veterans\u2019 Affairs<br/>Ways and Means<br/>Permanent Select Committee on Intelligence</p>",
      "updateDate": "2025-01-16",
      "versionCode": "id119hres11"
    },
    "title": "Fair Representation Amendment"
  },
  "summaries": [
    {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Fair Representation Amendment</strong></p><p>This resolution directs specified House committees to conduct a comprehensive review of laws within their jurisdiction and to recommend changes to eliminate excessive executive branch discretion in the application of those laws. Thereafter, the Committee on Oversight and Government Reform must report legislation containing all such recommendations with the short title<em>\u00a0Article One Restoration Act</em>.</p><p>The requirement applies to the following House committees:</p><p>Agriculture<br/>Armed Services<br/>Budget<br/>Education and Workforce<br/>Energy and Commerce<br/>Financial Services<br/>Foreign Affairs<br/>Judiciary<br/>Natural Resources<br/>Oversight and Government Reform<br/>Science, Space, and Technology<br/>Small Business<br/>Transportation and Infrastructure<br/>Veterans\u2019 Affairs<br/>Ways and Means<br/>Permanent Select Committee on Intelligence</p>",
      "updateDate": "2025-01-16",
      "versionCode": "id119hres11"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres11ih.xml"
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
      "title": "Fair Representation Amendment",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-07T14:39:08Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Authorizing and directing certain authorizing committees to review laws within their jurisdiction and submit to the Committee on Oversight and Government Reform changes in such laws necessary to eliminate excessive Executive Branch discretion in the application of those laws.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-07T14:39:08Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Fair Representation Amendment",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-01-06T13:23:14Z"
    }
  ]
}
```
