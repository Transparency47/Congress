# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2841?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2841
- Title: CIVICS Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2841
- Origin chamber: Senate
- Introduced date: 2025-09-17
- Update date: 2026-03-30T18:19:13Z
- Update date including text: 2026-03-30T18:19:13Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-17: Introduced in Senate
- 2025-09-17 - IntroReferral: Introduced in Senate
- 2025-09-17 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- 2026-03-19 - Committee: Committee on Health, Education, Labor, and Pensions. Hearings held.
- Latest action: 2025-09-17: Introduced in Senate

## Actions

- 2025-09-17 - IntroReferral: Introduced in Senate
- 2025-09-17 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- 2026-03-19 - Committee: Committee on Health, Education, Labor, and Pensions. Hearings held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-17",
    "latestAction": {
      "actionDate": "2025-09-17",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2841",
    "number": "2841",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "K000383",
        "district": "",
        "firstName": "Angus",
        "fullName": "Sen. King, Angus S., Jr. [I-ME]",
        "lastName": "King",
        "party": "I",
        "state": "ME"
      }
    ],
    "title": "CIVICS Act of 2025",
    "type": "S",
    "updateDate": "2026-03-30T18:19:13Z",
    "updateDateIncludingText": "2026-03-30T18:19:13Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-19",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Health, Education, Labor, and Pensions. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-09-17",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-09-17",
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
        "item": [
          {
            "date": "2026-03-19T14:00:54Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-09-17T19:45:10Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2025-09-17",
      "state": "OK"
    },
    {
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-09-17",
      "state": "MS"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-09-17",
      "state": "VA"
    },
    {
      "bioguideId": "S001227",
      "firstName": "Eric",
      "fullName": "Sen. Schmitt, Eric [R-MO]",
      "isOriginalCosponsor": "False",
      "lastName": "Schmitt",
      "middleName": "S.",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "MO"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "MD"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2841is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2841\nIN THE SENATE OF THE UNITED STATES\nSeptember 17 (legislative day, September 16), 2025 Mr. King (for himself, Mr. Lankford , Mr. Wicker , and Mr. Kaine ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo amend the American History and Civics Education program under the Elementary and Secondary Education Act of 1965 to require hands-on civic engagement activities for teachers and students and programs that educate students about the history and principles of the Constitution of the United States, including the Bill of Rights.\n#### 1. Short title\nThis Act may be cited as the Constitution and Civics Education Is Valuable In Community Schools Act of 2025 or the CIVICS Act of 2025 .\n#### 2. National activities\nSection 2233(b) of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 6663(b) ) is amended\u2014\n**(1)**\nin the matter preceding paragraph (1), by inserting shall after , which ; and\n**(2)**\nby striking paragraphs (1) and (2) and inserting the following:\n(1) show potential to improve the quality of student achievement in, and teaching of, American history, civics and government, or geography, in elementary schools and secondary schools; (2) demonstrate innovation, scalability, accountability, and a focus on underserved populations; (3) include hands-on civic engagement activities for teachers and students; and (4) include programs that educate students about the history and principles of the Constitution of the United States, including the Bill of Rights. .",
      "versionDate": "2025-09-17",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Civics education",
            "updateDate": "2026-03-30T18:19:12Z"
          },
          {
            "name": "Elementary and secondary education",
            "updateDate": "2026-03-30T18:19:04Z"
          },
          {
            "name": "Teaching, teachers, curricula",
            "updateDate": "2026-03-30T18:19:08Z"
          }
        ]
      },
      "policyArea": {
        "name": "Education",
        "updateDate": "2025-11-18T18:47:53Z"
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
      "date": "2025-09-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2841is.xml"
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
      "title": "CIVICS Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-20T11:03:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "CIVICS Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-02T04:23:13Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Constitution and Civics Education Is Valuable In Community Schools Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-02T04:23:13Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the American History and Civics Education program under the Elementary and Secondary Education Act of 1965 to require hands-on civic engagement activities for teachers and students and programs that educate students about the history and principles of the Constitution of the United States, including the Bill of Rights.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-02T04:18:11Z"
    }
  ]
}
```
