# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3939?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3939
- Title: RISE Act
- Congress: 119
- Bill type: HR
- Bill number: 3939
- Origin chamber: House
- Introduced date: 2025-06-12
- Update date: 2026-02-04T09:06:48Z
- Update date including text: 2026-02-04T09:06:48Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-12: Introduced in House
- 2025-06-12 - IntroReferral: Introduced in House
- 2025-06-12 - IntroReferral: Introduced in House
- 2025-06-12 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-06-12: Introduced in House

## Actions

- 2025-06-12 - IntroReferral: Introduced in House
- 2025-06-12 - IntroReferral: Introduced in House
- 2025-06-12 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-12",
    "latestAction": {
      "actionDate": "2025-06-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3939",
    "number": "3939",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "B001278",
        "district": "1",
        "firstName": "Suzanne",
        "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
        "lastName": "Bonamici",
        "party": "D",
        "state": "OR"
      }
    ],
    "title": "RISE Act",
    "type": "HR",
    "updateDate": "2026-02-04T09:06:48Z",
    "updateDateIncludingText": "2026-02-04T09:06:48Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-12",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Education and Workforce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-12",
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
          "date": "2025-06-12T14:02:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
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
      "bioguideId": "H001093",
      "district": "9",
      "firstName": "Erin",
      "fullName": "Rep. Houchin, Erin [R-IN-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Houchin",
      "party": "R",
      "sponsorshipDate": "2025-06-12",
      "state": "IN"
    },
    {
      "bioguideId": "C001069",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Courtney, Joe [D-CT-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Courtney",
      "party": "D",
      "sponsorshipDate": "2025-06-12",
      "state": "CT"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-06-12",
      "state": "NY"
    },
    {
      "bioguideId": "S001216",
      "district": "8",
      "firstName": "Kim",
      "fullName": "Rep. Schrier, Kim [D-WA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Schrier",
      "party": "D",
      "sponsorshipDate": "2025-06-12",
      "state": "WA"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-06-17",
      "state": "PA"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-06-26",
      "state": "NE"
    },
    {
      "bioguideId": "D000623",
      "district": "10",
      "firstName": "Mark",
      "fullName": "Rep. DeSaulnier, Mark [D-CA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "DeSaulnier",
      "party": "D",
      "sponsorshipDate": "2025-08-19",
      "state": "CA"
    },
    {
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2025-10-17",
      "state": "IA"
    },
    {
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2025-10-17",
      "state": "MN"
    },
    {
      "bioguideId": "B001295",
      "district": "12",
      "firstName": "Mike",
      "fullName": "Rep. Bost, Mike [R-IL-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Bost",
      "party": "R",
      "sponsorshipDate": "2025-10-17",
      "state": "IL"
    },
    {
      "bioguideId": "H001085",
      "district": "6",
      "firstName": "Chrissy",
      "fullName": "Rep. Houlahan, Chrissy [D-PA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Houlahan",
      "party": "D",
      "sponsorshipDate": "2025-10-17",
      "state": "PA"
    },
    {
      "bioguideId": "S001230",
      "district": "10",
      "firstName": "Suhas",
      "fullName": "Rep. Subramanyam, Suhas [D-VA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Subramanyam",
      "party": "D",
      "sponsorshipDate": "2026-02-03",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3939ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3939\nIN THE HOUSE OF REPRESENTATIVES\nJune 12, 2025 Ms. Bonamici (for herself, Mrs. Houchin , Mr. Courtney , Mr. Lawler , and Ms. Schrier ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo amend the Higher Education Act of 1965 to provide students with disabilities and their families with access to critical information needed to select the right college and succeed once enrolled.\n#### 1. Short title\nThis Act may be cited as the Respond, Innovate, Succeed, and Empower Act or the RISE Act .\n#### 2. Perfecting amendment to the definition of disability\nSection 103(6) of the Higher Education Act of 1965 ( 20 U.S.C. 1003(6) ) is amended by striking section 3(2) and inserting section 3 .\n#### 3. Supporting students with disabilities to succeed once enrolled in college\nSection 487(a) of the Higher Education Act of 1965 ( 20 U.S.C. 1094(a) ) is amended by adding at the end the following:\n(30) (A) The institution will carry out the following: (i) Adopt policies that make any of the following documentation submitted by an individual sufficient to establish that such individual is an individual with a disability: (I) Documentation that the individual has had an individualized education program (IEP) in accordance with section 614(d) of the Individuals with Disabilities Education Act, including an IEP that may not be current on the date of the determination that the individual has a disability. The institution may ask for additional documentation from an individual who had an IEP but who was subsequently evaluated and determined to be ineligible for services under the Individuals with Disabilities Education Act, including an individual determined to be ineligible during elementary school. (II) Documentation describing services or accommodations provided to the individual pursuant to section 504 of the Rehabilitation Act of 1973 ( 29 U.S.C. 794 ) (commonly referred to as a Section 504 plan ). (III) A plan or record of service for the individual from a private school, a local educational agency, a State educational agency, or an institution of higher education provided in accordance with the Americans with Disabilities Act of 1990 ( 42 U.S.C. 12101 et seq. ). (IV) A record or evaluation from a relevant licensed professional finding that the individual has a disability. (V) A plan or record of disability from another institution of higher education. (VI) Documentation of a disability due to service in the uniformed services, as defined in section 484C(a). (ii) Adopt policies that are transparent and explicit regarding information about the process by which the institution determines eligibility for accommodations. (iii) Disseminate such information to students, parents, and faculty in an accessible format, including during any student orientation and making such information readily available on a public website of the institution. (B) Nothing in this paragraph shall be construed to preclude an institution from establishing less burdensome criteria than that described in subparagraph (A) to establish an individual as an individual with a disability and therefore eligible for accommodations. .\n#### 4. Authorization of funds for the national center for information and technical support for postsecondary students with disabilities\nSection 777(a) of the Higher Education Act of 1965 ( 20 U.S.C. 1140q(a) ) is amended\u2014\n**(1)**\nin paragraph (1), by striking From amounts appropriated under section 778, and inserting From amounts appropriated under paragraph (5), ; and\n**(2)**\nby adding at the end the following:\n(5) Authorization of appropriations There is authorized to be appropriated to carry out this subsection $10,000,000. .\n#### 5. Inclusion of information on students with disabilities\nSection 487(a) of the Higher Education Act of 1965 ( 20 U.S.C. 1094(a) ), as amended by section 3, is further amended by adding at the end the following:\n(31) The institution will submit, for inclusion in the Integrated Postsecondary Education Data System (IPEDS) or any other Federal postsecondary institution data collection effort, key data related to undergraduate students enrolled at the institution who are formally registered as students with disabilities with the institution\u2019s office of disability services (or the equivalent office), including the total number of students with disabilities enrolled, the number of students accessing or receiving accommodations, the percentage of students with disabilities of all undergraduate students, and the total number of undergraduate certificates or degrees awarded to students with disabilities. An institution shall not be required to submit the information described in the preceding sentence if the number of such students would reveal personally identifiable information about an individual student. .\n#### 6. Rule of construction\nNone of the amendments made by this Act shall be construed to affect the meaning of the terms reasonable accommodation or record of impairment under the Americans with Disabilities Act of 1990 ( 42 U.S.C. 12101 et seq. ) or the rights or remedies provided under such Act.",
      "versionDate": "2025-06-12",
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
        "name": "Education",
        "updateDate": "2025-07-02T18:24:06Z"
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
      "date": "2025-06-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3939ih.xml"
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
      "title": "RISE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-19T04:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "RISE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-19T04:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Respond, Innovate, Succeed, and Empower Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-19T04:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Higher Education Act of 1965 to provide students with disabilities and their families with access to critical information needed to select the right college and succeed once enrolled.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-19T04:48:29Z"
    }
  ]
}
```
