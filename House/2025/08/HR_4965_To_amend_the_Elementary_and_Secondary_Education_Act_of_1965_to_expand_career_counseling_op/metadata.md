# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4965?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4965
- Title: Counseling for Career Choice Act
- Congress: 119
- Bill type: HR
- Bill number: 4965
- Origin chamber: House
- Introduced date: 2025-08-12
- Update date: 2026-05-13T08:06:08Z
- Update date including text: 2026-05-13T08:06:08Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-08-12: Introduced in House
- 2025-08-12 - IntroReferral: Introduced in House
- 2025-08-12 - IntroReferral: Introduced in House
- 2025-08-12 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-08-12: Introduced in House

## Actions

- 2025-08-12 - IntroReferral: Introduced in House
- 2025-08-12 - IntroReferral: Introduced in House
- 2025-08-12 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-08-12",
    "latestAction": {
      "actionDate": "2025-08-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4965",
    "number": "4965",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "T000467",
        "district": "15",
        "firstName": "Glenn",
        "fullName": "Rep. Thompson, Glenn [R-PA-15]",
        "lastName": "Thompson",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "Counseling for Career Choice Act",
    "type": "HR",
    "updateDate": "2026-05-13T08:06:08Z",
    "updateDateIncludingText": "2026-05-13T08:06:08Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-08-12",
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
      "actionDate": "2025-08-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-08-12",
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
          "date": "2025-08-12T13:02:30Z",
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
      "bioguideId": "B001278",
      "district": "1",
      "firstName": "Suzanne",
      "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bonamici",
      "party": "D",
      "sponsorshipDate": "2025-08-12",
      "state": "OR"
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
      "sponsorshipDate": "2025-09-02",
      "state": "VA"
    },
    {
      "bioguideId": "V000136",
      "district": "2",
      "firstName": "Gabe",
      "fullName": "Rep. Vasquez, Gabe [D-NM-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Vasquez",
      "party": "D",
      "sponsorshipDate": "2025-10-21",
      "state": "NM"
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
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2025-12-23",
      "state": "CO"
    },
    {
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4965ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4965\nIN THE HOUSE OF REPRESENTATIVES\nAugust 12, 2025 Mr. Thompson of Pennsylvania (for himself and Ms. Bonamici ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo amend the Elementary and Secondary Education Act of 1965 to expand career counseling opportunities within student support and academic enrichment grants.\n#### 1. Short title\nThis Act may be cited as the Counseling for Career Choice Act .\n#### 2. Amendment\nSection 4107(a)(3)(A) of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7117(a)(3)(A) ) is amended to read as follows:\n(A) career guidance and school counseling programs, such as\u2014 (i) guidance for school career counseling programs, and school counselors and students who may be interested in such programs; (ii) identifying and assessing school counseling activities and postsecondary options available within the State, and outside the State as applicable; (iii) identifying regional workforce trends in collaboration with entities at the State and regional level with expertise in identifying such trends (such as State boards and local boards (as such terms are defined in section 3 of the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3102 )), regional economic development organizations, or State employment agencies); (iv) developing and implementing a process and infrastructure for school counselors and school counseling programs to access information regarding the regional workforce trends identified in clause (iii); (v) information for school counselors on how to effectively provide students with current and relevant workforce information, financial aid assistance, personal counseling, and academic advising relevant to students\u2019 individual career and postsecondary education goals; (vi) financial literacy and Federal financial aid awareness activities other than the activities described in clause (v); (vii) developing and implementing professional development or career development training certification programs for counselors and other educators involved in preparing students for postsecondary opportunities, which may include partnering with an industry association that provides a nationally recognized certification in career development; (viii) establishing, improving, or coordinating postsecondary opportunities for students, which shall include\u2014 (I) individual career planning; (II) personalized learning plans; (III) registered apprenticeships; (IV) internships; (V) dual enrollment programs; (VI) programs leading to recognized postsecondary credentials (as defined in section 3 of the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3102 )), including programs at a secondary school; (VII) 2-year degree programs; or (VIII) 4-year degree programs; (ix) encouraging partnerships with one-stop centers as defined in section 3 of the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3102 ), which may include colocating a one-stop center in a high school, transporting students to local one-stop centers, or having one-stop center career counselors and business liaisons assist school counselors in hosting job fairs, career days, or other such similar tasks; (x) leveraging resources and emerging technologies, including artificial intelligence, that are being developed to support career development and career counseling activities; and (xi) evaluating secondary and postsecondary outcomes for individuals served by school or other career counseling programs; .",
      "versionDate": "2025-08-12",
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
        "updateDate": "2025-09-19T14:18:54Z"
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
      "date": "2025-08-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4965ih.xml"
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
      "title": "Counseling for Career Choice Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-13T08:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Counseling for Career Choice Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-13T08:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Elementary and Secondary Education Act of 1965 to expand career counseling opportunities within student support and academic enrichment grants.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-13T08:18:18Z"
    }
  ]
}
```
