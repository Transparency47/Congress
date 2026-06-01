# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4204?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4204
- Title: Medicare Patient Choice Act
- Congress: 119
- Bill type: HR
- Bill number: 4204
- Origin chamber: House
- Introduced date: 2025-06-26
- Update date: 2026-03-28T08:06:30Z
- Update date including text: 2026-03-28T08:06:30Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-26: Introduced in House
- 2025-06-26 - IntroReferral: Introduced in House
- 2025-06-26 - IntroReferral: Introduced in House
- 2025-06-26 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-06-26 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-06-26: Introduced in House

## Actions

- 2025-06-26 - IntroReferral: Introduced in House
- 2025-06-26 - IntroReferral: Introduced in House
- 2025-06-26 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-06-26 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-26",
    "latestAction": {
      "actionDate": "2025-06-26",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4204",
    "number": "4204",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "S001199",
        "district": "11",
        "firstName": "Lloyd",
        "fullName": "Rep. Smucker, Lloyd [R-PA-11]",
        "lastName": "Smucker",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "Medicare Patient Choice Act",
    "type": "HR",
    "updateDate": "2026-03-28T08:06:30Z",
    "updateDateIncludingText": "2026-03-28T08:06:30Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-26",
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
      "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-26",
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
      "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-26",
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
          "date": "2025-06-26T14:04:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-06-26T14:04:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-06-26",
      "state": "NC"
    },
    {
      "bioguideId": "H001082",
      "district": "1",
      "firstName": "Kevin",
      "fullName": "Rep. Hern, Kevin [R-OK-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Hern",
      "party": "R",
      "sponsorshipDate": "2025-07-15",
      "state": "OK"
    },
    {
      "bioguideId": "F000110",
      "district": "6",
      "firstName": "Cleo",
      "fullName": "Rep. Fields, Cleo [D-LA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Fields",
      "party": "D",
      "sponsorshipDate": "2025-08-08",
      "state": "LA"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-08-29",
      "state": "DC"
    },
    {
      "bioguideId": "G000576",
      "district": "6",
      "firstName": "Glenn",
      "fullName": "Rep. Grothman, Glenn [R-WI-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Grothman",
      "party": "R",
      "sponsorshipDate": "2025-12-01",
      "state": "WI"
    },
    {
      "bioguideId": "K000376",
      "district": "16",
      "firstName": "Mike",
      "fullName": "Rep. Kelly, Mike [R-PA-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Kelly",
      "party": "R",
      "sponsorshipDate": "2026-03-27",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4204ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4204\nIN THE HOUSE OF REPRESENTATIVES\nJune 26, 2025 Mr. Smucker (for himself and Mr. Davis of North Carolina ) introduced the following bill; which was referred to the Committee on Ways and Means , and in addition to the Committee on Energy and Commerce , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend title XVIII of the Social Security Act to allow Medicare beneficiaries to choose their physical and occupational therapists, speech-language pathologists, audiologists, and chiropractors.\n#### 1. Short title\nThis Act may be cited as the Medicare Patient Choice Act .\n#### 2. Free choice of therapists for Medicare beneficiaries\nSection 1802(b) of the Social Security Act ( 42 U.S.C. 1395a(b) ) is amended\u2014\n**(1)**\nin paragraph (1)\u2014\n**(A)**\nin the matter preceding subparagraph (A), by striking physician or practitioner and inserting physician, practitioner, therapist, or qualified audiologist ; and\n**(B)**\nin subparagraph (B), in the matter preceding clause (i), by striking physician or practitioner and inserting physician, practitioner, therapist, or qualified audiologist ;\n**(2)**\nin paragraph (2)(B)\u2014\n**(A)**\nin clause (i), by striking physician or practitioner and inserting physician, practitioner, therapist, or qualified audiologist ;\n**(B)**\nin clause (v), by striking physicians or practitioners and inserting physicians, practitioners, therapists, or qualified audiologists ; and\n**(C)**\nin the matter following clause (v), by striking physician or practitioner and inserting physician, practitioner, therapist, or qualified audiologist ;\n**(3)**\nin paragraph (3)\u2014\n**(A)**\nin the heading, by striking physician or practitioner and inserting physician, practitioner, therapist, or qualified audiologist ;\n**(B)**\nin subparagraph (A), by striking physician or practitioner and inserting physician, practitioner, therapist, or qualified audiologist ;\n**(C)**\nin subparagraph (B)\u2014\n**(i)**\nin clause (i), by striking physician or practitioner each place it appears and inserting physician, practitioner, therapist, or qualified audiologist ; and\n**(ii)**\nin clause (ii), by striking physician or practitioner and inserting physician, practitioner, therapist, or qualified audiologist ;\n**(D)**\nin subparagraph (C)\u2014\n**(i)**\nin the matter preceding clause (i), by striking physician or practitioner and inserting physician, practitioner, therapist, or qualified audiologist ;\n**(ii)**\nin clause (i), by striking physician or practitioner and inserting physician, practitioner, therapist, or qualified audiologist ; and\n**(iii)**\nin clause (ii), by striking physician or practitioner and inserting physician, practitioner, therapist, or qualified audiologist ; and\n**(E)**\nin subparagraph (D), by striking physician or practitioner each place it appears and inserting physician, practitioner, therapist, or qualified audiologist ;\n**(4)**\nin paragraph (5)\u2014\n**(A)**\nin the heading, by striking physicians and practitioners and inserting physicians, practitioners, therapists, and qualified audiologists ;\n**(B)**\nin subparagraph (A), by striking physicians and practitioners and inserting physicians, practitioners, therapists, and qualified audiologists ; and\n**(C)**\nin subparagraph (B)\u2014\n**(i)**\nin the manner preceding clause (i), by striking physicians and practitioners and inserting physicians, practitioners, therapists, and qualified audiologists ;\n**(ii)**\nin clause (iv), by striking physicians and practitioners and inserting physicians, practitioners, therapists, and qualified audiologists ; and\n**(iii)**\nin clause (v), by striking physicians and practitioners and inserting physicians, practitioners, therapists, and qualified audiologists ; and\n**(5)**\nin paragraph (6)\u2014\n**(A)**\nin subparagraph (B), by striking paragraphs (1), (2), (3), and (4) of ;\n**(B)**\nin subparagraph (D)\u2014\n**(i)**\nin the heading, by striking physician or practitioner and inserting physician, practitioner, therapist, or qualified audiologist ; and\n**(ii)**\nby striking physician or practitioner each place it appears and inserting physician, practitioner, therapist, or qualified audiologist ; and\n**(C)**\nby adding at the end the following:\n(E) Therapist The term therapist means a qualified physical therapist (as such term is used in section 1861(p)), a qualified occupational therapist (as such term is used in 1861(g)), or a qualified speech-language pathologist (as defined in 1861(ll)(4)(A)). (F) Qualified audiologist The term qualified audiologist has the meaning given such term in section 1861(ll)(4)(B). .",
      "versionDate": "2025-06-26",
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
        "updateDate": "2025-07-16T13:39:06Z"
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
      "date": "2025-06-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4204ih.xml"
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
      "title": "Medicare Patient Choice Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-17T11:31:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Medicare Patient Choice Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-08T07:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XVIII of the Social Security Act to allow Medicare beneficiaries to choose their physical and occupational therapists, speech-language pathologists, audiologists, and chiropractors.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-08T07:18:54Z"
    }
  ]
}
```
