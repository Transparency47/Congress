# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/649?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/649
- Title: Guard and Reserve GI Bill Parity Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 649
- Origin chamber: Senate
- Introduced date: 2025-02-20
- Update date: 2026-04-01T21:35:54Z
- Update date including text: 2026-04-01T21:35:54Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-20: Introduced in Senate
- 2025-02-20 - IntroReferral: Introduced in Senate
- 2025-02-20 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2025-05-21 - Committee: Committee on Veterans' Affairs. Hearings held. Hearings printed: S.Hrg. 119-86.
- 2026-03-18 - Committee: Committee on Veterans' Affairs. Ordered to be reported with an amendment in the nature of a substitute favorably.
- Latest action: 2025-02-20: Introduced in Senate

## Actions

- 2025-02-20 - IntroReferral: Introduced in Senate
- 2025-02-20 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2025-05-21 - Committee: Committee on Veterans' Affairs. Hearings held. Hearings printed: S.Hrg. 119-86.
- 2026-03-18 - Committee: Committee on Veterans' Affairs. Ordered to be reported with an amendment in the nature of a substitute favorably.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-20",
    "latestAction": {
      "actionDate": "2025-02-20",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/649",
    "number": "649",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "M000934",
        "district": "",
        "firstName": "Jerry",
        "fullName": "Sen. Moran, Jerry [R-KS]",
        "lastName": "Moran",
        "party": "R",
        "state": "KS"
      }
    ],
    "title": "Guard and Reserve GI Bill Parity Act of 2025",
    "type": "S",
    "updateDate": "2026-04-01T21:35:54Z",
    "updateDateIncludingText": "2026-04-01T21:35:54Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-18",
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
      "actionDate": "2025-05-21",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Veterans' Affairs. Hearings held. Hearings printed: S.Hrg. 119-86.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-02-20",
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
      "actionDate": "2025-02-20",
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
            "date": "2026-03-18T20:00:02Z",
            "name": "Markup By"
          },
          {
            "date": "2025-05-21T20:00:14Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-05-21T20:00:14Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-02-20T17:38:41Z",
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
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-02-20",
      "state": "CT"
    },
    {
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "False",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2025-03-24",
      "state": "WI"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-04-30",
      "state": "NJ"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "False",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2025-12-02",
      "state": "MD"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "False",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2026-03-04",
      "state": "OR"
    },
    {
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "False",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2026-03-19",
      "state": "NH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s649is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 649\nIN THE SENATE OF THE UNITED STATES\nFebruary 20, 2025 Mr. Moran (for himself and Mr. Blumenthal ) introduced the following bill; which was read twice and referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to expand eligibility for Post-9/11 Educational Assistance to members of the National Guard who perform certain full-time duty, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Guard and Reserve GI Bill Parity Act of 2025 .\n#### 2. Expansion of eligibility for Post-9/11 Educational Assistance to members of the National Guard who perform certain full-time duty\n##### (a) In general\nSection 3301(1) of title 38, United States Code, is amended\u2014\n**(1)**\nby amending subparagraph (B) to read as follows:\n(B) In the case of members of the reserve components of the Armed Forces\u2014 (i) service on active duty (as defined in section 101(d) of title 10), inactive-duty training (as defined in section 101(d) of title 10), or annual training duty; or (ii) service on active duty under a call or order to active duty under section 688, 12301(a), 12301(d), 12301(g), 12301(h), 12302, 12304, 12304a, or 12304b of title 10 or section 3713 of title 14, but not including inactive duty training (as defined in section 101(d) of title 10) or annual training duty. ; and\n**(2)**\nin subparagraph (C)\u2014\n**(A)**\nin clause (i), by striking ; or and inserting a semicolon; and\n**(B)**\nby striking clause (ii) and inserting the following new clauses:\n(ii) in the National Guard when performing full-time National Guard duty (as defined in section 101 of title 32); or (iii) in the National Guard when performing active duty (as defined in section 101 of title 32). .\n##### (b) Effective date\nThe amendments made by subsection (a) shall take effect on the date that is one year after the date of the enactment of this Act.\n##### (c) Retroactive applicability\nThe amendments made by subsection (a) shall apply with respect to service performed on or after September 11, 2001.\n##### (d) Application of time limitation for use of entitlement\nSection 3321(a) of title 38, United States Code, shall apply to entitlement to educational assistance acquired as a result of the amendments made by subsection (a) as if such amendments had been enacted immediately after the enactment of the Post-9/11 Veterans Educational Assistance Act of 2008 ( Public Law 110\u2013252 ).",
      "versionDate": "2025-02-20",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2025-04-09",
        "text": "Forwarded by Subcommittee to Full Committee by Voice Vote."
      },
      "number": "1423",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Guard and Reserve GI Bill Parity Act of 2025",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "National Guard and reserves",
            "updateDate": "2025-03-21T20:00:04Z"
          },
          {
            "name": "Student aid and college costs",
            "updateDate": "2025-03-21T20:00:04Z"
          },
          {
            "name": "Veterans' education, employment, rehabilitation",
            "updateDate": "2025-03-21T20:00:04Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-03-25T17:40:50Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-20",
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
          "measure-id": "id119s649",
          "measure-number": "649",
          "measure-type": "s",
          "orig-publish-date": "2025-02-20",
          "originChamber": "SENATE",
          "update-date": "2026-03-04"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s649v00",
            "update-date": "2026-03-04"
          },
          "action-date": "2025-02-20",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Guard and Reserve GI Bill Parity Act of 2025</strong></p><p>This bill expands eligibility for Post-9/11 educational assistance for members of the reserve components of the Armed Forces and members of the National Guard. Specifically, the bill expands the types of activities that count towards Post-9/11 GI Bill eligibility to include active duty, inactive-duty training, annual training duty, and full-time National Guard duty or active duty. (Generally, under current law, only federal active duty counts towards educational assistance eligibility.)</p>"
        },
        "title": "Guard and Reserve GI Bill Parity Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s649.xml",
    "summary": {
      "actionDate": "2025-02-20",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Guard and Reserve GI Bill Parity Act of 2025</strong></p><p>This bill expands eligibility for Post-9/11 educational assistance for members of the reserve components of the Armed Forces and members of the National Guard. Specifically, the bill expands the types of activities that count towards Post-9/11 GI Bill eligibility to include active duty, inactive-duty training, annual training duty, and full-time National Guard duty or active duty. (Generally, under current law, only federal active duty counts towards educational assistance eligibility.)</p>",
      "updateDate": "2026-03-04",
      "versionCode": "id119s649"
    },
    "title": "Guard and Reserve GI Bill Parity Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-20",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Guard and Reserve GI Bill Parity Act of 2025</strong></p><p>This bill expands eligibility for Post-9/11 educational assistance for members of the reserve components of the Armed Forces and members of the National Guard. Specifically, the bill expands the types of activities that count towards Post-9/11 GI Bill eligibility to include active duty, inactive-duty training, annual training duty, and full-time National Guard duty or active duty. (Generally, under current law, only federal active duty counts towards educational assistance eligibility.)</p>",
      "updateDate": "2026-03-04",
      "versionCode": "id119s649"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s649is.xml"
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
      "title": "Guard and Reserve GI Bill Parity Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-20T11:03:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Guard and Reserve GI Bill Parity Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-13T01:23:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 38, United States Code, to expand eligibility for Post-9/11 Educational Assistance to members of the National Guard who perform certain full-time duty, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-13T01:18:42Z"
    }
  ]
}
```
