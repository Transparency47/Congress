# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1101?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1101
- Title: SHARE Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1101
- Origin chamber: Senate
- Introduced date: 2025-03-25
- Update date: 2026-03-19T11:03:26Z
- Update date including text: 2026-03-19T11:03:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-25: Introduced in Senate
- 2025-03-25 - IntroReferral: Introduced in Senate
- 2025-03-25 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-03-25: Introduced in Senate

## Actions

- 2025-03-25 - IntroReferral: Introduced in Senate
- 2025-03-25 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-25",
    "latestAction": {
      "actionDate": "2025-03-25",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1101",
    "number": "1101",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "W000800",
        "district": "",
        "firstName": "Peter",
        "fullName": "Sen. Welch, Peter [D-VT]",
        "lastName": "Welch",
        "party": "D",
        "state": "VT"
      }
    ],
    "title": "SHARE Act of 2025",
    "type": "S",
    "updateDate": "2026-03-19T11:03:26Z",
    "updateDateIncludingText": "2026-03-19T11:03:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-25",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-25",
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
            "date": "2025-03-25T15:27:02Z",
            "name": "Referred To"
          },
          {
            "date": "2025-03-25T15:27:02Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-03-25",
      "state": "TN"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-03-25",
      "state": "ME"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "MD"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "False",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "RI"
    },
    {
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "False",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-06-09",
      "state": "ME"
    },
    {
      "bioguideId": "M001190",
      "firstName": "Markwayne",
      "fullName": "Sen. Mullin, Markwayne [R-OK]",
      "isOriginalCosponsor": "False",
      "lastName": "Mullin",
      "party": "R",
      "sponsorshipDate": "2025-09-04",
      "state": "OK"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "False",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "MN"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "False",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "NH"
    },
    {
      "bioguideId": "O000174",
      "firstName": "Jon",
      "fullName": "Sen. Ossoff, Jon [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Ossoff",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "GA"
    },
    {
      "bioguideId": "T000278",
      "firstName": "Tommy",
      "fullName": "Sen. Tuberville, Tommy [R-AL]",
      "isOriginalCosponsor": "False",
      "lastName": "Tuberville",
      "party": "R",
      "sponsorshipDate": "2026-03-18",
      "state": "AL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1101is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1101\nIN THE SENATE OF THE UNITED STATES\nMarch 25, 2025 Mr. Welch (for himself, Mrs. Blackburn , and Mr. King ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo authorize the use of Federal Bureau of Investigation criminal history record information for administration of certain licenses.\n#### 1. Short title\nThis Act may be cited as the States Handling Access to Reciprocity for Employment Act of 2025 or the SHARE Act of 2025 .\n#### 2. Sharing and use of criminal history record information\nSubtitle E of title VI of the Intelligence Reform and Terrorism Prevention Act of 2004 ( 34 U.S.C. 41106 et seq. ) is amended by adding at the end the following:\n6404. Sharing and use of criminal history record information (a) Definitions In this section: (1) Commission The term Commission means a joint governmental entity, including an interstate compact commission, established by legislative enactment of an interstate compact. (2) Criminal history record information The term criminal history record information \u2014 (A) means information collected by criminal justice agencies on individuals consisting of identifiable descriptions and notations of arrests, detentions, indictments, information, or other formal criminal charges, and any disposition arising therefrom, including acquittal, sentencing, correctional supervision, and release; and (B) does not include identification information, such as fingerprint records, if such information does not indicate the individual\u2019s involvement with the criminal justice system. (3) License The term license means a license, multistate license, certification, or other authorization by which a State licensing authority authorizes an individual to practice an occupation or profession in that State. (4) Privilege The term privilege means a grant of authority issued pursuant to an interstate compact to a license holder that permits the license holder to practice in a compact member State. (5) State The term State means any State, territory, or possession of the United States, and the District of Columbia. (6) State identification bureau The term State identification bureau has the meaning given such term in section 6402(c). (7) State licensing authority The term State licensing authority means a State licensing board, agency, department, or other entity that is empowered under the law of that State to grant a license to practice an occupation or profession. (b) Requirement for Federal Bureau of Investigation To provide certain criminal history record information Subject to the restrictions in subsection (c), the Director of the Federal Bureau of Investigation shall furnish or otherwise make available to a State licensing authority, through an agreement with a State law enforcement agency or State identification bureau, criminal history record information to the extent required by an interstate compact, or the regulations duly promulgated thereunder, for the purpose of conducting a criminal history background check of any individual seeking a license or privilege to practice an occupation or profession in a compact member State. (c) State licensing authority use of criminal history record information (1) Prohibition A State licensing authority that is a member of an interstate compact that requires completion of a criminal history background check for an individual for the purpose of acting upon a license or privilege of that individual to practice an occupation or profession in a State shall use such information solely for that purpose and may not share criminal history record information or any part thereof with the compact\u2019s Commission, any other State entity or State Licensing Authority, or the public. (2) Sharing fact of completion of criminal history background check expressly permitted A State licensing authority informing a compact Commission of the completion of the criminal history background check, including a binary determination of whether or not the criminal history background check of an applicant was satisfactory, is expressly permitted under this section and shall not constitute the sharing of criminal history record information under paragraph (1). .",
      "versionDate": "2025-03-25",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2025-03-25",
        "text": "Referred to the Committee on Education and Workforce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "2332",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "SHARE Act of 2025",
      "type": "HR"
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
        "name": "Government Operations and Politics",
        "updateDate": "2025-05-20T12:40:56Z"
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
      "date": "2025-03-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1101is.xml"
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
      "title": "SHARE Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-19T11:03:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "SHARE Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-08T02:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "States Handling Access to Reciprocity for Employment Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-08T02:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to authorize the use of Federal Bureau of Investigation criminal history record information for administration of certain licenses.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-08T02:48:20Z"
    }
  ]
}
```
