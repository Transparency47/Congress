# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8705?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8705
- Title: CHARLIE Act
- Congress: 119
- Bill type: HR
- Bill number: 8705
- Origin chamber: House
- Introduced date: 2026-05-07
- Update date: 2026-05-22T08:08:53Z
- Update date including text: 2026-05-22T08:08:53Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-05-07: Introduced in House
- 2026-05-07 - IntroReferral: Introduced in House
- 2026-05-07 - IntroReferral: Introduced in House
- 2026-05-07 - IntroReferral: Referred to the House Committee on Education and Workforce.
- 2026-05-21 - Committee: Committee Consideration and Mark-up Session Held
- 2026-05-21 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 19 - 15.
- Latest action: 2026-05-07: Introduced in House

## Actions

- 2026-05-07 - IntroReferral: Introduced in House
- 2026-05-07 - IntroReferral: Introduced in House
- 2026-05-07 - IntroReferral: Referred to the House Committee on Education and Workforce.
- 2026-05-21 - Committee: Committee Consideration and Mark-up Session Held
- 2026-05-21 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 19 - 15.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-07",
    "latestAction": {
      "actionDate": "2026-05-07",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8705",
    "number": "8705",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "O000086",
        "district": "4",
        "firstName": "Burgess",
        "fullName": "Rep. Owens, Burgess [R-UT-4]",
        "lastName": "Owens",
        "party": "R",
        "state": "UT"
      }
    ],
    "title": "CHARLIE Act",
    "type": "HR",
    "updateDate": "2026-05-22T08:08:53Z",
    "updateDateIncludingText": "2026-05-22T08:08:53Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-21",
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
      "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 19 - 15.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-05-21",
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
      "actionDate": "2026-05-07",
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
      "actionDate": "2026-05-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-05-07",
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
            "date": "2026-05-21T20:07:26Z",
            "name": "Markup By"
          },
          {
            "date": "2026-05-07T13:01:45Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8705ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8705\nIN THE HOUSE OF REPRESENTATIVES\nMay 7, 2026 Mr. Owens introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo amend the Elementary and Secondary Education Act of 1965 to prevent the American History and Civics program from funding radical indoctrination, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Civics and History Advancement to Restore Learning, Integrity, and Education Act or the CHARLIE Act .\n#### 2. Prohibiting American history and civics funds for radical indoctrination\nSection 2231 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 6661 ) is amended by adding at the end the following:\n(c) Prohibitions (1) In general Of the amount made available to carry out this subpart, no funds may be used for discriminatory equity ideology or gender ideology. (2) Priority In awarding grants under this subpart, the Secretary may not give priority to an eligible entity on the basis of race, sex, sexual orientation, gender identity, or immigration status, including with respect to\u2014 (A) the identity or purpose of the eligible entity; (B) the identity of the individuals who control, are employed by, or are served by the eligible entity; or (C) the proposed activities to be carried out under such a grant. (d) Definitions In this section: (1) Discriminatory equity ideology The term discriminatory equity ideology has the meaning given the term in section 2 of Executive Order 14190 (90 Fed. Reg. 8853; relating to ending radical indoctrination in K\u201312 schooling). (2) Gender ideology The term gender ideology has the meaning given the term in section 2 of Executive Order 14168 (90 Fed. Reg. 8615; relating to defending women from gender ideology extremism and restoring biological truth to the Federal Government). .",
      "versionDate": "2026-05-07",
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
        "updateDate": "2026-05-21T15:07:25Z"
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
      "date": "2026-05-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8705ih.xml"
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
      "title": "CHARLIE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-09T05:23:46Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "CHARLIE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-09T05:23:43Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Civics and History Advancement to Restore Learning, Integrity, and Education Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-09T05:23:43Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Elementary and Secondary Education Act of 1965 to prevent the American History and Civics program from funding radical indoctrination, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-09T05:18:36Z"
    }
  ]
}
```
