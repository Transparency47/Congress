# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7676?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7676
- Title: Career-Connected Learning Pathways Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7676
- Origin chamber: House
- Introduced date: 2026-02-25
- Update date: 2026-04-21T08:06:20Z
- Update date including text: 2026-04-21T08:06:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-25: Introduced in House
- 2026-02-25 - IntroReferral: Introduced in House
- 2026-02-25 - IntroReferral: Introduced in House
- 2026-02-25 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2026-02-25: Introduced in House

## Actions

- 2026-02-25 - IntroReferral: Introduced in House
- 2026-02-25 - IntroReferral: Introduced in House
- 2026-02-25 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-25",
    "latestAction": {
      "actionDate": "2026-02-25",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7676",
    "number": "7676",
    "originChamber": "House",
    "policyArea": {
      "name": "Labor and Employment"
    },
    "sponsors": [
      {
        "bioguideId": "M001227",
        "district": "4",
        "firstName": "Jennifer",
        "fullName": "Rep. McClellan, Jennifer L. [D-VA-4]",
        "lastName": "McClellan",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "Career-Connected Learning Pathways Act of 2026",
    "type": "HR",
    "updateDate": "2026-04-21T08:06:20Z",
    "updateDateIncludingText": "2026-04-21T08:06:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-25",
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
      "actionDate": "2026-02-25",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-25",
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
          "date": "2026-02-25T14:06:30Z",
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
      "bioguideId": "R000305",
      "district": "2",
      "firstName": "Deborah",
      "fullName": "Rep. Ross, Deborah K. [D-NC-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Ross",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-02-25",
      "state": "NC"
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
      "sponsorshipDate": "2026-02-25",
      "state": "GA"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2026-02-25",
      "state": "DC"
    },
    {
      "bioguideId": "G000587",
      "district": "29",
      "firstName": "Sylvia",
      "fullName": "Rep. Garcia, Sylvia R. [D-TX-29]",
      "isOriginalCosponsor": "True",
      "lastName": "Garcia",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-02-25",
      "state": "TX"
    },
    {
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2026-02-25",
      "state": "MN"
    },
    {
      "bioguideId": "P000597",
      "district": "1",
      "firstName": "Chellie",
      "fullName": "Rep. Pingree, Chellie [D-ME-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Pingree",
      "party": "D",
      "sponsorshipDate": "2026-02-26",
      "state": "ME"
    },
    {
      "bioguideId": "G000606",
      "district": "7",
      "firstName": "Adelita",
      "fullName": "Rep. Grijalva, Adelita S. [D-AZ-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Grijalva",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "AZ"
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
      "sponsorshipDate": "2026-03-27",
      "state": "AL"
    },
    {
      "bioguideId": "J000309",
      "district": "1",
      "firstName": "Jonathan",
      "fullName": "Rep. Jackson, Jonathan L. [D-IL-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Jackson",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2026-04-13",
      "state": "IL"
    },
    {
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2026-04-13",
      "state": "CA"
    },
    {
      "bioguideId": "D000216",
      "district": "3",
      "firstName": "Rosa",
      "fullName": "Rep. DeLauro, Rosa L. [D-CT-3]",
      "isOriginalCosponsor": "False",
      "lastName": "DeLauro",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2026-04-20",
      "state": "CT"
    },
    {
      "bioguideId": "D000629",
      "district": "3",
      "firstName": "Sharice",
      "fullName": "Rep. Davids, Sharice [D-KS-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Davids",
      "party": "D",
      "sponsorshipDate": "2026-04-20",
      "state": "KS"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7676ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7676\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 25, 2026 Ms. McClellan (for herself, Ms. Ross , Mr. Johnson of Georgia , Ms. Norton , Ms. Garcia of Texas , and Ms. Craig ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo amend the Carl D. Perkins Career and Technical Education Act of 2006 to authorize States to develop directories of career and technical education programs of study and career pathways, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Career-Connected Learning Pathways Act of 2026 .\n#### 2. State directories of career and technical education programs of study and career pathways\n##### (a) Establishment\nSection 124(b) of the Carl D. Perkins Career and Technical Education Act of 2006 ( 20 U.S.C. 2344(b) ) is amended by striking paragraph (12) and inserting the following:\n(12) developing, publishing, and maintaining a searchable public statewide directory of career and technical education programs of study and career pathways offered in the State that\u2014 (A) includes, for each such program of study and career pathway, the information described in section 134(b)(10) with respect to such program of study or career pathway; (B) is searchable by\u2014 (i) the school district or political subdivision of the State in which each program of study or career pathway is located; (ii) the industry or career cluster for which each program of study or career pathway provides preparation; and (iii) the credential available upon completion of each program of study or career pathway; (C) uses data formats that are\u2014 (i) standard; (ii) open; (iii) linked; and (iv) interoperable; and (D) is updated not less than once each program year; .\n##### (b) Information sharing\nSection 134(b) of such Act ( 20 U.S.C. 2354(b) ) is amended\u2014\n**(1)**\nin paragraph (8), by striking and at the end;\n**(2)**\nin paragraph (9), by striking the period at the end and inserting ; and ; and\n**(3)**\nby adding at the end the following:\n(10) if the eligible agency elects to carry out the activities described in section 124(b)(12), for each career and technical education program of study and career pathway offered by the eligible recipient\u2014 (A) the name of such program of study or career pathway; (B) a description of such program of study or career pathway; (C) the school district or political subdivision of the State in which such program of study or career pathway is located; (D) the industry or career cluster for which such program of study or career pathway provides preparation; (E) each sequence of courses within such program of study or career pathway; (F) any dual or concurrent enrollment credit or recognized postsecondary credential available upon completion of such program of study or career pathway; (G) the postsecondary institution, local workforce development board, or industry or sector partnership affiliated with such program of study or career pathway; (H) any work-based learning opportunities provided by such program of study or career pathway; and (I) evidence of the alignment between such program of study or career pathway and the needs or projected needs of the labor market. .",
      "versionDate": "2026-02-25",
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
        "name": "Labor and Employment",
        "updateDate": "2026-03-16T15:17:36Z"
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
      "date": "2026-02-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7676ih.xml"
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
      "title": "Career-Connected Learning Pathways Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-12T04:53:31Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Career-Connected Learning Pathways Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-12T04:53:30Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Carl D. Perkins Career and Technical Education Act of 2006 to authorize States to develop directories of career and technical education programs of study and career pathways, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-12T04:48:33Z"
    }
  ]
}
```
