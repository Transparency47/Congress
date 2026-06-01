# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3409?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3409
- Title: HEADs UP Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3409
- Origin chamber: House
- Introduced date: 2025-05-14
- Update date: 2026-04-14T08:05:30Z
- Update date including text: 2026-04-14T08:05:30Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-14: Introduced in House
- 2025-05-14 - IntroReferral: Introduced in House
- 2025-05-14 - IntroReferral: Introduced in House
- 2025-05-14 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-05-14: Introduced in House

## Actions

- 2025-05-14 - IntroReferral: Introduced in House
- 2025-05-14 - IntroReferral: Introduced in House
- 2025-05-14 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-14",
    "latestAction": {
      "actionDate": "2025-05-14",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3409",
    "number": "3409",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "M001196",
        "district": "6",
        "firstName": "Seth",
        "fullName": "Rep. Moulton, Seth [D-MA-6]",
        "lastName": "Moulton",
        "party": "D",
        "state": "MA"
      }
    ],
    "title": "HEADs UP Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-14T08:05:30Z",
    "updateDateIncludingText": "2026-04-14T08:05:30Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-14",
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
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-05-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-14",
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
          "date": "2025-05-14T14:05:25Z",
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
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-05-14",
      "state": "PA"
    },
    {
      "bioguideId": "D000624",
      "district": "6",
      "firstName": "Debbie",
      "fullName": "Rep. Dingell, Debbie [D-MI-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Dingell",
      "party": "D",
      "sponsorshipDate": "2025-05-14",
      "state": "MI"
    },
    {
      "bioguideId": "M001206",
      "district": "25",
      "firstName": "Joseph",
      "fullName": "Rep. Morelle, Joseph D. [D-NY-25]",
      "isOriginalCosponsor": "True",
      "lastName": "Morelle",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-05-14",
      "state": "NY"
    },
    {
      "bioguideId": "T000469",
      "district": "20",
      "firstName": "Paul",
      "fullName": "Rep. Tonko, Paul [D-NY-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Tonko",
      "party": "D",
      "sponsorshipDate": "2025-05-14",
      "state": "NY"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2025-05-14",
      "state": "IL"
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
      "sponsorshipDate": "2025-05-19",
      "state": "DC"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-05-19",
      "state": "NJ"
    },
    {
      "bioguideId": "F000110",
      "district": "6",
      "firstName": "Cleo",
      "fullName": "Rep. Fields, Cleo [D-LA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Fields",
      "party": "D",
      "sponsorshipDate": "2025-06-09",
      "state": "LA"
    },
    {
      "bioguideId": "K000402",
      "district": "26",
      "firstName": "Timothy",
      "fullName": "Rep. Kennedy, Timothy M. [D-NY-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Kennedy",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-06-10",
      "state": "NY"
    },
    {
      "bioguideId": "S001201",
      "district": "3",
      "firstName": "Thomas",
      "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Suozzi",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-06-23",
      "state": "NY"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2025-07-02",
      "state": "DE"
    },
    {
      "bioguideId": "H001085",
      "district": "6",
      "firstName": "Chrissy",
      "fullName": "Rep. Houlahan, Chrissy [D-PA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Houlahan",
      "party": "D",
      "sponsorshipDate": "2025-10-21",
      "state": "PA"
    },
    {
      "bioguideId": "B001285",
      "district": "26",
      "firstName": "Julia",
      "fullName": "Rep. Brownley, Julia [D-CA-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Brownley",
      "party": "D",
      "sponsorshipDate": "2025-11-07",
      "state": "CA"
    },
    {
      "bioguideId": "P000597",
      "district": "1",
      "firstName": "Chellie",
      "fullName": "Rep. Pingree, Chellie [D-ME-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Pingree",
      "party": "D",
      "sponsorshipDate": "2025-11-07",
      "state": "ME"
    },
    {
      "bioguideId": "K000398",
      "district": "7",
      "firstName": "Thomas",
      "fullName": "Rep. Kean, Thomas H. [R-NJ-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Kean",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2026-03-25",
      "state": "NJ"
    },
    {
      "bioguideId": "M000312",
      "district": "2",
      "firstName": "James",
      "fullName": "Rep. McGovern, James P. [D-MA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "McGovern",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2026-04-13",
      "state": "MA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3409ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3409\nIN THE HOUSE OF REPRESENTATIVES\nMay 14, 2025 Mr. Moulton (for himself, Mr. Fitzpatrick , Mrs. Dingell , Mr. Morelle , Mr. Tonko , and Mr. Krishnamoorthi ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Public Health Service Act to expand and improve health care services by health centers and the National Health Service Corps for individuals with a developmental disability, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Healthcare Extension and Accessibility for Developmentally disabled and Underserved Population Act of 2025 or the HEADs UP Act of 2025 .\n#### 2. Health care services by health centers and National Health Service Corps for individuals with a developmental disability\n##### (a) Inclusion within special medically underserved populations for purposes of health center definition\nSection 330(a)(1) of the Public Health Service Act ( 42 U.S.C. 254b(a)(1) ) is amended by striking and residents of public housing, and inserting residents of public housing, and individuals with a developmental disability .\n##### (b) Definition\nSection 330(b) of the Public Health Service Act ( 42 U.S.C. 254b(a)(1) ) is amended by adding at the end the following:\n(4) Individuals with a developmental disability In this section, the term individuals with a developmental disability means individuals with a developmental disability as defined in section 102 of the Developmental Disabilities Assistance and Bill of Rights Act of 2000. .\n##### (c) Grants for services\n**(1) Authorization**\nSection 330 of the Public Health Service Act ( 42 U.S.C. 254b ) is amended\u2014\n**(A)**\nby redesignating subsections (j) through (r) as subsections (k) through (s), respectively; and\n**(B)**\nby inserting after subsection (i) the following:\n(j) Individuals with a developmental disability (1) In general The Secretary may award grants to existing health centers for the purposes described in subsections (e) and (f) to establish or operate new delivery sites for comprehensive primary health services, including dental care, to a special medically underserved population comprised of individuals with a developmental disability. (2) Required services In addition to required primary health services (as defined in subsection (b)(1)), an entity that receives a grant under this subsection shall be required to provide specialized treatment, as necessary, including specially trained dental care services, to individuals with a developmental disability as a condition of such grant. (3) Supplement not supplant requirement A grant awarded under this subsection shall be expended to supplement, and not supplant, the expenditures of the health center and the value of in kind contributions for the delivery of services to the population described in paragraph (1). .\n**(2) Conforming change**\nSection 330(a)(2) of the Public Health Service Act ( 42 U.S.C. 254b(a)(2) ) is amended by striking or (i) and inserting (i), or (j) .\n##### (d) Funding\n**(1) Preserving the distribution of grants**\nSubsection (s)(2)(B) (as redesignated) of section 330 of the Public Health Service Act ( 42 U.S.C. 254b ) is amended by striking the total amount appropriated to carry out this section for that fiscal year and inserting the total amount appropriated to carry out this section (other than subsection (j)) for that fiscal year .\n**(2) Funding report**\nSubsection (s)(3)(A) (as redesignated) of section 330 of the Public Health Service Act ( 42 U.S.C. 254b ) is amended by striking and migratory and seasonal agricultural workers, and inserting migratory and seasonal agricultural workers, and individuals with a developmental disability, .\n**(3) Authorization of appropriations**\nSubsection (s) (as redesignated) of section 330 of the Public Health Service Act ( 42 U.S.C. 254b ) is amended by adding at the end the following:\n(7) Funding for services for individuals with a developmental disability To carry out subsection (j), there is authorized to be appropriated $15,000,000 for each of fiscal years 2026 through 2030. .\n##### (e) Inclusion for purposes of health professional shortage areas\nSection 332(a)(3) of the Public Health Service Act is amended by striking and residents of public housing (as defined in section 3(b)(1) of the United States Housing Act of 1937 ( 42 U.S.C. 1437a(b)(1) )) and inserting residents of public housing (as defined in section 3(b)(1) of the United States Housing Act of 1937 ( 42 U.S.C. 1437a(b)(1) )), and individuals with a developmental disability (as defined in section 330(b)) .",
      "versionDate": "2025-05-14",
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
        "updateDate": "2025-05-28T12:30:34Z"
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
      "date": "2025-05-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3409ih.xml"
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
      "title": "HEADs UP Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-21T04:08:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "HEADs UP Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-21T04:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Healthcare Extension and Accessibility for Developmentally disabled and Underserved Population Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-21T04:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Public Health Service Act to expand and improve health care services by health centers and the National Health Service Corps for individuals with a developmental disability, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-21T04:03:23Z"
    }
  ]
}
```
