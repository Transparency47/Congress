# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1867?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1867
- Title: To amend title XVIII of the Social Security Act to remove in-person requirements under Medicare for mental health services furnished through telehealth and telecommunications technology.
- Congress: 119
- Bill type: HR
- Bill number: 1867
- Origin chamber: House
- Introduced date: 2025-03-05
- Update date: 2026-02-13T21:00:34Z
- Update date including text: 2026-02-13T21:00:34Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-05: Introduced in House
- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-05 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-03-05: Introduced in House

## Actions

- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-05 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-05",
    "latestAction": {
      "actionDate": "2025-03-05",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1867",
    "number": "1867",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "H001082",
        "district": "1",
        "firstName": "Kevin",
        "fullName": "Rep. Hern, Kevin [R-OK-1]",
        "lastName": "Hern",
        "party": "R",
        "state": "OK"
      }
    ],
    "title": "To amend title XVIII of the Social Security Act to remove in-person requirements under Medicare for mental health services furnished through telehealth and telecommunications technology.",
    "type": "HR",
    "updateDate": "2026-02-13T21:00:34Z",
    "updateDateIncludingText": "2026-02-13T21:00:34Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-05",
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
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-05",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-05",
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
          "date": "2025-03-05T15:02:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-03-05T15:02:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "S001201",
      "district": "3",
      "firstName": "Thomas",
      "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Suozzi",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "NY"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-03-05",
      "state": "PA"
    },
    {
      "bioguideId": "L000590",
      "district": "3",
      "firstName": "Susie",
      "fullName": "Rep. Lee, Susie [D-NV-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "NV"
    },
    {
      "bioguideId": "M000317",
      "district": "11",
      "firstName": "Nicole",
      "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Malliotakis",
      "party": "R",
      "sponsorshipDate": "2025-03-05",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1867ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1867\nIN THE HOUSE OF REPRESENTATIVES\nMarch 5, 2025 Mr. Hern of Oklahoma (for himself, Mr. Suozzi , Mr. Fitzpatrick , Ms. Lee of Nevada , and Ms. Malliotakis ) introduced the following bill; which was referred to the Committee on Energy and Commerce , and in addition to the Committee on Ways and Means , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend title XVIII of the Social Security Act to remove in-person requirements under Medicare for mental health services furnished through telehealth and telecommunications technology.\n#### 1. Removing the in-person requirements under Medicare for mental health services furnished through telehealth and telecommunications technology\n##### (a) In general\nSection 1834(m)(7) of the Social Security Act ( 42 U.S.C. 1395m(m)(7) ) is amended to read as follows:\n(7) Treatment of substance use disorder services and mental health services furnished through telehealth The geographic requirements described in paragraph (4)(C)(i) shall not apply with respect to telehealth services furnished on or after July 1, 2020, to an eligible telehealth individual with a substance use disorder diagnosis for purposes of treatment of such disorder or co-occurring mental health disorder, as determined by the Secretary, or, on or after the first day after the end of the emergency period described in section 1135(g)(1)(B), to an eligible telehealth individual for purposes of diagnosis, evaluation, or treatment of a mental health disorder, as determined by the Secretary, at an originating site described in paragraph (4)(C)(ii) (other than an originating site described in subclause (IX) of such paragraph) or, for the period for which clause (iii) of paragraph (4)(C) applies, at any site described in such clause. .\n##### (b) Mental health visits furnished by rural health clinics\nSection 1834(y)(2) of the Social Security Act ( 42 U.S.C. 1395m(y)(2) ) is amended by striking prior to April 1, 2025 .\n##### (c) Mental health visits furnished by federally qualified health centers\nSection 1834(o)(4)(B) of the Social Security Act ( 42 U.S.C. 1395m(o)(4)(B) ) is amended by striking prior to April 1, 2025 .",
      "versionDate": "2025-03-05",
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
        "name": "Health",
        "updateDate": "2025-03-21T16:55:49Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-05",
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
          "measure-id": "id119hr1867",
          "measure-number": "1867",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-05",
          "originChamber": "HOUSE",
          "update-date": "2026-02-13"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1867v00",
            "update-date": "2026-02-13"
          },
          "action-date": "2025-03-05",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This bill permanently removes in-person evaluation requirements for mental health telehealth services under Medicare. </p>"
        },
        "title": "To amend title XVIII of the Social Security Act to remove in-person requirements under Medicare for mental health services furnished through telehealth and telecommunications technology."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1867.xml",
    "summary": {
      "actionDate": "2025-03-05",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill permanently removes in-person evaluation requirements for mental health telehealth services under Medicare. </p>",
      "updateDate": "2026-02-13",
      "versionCode": "id119hr1867"
    },
    "title": "To amend title XVIII of the Social Security Act to remove in-person requirements under Medicare for mental health services furnished through telehealth and telecommunications technology."
  },
  "summaries": [
    {
      "actionDate": "2025-03-05",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill permanently removes in-person evaluation requirements for mental health telehealth services under Medicare. </p>",
      "updateDate": "2026-02-13",
      "versionCode": "id119hr1867"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1867ih.xml"
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
      "title": "To amend title XVIII of the Social Security Act to remove in-person requirements under Medicare for mental health services furnished through telehealth and telecommunications technology.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-21T04:03:39Z"
    },
    {
      "title": "To amend title XVIII of the Social Security Act to remove in-person requirements under Medicare for mental health services furnished through telehealth and telecommunications technology.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-06T09:06:24Z"
    }
  ]
}
```
