# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7893?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7893
- Title: FAFSA Verification Efficiency Act
- Congress: 119
- Bill type: HR
- Bill number: 7893
- Origin chamber: House
- Introduced date: 2026-03-12
- Update date: 2026-05-12T15:27:22Z
- Update date including text: 2026-05-12T15:27:22Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-03-12: Introduced in House
- 2026-03-12 - IntroReferral: Introduced in House
- 2026-03-12 - IntroReferral: Introduced in House
- 2026-03-12 - IntroReferral: Referred to the House Committee on Education and Workforce.
- 2026-03-17 - Committee: Committee Consideration and Mark-up Session Held
- 2026-03-17 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 19 - 13.
- Latest action: 2026-03-12: Introduced in House

## Actions

- 2026-03-12 - IntroReferral: Introduced in House
- 2026-03-12 - IntroReferral: Introduced in House
- 2026-03-12 - IntroReferral: Referred to the House Committee on Education and Workforce.
- 2026-03-17 - Committee: Committee Consideration and Mark-up Session Held
- 2026-03-17 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 19 - 13.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-12",
    "latestAction": {
      "actionDate": "2026-03-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7893",
    "number": "7893",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "W000798",
        "district": "5",
        "firstName": "Tim",
        "fullName": "Rep. Walberg, Tim [R-MI-5]",
        "lastName": "Walberg",
        "party": "R",
        "state": "MI"
      }
    ],
    "title": "FAFSA Verification Efficiency Act",
    "type": "HR",
    "updateDate": "2026-05-12T15:27:22Z",
    "updateDateIncludingText": "2026-05-12T15:27:22Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-17",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 19 - 13.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-03-17",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-12",
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
      "actionDate": "2026-03-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-12",
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
        "item": [
          {
            "date": "2026-03-17T19:33:30Z",
            "name": "Markup By"
          },
          {
            "date": "2026-03-12T13:34:10Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "F000450",
      "district": "5",
      "firstName": "Virginia",
      "fullName": "Rep. Foxx, Virginia [R-NC-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Foxx",
      "party": "R",
      "sponsorshipDate": "2026-03-18",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7893ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7893\nIN THE HOUSE OF REPRESENTATIVES\nMarch 12, 2026 Mr. Walberg introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo amend the Higher Education Act of 1965 to improve the process for the verification of social security numbers required to be provided to the Secretary of Education for Federal student aid, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the FAFSA Verification Efficiency Act .\n#### 2. Verification of social security number\nSection 484(o) of the Higher Education Act of 1965 ( 20 U.S.C. 1091(o) ) is amended, in the matter preceding paragraph (1), by striking The Secretary and all that follows through following conditions and inserting Notwithstanding any other provision of law, the Secretary of Education, in cooperation with the Commissioner of the Social Security Administration, shall verify the social security number and citizenship status of any individual that is required to be provided to the Secretary for Federal student aid under sections 483, 484(a), and 494, and shall enforce the following conditions .",
      "versionDate": "2026-03-12",
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
        "actionDate": "2026-04-21",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "4365",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "FAFSA Verification Efficiency Act",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Citizenship and naturalization",
            "updateDate": "2026-04-02T18:43:22Z"
          },
          {
            "name": "Government lending and loan guarantees",
            "updateDate": "2026-04-02T18:43:13Z"
          },
          {
            "name": "Higher education",
            "updateDate": "2026-04-02T18:42:45Z"
          },
          {
            "name": "Student aid and college costs",
            "updateDate": "2026-04-02T18:42:51Z"
          }
        ]
      },
      "policyArea": {
        "name": "Education",
        "updateDate": "2026-03-16T16:28:29Z"
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
      "date": "2026-03-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7893ih.xml"
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
      "title": "FAFSA Verification Efficiency Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-13T08:23:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "FAFSA Verification Efficiency Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-13T08:23:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Higher Education Act of 1965 to improve the process for the verification of social security numbers required to be provided to the Secretary of Education for Federal student aid, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-13T08:19:26Z"
    }
  ]
}
```
