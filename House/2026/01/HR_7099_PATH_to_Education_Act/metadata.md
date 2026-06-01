# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7099?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7099
- Title: PATH to Education Act
- Congress: 119
- Bill type: HR
- Bill number: 7099
- Origin chamber: House
- Introduced date: 2026-01-15
- Update date: 2026-04-15T08:05:51Z
- Update date including text: 2026-04-15T08:05:51Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-01-15: Introduced in House
- 2026-01-15 - IntroReferral: Introduced in House
- 2026-01-15 - IntroReferral: Introduced in House
- 2026-01-15 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- Latest action: 2026-01-15: Introduced in House

## Actions

- 2026-01-15 - IntroReferral: Introduced in House
- 2026-01-15 - IntroReferral: Introduced in House
- 2026-01-15 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-15",
    "latestAction": {
      "actionDate": "2026-01-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7099",
    "number": "7099",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "G000604",
        "district": "2",
        "firstName": "Maggie",
        "fullName": "Rep. Goodlander, Maggie [D-NH-2]",
        "lastName": "Goodlander",
        "party": "D",
        "state": "NH"
      }
    ],
    "title": "PATH to Education Act",
    "type": "HR",
    "updateDate": "2026-04-15T08:05:51Z",
    "updateDateIncludingText": "2026-04-15T08:05:51Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-15",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Transportation and Infrastructure.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-01-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-15",
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
          "date": "2026-01-15T14:04:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "systemCode": "hspw00",
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
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2026-01-15",
      "state": "NJ"
    },
    {
      "bioguideId": "W000808",
      "district": "24",
      "firstName": "Frederica",
      "fullName": "Rep. Wilson, Frederica S. [D-FL-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Wilson",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-01-15",
      "state": "FL"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2026-01-15",
      "state": "PA"
    },
    {
      "bioguideId": "K000398",
      "district": "7",
      "firstName": "Thomas",
      "fullName": "Rep. Kean, Thomas H. [R-NJ-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Kean",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2026-01-15",
      "state": "NJ"
    },
    {
      "bioguideId": "M001237",
      "district": "8",
      "firstName": "Kristen",
      "fullName": "Rep. McDonald Rivet, Kristen [D-MI-8]",
      "isOriginalCosponsor": "True",
      "lastName": "McDonald Rivet",
      "party": "D",
      "sponsorshipDate": "2026-01-15",
      "state": "MI"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2026-03-02",
      "state": "MI"
    },
    {
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2026-03-02",
      "state": "MN"
    },
    {
      "bioguideId": "S001225",
      "district": "17",
      "firstName": "Eric",
      "fullName": "Rep. Sorensen, Eric [D-IL-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Sorensen",
      "party": "D",
      "sponsorshipDate": "2026-03-02",
      "state": "IL"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2026-04-14",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7099ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7099\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 15, 2026 Ms. Goodlander (for herself, Mr. Van Drew , Ms. Wilson of Florida , Mr. Fitzpatrick , Mr. Kean , and Ms. McDonald Rivet ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo increase access to higher education and center-based Head Start programs by providing public transit grants.\n#### 1. Short title\nThis Act may be cited as the Promoting Advancement Through Transit Help to Education Act or the PATH to Education Act .\n#### 2. Increasing access to education through public transit grants\nChapter 53 of title 49, United States Code, is amended\u2014\n**(1)**\nin section 5307, by adding at the end the following:\n(i) Promoting advancement through transit help to education grants (1) Definitions In this subsection: (A) Center-based Head Start program The term center-based Head Start program means a center-based Head Start program, including a center-based Early Head Start program, under the Head Start Act ( 42 U.S.C. 9831 et seq. ). (B) Eligible institution The term eligible institution means\u2014 (i) a community college; (ii) a minority-serving institution; (iii) a Head Start agency, including an Early Head Start agency, that operates a center-based Head Start program; (iv) an area career and technical education school, as defined in section 3 of the Carl D. Perkins Career and Technical Education Act of 2006 ( 20 U.S.C. 2302 ); or (v) a rural-serving institution of higher education, as defined in section 861 of the Higher Education Act of 1965 ( 20 U.S.C. 1161q ). (C) Eligible recipient The term eligible recipient means a public transportation provider that is eligible for assistance under this section in partnership with 1 or more eligible institutions. (D) Minority-serving institution The term minority-serving institution means an eligible institution under section 371(a) of the Higher Education Act of 1965 ( 20 U.S.C. 1067q(a) ). (2) Authority The Secretary may make grants under this subsection to eligible recipients to enable those eligible recipients to carry out projects described in paragraph (3) to better connect students with transportation to eligible institutions. (3) Eligible projects An eligible recipient receiving a grant under this subsection shall use grant funds to carry out 1 or more of the following activities to better connect students with transportation to 1 or more eligible institutions that are served by the eligible recipient partnership: (A) Adding bus or rail stops or routes and complementary paratransit service that serve eligible institution campuses and connect to surrounding areas or other cities. (B) Increasing the frequency of service or adjusting the time of bus, rail, or paratransit routes to\u2014 (i) allow students of an eligible institution to get to and from their classes; and (ii) allow participants in a center-based Head Start program, and their families, to get to and from the Head Start program. (C) Operating costs for service described in subparagraphs (A) and (B), if such costs are eligible under this section. (4) Application (A) In general An eligible recipient that desires a grant under this subsection shall submit an application to the Secretary at such time, in such manner, and containing such information as the Secretary may require, including information on the extent to which the proposed projects using grant funds will improve the availability of transit access for students of eligible institutions and participants, and families of participants, in center-based Head Start programs. (B) Priority In awarding grants under this subsection, the Secretary shall give priority to an eligible recipient whose partnership includes an eligible institution with respect to which more than 25 percent of students enrolled in that eligible institution receive a Federal Pell Grant under section 401 of the Higher Education Act of 1965 ( 20 U.S.C. 1070a ). ;\n**(2)**\nin section 5311\u2014\n**(A)**\nin subsection (c)\u2014\n**(i)**\nin paragraph (1)(A), by striking and ;\n**(ii)**\nin paragraph (1)(B), by striking the period at the end and inserting ; and ; and\n**(iii)**\nby adding at the end the following:\n(C) there shall be set aside to carry out subsection (k)\u2014 (i) for fiscal year 2027, $1,000,000; (ii) for fiscal year 2028, $2,000,000; (iii) for fiscal year 2029, $3,000,000; (iv) for fiscal year 2030, $4,000,000; and (v) for fiscal year 2031, $5,000,000. ; and\n**(B)**\nby adding at the end the following:\n(k) Promoting advancement through transit help to education grants (1) Definitions In this subsection: (A) Center-based head start program The term center-based Head Start program means a center-based Head Start program, including a center-based Early Head Start program, under the Head Start Act ( 42 U.S.C. 9831 et seq. ). (B) Eligible institution The term eligible institution means\u2014 (i) a community college; (ii) a minority-serving institution; (iii) a Head Start agency, including an Early Head Start agency, that operates a center-based Head Start program; (iv) an area career and technical education school, as defined in section 3 of the Carl D. Perkins Career and Technical Education Act of 2006 ( 20 U.S.C. 2302 ); or (v) a rural-serving institution of higher education, as defined in section 861 of the Higher Education Act of 1965 ( 20 U.S.C. 1161q ). (C) Eligible recipient The term eligible recipient means a public transportation provider that is eligible for assistance under this section in partnership with 1 or more eligible entities. (2) Authority The Secretary may make grants under this subsection to eligible recipients to enable those eligible recipients to carry out projects described in paragraph (3) to better connect students with transportation to eligible institutions. (3) Eligible projects An eligible recipient receiving a grant under this subsection shall use grant funds to carry out 1 or more of the following activities to better connect students with transportation to 1 or more eligible institutions that are served by the eligible recipient partnership: (A) Adding bus or rail stops or routes and complementary paratransit service that serve eligible institution campuses and connect to surrounding areas or other cities. (B) Increasing the frequency of service or adjusting the time of bus, rail, or paratransit routes to\u2014 (i) allow students of an eligible institution to get to and from their classes; and (ii) allow participants in a center-based Head Start program, and their families, to get to and from the Head Start program. (C) Operating costs for service described in subparagraphs (A) and (B), if such costs are eligible under this section. (4) Application (A) In general An eligible recipient that desires a grant under this subsection shall submit an application to the Secretary at such time, in such manner, and containing such information as the Secretary may require, including information on the extent to which the proposed projects using grant funds will improve the availability of transit access for students of eligible institutions and participants, and families of participants, in center-based Head Start programs. (B) Priority In awarding grants under this subsection, the Secretary shall give priority to an eligible recipient whose partnership includes an eligible institution with respect to which more than 25 percent of students enrolled in that eligible institution receive a Federal Pell Grant under section 401 of the Higher Education Act of 1965 ( 20 U.S.C. 1070a ). ; and\n**(3)**\nin section 5336(h)\u2014\n**(A)**\nby redesignating paragraphs (3) through (5) as paragraphs (4) through (6), respectively;\n**(B)**\nby inserting after paragraph (2) the following:\n(3) there shall be set aside to carry out section 5307(i)\u2014 (A) for fiscal year 2027, $1,000,000; (B) for fiscal year 2028, $2,000,000; (C) for fiscal year 2029, $3,000,000; (D) for fiscal year 2030, $4,000,000; and (E) for fiscal year 2031, $5,000,000. ;\n**(C)**\nin paragraph (4), as so redesignated, by striking and (2), and inserting , (2), and (3), ; and\n**(D)**\nin paragraph (5), as so redesignated, by striking and (4) and inserting (4), and (5) .",
      "versionDate": "2026-01-15",
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
        "actionDate": "2026-01-15",
        "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs."
      },
      "number": "3661",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "PATH to Education Act",
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
        "name": "Transportation and Public Works",
        "updateDate": "2026-02-06T18:44:14Z"
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
      "date": "2026-01-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7099ih.xml"
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
      "title": "PATH to Education Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-05T04:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "PATH to Education Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-05T04:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Promoting Advancement Through Transit Help to Education Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-05T04:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To increase access to higher education and center-based Head Start programs by providing public transit grants.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-05T04:18:20Z"
    }
  ]
}
```
