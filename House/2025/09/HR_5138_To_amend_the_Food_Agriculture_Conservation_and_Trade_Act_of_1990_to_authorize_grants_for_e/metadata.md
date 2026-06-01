# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5138?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5138
- Title: ASPIRE Act
- Congress: 119
- Bill type: HR
- Bill number: 5138
- Origin chamber: House
- Introduced date: 2025-09-04
- Update date: 2025-12-19T09:08:03Z
- Update date including text: 2025-12-19T09:08:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-09-04: Introduced in House
- 2025-09-04 - IntroReferral: Introduced in House
- 2025-09-04 - IntroReferral: Introduced in House
- 2025-09-04 - IntroReferral: Referred to the House Committee on Agriculture.
- Latest action: 2025-09-04: Introduced in House

## Actions

- 2025-09-04 - IntroReferral: Introduced in House
- 2025-09-04 - IntroReferral: Introduced in House
- 2025-09-04 - IntroReferral: Referred to the House Committee on Agriculture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-04",
    "latestAction": {
      "actionDate": "2025-09-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5138",
    "number": "5138",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "F000475",
        "district": "1",
        "firstName": "Brad",
        "fullName": "Rep. Finstad, Brad [R-MN-1]",
        "lastName": "Finstad",
        "party": "R",
        "state": "MN"
      }
    ],
    "title": "ASPIRE Act",
    "type": "HR",
    "updateDate": "2025-12-19T09:08:03Z",
    "updateDateIncludingText": "2025-12-19T09:08:03Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-04",
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
      "actionDate": "2025-09-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-04",
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
          "date": "2025-09-04T13:01:10Z",
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
      "bioguideId": "P000597",
      "district": "1",
      "firstName": "Chellie",
      "fullName": "Rep. Pingree, Chellie [D-ME-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Pingree",
      "party": "D",
      "sponsorshipDate": "2025-09-04",
      "state": "ME"
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
      "sponsorshipDate": "2025-09-15",
      "state": "VA"
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
      "bioguideId": "T000491",
      "district": "45",
      "firstName": "Derek",
      "fullName": "Rep. Tran, Derek [D-CA-45]",
      "isOriginalCosponsor": "False",
      "lastName": "Tran",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5138ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5138\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 4, 2025 Mr. Finstad (for himself and Ms. Pingree ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the Food, Agriculture, Conservation, and Trade Act of 1990 to authorize grants for eligible institutions to carry out agriculture workforce training programs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Agriculture Skills Preparation for Industry Recruitment Efforts Act or the ASPIRE Act .\n#### 2. Agriculture workforce training program grants\n##### (a) In general\nSection 2501(d) of the Food, Agriculture, Conservation, and Trade Act of 1990 ( 7 U.S.C. 2279(d) ) is amended by adding at the end the following:\n(16) Agriculture workforce training program grants (A) Definitions In this paragraph: (i) Agriculture workforce training program The term agriculture workforce training program means a training program developed by an eligible institution in collaboration with a targeted industry partner through which students enrolled at that eligible institution receive training from that targeted industry partner, including through\u2014 (I) internships; (II) apprenticeships; (III) experience-based curricula; and (IV) educational programs and workshops to promote technical skills. (ii) Eligible institution The term eligible institution means\u2014 (I) an 1862 Institution (as defined in section 2 of the Agricultural Research, Extension, and Education Reform Act of 1998 ( 7 U.S.C. 7601 )); (II) an 1890 Institution (as defined in that section); (III) a 1994 Institution (as defined in section 532 of the Equity in Educational Land-Grant Status Act of 1994 ( 7 U.S.C. 301 note; Public Law 103\u2013382 )); (IV) a non-land-grant college of agriculture (as defined in section 1404 of the National Agricultural Research, Extension, and Teaching Policy Act of 1977 ( 7 U.S.C. 3103 )); (V) Hispanic-serving agricultural colleges and universities (as defined in that section); (VI) a center of excellence recognized under section 1673; (VII) a junior or community college (as defined in section 312 of the Higher Education Act of 1965 ( 20 U.S.C. 1058 )) that offers a program of study in agriculture; and (VIII) an area career and technical education school (as defined in section 3 of the Carl D. Perkins Career and Technical Education Act of 2006 ( 20 U.S.C. 2302 )) that offers a program of study in agriculture. (iii) Targeted industry partner The term targeted industry partner means 1 or more of the following entities: (I) A member of the agriculture industry, such as a company or industry association. (II) An apprenticeship program in agriculture registered under the Act of August 16, 1937 (commonly known as the National Apprenticeship Act ) (50 Stat. 664, chapter 663; 29 U.S.C. 50 et seq. ). (III) A nonprofit organization that aims to help individuals gain employment in the agriculture industry. (B) Authorization of grants The Secretary, acting through the Director of the National Institute of Food and Agriculture, shall award grants in accordance with this subsection to eligible institutions to develop and carry out agriculture workforce training programs\u2014 (i) to promote the growth of the agriculture industry; (ii) to foster competitiveness within the agriculture industry; and (iii) to improve the training and retention of workers in the agriculture industry. (C) Use of grant funds An eligible institution awarded a grant under this paragraph shall use not less than 5 percent of the funds received through the grant to carry out an agriculture workforce training program, including\u2014 (i) preliminary recruitment measures to encourage students to participate in the agriculture workforce training program; and (ii) professional development sessions to train faculty to prepare students for employment in the agriculture industry. .\n##### (b) Implementation\nNot later than January 31, 2026, the Secretary of Agriculture shall implement paragraph (16) of section 2501(d) of the Food, Agriculture, Conservation, and Trade Act of 1990 ( 7 U.S.C. 2279(d) ) (as added by subsection (a)).",
      "versionDate": "2025-09-04",
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
        "actionDate": "2025-09-04",
        "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry."
      },
      "number": "2727",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "A bill to amend the Food, Agriculture, Conservation, and Trade Act of 1990 to authorize grants for eligible institutions to carry out agriculture workforce training programs, and for other purposes.",
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
        "updateDate": "2025-09-23T15:29:56Z"
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
      "date": "2025-09-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5138ih.xml"
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
      "title": "ASPIRE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-09T04:08:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "ASPIRE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-09T04:08:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Agriculture Skills Preparation for Industry Recruitment Efforts Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-09T04:08:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Food, Agriculture, Conservation, and Trade Act of 1990 to authorize grants for eligible institutions to carry out agriculture workforce training programs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-09T04:03:24Z"
    }
  ]
}
```
