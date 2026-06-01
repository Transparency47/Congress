# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6841?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6841
- Title: PEERS Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6841
- Origin chamber: House
- Introduced date: 2025-12-18
- Update date: 2026-03-11T14:07:28Z
- Update date including text: 2026-03-11T14:07:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-18: Introduced in House
- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-12-18 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-12-18: Introduced in House

## Actions

- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-12-18 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-18",
    "latestAction": {
      "actionDate": "2025-12-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6841",
    "number": "6841",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "C001080",
        "district": "28",
        "firstName": "Judy",
        "fullName": "Rep. Chu, Judy [D-CA-28]",
        "lastName": "Chu",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "PEERS Act of 2025",
    "type": "HR",
    "updateDate": "2026-03-11T14:07:28Z",
    "updateDateIncludingText": "2026-03-11T14:07:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-18",
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
      "actionDate": "2025-12-18",
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
      "actionDate": "2025-12-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-18",
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
          "date": "2025-12-18T14:09:10Z",
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
          "date": "2025-12-18T14:09:05Z",
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
      "bioguideId": "S001172",
      "district": "3",
      "firstName": "Adrian",
      "fullName": "Rep. Smith, Adrian [R-NE-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "R",
      "sponsorshipDate": "2025-12-18",
      "state": "NE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6841ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6841\nIN THE HOUSE OF REPRESENTATIVES\nDecember 18, 2025 Ms. Chu (for herself and Mr. Smith of Nebraska ) introduced the following bill; which was referred to the Committee on Energy and Commerce , and in addition to the Committee on Ways and Means , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend title XVIII of the Social Security Act to include peer support services at certain facilities under the Medicare program.\n#### 1. Short title\nThis Act may be cited as the Promoting Effective and Empowering Recovery Services in Medicare Act of 2025 or the PEERS Act of 2025 .\n#### 2. Inclusion of peer support services at certain facilities under the Medicare program\n##### (a) Services\n**(1) Inclusion at community mental health centers**\nSection 1832(a)(2)(J) of the Social Security Act ( 42 U.S.C. 1395k(a)(2)(J) ) is amended by striking and intensive outpatient services and all that follows through the period at the end and inserting , intensive outpatient services, and peer support services (as defined in section 1861(nnn)(1)) provided by a community mental health center (as defined in section 1861(ff)(3)(B)). .\n**(2) Inclusion as RHC and FQHC services**\nSection 1861(aa)(1)(B) of the Social Security Act ( 42 U.S.C. 1395x(aa)(1)(B) ) is amended\u2014\n**(A)**\nby striking or by a mental and inserting by a mental ; and\n**(B)**\nby inserting or by a peer support specialist (as defined in subsection (nnn)(2)) after subsection (ll)(4)), .\n##### (b) Definition\nSection 1861 of the Social Security Act ( 42 U.S.C. 1395x ) is amended by adding at the end the following new subsection:\n(nnn) Peer support services and peer support specialist (1) Peer support services The term peer support services means emotional, informational, instrumental, and social and community support services\u2014 (A) furnished\u2014 (i) by a Federally qualified health center, a rural health clinic, a community mental health center, or a certified community behavioral health clinic (as described in section 223 of the Protecting Access to Medicare Act of 2014), using a peer support specialist; and (ii) to an individual who has been diagnosed with a mental health condition or substance use disorder; and (B) that are designed to assist such individual in achieving recovery, integration in the community, self-empowerment, and self-determination (as specified by the Secretary). (2) Peer support specialist The term peer support specialist means an individual who\u2014 (A) is recovering from a mental health or substance use condition; and (B) is certified as qualified to furnish peer support services under a certification process consistent with the National Practice Guidelines for Peer Supporters and inclusive of the Substance Abuse and Mental Health Services Administration Core Competencies for Peer Workers in Behavioral Health Settings (as established by the State in which such individual furnishes such services or under such certification process determined appropriate by the Secretary). .\n##### (c) Exclusion modification\nSection 1862(a)(1) of the Social Security Act ( 42 U.S.C. 1395y(a)(1) ) is amended\u2014\n**(1)**\nin subparagraph (O), by striking and at the end;\n**(2)**\nin subparagraph (P), by striking the semicolon at the end and inserting , and ; and\n**(3)**\nby adding at the end the following new subparagraph:\n(Q) in the case of peer support services (as defined in section 1861(nnn(1))), which are not furnished by a rural health clinic, a Federally qualified health center, a community mental health center, or a certified community behavioral health clinic (as described in section 223 of the Protecting Access to Medicare Act of 2014); .\n##### (d) Effective date\nThe amendments made by this section shall apply to items and services furnished on or after January 1, 2027.",
      "versionDate": "2025-12-18",
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
        "actionDate": "2025-12-17",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "3521",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "PEERS Act of 2025",
      "type": "S"
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
        "updateDate": "2026-03-11T14:07:27Z"
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
      "date": "2025-12-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6841ih.xml"
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
      "title": "PEERS Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-10T05:23:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "PEERS Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-10T05:23:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Promoting Effective and Empowering Recovery Services in Medicare Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-10T05:23:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XVIII of the Social Security Act to include peer support services at certain facilities under the Medicare program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-10T05:18:20Z"
    }
  ]
}
```
