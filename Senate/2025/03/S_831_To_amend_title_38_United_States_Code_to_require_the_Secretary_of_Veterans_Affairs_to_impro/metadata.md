# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/831?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/831
- Title: REP VA Act
- Congress: 119
- Bill type: S
- Bill number: 831
- Origin chamber: Senate
- Introduced date: 2025-03-04
- Update date: 2025-11-18T20:05:16Z
- Update date including text: 2025-11-18T20:05:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-04: Introduced in Senate
- 2025-03-04 - IntroReferral: Introduced in Senate
- 2025-03-04 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2025-03-11 - Committee: Committee on Veterans' Affairs. Hearings held.
- 2025-07-30 - Committee: Committee on Veterans' Affairs. Ordered to be reported with an amendment in the nature of a substitute favorably.
- Latest action: 2025-03-04: Introduced in Senate

## Actions

- 2025-03-04 - IntroReferral: Introduced in Senate
- 2025-03-04 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2025-03-11 - Committee: Committee on Veterans' Affairs. Hearings held.
- 2025-07-30 - Committee: Committee on Veterans' Affairs. Ordered to be reported with an amendment in the nature of a substitute favorably.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-04",
    "latestAction": {
      "actionDate": "2025-03-04",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/831",
    "number": "831",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "S001198",
        "district": "",
        "firstName": "Dan",
        "fullName": "Sen. Sullivan, Dan [R-AK]",
        "lastName": "Sullivan",
        "party": "R",
        "state": "AK"
      }
    ],
    "title": "REP VA Act",
    "type": "S",
    "updateDate": "2025-11-18T20:05:16Z",
    "updateDateIncludingText": "2025-11-18T20:05:16Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-30",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Veterans' Affairs. Ordered to be reported with an amendment in the nature of a substitute favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-03-11",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Veterans' Affairs. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-03-04",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
        "item": [
          {
            "date": "2025-07-30T20:00:18Z",
            "name": "Markup By"
          },
          {
            "date": "2025-03-11T14:30:22Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-03-04T17:22:18Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Veterans' Affairs Committee",
      "systemCode": "ssva00",
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
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-03-04",
      "state": "HI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s831is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 831\nIN THE SENATE OF THE UNITED STATES\nMarch 4, 2025 Mr. Sullivan (for himself and Ms. Hirono ) introduced the following bill; which was read twice and referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to require the Secretary of Veterans Affairs to improve telephone communication by the Department of Veterans Affairs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Representing VA with Accuracy Act or the REP VA Act .\n#### 2. Improvement of telephone communication by Department of Veterans Affairs\n##### (a) In general\nChapter 63 of title 38, United States Code, is amended by adding at the end the following new section:\n6321. Telephone communication (a) Calls associated with Department Not later than January 1, 2026, the Secretary shall ensure that any call made to a veteran by an employee or contractor of the Department regarding services or benefits furnished by the Department\u2014 (1) is made from a single, well-known telephone number; and (2) uses caller identification branding that indicates to the veteran that the call is from or on behalf of the Department. (b) Call centers for health care appointments and referrals (1) In general Not later than January 1, 2026, the Secretary shall ensure that the Veterans Health Administration has at least one call center in each of the time zones specified in paragraph (2) to address concerns regarding appointments and referrals for health care under the laws administered by the Secretary. (2) Time zones specified The time zones specified in this paragraph are the following: (A) Eastern time. (B) Central time. (C) Mountain time. (D) Pacific time. (E) Alaska time. (F) Hawaii time. (3) Clarification The Secretary is not required to ensure that the Veterans Health Administration has a call center in any location generally within a time zone specified in paragraph (2) that does not follow daylight time. .\n##### (b) Clerical amendment\nThe table of sections at the beginning of chapter 63 of such title is amended by adding at the end the following new item:\n6321. Telephone communication. .",
      "versionDate": "2025-03-04",
      "versionType": "Introduced in Senate"
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
            "name": "Department of Veterans Affairs",
            "updateDate": "2025-04-08T13:58:42Z"
          },
          {
            "name": "Telephone and wireless communication",
            "updateDate": "2025-04-08T13:58:36Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-04-04T20:49:50Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-04",
    "originChamber": "Senate",
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
          "measure-id": "id119s831",
          "measure-number": "831",
          "measure-type": "s",
          "orig-publish-date": "2025-03-04",
          "originChamber": "SENATE",
          "update-date": "2025-06-16"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s831v00",
            "update-date": "2025-06-16"
          },
          "action-date": "2025-03-04",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Representing VA with Accuracy Act or the REP VA Act</strong></p><p>This bill requires the Department of Veterans Affairs (VA) to ensure that any call made to a veteran by a VA employee or contractor regarding VA services or benefits is made from a single, well-known telephone number and uses caller identification that indicates the call is from or on behalf of the VA.</p><p>The VA must also ensure the Veterans Health Administration has at least one call center in each time zone in the United States to address concerns regarding appointments and referrals for health care.</p>"
        },
        "title": "REP VA Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s831.xml",
    "summary": {
      "actionDate": "2025-03-04",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Representing VA with Accuracy Act or the REP VA Act</strong></p><p>This bill requires the Department of Veterans Affairs (VA) to ensure that any call made to a veteran by a VA employee or contractor regarding VA services or benefits is made from a single, well-known telephone number and uses caller identification that indicates the call is from or on behalf of the VA.</p><p>The VA must also ensure the Veterans Health Administration has at least one call center in each time zone in the United States to address concerns regarding appointments and referrals for health care.</p>",
      "updateDate": "2025-06-16",
      "versionCode": "id119s831"
    },
    "title": "REP VA Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-04",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Representing VA with Accuracy Act or the REP VA Act</strong></p><p>This bill requires the Department of Veterans Affairs (VA) to ensure that any call made to a veteran by a VA employee or contractor regarding VA services or benefits is made from a single, well-known telephone number and uses caller identification that indicates the call is from or on behalf of the VA.</p><p>The VA must also ensure the Veterans Health Administration has at least one call center in each time zone in the United States to address concerns regarding appointments and referrals for health care.</p>",
      "updateDate": "2025-06-16",
      "versionCode": "id119s831"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s831is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "REP VA Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-31T11:03:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 38, United States Code, to require the Secretary of Veterans Affairs to improve telephone communication by the Department of Veterans Affairs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-27T18:33:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "REP VA Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-27T18:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Representing VA with Accuracy Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-27T18:23:20Z"
    }
  ]
}
```
