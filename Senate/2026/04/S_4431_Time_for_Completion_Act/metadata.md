# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4431?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4431
- Title: Time for Completion Act
- Congress: 119
- Bill type: S
- Bill number: 4431
- Origin chamber: Senate
- Introduced date: 2026-04-29
- Update date: 2026-05-21T16:28:20Z
- Update date including text: 2026-05-21T16:28:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-29: Introduced in Senate
- 2026-04-29 - IntroReferral: Introduced in Senate
- 2026-04-29 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S2130-2131)
- Latest action: 2026-04-29: Introduced in Senate

## Actions

- 2026-04-29 - IntroReferral: Introduced in Senate
- 2026-04-29 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S2130-2131)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-29",
    "latestAction": {
      "actionDate": "2026-04-29",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4431",
    "number": "4431",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "B001261",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Barrasso, John [R-WY]",
        "lastName": "Barrasso",
        "party": "R",
        "state": "WY"
      }
    ],
    "title": "Time for Completion Act",
    "type": "S",
    "updateDate": "2026-05-21T16:28:20Z",
    "updateDateIncludingText": "2026-05-21T16:28:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-29",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S2130-2131)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-04-29",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
          "date": "2026-04-29T17:09:56Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2026-04-29",
      "state": "NC"
    },
    {
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-04-29",
      "state": "WY"
    },
    {
      "bioguideId": "C001114",
      "firstName": "John",
      "fullName": "Sen. Curtis, John R. [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Curtis",
      "party": "R",
      "sponsorshipDate": "2026-04-29",
      "state": "UT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4431is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4431\nIN THE SENATE OF THE UNITED STATES\nApril 29, 2026 Mr. Barrasso (for himself, Mr. Budd , Ms. Lummis , and Mr. Curtis ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo amend the Higher Education Act of 1965 to provide for comprehensive student achievement information.\n#### 1. Short title\nThis Act may be cited as the Time for Completion Act .\n#### 2. Consumer information about completion or graduation times\n##### (a) Transparency in college tuition for consumers\nSubparagraph (J) of section 132(i)(1) of the Higher Education Act of 1965 ( 20 U.S.C. 1015a(i)(1)(J) ) is amended to read as follows:\n(J) (i) For programs of study 4 years of length or longer\u2014 (I) the percentages of first-time, full-time, degree- or certificate-seeking undergraduate students enrolled at the institution who obtain a degree or certificate within each of the times for completion or graduation described in subclauses (I) through (III) of clause (iii); (II) the percentages of first-time, part-time, degree- or certificate-seeking undergraduate students enrolled at the institution who obtain a degree or certificate within each of the times for completion or graduation described in subclauses (I) through (III) of clause (iii); (III) the percentages of non-first time, full-time, degree- or certificate-seeking undergraduate students enrolled at the institution who obtain a degree or certificate within each of the times for completion or graduation described in subclauses (I) through (III) of clause (iii); and (IV) the percentages of non-first-time, part-time, degree- or certificate-seeking undergraduate students enrolled at the institution who obtain a degree or certificate within each of the times for completion or graduation described in subclauses (I) through (III) of clause (iii). (ii) For programs of study less than 4 years\u2014 (I) the percentages of first-time, full-time, degree- or certificate-seeking undergraduate students enrolled at the institution who obtain a degree or certificate within each of the times for completion or graduation described in subclauses (I) through (IV) of clause (iii); (II) the percentages of first-time, part-time, degree- or certificate-seeking undergraduate students enrolled at the institution who obtain a degree or certificate within each of the times for completion or graduation described in subclauses (I) through (IV) of clause (iii); (III) the percentages of non-first-time, full-time, degree- or certificate-seeking undergraduate students enrolled at the institution who obtain a degree or certificate within each of the times for completion or graduation described in subclauses (I) through (IV) of clause (iii); and (IV) the percentages of non-first-time, part-time, degree- or certificate-seeking undergraduate students enrolled at the institution who obtain a degree or certificate within each of the times for completion or graduation described in subclauses (I) through (IV) of clause (iii). (iii) For purposes of this subparagraph, the times for completion or graduation are as follows: (I) The normal time for completion of, or graduation from, the student\u2019s program. (II) 150 percent of the normal time for completion of, or graduation from, the student\u2019s program. (III) 200 percent of the normal time for completion of, or graduation from, the student\u2019s program. (IV) 300 percent of the normal time for completion of, or graduation from, the student\u2019s program. (iv) In making publicly available the percentages described in this subparagraph, the Secretary shall display each percentage in a consistent manner and with equal visibility. .\n##### (b) Institutional and financial assistance information for students\nSection 485(a) of the Higher Education Act of 1965 ( 20 U.S.C. 1092(a) ) is amended\u2014\n**(1)**\nin paragraph (1), by striking subparagraph (L) and inserting the following:\n(L) each completion or graduation rate for each type of student and program described in clauses (i) and (ii) of section 132(i)(1)(J); ; and\n**(2)**\nin the matter preceding subparagraph (A) of paragraph (3), by striking within 150 percent of the normal time for completion of or graduation from the program and inserting within the time for completion or graduation described in section 132(i)(1)(J) applicable to such student and such program .",
      "versionDate": "2026-04-29",
      "versionType": "Introduced in Senate"
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
        "updateDate": "2026-05-21T16:28:20Z"
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
      "date": "2026-04-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4431is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Time for Completion Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-12T05:53:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Time for Completion Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-12T05:53:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Higher Education Act of 1965 to provide for comprehensive student achievement information.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-12T05:48:30Z"
    }
  ]
}
```
