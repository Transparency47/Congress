# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5428?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5428
- Title: Medical Student Education Authorization Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5428
- Origin chamber: House
- Introduced date: 2025-09-17
- Update date: 2026-01-08T09:06:59Z
- Update date including text: 2026-01-08T09:06:59Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-17: Introduced in House
- 2025-09-17 - IntroReferral: Introduced in House
- 2025-09-17 - IntroReferral: Introduced in House
- 2025-09-17 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-09-17: Introduced in House

## Actions

- 2025-09-17 - IntroReferral: Introduced in House
- 2025-09-17 - IntroReferral: Introduced in House
- 2025-09-17 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-17",
    "latestAction": {
      "actionDate": "2025-09-17",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5428",
    "number": "5428",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "C001053",
        "district": "4",
        "firstName": "Tom",
        "fullName": "Rep. Cole, Tom [R-OK-4]",
        "lastName": "Cole",
        "party": "R",
        "state": "OK"
      }
    ],
    "title": "Medical Student Education Authorization Act of 2025",
    "type": "HR",
    "updateDate": "2026-01-08T09:06:59Z",
    "updateDateIncludingText": "2026-01-08T09:06:59Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-17",
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
      "actionDate": "2025-09-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-17",
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
          "date": "2025-09-17T14:02:15Z",
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
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2025-09-17",
      "state": "NV"
    },
    {
      "bioguideId": "A000055",
      "district": "4",
      "firstName": "Robert",
      "fullName": "Rep. Aderholt, Robert B. [R-AL-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Aderholt",
      "middleName": "B.",
      "party": "R",
      "sponsorshipDate": "2025-10-28",
      "state": "AL"
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
      "sponsorshipDate": "2025-10-28",
      "state": "VA"
    },
    {
      "bioguideId": "B000740",
      "district": "5",
      "firstName": "Stephanie",
      "fullName": "Rep. Bice, Stephanie I. [R-OK-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Bice",
      "middleName": "I.",
      "party": "R",
      "sponsorshipDate": "2025-10-31",
      "state": "OK"
    },
    {
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2025-10-31",
      "state": "FL"
    },
    {
      "bioguideId": "C001061",
      "district": "5",
      "firstName": "Emanuel",
      "fullName": "Rep. Cleaver, Emanuel [D-MO-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Cleaver",
      "party": "D",
      "sponsorshipDate": "2025-11-04",
      "state": "MO"
    },
    {
      "bioguideId": "C001133",
      "district": "6",
      "firstName": "Juan",
      "fullName": "Rep. Ciscomani, Juan [R-AZ-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Ciscomani",
      "party": "R",
      "sponsorshipDate": "2025-11-04",
      "state": "AZ"
    },
    {
      "bioguideId": "H001099",
      "district": "8",
      "firstName": "Mike",
      "fullName": "Rep. Haridopolos, Mike [R-FL-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Haridopolos",
      "party": "R",
      "sponsorshipDate": "2025-11-04",
      "state": "FL"
    },
    {
      "bioguideId": "P000621",
      "district": "9",
      "firstName": "Nellie",
      "fullName": "Rep. Pou, Nellie [D-NJ-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Pou",
      "party": "D",
      "sponsorshipDate": "2025-11-07",
      "state": "NJ"
    },
    {
      "bioguideId": "H001052",
      "district": "1",
      "firstName": "Andy",
      "fullName": "Rep. Harris, Andy [R-MD-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2025-11-07",
      "state": "MD"
    },
    {
      "bioguideId": "G000591",
      "district": "3",
      "firstName": "Michael",
      "fullName": "Rep. Guest, Michael [R-MS-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Guest",
      "party": "R",
      "sponsorshipDate": "2025-11-12",
      "state": "MS"
    },
    {
      "bioguideId": "Y000067",
      "district": "2",
      "firstName": "Rudy",
      "fullName": "Rep. Yakym, Rudy [R-IN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Yakym",
      "party": "R",
      "sponsorshipDate": "2025-11-17",
      "state": "IN"
    },
    {
      "bioguideId": "J000298",
      "district": "7",
      "firstName": "Pramila",
      "fullName": "Rep. Jayapal, Pramila [D-WA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Jayapal",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "WA"
    },
    {
      "bioguideId": "R000609",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. Rutherford, John H. [R-FL-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Rutherford",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-12-02",
      "state": "FL"
    },
    {
      "bioguideId": "D000629",
      "district": "3",
      "firstName": "Sharice",
      "fullName": "Rep. Davids, Sharice [D-KS-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Davids",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "KS"
    },
    {
      "bioguideId": "F000484",
      "district": "6",
      "firstName": "Randy",
      "fullName": "Rep. Fine, Randy [R-FL-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Fine",
      "party": "R",
      "sponsorshipDate": "2025-12-09",
      "state": "FL"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-12-10",
      "state": "NJ"
    },
    {
      "bioguideId": "C001136",
      "district": "3",
      "firstName": "Herbert",
      "fullName": "Rep. Conaway, Herbert C. [D-NJ-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Conaway",
      "middleName": "C.",
      "party": "D",
      "sponsorshipDate": "2025-12-10",
      "state": "NJ"
    },
    {
      "bioguideId": "W000804",
      "district": "1",
      "firstName": "Robert",
      "fullName": "Rep. Wittman, Robert J. [R-VA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Wittman",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2026-01-07",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5428ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5428\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 17, 2025 Mr. Cole (for himself and Ms. Titus ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Public Health Service Act to establish a grant program to award grants to accredited public institutions of higher education, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Medical Student Education Authorization Act of 2025 .\n#### 2. Education program to support primary health care for medically underserved communities\nPart B of title VII of the Public Health Service Act ( 42 U.S.C. 293 et seq. ) is amended by adding at the end the following:\n742. Education program to support primary health care for medically underserved communities (a) Establishment The Secretary, acting through the Administrator of the Health Resources and Services Administration (in this section referred to as the Secretary ) shall establish a grant program to award grants to accredited public institutions of higher education to carry out the activities described in subsection (d) for the purposes of\u2014 (1) supporting education for medical students who are preparing to become physicians; and (2) preparing and encouraging each such student trained by a grantee to serve in a Tribal, rural, or medically underserved community as a primary care physician after completing residency training. (b) Eligibility In order to be eligible to receive a grant under this section, an accredited public institution of higher education shall\u2014 (1) be located in a State that is in the top quartile of States with a projected shortage of primary care physicians, as determined by the Secretary; and (2) submit an application to the Secretary at such time, in such manner, and containing such information as the Secretary may require, that includes\u2014 (A) a certification that such institution will use amounts provided to the institution through the grant to carry out the activities described in subsection (d); and (B) a description of how such institution will carry out such activities. (c) Priority In awarding grants under this section, the Secretary shall give priority to accredited public institutions of higher education that meet the eligibility requirements of subsection (b) and\u2014 (1) are located in a State with not fewer than 2 Indian Tribes or Tribal organizations (as such terms are defined in section 4 of the Indian Self-Determination and Education Assistance Act); and (2) have established, or demonstrate plans to establish, a strategic partnership with entities described in subsection (d)(4) that supports the purposes described in subsection (a). (d) Use of funds An eligible entity that receives a grant under this section shall, as appropriate, use the funds made available under such grant to carry out the following activities: (1) Support community-based training for medical students who will practice in or serve Tribal, rural, or medically underserved communities. (2) Develop and operate programs to train medical students in the provision of primary care services, which may include developing training programs and activities that\u2014 (A) emphasize care for Tribal, rural, or medically underserved communities; (B) are applicable to primary care practice with respect to individuals from Tribal, rural, or medically underserved communities; and (C) promote interdisciplinary training. (3) Increase the capacity of faculty to develop and operate programs described in paragraph (2). (4) Develop strategic partnerships, such as public-private partnerships, to improve health outcomes for individuals from Tribal, rural, or medically underserved communities, which partnerships may include\u2014 (A) federally recognized Tribes, Tribal Colleges or Universities (as such term is defined in section 316 of the Higher Education Act of 1965), and Tribal organizations (as such term is defined in section 4 of the Indian Self-Determination and Education Assistance Act); (B) Federally qualified health centers; (C) rural health clinics; (D) health facilities or programs operated by or in accordance with a contract or grant with the Indian Health Service; and (E) primary care clinics. (5) Develop a plan, as appropriate, for followup with graduates, including with respect to specialties, as applicable. (6) Develop, implement, and evaluate methods to improve recruitment and retention of medical students from Tribal, rural, or medically underserved communities. (7) Train and support instructors to serve Tribal, rural, or medically underserved communities. (8) Prepare medical students for transition into primary care residency training and future practice. (9) Provide scholarships to medical students. (e) Grant period A grant under this section shall be awarded for a period of not more than 5 years. (f) Grant amount Each fiscal year, the amount of a grant made to an eligible entity under this section shall be not less than $1,000,000. (g) Matching requirement The Secretary shall, as appropriate, require that an eligible entity receiving a grant under this section provide non-Federal matching funds, which may be in cash or in kind, in an amount that is not more than 10 percent of the total amount of Federal funds provided through the grant each fiscal year. (h) Authorization of appropriations There is authorized to be appropriated to carry out this section $75,000,000 for each of fiscal years 2026 through 2028. .",
      "versionDate": "2025-09-17",
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
        "updateDate": "2025-11-17T18:37:16Z"
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
      "date": "2025-09-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5428ih.xml"
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
      "title": "Medical Student Education Authorization Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-30T04:38:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Medical Student Education Authorization Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-30T04:38:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Public Health Service Act to establish a grant program to award grants to accredited public institutions of higher education, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-30T04:33:18Z"
    }
  ]
}
```
