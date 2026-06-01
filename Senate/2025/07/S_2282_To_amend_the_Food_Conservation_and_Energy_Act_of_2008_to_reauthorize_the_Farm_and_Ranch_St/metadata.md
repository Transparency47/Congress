# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2282?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2282
- Title: Farmers First Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2282
- Origin chamber: Senate
- Introduced date: 2025-07-15
- Update date: 2026-03-03T12:03:26Z
- Update date including text: 2026-03-03T12:03:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-07-15: Introduced in Senate
- 2025-07-15 - IntroReferral: Introduced in Senate
- 2025-07-15 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- Latest action: 2025-07-15: Introduced in Senate

## Actions

- 2025-07-15 - IntroReferral: Introduced in Senate
- 2025-07-15 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-15",
    "latestAction": {
      "actionDate": "2025-07-15",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2282",
    "number": "2282",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "B001230",
        "district": "",
        "firstName": "Tammy",
        "fullName": "Sen. Baldwin, Tammy [D-WI]",
        "lastName": "Baldwin",
        "party": "D",
        "state": "WI"
      }
    ],
    "title": "Farmers First Act of 2025",
    "type": "S",
    "updateDate": "2026-03-03T12:03:26Z",
    "updateDateIncludingText": "2026-03-03T12:03:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-15",
      "committees": {
        "item": {
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-15",
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
            "date": "2025-07-15T19:31:03Z",
            "name": "Referred To"
          },
          {
            "date": "2025-07-15T19:31:03Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Agriculture, Nutrition, and Forestry Committee",
      "systemCode": "ssaf00",
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
      "bioguideId": "E000295",
      "firstName": "Joni",
      "fullName": "Sen. Ernst, Joni [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Ernst",
      "party": "R",
      "sponsorshipDate": "2025-07-15",
      "state": "IA"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-07-15",
      "state": "MN"
    },
    {
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-07-15",
      "state": "ME"
    },
    {
      "bioguideId": "B001236",
      "firstName": "John",
      "fullName": "Sen. Boozman, John [R-AR]",
      "isOriginalCosponsor": "True",
      "lastName": "Boozman",
      "party": "R",
      "sponsorshipDate": "2025-07-15",
      "state": "AR"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "False",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-07-28",
      "state": "MN"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "False",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2025-08-01",
      "state": "CO"
    },
    {
      "bioguideId": "F000463",
      "firstName": "Deb",
      "fullName": "Sen. Fischer, Deb [R-NE]",
      "isOriginalCosponsor": "False",
      "lastName": "Fischer",
      "party": "R",
      "sponsorshipDate": "2025-08-01",
      "state": "NE"
    },
    {
      "bioguideId": "O000174",
      "firstName": "Jon",
      "fullName": "Sen. Ossoff, Jon [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Ossoff",
      "party": "D",
      "sponsorshipDate": "2025-09-11",
      "state": "GA"
    },
    {
      "bioguideId": "M000934",
      "firstName": "Jerry",
      "fullName": "Sen. Moran, Jerry [R-KS]",
      "isOriginalCosponsor": "False",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2025-10-09",
      "state": "KS"
    },
    {
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "False",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2026-03-02",
      "state": "KS"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2282is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2282\nIN THE SENATE OF THE UNITED STATES\nJuly 15, 2025 Ms. Baldwin (for herself, Ms. Ernst , Ms. Smith , Ms. Collins , and Mr. Boozman ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo amend the Food, Conservation, and Energy Act of 2008 to reauthorize the Farm and Ranch Stress Assistance Network, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Farmers First Act of 2025 .\n#### 2. Farm and Ranch Stress Assistance Network\nSection 7522 of the Food, Conservation, and Energy Act of 2008 ( 7 U.S.C. 5936 ) is amended\u2014\n**(1)**\nin subsection (b)(1)(A), by inserting , including crisis lines before the semicolon at the end;\n**(2)**\nin subsection (d), by striking $10,000,000 for each of fiscal years 2019 through 2023 and inserting $15,000,000 for each of fiscal years 2026 through 2030 ; and\n**(3)**\nby striking subsection (e) and inserting the following:\n(e) Referrals to providers As part of the efforts of the recipient of a grant under subsection (a) to connect individuals to behavioral health counseling and wellness support and to ensure individuals have access to a comprehensive scope of mental health and substance use treatments and supports, when applicable, the grant recipient may establish referral relationships with\u2014 (1) certified community behavioral health clinics described in section 223 of the Protecting Access to Medicare Act of 2014 ( 42 U.S.C. 1396a note; Public Law 113\u201393 ); (2) health centers (as defined in section 330(a) of the Public Health Service Act ( 42 U.S.C. 254b(a) )); (3) rural health clinics (as defined in section 1861(aa) of the Social Security Act ( 42 U.S.C. 1395x(aa) )); (4) Federally qualified health centers (as defined in that section); and (5) critical access hospitals (as defined in section 1861(mm) of the Social Security Act ( 42 U.S.C. 1395x(mm) )). .",
      "versionDate": "2025-07-15",
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
        "actionDate": "2026-02-13",
        "text": "Referred to the House Committee on Agriculture."
      },
      "number": "7567",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Farm, Food, and National Security Act of 2026",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-07-15",
        "text": "Referred to the House Committee on Agriculture."
      },
      "number": "4400",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Farmers First Act of 2025",
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
        "name": "Agriculture and Food",
        "updateDate": "2025-08-01T15:09:32Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-07-15",
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
          "measure-id": "id119s2282",
          "measure-number": "2282",
          "measure-type": "s",
          "orig-publish-date": "2025-07-15",
          "originChamber": "SENATE",
          "update-date": "2025-08-07"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s2282v00",
            "update-date": "2025-08-07"
          },
          "action-date": "2025-07-15",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Farmers First Act of 2025</strong></p><p>This bill extends through FY2030 and revises the Farm and Ranch Stress Assistance Network (FRSAN). This Department of Agriculture program provides competitive grants to states, Indian tribes, and qualified nonprofit organizations to provide stress assistance programs (i.e., professional agricultural behavioral health counseling, helplines, and resources) to individuals engaged in farming, ranching, and agriculture-related occupations.</p><p>The bill specifies that the grant funding for farm telephone helplines and websites may also be used for crisis lines.</p><p>Further, FRSAN grant recipients may establish referral relationships with providers, including Certified Community Behavioral Health Clinics, health centers, rural health clinics, and critical access hospitals.</p>"
        },
        "title": "Farmers First Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s2282.xml",
    "summary": {
      "actionDate": "2025-07-15",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Farmers First Act of 2025</strong></p><p>This bill extends through FY2030 and revises the Farm and Ranch Stress Assistance Network (FRSAN). This Department of Agriculture program provides competitive grants to states, Indian tribes, and qualified nonprofit organizations to provide stress assistance programs (i.e., professional agricultural behavioral health counseling, helplines, and resources) to individuals engaged in farming, ranching, and agriculture-related occupations.</p><p>The bill specifies that the grant funding for farm telephone helplines and websites may also be used for crisis lines.</p><p>Further, FRSAN grant recipients may establish referral relationships with providers, including Certified Community Behavioral Health Clinics, health centers, rural health clinics, and critical access hospitals.</p>",
      "updateDate": "2025-08-07",
      "versionCode": "id119s2282"
    },
    "title": "Farmers First Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-07-15",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Farmers First Act of 2025</strong></p><p>This bill extends through FY2030 and revises the Farm and Ranch Stress Assistance Network (FRSAN). This Department of Agriculture program provides competitive grants to states, Indian tribes, and qualified nonprofit organizations to provide stress assistance programs (i.e., professional agricultural behavioral health counseling, helplines, and resources) to individuals engaged in farming, ranching, and agriculture-related occupations.</p><p>The bill specifies that the grant funding for farm telephone helplines and websites may also be used for crisis lines.</p><p>Further, FRSAN grant recipients may establish referral relationships with providers, including Certified Community Behavioral Health Clinics, health centers, rural health clinics, and critical access hospitals.</p>",
      "updateDate": "2025-08-07",
      "versionCode": "id119s2282"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-07-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2282is.xml"
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
      "title": "Farmers First Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-03T12:03:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Farmers First Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-24T01:53:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Food, Conservation, and Energy Act of 2008 to reauthorize the Farm and Ranch Stress Assistance Network, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-24T01:48:37Z"
    }
  ]
}
```
