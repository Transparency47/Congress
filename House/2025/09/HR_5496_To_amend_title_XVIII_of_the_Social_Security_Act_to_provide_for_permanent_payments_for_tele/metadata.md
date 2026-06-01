# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5496?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5496
- Title: HEALTH Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5496
- Origin chamber: House
- Introduced date: 2025-09-18
- Update date: 2026-01-15T22:50:33Z
- Update date including text: 2026-01-15T22:50:33Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-09-18: Introduced in House
- 2025-09-18 - IntroReferral: Introduced in House
- 2025-09-18 - IntroReferral: Introduced in House
- 2025-09-18 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-09-18 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-09-18: Introduced in House

## Actions

- 2025-09-18 - IntroReferral: Introduced in House
- 2025-09-18 - IntroReferral: Introduced in House
- 2025-09-18 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-09-18 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-18",
    "latestAction": {
      "actionDate": "2025-09-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5496",
    "number": "5496",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "T000467",
        "district": "15",
        "firstName": "Glenn",
        "fullName": "Rep. Thompson, Glenn [R-PA-15]",
        "lastName": "Thompson",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "HEALTH Act of 2025",
    "type": "HR",
    "updateDate": "2026-01-15T22:50:33Z",
    "updateDateIncludingText": "2026-01-15T22:50:33Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-18",
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
      "actionDate": "2025-09-18",
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
      "actionDate": "2025-09-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-18",
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
          "date": "2025-09-18T14:03:40Z",
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
          "date": "2025-09-18T14:03:35Z",
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
      "bioguideId": "T000487",
      "district": "2",
      "firstName": "Jill",
      "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Tokuda",
      "middleName": "N.",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "HI"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-10-21",
      "state": "VA"
    },
    {
      "bioguideId": "S001218",
      "district": "1",
      "firstName": "Melanie",
      "fullName": "Rep. Stansbury, Melanie A. [D-NM-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Stansbury",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "NM"
    },
    {
      "bioguideId": "P000614",
      "district": "1",
      "firstName": "Chris",
      "fullName": "Rep. Pappas, Chris [D-NH-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Pappas",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "NH"
    },
    {
      "bioguideId": "K000009",
      "district": "9",
      "firstName": "Marcy",
      "fullName": "Rep. Kaptur, Marcy [D-OH-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Kaptur",
      "party": "D",
      "sponsorshipDate": "2026-01-07",
      "state": "OH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5496ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5496\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 18, 2025 Mr. Thompson of Pennsylvania (for himself and Ms. Tokuda ) introduced the following bill; which was referred to the Committee on Energy and Commerce , and in addition to the Committee on Ways and Means , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend title XVIII of the Social Security Act to provide for permanent payments for telehealth services furnished by federally qualified health centers and rural health clinics under the Medicare program.\n#### 1. Short title\nThis Act may be cited as the Helping Ensure Access to Local TeleHealth Act of 2025 or the HEALTH Act of 2025 .\n#### 2. Providing for permanent cost-related payments for telehealth services furnished by federally qualified health centers and rural health clinics under the Medicare program and permanently removing originating site facility and location requirements for distant site telehealth services furnished by such centers and such clinics\n##### (a) Coverage of audio-Only telehealth services\n**(1) In general**\nSection 1834(m)(4) of the Social Security Act ( 42 U.S.C. 1395m(m)(4) ) is amended by adding at the end the following new subparagraph:\n(G) Telecommunications system Except as provided in paragraph (1), the term telecommunications system means a two-way, real-time interactive communications system, whether by audiovisual or audio-only communications. .\n**(2) Required implementation steps**\nNot later than 60 days after the date of the enactment of this Act, the Secretary of Health and Human Services shall\u2014\n**(A)**\nrevise section 410.78(a)(3) of title 42, Code of Federal Regulations (or a successor regulation) to define the term interactive telecommunications system in accordance with the amendment made by paragraph (1); and\n**(B)**\nrevise section 405.2463 of such title (or a successor regulation) to provide that, for purposes of distant site telehealth services furnished by federally qualified health centers and rural health clinics under section 1834(m)(8) of the Social Security Act ( 42 U.S.C. 1395m(m)(8) ), a visit includes any two-way, real-time interactive communication between an individual and the distant site Federally qualified health center provider or rural health clinic, whether by audiovisual or audio-only communication.\n##### (b) Permanent telehealth payments\nSection 1834(m)(8) of the Social Security Act ( 42 U.S.C. 1395m(m)(8) ) is amended\u2014\n**(1)**\nin subparagraph (A), in the matter preceding clause (i), by striking During the emergency period and all that follows through 2025\u2014 and inserting With respect to telehealth services furnished on or after the date of the beginning of the emergency period described in section 1135(g)(1)(B)\u2014 ; and\n**(2)**\nby striking subparagraph (B) and inserting the following new subparagraph:\n(B) Payment (i) In general A telehealth service furnished by a rural health clinic or a federally qualified health center serving as a distant site to an individual shall be deemed to be so furnished to such individual as an outpatient of such clinic or facility (as applicable) for purposes of paragraph (1) or (3), respectively, of section 1861(aa) and payable as a rural health clinic service or federally qualified health center service (as applicable) under section 1833(a)(3) or under the prospective payment system established under section 1834(o), respectively. (ii) Treatment of costs for FQHC PPS calculations and RHC AIR calculations Costs associated with the delivery of telehealth services by a federally qualified health center or rural health clinic serving as a distant site pursuant to this paragraph shall be considered allowable costs for purposes of the prospective payment system established under section 1834(o) and any payment methodologies developed under section 1833(a)(3), as applicable. .\n##### (c) Elimination of originating site requirements for telehealth services furnished by FQHCs or RHCs\n**(1) In general**\nSection 1834(m) of the Social Security Act ( 42 U.S.C. 1395m(m) ), as amended by subsection (b), is further amended\u2014\n**(A)**\nin paragraph (4)(C)(i), by striking and (7) and inserting (7), and (8) ; and\n**(B)**\nin paragraph (8), by adding at the end the following new subparagraph:\n(C) Nonapplication of originating site requirements The geographic and site requirements described in paragraph (4)(C) shall not apply with respect to telehealth services furnished by a federally qualified health center or a rural health clinic serving as a distant site. .\n**(2) Special payment rule for originating sites with respect to telehealth services furnished by an FQHC or RHC**\nSection 1834(m)(2)(B) of the Social Security Act ( 42 U.S.C. 1395m(m)(2)(B) ) is amended\u2014\n**(A)**\nin clause (i), by striking clause (ii) and inserting clauses (ii) and (iii) ; and\n**(B)**\nby adding at the end the following new clause:\n(iii) Special rule for telehealth services furnished by FQHCs and RHCs No facility fee shall be paid under this subparagraph to an originating site with respect to telehealth services furnished by a federally qualified health center or rural health clinic serving as a distant site unless such originating site is a site described in any of subclauses (I) through (IX) or (XI) of paragraph (4)(C)(ii). .",
      "versionDate": "2025-09-18",
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
        "updateDate": "2025-11-18T17:37:33Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-09-18",
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
          "measure-id": "id119hr5496",
          "measure-number": "5496",
          "measure-type": "hr",
          "orig-publish-date": "2025-09-18",
          "originChamber": "HOUSE",
          "update-date": "2026-01-15"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr5496v00",
            "update-date": "2026-01-15"
          },
          "action-date": "2025-09-18",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Helping Ensure Access to Local TeleHealth Act of 2025 or the HEALTH Act of </strong><strong>2025</strong>\u00a0</p><p>This bill modifies requirements relating to Medicare coverage of telehealth services, including services that are furnished by federally qualified health centers (FQHCs) and rural health clinics (RHCs).</p><p>Specifically, the bill expands coverage to include audio-only telehealth services. It also permanently allows FQHCs and RHCs to serve as the distant site (i.e., the location of the health care practitioner) for telehealth services and excludes such services from certain geographic restrictions. Payment must be made in the same manner as for non-telehealth services, rather than in accordance with a separate methodology determined by the Centers for Medicare & Medicaid Services.</p>"
        },
        "title": "HEALTH Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr5496.xml",
    "summary": {
      "actionDate": "2025-09-18",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Helping Ensure Access to Local TeleHealth Act of 2025 or the HEALTH Act of </strong><strong>2025</strong>\u00a0</p><p>This bill modifies requirements relating to Medicare coverage of telehealth services, including services that are furnished by federally qualified health centers (FQHCs) and rural health clinics (RHCs).</p><p>Specifically, the bill expands coverage to include audio-only telehealth services. It also permanently allows FQHCs and RHCs to serve as the distant site (i.e., the location of the health care practitioner) for telehealth services and excludes such services from certain geographic restrictions. Payment must be made in the same manner as for non-telehealth services, rather than in accordance with a separate methodology determined by the Centers for Medicare & Medicaid Services.</p>",
      "updateDate": "2026-01-15",
      "versionCode": "id119hr5496"
    },
    "title": "HEALTH Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-09-18",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Helping Ensure Access to Local TeleHealth Act of 2025 or the HEALTH Act of </strong><strong>2025</strong>\u00a0</p><p>This bill modifies requirements relating to Medicare coverage of telehealth services, including services that are furnished by federally qualified health centers (FQHCs) and rural health clinics (RHCs).</p><p>Specifically, the bill expands coverage to include audio-only telehealth services. It also permanently allows FQHCs and RHCs to serve as the distant site (i.e., the location of the health care practitioner) for telehealth services and excludes such services from certain geographic restrictions. Payment must be made in the same manner as for non-telehealth services, rather than in accordance with a separate methodology determined by the Centers for Medicare & Medicaid Services.</p>",
      "updateDate": "2026-01-15",
      "versionCode": "id119hr5496"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-09-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5496ih.xml"
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
      "title": "HEALTH Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-03T04:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "HEALTH Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-03T04:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Helping Ensure Access to Local TeleHealth Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-03T04:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XVIII of the Social Security Act to provide for permanent payments for telehealth services furnished by federally qualified health centers and rural health clinics under the Medicare program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-03T04:18:18Z"
    }
  ]
}
```
