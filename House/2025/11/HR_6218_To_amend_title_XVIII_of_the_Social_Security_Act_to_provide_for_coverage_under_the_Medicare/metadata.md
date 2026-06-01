# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6218?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6218
- Title: HEAR Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6218
- Origin chamber: House
- Introduced date: 2025-11-20
- Update date: 2026-01-26T16:34:33Z
- Update date including text: 2026-01-26T16:34:33Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-11-20: Introduced in House
- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-11-20 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-11-20: Introduced in House

## Actions

- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-11-20 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-20",
    "latestAction": {
      "actionDate": "2025-11-20",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6218",
    "number": "6218",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "M001225",
        "district": "15",
        "firstName": "Kevin",
        "fullName": "Rep. Mullin, Kevin [D-CA-15]",
        "lastName": "Mullin",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "HEAR Act of 2025",
    "type": "HR",
    "updateDate": "2026-01-26T16:34:33Z",
    "updateDateIncludingText": "2026-01-26T16:34:33Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-20",
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
      "actionDate": "2025-11-20",
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
      "actionDate": "2025-11-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-20",
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
          "date": "2025-11-20T15:04:45Z",
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
          "date": "2025-11-20T15:04:40Z",
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
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-11-20",
      "state": "NY"
    },
    {
      "bioguideId": "D000624",
      "district": "6",
      "firstName": "Debbie",
      "fullName": "Rep. Dingell, Debbie [D-MI-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Dingell",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "MI"
    },
    {
      "bioguideId": "T000472",
      "district": "39",
      "firstName": "Mark",
      "fullName": "Rep. Takano, Mark [D-CA-39]",
      "isOriginalCosponsor": "True",
      "lastName": "Takano",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "CA"
    },
    {
      "bioguideId": "D000631",
      "district": "4",
      "firstName": "Madeleine",
      "fullName": "Rep. Dean, Madeleine [D-PA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Dean",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "PA"
    },
    {
      "bioguideId": "D000530",
      "district": "17",
      "firstName": "Christopher",
      "fullName": "Rep. Deluzio, Christopher R. [D-PA-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Deluzio",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "PA"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6218ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6218\nIN THE HOUSE OF REPRESENTATIVES\nNovember 20, 2025 Mr. Mullin (for himself, Mr. Lawler , Mrs. Dingell , Mr. Takano , Ms. Dean of Pennsylvania , Mr. Deluzio , and Mr. Johnson of Georgia ) introduced the following bill; which was referred to the Committee on Energy and Commerce , and in addition to the Committee on Ways and Means , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend title XVIII of the Social Security Act to provide for coverage under the Medicare program of hearing aids and related hearing services.\n#### 1. Short title\nThis Act may be cited as the Help Extend Auditory Relief Act of 2025 or the HEAR Act of 2025 .\n#### 2. Medicare coverage of hearing rehabilitation\n##### (a) Coverage of aural rehabilitation services\nSection 1861(s)(2) of the Social Security Act ( 42 U.S.C. 1395x(s)(2) ) is amended\u2014\n**(1)**\nin subparagraph (JJ) by adding and at the end; and\n**(2)**\nby adding at the end the following new subparagraph:\n(KK) aural rehabilitation services (as described in subsection (nnn)(1)(A)); .\n##### (b) Coverage of hearing aids as durable medical equipment\nSection 1861(s)(8) of the Social Security Act ( 42 U.S.C. 1395x(s)(8) ) is amended by inserting and hearing aids (as defined in subsection (nnn)(3)) before the period.\n##### (c) Hearing rehabilitation and hearing aid defined\nSection 1861 of the Social Security Act ( 42 U.S.C. 1395x ) is amended by adding at the end the following new subsection:\n(nnn) Hearing Rehabilitation (1) The term hearing rehabilitation means\u2014 (A) aural rehabilitation services (described in paragraph (2)) which meet such requirements as the Secretary prescribes and which are furnished by a physician or qualified audiologist, who is legally authorized to furnish such services under the State law (or the State regulatory mechanism provided by State law) of the State in which the services are furnished; and (B) hearing aids (as defined in paragraph (3)). (2) The services described in this subparagraph include\u2014 (A) aural rehabilitation services; (B) in the case of an individual who has a hearing loss (as defined by the Secretary), a comprehensive audiologic assessment to determine if a hearing aid is appropriate and to determine the need for other diagnostic medical or audiologic testing; and (C) a threshold test to determine audio acuity. (3) (A) The term hearing aid means a hearing aid described in subparagraph (B), including the services described in subparagraph (C) furnished by a physician or qualified audiologist, who is legally authorized to supply such hearing aid under the State law (or State regulatory mechanism provided by State law) of the State in which the hearing aid is supplied, to an individual described in subparagraph (D). (B) A hearing aid described in this subparagraph is any wearable instrument or device for, offered for the purpose of, or represented as aiding individuals with, or compensating for, hearing loss that meets requirements of the Food and Drug Administration for marketing, but does not include an over-the-counter hearing aid (as defined in section 520(q)(1) of the Federal Food, Drug, and Cosmetic Act). (C) The services described in this subparagraph include\u2014 (i) audiology services (as defined in subsection (ll)(2)); (ii) a hearing aid assessment to determine the appropriate hearing aid for the individual; (iii) procurement of an appropriate hearing aid; (iv) initial fitting and adjustment of the hearing aid; (v) appropriate instruction on the use of the hearing aid; (vi) periodic refittings and adjustments; and (vii) rehabilitation, including counseling on hearing loss, speech reading, and auditory training. (D) The individuals described in this subparagraph\u2014 (i) have been determined (as a result of a comprehensive audiologic assessment) to have a hearing loss which can be appropriately treated with a hearing aid; (ii) have not been supplied with one monaural hearing aid or two binaural hearing aids during the preceding 3 years; and (iii) have had a comprehensive audiologic assessment which indicates that the hearing of such individual has deteriorated since such individual was last supplied with a hearing aid such that a hearing aid of a different type is appropriate for such individual. .\n##### (d) Inclusion of audiology rehabilitation services\nSection 1861(ll)(3) of the Social Security Act ( 42 U.S.C. 1395x(ll)(3) ) is amended by inserting and rehabilitation after balance assessment .\n##### (e) Exception to exclusions from coverage\nSection 1862(a) of the Social Security Act ( 42 U.S.C. 1395y(a) ) is amended\u2014\n**(1)**\nin paragraph (1)\u2014\n**(A)**\nin subparagraph (O), by striking and at the end;\n**(B)**\nin subparagraph (P); by striking the semicolon at the end and inserting , and ; and\n**(C)**\nby adding at the end the following new subparagraph:\n(Q) in the case of hearing rehabilitation, which is furnished or supplied more frequently than is provided under section 1861(nnn)(3)(D)(ii). ; and\n**(2)**\nin paragraph (7) by striking hearing aids or examinations therefor .\n##### (f) Effective date\nThe amendments made by this section shall take effect on the date of the enactment of this Act, and shall apply to items and services furnished on or after a date specified by the Secretary of Health and Human Services that is not sooner than January 1 of the first year beginning after such date of enactment and not later than January 1 of the third year beginning after such date of enactment.",
      "versionDate": "2025-11-20",
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
        "updateDate": "2025-12-10T16:46:27Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-11-20",
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
          "measure-id": "id119hr6218",
          "measure-number": "6218",
          "measure-type": "hr",
          "orig-publish-date": "2025-11-20",
          "originChamber": "HOUSE",
          "update-date": "2026-01-26"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr6218v00",
            "update-date": "2026-01-26"
          },
          "action-date": "2025-11-20",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Help Extend Auditory Relief Act of 2025 or the HEAR Act of 2025</strong>\u00a0</p><p>This bill provides for Medicare coverage of hearing aids and hearing rehabilitation services. Covered services include hearing aid assessments, fittings, and related instructional services.</p>"
        },
        "title": "HEAR Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr6218.xml",
    "summary": {
      "actionDate": "2025-11-20",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Help Extend Auditory Relief Act of 2025 or the HEAR Act of 2025</strong>\u00a0</p><p>This bill provides for Medicare coverage of hearing aids and hearing rehabilitation services. Covered services include hearing aid assessments, fittings, and related instructional services.</p>",
      "updateDate": "2026-01-26",
      "versionCode": "id119hr6218"
    },
    "title": "HEAR Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-11-20",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Help Extend Auditory Relief Act of 2025 or the HEAR Act of 2025</strong>\u00a0</p><p>This bill provides for Medicare coverage of hearing aids and hearing rehabilitation services. Covered services include hearing aid assessments, fittings, and related instructional services.</p>",
      "updateDate": "2026-01-26",
      "versionCode": "id119hr6218"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-11-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6218ih.xml"
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
      "title": "HEAR Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-09T10:23:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "HEAR Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-09T10:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Help Extend Auditory Relief Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-09T10:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XVIII of the Social Security Act to provide for coverage under the Medicare program of hearing aids and related hearing services.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-09T10:18:22Z"
    }
  ]
}
```
