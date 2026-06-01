# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1874?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1874
- Title: Title VIII Nursing Workforce Reauthorization Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1874
- Origin chamber: Senate
- Introduced date: 2025-05-22
- Update date: 2026-04-28T11:03:22Z
- Update date including text: 2026-04-28T11:03:22Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-22: Introduced in Senate
- 2025-05-22 - IntroReferral: Introduced in Senate
- 2025-05-22 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-05-22: Introduced in Senate

## Actions

- 2025-05-22 - IntroReferral: Introduced in Senate
- 2025-05-22 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-22",
    "latestAction": {
      "actionDate": "2025-05-22",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1874",
    "number": "1874",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "M001176",
        "district": "",
        "firstName": "Jeff",
        "fullName": "Sen. Merkley, Jeff [D-OR]",
        "lastName": "Merkley",
        "party": "D",
        "state": "OR"
      }
    ],
    "title": "Title VIII Nursing Workforce Reauthorization Act of 2025",
    "type": "S",
    "updateDate": "2026-04-28T11:03:22Z",
    "updateDateIncludingText": "2026-04-28T11:03:22Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-22",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-05-22",
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
            "date": "2025-05-22T16:58:28Z",
            "name": "Referred To"
          },
          {
            "date": "2025-05-22T16:58:28Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-05-22",
      "state": "ME"
    },
    {
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2025-05-22",
      "state": "WI"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-05-22",
      "state": "TN"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-05-22",
      "state": "CT"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-05-22",
      "state": "DE"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-05-22",
      "state": "NY"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-05-22",
      "state": "AZ"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-05-22",
      "state": "CA"
    },
    {
      "bioguideId": "M001153",
      "firstName": "Lisa",
      "fullName": "Sen. Murkowski, Lisa [R-AK]",
      "isOriginalCosponsor": "True",
      "lastName": "Murkowski",
      "party": "R",
      "sponsorshipDate": "2025-05-22",
      "state": "AK"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "False",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-06-24",
      "state": "MS"
    },
    {
      "bioguideId": "B001303",
      "firstName": "Lisa",
      "fullName": "Sen. Blunt Rochester, Lisa [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Blunt Rochester",
      "party": "D",
      "sponsorshipDate": "2025-06-25",
      "state": "DE"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
      "isOriginalCosponsor": "False",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-07-14",
      "state": "NM"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "False",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1874is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1874\nIN THE SENATE OF THE UNITED STATES\nMay 22, 2025 Mr. Merkley (for himself, Ms. Collins , Ms. Baldwin , Mrs. Blackburn , Mr. Blumenthal , Mr. Coons , Mrs. Gillibrand , Mr. Kelly , Mr. Schiff , and Ms. Murkowski ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo amend the Public Health Service Act to reauthorize certain nursing workforce development programs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Title VIII Nursing Workforce Reauthorization Act of 2025 .\n#### 2. Advanced nursing education grants\nSection 811 of the Public Health Service Act ( 42 U.S.C. 296j ) is amended\u2014\n**(1)**\nin subsection (a)(2), by striking programs. and inserting the following: \u201cprograms, including individuals enrolled in\u2014\n(A) authorized nurse practitioner programs described in subsection (c); (B) authorized nurse-midwifery programs described in subsection (d); (C) authorized nurse anesthesia programs described in subsection (e); and (D) authorized clinical nurse specialist programs described in subsection (f). ;\n**(2)**\nin subsection (d)\u2014\n**(A)**\nin paragraph (1), by striking midwives and inserting nurse-midwives ; and\n**(B)**\nin paragraph (2), by striking American College of Nurse-Midwives ; and\n**(3)**\nin subsection (h)(1)(A), by striking fees and inserting fees, including costs for clinical education and preceptors, .\n#### 3. Strengthening capacity for nurse education and practice\n##### (a) In general\nPart D of title VIII of the Public Health Service Act ( 42 U.S.C. 296p et seq. ) is amended\u2014\n**(1)**\nin the part heading, by striking basic ; and\n**(2)**\nin section 831 ( 42 U.S.C. 296p )\u2014\n**(A)**\nin subsection (a)\u2014\n**(i)**\nin paragraph (1), by striking or after the semicolon;\n**(ii)**\nin paragraph (2), by striking methodologies. and inserting methodologies, audiovisual or other equipment, simulation and augmented reality resources, telehealth technologies, and virtual and physical laboratories; or ; and\n**(iii)**\nby adding at the end the following:\n(3) increasing the number of faculty and students at schools of nursing in order to address nursing workforce shortages. ; and\n**(B)**\nin subsection (b)\u2014\n**(i)**\nin paragraph (2), by striking and survivors of domestic violence and inserting survivors of domestic violence, and survivors of sexual assault ;\n**(ii)**\nin paragraph (3), by striking or after the semicolon;\n**(iii)**\nin paragraph (4), by striking the period and inserting ; or ; and\n**(iv)**\nby adding at the end the following:\n(5) partnering with a health care facility, nurse-managed health clinic, community health center, or other facility that provides health care in order to provide education opportunities for the purpose of establishing or expanding clinical education. .\n##### (b) Conforming amendment\nSection 806(f)(2)(C) of the Public Health Service Act ( 42 U.S.C. 296e(f)(2)(C) ) is amended by striking basic .\n#### 4. Authorization of appropriations\nSection 871 of the Public Health Service Act ( 42 U.S.C. 298d ) is amended\u2014\n**(1)**\nin subsection (a), by striking $137,837,000 for each of fiscal years 2021 through 2025 and inserting $184,337,000 for each of fiscal years 2026 through 2030 ; and\n**(2)**\nin subsection (b), by striking $117,135,000 for each of the fiscal years 2021 through 2025 and inserting $121,135,000 for each of fiscal years 2026 through 2030 .",
      "versionDate": "2025-05-22",
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
        "actionDate": "2025-09-10",
        "text": "Forwarded by Subcommittee to Full Committee by Voice Vote."
      },
      "number": "3593",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Title VIII Nursing Workforce Reauthorization Act of 2025",
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
            "name": "Employment and training programs",
            "updateDate": "2025-09-16T14:11:56Z"
          },
          {
            "name": "Health personnel",
            "updateDate": "2025-09-16T14:11:56Z"
          },
          {
            "name": "Health programs administration and funding",
            "updateDate": "2025-09-16T14:11:56Z"
          },
          {
            "name": "Medical education",
            "updateDate": "2025-09-16T14:11:56Z"
          },
          {
            "name": "Nursing",
            "updateDate": "2025-09-16T14:11:56Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-06-16T13:23:01Z"
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
      "date": "2025-05-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1874is.xml"
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
      "title": "Title VIII Nursing Workforce Reauthorization Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-28T11:03:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Title VIII Nursing Workforce Reauthorization Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-04T03:23:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Public Health Service Act to reauthorize certain nursing workforce development programs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-04T03:18:25Z"
    }
  ]
}
```
