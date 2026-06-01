# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2426?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2426
- Title: Equitable Community Access to Pharmacist Services Act
- Congress: 119
- Bill type: S
- Bill number: 2426
- Origin chamber: Senate
- Introduced date: 2025-07-24
- Update date: 2026-02-10T12:03:17Z
- Update date including text: 2026-02-10T12:03:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-24: Introduced in Senate
- 2025-07-24 - IntroReferral: Introduced in Senate
- 2025-07-24 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-07-24: Introduced in Senate

## Actions

- 2025-07-24 - IntroReferral: Introduced in Senate
- 2025-07-24 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-24",
    "latestAction": {
      "actionDate": "2025-07-24",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2426",
    "number": "2426",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "T000250",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Thune, John [R-SD]",
        "lastName": "Thune",
        "party": "R",
        "state": "SD"
      }
    ],
    "title": "Equitable Community Access to Pharmacist Services Act",
    "type": "S",
    "updateDate": "2026-02-10T12:03:17Z",
    "updateDateIncludingText": "2026-02-10T12:03:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-24",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-24",
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
            "date": "2025-07-24T14:27:18Z",
            "name": "Referred To"
          },
          {
            "date": "2025-07-24T14:27:18Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-07-24",
      "state": "VA"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-07-24",
      "state": "NC"
    },
    {
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2025-07-24",
      "state": "MT"
    },
    {
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2025-07-24",
      "state": "NH"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-07-24",
      "state": "MA"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-07-24",
      "state": "VT"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2025-07-24",
      "state": "NV"
    },
    {
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "False",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2025-07-30",
      "state": "OK"
    },
    {
      "bioguideId": "B001303",
      "firstName": "Lisa",
      "fullName": "Sen. Blunt Rochester, Lisa [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Blunt Rochester",
      "party": "D",
      "sponsorshipDate": "2025-09-03",
      "state": "DE"
    },
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "False",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2025-09-03",
      "state": "ND"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "False",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-09-09",
      "state": "MN"
    },
    {
      "bioguideId": "S001198",
      "firstName": "Dan",
      "fullName": "Sen. Sullivan, Dan [R-AK]",
      "isOriginalCosponsor": "False",
      "lastName": "Sullivan",
      "party": "R",
      "sponsorshipDate": "2025-09-09",
      "state": "AK"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "False",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2025-09-17",
      "state": "NM"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "False",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-09-17",
      "state": "NH"
    },
    {
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "False",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-09-17",
      "state": "WV"
    },
    {
      "bioguideId": "F000463",
      "firstName": "Deb",
      "fullName": "Sen. Fischer, Deb [R-NE]",
      "isOriginalCosponsor": "False",
      "lastName": "Fischer",
      "party": "R",
      "sponsorshipDate": "2025-09-17",
      "state": "NE"
    },
    {
      "bioguideId": "M001153",
      "firstName": "Lisa",
      "fullName": "Sen. Murkowski, Lisa [R-AK]",
      "isOriginalCosponsor": "False",
      "lastName": "Murkowski",
      "party": "R",
      "sponsorshipDate": "2025-10-07",
      "state": "AK"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "False",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-10-07",
      "state": "VA"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "DE"
    },
    {
      "bioguideId": "R000605",
      "firstName": "Mike",
      "fullName": "Sen. Rounds, Mike [R-SD]",
      "isOriginalCosponsor": "False",
      "lastName": "Rounds",
      "party": "R",
      "sponsorshipDate": "2025-10-08",
      "state": "SD"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-10-14",
      "state": "CA"
    },
    {
      "bioguideId": "K000393",
      "firstName": "John",
      "fullName": "Sen. Kennedy, John [R-LA]",
      "isOriginalCosponsor": "False",
      "lastName": "Kennedy",
      "party": "R",
      "sponsorshipDate": "2025-10-14",
      "state": "LA"
    },
    {
      "bioguideId": "M001190",
      "firstName": "Markwayne",
      "fullName": "Sen. Mullin, Markwayne [R-OK]",
      "isOriginalCosponsor": "False",
      "lastName": "Mullin",
      "party": "R",
      "sponsorshipDate": "2025-10-16",
      "state": "OK"
    },
    {
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "False",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2025-10-22",
      "state": "KS"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "False",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-11-20",
      "state": "TN"
    },
    {
      "bioguideId": "P000595",
      "firstName": "Gary",
      "fullName": "Sen. Peters, Gary C. [D-MI]",
      "isOriginalCosponsor": "False",
      "lastName": "Peters",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "MI"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "False",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2025-12-02",
      "state": "RI"
    },
    {
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "False",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "ME"
    },
    {
      "bioguideId": "M001111",
      "firstName": "Patty",
      "fullName": "Sen. Murray, Patty [D-WA]",
      "isOriginalCosponsor": "False",
      "lastName": "Murray",
      "party": "D",
      "sponsorshipDate": "2026-02-09",
      "state": "WA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2426is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2426\nIN THE SENATE OF THE UNITED STATES\nJuly 24, 2025 Mr. Thune (for himself, Mr. Warner , Mr. Tillis , Mr. Daines , Ms. Hassan , Ms. Warren , Mr. Welch , and Ms. Cortez Masto ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend title XVIII of the Social Security Act to provide pharmacy payment of certain services.\n#### 1. Short title\nThis Act may be cited as the Equitable Community Access to Pharmacist Services Act .\n#### 2. Coverage of pharmacist services under medicare part B\n##### (a) Coverage\nSection 1861 of the Social Security Act ( 42 U.S.C. 1395x ) is amended\u2014\n**(1)**\nin subsection (s)(2)\u2014\n**(A)**\nin subparagraph (JJ), by adding and at the end; and\n**(B)**\nby adding at the end the following new subparagraph:\n(KK) pharmacist services (as defined in subsection (nnn)); ; and\n**(2)**\nby adding at the end the following new subsection:\n(nnn) Pharmacist services (1) In general The term pharmacist services means such services furnished by a pharmacist, and such services and supplies furnished as an incident to the pharmacist\u2019s service, which the pharmacist is legally authorized to perform under State law as would otherwise be covered if furnished by a physician or as an incident to a physicians\u2019 service which\u2014 (A) in the case such State law requires such services to be furnished under the supervision of, or working in collaboration with, a physician or practitioner (as defined in section 1842(b)(18)(C)(i)), are so furnished under the supervision of, or working in collaboration with, such physician or practitioner in the manner and to the extent as so required by such State law; and (B) are\u2014 (i) for visits for the evaluation and management of individuals for testing or treatment for COVID\u201319, influenza, respiratory syncytial virus, or streptococcal pharyngitis; or (ii) testing or treatment services that address a public health need related to a public health emergency declared under section 319 of the Public Health Service Act (as determined by the Secretary). (2) Collaboration For purposes of this subsection, the term collaboration means a process in which a pharmacist works with a physician or practitioner (as defined in section 1842(b)(18)(C)(i)), as applicable, to deliver health care services within the scope of the pharmacist\u2019s professional expertise, with medical direction and appropriate supervision as provided for in jointly developed guidelines or other mechanisms as defined by the law of the State in which the services are performed. .\n##### (b) Payment\nSection 1833(a)(1) of the Social Security Act ( 42 U.S.C. 1395l(a)(1) ) is amended\u2014\n**(1)**\nby striking and (HH) and inserting (HH) ; and\n**(2)**\nby inserting before the semicolon at the end the following: , and (II) with respect to pharmacist services (as defined in section 1861(nnn)), the amounts paid shall be equal to 80 percent of the lesser of (i) the actual charge for the services or (ii) 85 percent (or 100 percent, in the case of such services that address a public health need described in paragraph (2)(B) of such section) of the amount determined under the payment basis under section 1848 for such services. .\n##### (c) Prohibition on balance billing for pharmacist services\nSection 1842(b)(18) of the Social Security Act ( 42 U.S.C. 1395u(b)(18) ) is amended\u2014\n**(1)**\nin subparagraph (A), by inserting or a pharmacist after a practitioner described in subparagraph (C) ; and\n**(2)**\nin subparagraph (B)\u2014\n**(A)**\nin the first sentence, by inserting , a pharmacist, after a practitioner described in subparagraph (C) ; and\n**(B)**\nin the third sentence\u2014\n**(i)**\nby inserting , a pharmacist, after a practitioner ; and\n**(ii)**\nby inserting , the pharmacist, after the practitioner .\n##### (d) Application\nThe amendments made by this section shall apply to items and services furnished on or after January 1, 2026.",
      "versionDate": "2025-07-24",
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
        "actionDate": "2025-05-01",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "3164",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Ensuring Community Access to Pharmacist Services Act",
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
        "name": "Health",
        "updateDate": "2025-09-16T15:03:13Z"
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
      "date": "2025-07-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2426is.xml"
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
      "title": "Equitable Community Access to Pharmacist Services Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-10T12:03:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Equitable Community Access to Pharmacist Services Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-06T04:38:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title XVIII of the Social Security Act to provide pharmacy payment of certain services.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-06T04:33:20Z"
    }
  ]
}
```
