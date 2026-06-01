# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4400?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4400
- Title: Farmers First Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 4400
- Origin chamber: House
- Introduced date: 2025-07-15
- Update date: 2026-04-07T08:05:28Z
- Update date including text: 2026-04-07T08:05:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-07-15: Introduced in House
- 2025-07-15 - IntroReferral: Introduced in House
- 2025-07-15 - IntroReferral: Introduced in House
- 2025-07-15 - IntroReferral: Referred to the House Committee on Agriculture.
- Latest action: 2025-07-15: Introduced in House

## Actions

- 2025-07-15 - IntroReferral: Introduced in House
- 2025-07-15 - IntroReferral: Introduced in House
- 2025-07-15 - IntroReferral: Referred to the House Committee on Agriculture.

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
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4400",
    "number": "4400",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "F000446",
        "district": "4",
        "firstName": "Randy",
        "fullName": "Rep. Feenstra, Randy [R-IA-4]",
        "lastName": "Feenstra",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "Farmers First Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-07T08:05:28Z",
    "updateDateIncludingText": "2026-04-07T08:05:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-15",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Agriculture.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-07-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-15",
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
          "date": "2025-07-15T14:01:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "systemCode": "hsag00",
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
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2025-07-15",
      "state": "MN"
    },
    {
      "bioguideId": "B001295",
      "district": "12",
      "firstName": "Mike",
      "fullName": "Rep. Bost, Mike [R-IL-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Bost",
      "party": "R",
      "sponsorshipDate": "2025-07-15",
      "state": "IL"
    },
    {
      "bioguideId": "C001059",
      "district": "21",
      "firstName": "Jim",
      "fullName": "Rep. Costa, Jim [D-CA-21]",
      "isOriginalCosponsor": "True",
      "lastName": "Costa",
      "party": "D",
      "sponsorshipDate": "2025-07-15",
      "state": "CA"
    },
    {
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2025-07-15",
      "state": "IA"
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
      "sponsorshipDate": "2025-08-08",
      "state": "VA"
    },
    {
      "bioguideId": "B000490",
      "district": "2",
      "firstName": "Sanford",
      "fullName": "Rep. Bishop, Sanford D. [D-GA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bishop",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-08-26",
      "state": "GA"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-09-02",
      "state": "NC"
    },
    {
      "bioguideId": "T000487",
      "district": "2",
      "firstName": "Jill",
      "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Tokuda",
      "middleName": "N.",
      "party": "D",
      "sponsorshipDate": "2025-09-09",
      "state": "HI"
    },
    {
      "bioguideId": "D000629",
      "district": "3",
      "firstName": "Sharice",
      "fullName": "Rep. Davids, Sharice [D-KS-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Davids",
      "party": "D",
      "sponsorshipDate": "2025-09-09",
      "state": "KS"
    },
    {
      "bioguideId": "S001221",
      "district": "3",
      "firstName": "Hillary",
      "fullName": "Rep. Scholten, Hillary J. [D-MI-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Scholten",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-10-14",
      "state": "MI"
    },
    {
      "bioguideId": "G000605",
      "district": "13",
      "firstName": "Adam",
      "fullName": "Rep. Gray, Adam [D-CA-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Gray",
      "party": "D",
      "sponsorshipDate": "2025-12-02",
      "state": "CA"
    },
    {
      "bioguideId": "H001103",
      "district": "0",
      "firstName": "Pablo",
      "fullName": "Rescom. Hern\u00e1ndez, Pablo Jose [D-PR-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Hern\u00e1ndez",
      "middleName": "Jose",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "PR"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "NJ"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "CO"
    },
    {
      "bioguideId": "H001072",
      "district": "2",
      "firstName": "J.",
      "fullName": "Rep. Hill, J. French [R-AR-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Hill",
      "middleName": "French",
      "party": "R",
      "sponsorshipDate": "2026-03-09",
      "state": "AR"
    },
    {
      "bioguideId": "S001216",
      "district": "8",
      "firstName": "Kim",
      "fullName": "Rep. Schrier, Kim [D-WA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Schrier",
      "party": "D",
      "sponsorshipDate": "2026-03-09",
      "state": "WA"
    },
    {
      "bioguideId": "T000469",
      "district": "20",
      "firstName": "Paul",
      "fullName": "Rep. Tonko, Paul [D-NY-20]",
      "isOriginalCosponsor": "False",
      "lastName": "Tonko",
      "party": "D",
      "sponsorshipDate": "2026-04-06",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4400ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4400\nIN THE HOUSE OF REPRESENTATIVES\nJuly 15, 2025 Mr. Feenstra (for himself, Ms. Craig , Mr. Bost , Mr. Costa , and Mr. Nunn of Iowa ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the Food, Conservation, and Energy Act of 2008 to reauthorize the Farm and Ranch Stress Assistance Network, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Farmers First Act of 2025 .\n#### 2. Farm and Ranch Stress Assistance Network\nSection 7522 of the Food, Conservation, and Energy Act of 2008 ( 7 U.S.C. 5936 ) is amended\u2014\n**(1)**\nin subsection (b)(1)(A), by inserting , including crisis lines before the semicolon at the end;\n**(2)**\nin subsection (d), by striking $10,000,000 for each of fiscal years 2019 through 2023 and inserting $15,000,000 for each of fiscal years 2026 through 2030 ; and\n**(3)**\nby striking subsection (e) and inserting the following:\n(e) Referrals to providers As part of the efforts of the recipient of a grant under subsection (a) to connect individuals to behavioral health counseling and wellness support and to ensure individuals have access to a comprehensive scope of mental health and substance use treatments and supports, when applicable, the grant recipient may establish referral relationships with\u2014 (1) certified community behavioral health clinics described in section 223 of the Protecting Access to Medicare Act of 2014 ( 42 U.S.C. 1396a note; Public Law 113\u201393 ); (2) health centers (as defined in section 330(a) of the Public Health Service Act ( 42 U.S.C. 254b(a) )); (3) rural health clinics (as defined in section 1861(aa) of the Social Security Act ( 42 U.S.C. 1395x(aa) )); (4) Federally qualified health centers (as defined in that section); and (5) critical access hospitals (as defined in section 1861(mm) of the Social Security Act ( 42 U.S.C. 1395x(mm) )). .",
      "versionDate": "2025-07-15",
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
        "actionDate": "2026-03-05",
        "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 34 - 17."
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
        "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry."
      },
      "number": "2282",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Farmers First Act of 2025",
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
        "name": "Agriculture and Food",
        "updateDate": "2025-08-01T15:08:32Z"
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
          "measure-id": "id119hr4400",
          "measure-number": "4400",
          "measure-type": "hr",
          "orig-publish-date": "2025-07-15",
          "originChamber": "HOUSE",
          "update-date": "2025-08-07"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr4400v00",
            "update-date": "2025-08-07"
          },
          "action-date": "2025-07-15",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Farmers First Act of 2025</strong></p><p>This bill extends through FY2030 and revises the Farm and Ranch Stress Assistance Network (FRSAN). This Department of Agriculture program provides competitive grants to states, Indian tribes, and qualified nonprofit organizations to provide stress assistance programs (i.e., professional agricultural behavioral health counseling, helplines, and resources) to individuals engaged in farming, ranching, and agriculture-related occupations.</p><p>The bill specifies that the grant funding for farm telephone helplines and websites may also be used for crisis lines.</p><p>Further, FRSAN grant recipients may establish referral relationships with providers, including Certified Community Behavioral Health Clinics, health centers, rural health clinics, and critical access hospitals.</p>"
        },
        "title": "Farmers First Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr4400.xml",
    "summary": {
      "actionDate": "2025-07-15",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Farmers First Act of 2025</strong></p><p>This bill extends through FY2030 and revises the Farm and Ranch Stress Assistance Network (FRSAN). This Department of Agriculture program provides competitive grants to states, Indian tribes, and qualified nonprofit organizations to provide stress assistance programs (i.e., professional agricultural behavioral health counseling, helplines, and resources) to individuals engaged in farming, ranching, and agriculture-related occupations.</p><p>The bill specifies that the grant funding for farm telephone helplines and websites may also be used for crisis lines.</p><p>Further, FRSAN grant recipients may establish referral relationships with providers, including Certified Community Behavioral Health Clinics, health centers, rural health clinics, and critical access hospitals.</p>",
      "updateDate": "2025-08-07",
      "versionCode": "id119hr4400"
    },
    "title": "Farmers First Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-07-15",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Farmers First Act of 2025</strong></p><p>This bill extends through FY2030 and revises the Farm and Ranch Stress Assistance Network (FRSAN). This Department of Agriculture program provides competitive grants to states, Indian tribes, and qualified nonprofit organizations to provide stress assistance programs (i.e., professional agricultural behavioral health counseling, helplines, and resources) to individuals engaged in farming, ranching, and agriculture-related occupations.</p><p>The bill specifies that the grant funding for farm telephone helplines and websites may also be used for crisis lines.</p><p>Further, FRSAN grant recipients may establish referral relationships with providers, including Certified Community Behavioral Health Clinics, health centers, rural health clinics, and critical access hospitals.</p>",
      "updateDate": "2025-08-07",
      "versionCode": "id119hr4400"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4400ih.xml"
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
      "title": "Farmers First Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-24T01:53:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Farmers First Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-24T01:53:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Food, Conservation, and Energy Act of 2008 to reauthorize the Farm and Ranch Stress Assistance Network, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-24T01:48:23Z"
    }
  ]
}
```
