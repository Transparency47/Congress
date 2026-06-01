# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6282?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6282
- Title: Providing Distance Education for Foreign Institutions Act
- Congress: 119
- Bill type: HR
- Bill number: 6282
- Origin chamber: House
- Introduced date: 2025-11-21
- Update date: 2026-04-15T08:05:57Z
- Update date including text: 2026-04-15T08:05:57Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-21: Introduced in House
- 2025-11-21 - IntroReferral: Introduced in House
- 2025-11-21 - IntroReferral: Introduced in House
- 2025-11-21 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-11-21: Introduced in House

## Actions

- 2025-11-21 - IntroReferral: Introduced in House
- 2025-11-21 - IntroReferral: Introduced in House
- 2025-11-21 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-21",
    "latestAction": {
      "actionDate": "2025-11-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6282",
    "number": "6282",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "S001199",
        "district": "11",
        "firstName": "Lloyd",
        "fullName": "Rep. Smucker, Lloyd [R-PA-11]",
        "lastName": "Smucker",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "Providing Distance Education for Foreign Institutions Act",
    "type": "HR",
    "updateDate": "2026-04-15T08:05:57Z",
    "updateDateIncludingText": "2026-04-15T08:05:57Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-21",
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
      "actionDate": "2025-11-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-21",
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
          "date": "2025-11-21T14:04:20Z",
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
      "bioguideId": "S001190",
      "district": "10",
      "firstName": "Bradley",
      "fullName": "Rep. Schneider, Bradley Scott [D-IL-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Schneider",
      "middleName": "Scott",
      "party": "D",
      "sponsorshipDate": "2025-11-21",
      "state": "IL"
    },
    {
      "bioguideId": "C001127",
      "district": "20",
      "firstName": "Sheila",
      "fullName": "Rep. Cherfilus-McCormick, Sheila [D-FL-20]",
      "isOriginalCosponsor": "False",
      "lastName": "Cherfilus-McCormick",
      "party": "D",
      "sponsorshipDate": "2026-04-06",
      "state": "FL"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2026-04-14",
      "state": "NV"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6282ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6282\nIN THE HOUSE OF REPRESENTATIVES\nNovember 21, 2025 Mr. Smucker (for himself and Mr. Schneider ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo amend title IV of the Higher Education Act of 1965 to provide program eligibility for distance education programs offered by foreign institutions of higher education.\n#### 1. Short title\nThis Act may be cited as the Providing Distance Education for Foreign Institutions Act .\n#### 2. Eligibility of distance education programs offered by foreign institutions of higher education\n##### (a) In general\nSection 481(b) of the Higher Education Act of 1965 ( 20 U.S.C. 1088(b) ) is amended\u2014\n**(1)**\nby redesignating paragraph (4) as paragraph (5); and\n**(2)**\nby inserting after paragraph (3), the following:\n(4) (A) An otherwise eligible program that is offered by a foreign institution and is offered in part through distance education is eligible for the purposes of this title if\u2014 (i) not more than 12.5 percent of such program consists of courses offered principally through distance education; (ii) the foreign institution has been evaluated and determined by an outside oversight entity, such as an accrediting agency or association or government entity, to have the capability to effectively deliver distance education programs; and (iii) the students receiving aid under this title are physically present in the country where the foreign institution is located during the distance education instruction. (B) In calculating the percentage of a program offered through distance education for purposes of clause (i) of subparagraph (A), any course that is part of such a program that requires a student\u2019s regular in-person attendance for more than 50 percent of the instruction, but also includes one or more distance education components as part of the course, shall not be considered to be offered principally through distance education. .\n##### (b) Effective date and application\nThe amendments made by subsection (a) shall take effect on the date of enactment of this Act, and shall apply with respect to the first semester (or the equivalent) that begins after such date, but not earlier than 3 months after such date.\n##### (c) Conforming amendment\nSection 83002(b) of Public Law 119\u201321 is amended by amending paragraph (1) to read as follows:\n(1) by redesignating paragraphs (3), (4), and (5) as paragraphs (4), (5), and (6), respectively; and .",
      "versionDate": "2025-11-21",
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
        "updateDate": "2025-12-19T16:21:02Z"
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
      "date": "2025-11-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6282ih.xml"
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
      "title": "Providing Distance Education for Foreign Institutions Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-18T05:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Providing Distance Education for Foreign Institutions Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-18T05:23:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title IV of the Higher Education Act of 1965 to provide program eligibility for distance education programs offered by foreign institutions of higher education.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-18T05:18:14Z"
    }
  ]
}
```
