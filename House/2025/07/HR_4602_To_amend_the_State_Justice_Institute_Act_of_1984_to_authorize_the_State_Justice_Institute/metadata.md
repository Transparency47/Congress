# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4602?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4602
- Title: Countering Threats and Attacks on Our Judges Act
- Congress: 119
- Bill type: HR
- Bill number: 4602
- Origin chamber: House
- Introduced date: 2025-07-22
- Update date: 2026-04-15T08:05:38Z
- Update date including text: 2026-04-15T08:05:38Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-22: Introduced in House
- 2025-07-22 - IntroReferral: Introduced in House
- 2025-07-22 - IntroReferral: Introduced in House
- 2025-07-22 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-07-22: Introduced in House

## Actions

- 2025-07-22 - IntroReferral: Introduced in House
- 2025-07-22 - IntroReferral: Introduced in House
- 2025-07-22 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-22",
    "latestAction": {
      "actionDate": "2025-07-22",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4602",
    "number": "4602",
    "originChamber": "House",
    "policyArea": {
      "name": "Law"
    },
    "sponsors": [
      {
        "bioguideId": "M001208",
        "district": "6",
        "firstName": "Lucy",
        "fullName": "Rep. McBath, Lucy [D-GA-6]",
        "lastName": "McBath",
        "party": "D",
        "state": "GA"
      }
    ],
    "title": "Countering Threats and Attacks on Our Judges Act",
    "type": "HR",
    "updateDate": "2026-04-15T08:05:38Z",
    "updateDateIncludingText": "2026-04-15T08:05:38Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-22",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-07-22",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-22",
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
          "date": "2025-07-22T14:02:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "M001157",
      "district": "10",
      "firstName": "Michael",
      "fullName": "Rep. McCaul, Michael T. [R-TX-10]",
      "isOriginalCosponsor": "True",
      "lastName": "McCaul",
      "middleName": "T.",
      "party": "R",
      "sponsorshipDate": "2025-07-22",
      "state": "TX"
    },
    {
      "bioguideId": "R000606",
      "district": "8",
      "firstName": "Jamie",
      "fullName": "Rep. Raskin, Jamie [D-MD-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Raskin",
      "party": "D",
      "sponsorshipDate": "2025-07-22",
      "state": "MD"
    },
    {
      "bioguideId": "G000589",
      "district": "5",
      "firstName": "Lance",
      "fullName": "Rep. Gooden, Lance [R-TX-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Gooden",
      "party": "R",
      "sponsorshipDate": "2025-07-22",
      "state": "TX"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2025-07-22",
      "state": "GA"
    },
    {
      "bioguideId": "S000250",
      "district": "17",
      "firstName": "Pete",
      "fullName": "Rep. Sessions, Pete [R-TX-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Sessions",
      "party": "R",
      "sponsorshipDate": "2025-07-22",
      "state": "TX"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2025-07-22",
      "state": "CO"
    },
    {
      "bioguideId": "D000399",
      "district": "37",
      "firstName": "Lloyd",
      "fullName": "Rep. Doggett, Lloyd [D-TX-37]",
      "isOriginalCosponsor": "True",
      "lastName": "Doggett",
      "party": "D",
      "sponsorshipDate": "2025-07-22",
      "state": "TX"
    },
    {
      "bioguideId": "M001224",
      "district": "1",
      "firstName": "Nathaniel",
      "fullName": "Rep. Moran, Nathaniel [R-TX-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2025-07-22",
      "state": "TX"
    },
    {
      "bioguideId": "K000392",
      "district": "8",
      "firstName": "David",
      "fullName": "Rep. Kustoff, David [R-TN-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Kustoff",
      "party": "R",
      "sponsorshipDate": "2025-07-22",
      "state": "TN"
    },
    {
      "bioguideId": "S001148",
      "district": "2",
      "firstName": "Michael",
      "fullName": "Rep. Simpson, Michael K. [R-ID-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Simpson",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-09-26",
      "state": "ID"
    },
    {
      "bioguideId": "S001185",
      "district": "7",
      "firstName": "Terri",
      "fullName": "Rep. Sewell, Terri A. [D-AL-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Sewell",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-09-26",
      "state": "AL"
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
      "sponsorshipDate": "2025-10-03",
      "state": "NJ"
    },
    {
      "bioguideId": "S001193",
      "district": "14",
      "firstName": "Eric",
      "fullName": "Rep. Swalwell, Eric [D-CA-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Swalwell",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "CA"
    },
    {
      "bioguideId": "M001228",
      "district": "2",
      "firstName": "Celeste",
      "fullName": "Rep. Maloy, Celeste [R-UT-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Maloy",
      "party": "R",
      "sponsorshipDate": "2025-10-21",
      "state": "UT"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2025-10-21",
      "state": "IL"
    },
    {
      "bioguideId": "Y000067",
      "district": "2",
      "firstName": "Rudy",
      "fullName": "Rep. Yakym, Rudy [R-IN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Yakym",
      "party": "R",
      "sponsorshipDate": "2026-03-03",
      "state": "IN"
    },
    {
      "bioguideId": "L000601",
      "district": "1",
      "firstName": "Greg",
      "fullName": "Rep. Landsman, Greg [D-OH-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Landsman",
      "party": "D",
      "sponsorshipDate": "2026-03-03",
      "state": "OH"
    },
    {
      "bioguideId": "B001307",
      "district": "4",
      "firstName": "James",
      "fullName": "Rep. Baird, James R. [R-IN-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Baird",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2026-03-12",
      "state": "IN"
    },
    {
      "bioguideId": "P000620",
      "district": "7",
      "firstName": "Brittany",
      "fullName": "Rep. Pettersen, Brittany [D-CO-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Pettersen",
      "party": "D",
      "sponsorshipDate": "2026-03-12",
      "state": "CO"
    },
    {
      "bioguideId": "H001093",
      "district": "9",
      "firstName": "Erin",
      "fullName": "Rep. Houchin, Erin [R-IN-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Houchin",
      "party": "R",
      "sponsorshipDate": "2026-03-24",
      "state": "IN"
    },
    {
      "bioguideId": "G000559",
      "district": "8",
      "firstName": "John",
      "fullName": "Rep. Garamendi, John [D-CA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Garamendi",
      "party": "D",
      "sponsorshipDate": "2026-03-24",
      "state": "CA"
    },
    {
      "bioguideId": "S001228",
      "district": "2",
      "firstName": "Derek",
      "fullName": "Rep. Schmidt, Derek [R-KS-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Schmidt",
      "party": "R",
      "sponsorshipDate": "2026-04-14",
      "state": "KS"
    },
    {
      "bioguideId": "M001234",
      "district": "3",
      "firstName": "Kelly",
      "fullName": "Rep. Morrison, Kelly [D-MN-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Morrison",
      "party": "D",
      "sponsorshipDate": "2026-04-14",
      "state": "MN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4602ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4602\nIN THE HOUSE OF REPRESENTATIVES\nJuly 22, 2025 Mrs. McBath (for herself, Mr. McCaul , Mr. Raskin , Mr. Gooden , Mr. Johnson of Georgia , Mr. Sessions , Mr. Neguse , Mr. Doggett , Mr. Moran , and Mr. Kustoff ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend the State Justice Institute Act of 1984 to authorize the State Justice Institute to provide awards to certain organizations to establish a State judicial threat intelligence and resource center.\n#### 1. Short title\nThis Act may be cited as the Countering Threats and Attacks on Our Judges Act .\n#### 2. Definitions\nSection 202 of the State Justice Institute Act of 1984 ( 42 U.S.C. 10701 ) is amended\u2014\n**(1)**\nin paragraph (7), by striking and at the end;\n**(2)**\nin paragraph (8)(B), by striking the period at the end and inserting ; and ; and\n**(3)**\nby adding at the end the following:\n(9) eligible organization means a national nonprofit organization that\u2014 (A) provides technical assistance and training on, and has expertise and national-level experience in, judicial security and safety at the State and local levels; (B) has experience in courthouse design and courthouse security design standards; (C) has an understanding of State judicial operations and public access to judicial services; and (D) has experience working with a wide array of different judges and court systems, including an understanding of the challenges facing trial courts, appellate courts, rural courts, and limited-jurisdiction courts at the State and local levels. .\n#### 3. Establishment of State judicial threat intelligence and resource center\nSection 206(c) of the State Justice Institute Act of 1984 ( 42 U.S.C. 10705(c) ) is amended\u2014\n**(1)**\nin paragraph (14), by striking and at the end;\n**(2)**\nby redesignating paragraph (15) as paragraph (16); and\n**(3)**\nby inserting after paragraph (14) the following:\n(15) to provide financial and technical support to eligible organizations to establish, implement, and operate a State judicial threat and intelligence resource center to\u2014 (A) provide technical assistance and training around judicial security, including\u2014 (i) providing judicial officer safety education and training for judicial officers, courts, and local law enforcement; (ii) creating resources and guides around judicial security; and (iii) providing physical security assessments for courts, homes, and other facilities where judicial officers and staff conduct court-related business; (B) proactively monitor threats to the safety of State and local judges and court staff; (C) coordinate with Federal, State, and local law enforcement agencies to mitigate threats to the safety of State and local judges and court staff; (D) develop standardized incident reporting and threat evaluation practices for State and local courts in coordination with State and local law enforcement and fusion centers; (E) develop a national database for reporting, tracking, and sharing information about threats and incidents towards judicial officers and court staff at local and State levels with entities working in the interest of judicial security, including State and local law enforcement and fusion centers; and (F) coordinate research to identify, examine, and advance best practices around judicial security. .\n#### 4. Reports\nNot later than 1 year after the date on which a State judicial threat intelligence and resource center is established under paragraph (15) of section 206(c) of the State Justice Institute Act of 1984, as added by section 3 of this Act, the State Justice Institute shall submit to the Committee on the Judiciary of the Senate and the Committee on the Judiciary of the House of Representatives an annual report on the number of threats to State and local judiciary members and court staff, with breakdown of types of threats and level of seriousness.",
      "versionDate": "2025-07-22",
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
        "actionDate": "2025-11-20",
        "actionTime": "18:18:43",
        "text": "Held at the desk."
      },
      "number": "2379",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Countering Threats and Attacks on Our Judges Act",
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
        "name": "Law",
        "updateDate": "2025-09-11T14:42:58Z"
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
      "date": "2025-07-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4602ih.xml"
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
      "title": "Countering Threats and Attacks on Our Judges Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-01T03:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Countering Threats and Attacks on Our Judges Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-01T03:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the State Justice Institute Act of 1984 to authorize the State Justice Institute to provide awards to certain organizations to establish a State judicial threat intelligence and resource center.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-01T03:48:21Z"
    }
  ]
}
```
