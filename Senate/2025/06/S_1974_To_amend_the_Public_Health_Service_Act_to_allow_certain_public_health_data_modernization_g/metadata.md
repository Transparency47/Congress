# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1974?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1974
- Title: ABC-ED Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1974
- Origin chamber: Senate
- Introduced date: 2025-06-05
- Update date: 2026-05-15T11:03:25Z
- Update date including text: 2026-05-15T11:03:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-05: Introduced in Senate
- 2025-06-05 - IntroReferral: Introduced in Senate
- 2025-06-05 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-06-05: Introduced in Senate

## Actions

- 2025-06-05 - IntroReferral: Introduced in Senate
- 2025-06-05 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-05",
    "latestAction": {
      "actionDate": "2025-06-05",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1974",
    "number": "1974",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "C001088",
        "district": "",
        "firstName": "Christopher",
        "fullName": "Sen. Coons, Christopher A. [D-DE]",
        "lastName": "Coons",
        "party": "D",
        "state": "DE"
      }
    ],
    "title": "ABC-ED Act of 2025",
    "type": "S",
    "updateDate": "2026-05-15T11:03:25Z",
    "updateDateIncludingText": "2026-05-15T11:03:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-05",
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
      "actionDate": "2025-06-05",
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
            "date": "2025-06-05T17:42:26Z",
            "name": "Referred To"
          },
          {
            "date": "2025-06-05T17:42:26Z",
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
      "bioguideId": "M001243",
      "firstName": "David",
      "fullName": "Sen. McCormick, David [R-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "McCormick",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-06-05",
      "state": "PA"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-06-05",
      "state": "NC"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-06-05",
      "state": "ME"
    },
    {
      "bioguideId": "M001190",
      "firstName": "Markwayne",
      "fullName": "Sen. Mullin, Markwayne [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Mullin",
      "party": "R",
      "sponsorshipDate": "2025-06-05",
      "state": "OK"
    },
    {
      "bioguideId": "B001303",
      "firstName": "Lisa",
      "fullName": "Sen. Blunt Rochester, Lisa [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Blunt Rochester",
      "party": "D",
      "sponsorshipDate": "2025-06-05",
      "state": "DE"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "False",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-06-26",
      "state": "NC"
    },
    {
      "bioguideId": "C000127",
      "firstName": "Maria",
      "fullName": "Sen. Cantwell, Maria [D-WA]",
      "isOriginalCosponsor": "False",
      "lastName": "Cantwell",
      "party": "D",
      "sponsorshipDate": "2025-06-26",
      "state": "WA"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "False",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-07-10",
      "state": "MS"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "False",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
      "state": "VT"
    },
    {
      "bioguideId": "T000278",
      "firstName": "Tommy",
      "fullName": "Sen. Tuberville, Tommy [R-AL]",
      "isOriginalCosponsor": "False",
      "lastName": "Tuberville",
      "party": "R",
      "sponsorshipDate": "2026-03-18",
      "state": "AL"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "False",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1974is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1974\nIN THE SENATE OF THE UNITED STATES\nJune 5, 2025 Mr. Coons (for himself, Mr. McCormick , Mr. Tillis , Mr. King , Mr. Mullin , and Ms. Blunt Rochester ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo amend the Public Health Service Act to allow certain public health data modernization grants to be used to track hospital bed capacity, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Addressing Boarding and Crowding in the Emergency Department Act of 2025 or the ABC-ED Act of 2025 .\n#### 2. Allowing public health data modernization grants to be used to track hospital bed capacity\nSection 2823(a)(1) of the Public Health Service Act ( 42 U.S.C. 300hh\u201333(a)(1) ) is amended\u2014\n**(1)**\nin subparagraph (A), by striking and at the end;\n**(2)**\nin subparagraph (B)(viii), by striking the period at the end and inserting ; and ; and\n**(3)**\nby adding at the end the following:\n(C) award grants or cooperative agreements to appropriate entities for the expansion and modernization of public health data systems by\u2014 (i) developing State- or region-wide, real-time (or near real-time), accurate, and scalable systems for tracking\u2014 (I) hospital bed capacity; and (II) how such capacity affects emergency department boarding rates, wait times for treatment in emergency departments, and the amount of time emergency medical services personnel are waiting in emergency departments to offload patients; and (ii) establishing or maintaining a public-facing dashboard of the information tracked pursuant to systems described in clause (i), with such information redacted in accordance with applicable privacy laws. .\n#### 3. Center for Medicare and Medicaid Innovation pilot program\nSection 1115A(b)(2) of the Social Security Act ( 42 U.S.C. 1315a(b)(2) ) is amended\u2014\n**(1)**\nin subparagraph (A), in the third sentence, by inserting , and shall include the models described in clauses (xxviii) and (xxix) of such subparagraph before the period at the end; and\n**(2)**\nin subparagraph (B), by adding at the end the following new clauses:\n(xxviii) Promoting research-based ways to facilitate improved emergency care for applicable individuals who are older adults, including through\u2014 (I) sufficient, flexible, and interdisciplinary staffing and education of staff at emergency departments; (II) changes to the physical infrastructure of emergency departments; (III) introducing geriatric-focused policies, protocols, and quality improvement metrics; and (IV) improving coordination between emergency departments and post-acute care facilities (including senior care facilities such as skilled nursing facilities, assisted living facilities, and independent living facilities) with respect to such individuals, which may include the mutual, bidirectional exchange of medical information and improvements to the transfer process. (xxix) Promoting research-based ways to facilitate improved emergency care for applicable individuals experiencing acute psychiatric crisis, including by\u2014 (I) implementing dedicated units at emergency departments to provide emergency care to such individuals; and (II) improving transfers between emergency departments and post-acute care facilities for such individuals, which may include expedited placement at such facilities. .\n#### 4. Study on best practices for public health data systems for tracking hospital capacity\n##### (a) In general\nThe Comptroller General of the United States shall conduct a study\u2014\n**(1)**\nto determine best practices for the development and maintenance of public health data systems for tracking hospital capacity (including such systems supported pursuant to section 2823(a)(1) of the Public Health Service Act, as amended by section 2) to ensure that such tracking\u2014\n**(A)**\nis State- or region-wide, real-time (or near real-time), accurate, and scalable;\n**(B)**\nincludes tracking of hospital capacity with respect to emergency departments, adult and pediatric intensive care units, inpatient psychiatric services, skilled nursing facilities, and other appropriate types of facilities and services; and\n**(C)**\nis seamlessly and directly integrated with relevant hospital electronic medical records systems; and\n**(2)**\nto assess how implementation of such public health data systems for tracking hospital capacity affects\u2014\n**(A)**\nemergency department boarding rates as determined using quality measures and other metrics that are established and utilized by the Centers for Medicare & Medicaid Services and others accreditation entities;\n**(B)**\nwait times for treatment and discharge in emergency departments; and\n**(C)**\nthe amount of time emergency medical services personnel are waiting in emergency departments to offload patients.\n##### (b) Report to Congress\nNot later than 1 year after the date of enactment of this Act, the Comptroller General shall\u2014\n**(1)**\ncomplete the study under subsection (a); and\n**(2)**\nsubmit to Congress a report on the results of such study.",
      "versionDate": "2025-06-05",
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
        "actionDate": "2025-04-17",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "2936",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Addressing Boarding and Crowding in the Emergency Department",
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
        "updateDate": "2025-06-25T12:15:24Z"
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
      "date": "2025-06-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1974is.xml"
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
      "title": "ABC-ED Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-15T11:03:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "ABC-ED Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-12T04:53:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Addressing Boarding and Crowding in the Emergency Department Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-12T04:53:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Public Health Service Act to allow certain public health data modernization grants to be used to track hospital bed capacity, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-12T04:48:16Z"
    }
  ]
}
```
