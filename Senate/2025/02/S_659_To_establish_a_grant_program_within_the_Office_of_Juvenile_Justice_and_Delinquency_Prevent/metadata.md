# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/659?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/659
- Title: GRACIE Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 659
- Origin chamber: Senate
- Introduced date: 2025-02-20
- Update date: 2025-07-22T13:25:42Z
- Update date including text: 2025-07-22T13:25:42Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-02-20: Introduced in Senate
- 2025-02-20 - IntroReferral: Introduced in Senate
- 2025-02-20 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-02-20: Introduced in Senate

## Actions

- 2025-02-20 - IntroReferral: Introduced in Senate
- 2025-02-20 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-20",
    "latestAction": {
      "actionDate": "2025-02-20",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/659",
    "number": "659",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "B001243",
        "district": "",
        "firstName": "Marsha",
        "fullName": "Sen. Blackburn, Marsha [R-TN]",
        "lastName": "Blackburn",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "GRACIE Act of 2025",
    "type": "S",
    "updateDate": "2025-07-22T13:25:42Z",
    "updateDateIncludingText": "2025-07-22T13:25:42Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-20",
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
      "actionDate": "2025-02-20",
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
          "date": "2025-02-20T17:52:52Z",
          "name": "Referred To"
        }
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
      "bioguideId": "O000174",
      "firstName": "Jon",
      "fullName": "Sen. Ossoff, Jon [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Ossoff",
      "party": "D",
      "sponsorshipDate": "2025-02-24",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s659is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 659\nIN THE SENATE OF THE UNITED STATES\nFebruary 20, 2025 Mrs. Blackburn introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo establish a grant program within the Office of Juvenile Justice and Delinquency Prevention to award grants to States that require the recording of all child welfare interviews with children and adults, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Generate Recordings of All Child protective Interviews Everywhere Act or the GRACIE Act of 2025 .\n#### 2. Child protective service interview recording grants\n##### (a) Definitions\nIn this section:\n**(1) Child welfare interview**\nThe term child welfare interview means a documented interview with all relevant parties, including a child and an adult, conducted by a child protective services agency of a State in order to elicit information regarding concerns of abuse, neglect, or exposure to violence.\n**(2) Director**\nThe term Director means the Director of the Office of Juvenile Justice and Delinquency Prevention of the Department of Justice.\n**(3) Eligible entity**\nThe term eligible entity means a child protective services agency of a State that has in effect a statute, ordinance, policy, or practice that requires\u2014\n**(A)**\nany child welfare interview conducted by a child protective services agency of the State to be recorded through\u2014\n**(i)**\nelectronic audio recording;\n**(ii)**\nbody camera video; or\n**(iii)**\nany other reasonable means of recording; and\n**(B)**\nthe retention and storage of a recording described in subparagraph (A)\u2014\n**(i)**\nfor not less than 5 years; and\n**(ii)**\nin a manner consistent with the protocols established by the State for such recordings, which shall include that\u2014\n**(I)**\na copy of such a recording\u2014\n**(aa)**\nsubject to item (bb), may only be released to those investigating an allegation; and\n**(bb)**\nupon a request by a caregiver or guardian in connection with a judicial proceeding, shall be made available to the caregiver or guardian, unless the court orders otherwise;\n**(II)**\na penalty is imposed for a violation of a limitation described in subclause (I); and\n**(III)**\nthe retention systems of the child protective services agency securely manage the storage and distribution of such a recording with access controls and role-based permission management.\n**(4) State**\nThe term State means\u2014\n**(A)**\neach of the several States;\n**(B)**\nthe District of Columbia;\n**(C)**\nthe Commonwealth of Puerto Rico; and\n**(D)**\nany territory or possession of the United States.\n##### (b) Grants\nThe Director may award a grant to an eligible entity for the purpose of recording and storing all child welfare interviews conducted by the eligible entity.\n##### (c) Application\nAn eligible entity seeking a grant under this section shall submit to the Director an application at such time, in such manner, and containing such information as the Director may require.\n##### (d) Use of funds\nAmounts received under a grant under this section shall be used exclusively for costs directly associated with conducting and retaining for 5 years the recording of all child welfare interviews by a child protective services agency of a State, including initial interviews conducted during a family assessment.\n##### (e) Funding\nThe Director shall carry out this section using amounts otherwise available to the Director.",
      "versionDate": "2025-02-20",
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
            "name": "Child safety and welfare",
            "updateDate": "2025-07-22T13:23:23Z"
          },
          {
            "name": "Digital media",
            "updateDate": "2025-07-22T13:25:36Z"
          },
          {
            "name": "Family services",
            "updateDate": "2025-07-22T13:24:17Z"
          },
          {
            "name": "Social work, volunteer service, charitable organizations",
            "updateDate": "2025-07-22T13:25:42Z"
          },
          {
            "name": "Sound recording",
            "updateDate": "2025-07-22T13:25:31Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2025-07-22T13:24:12Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-03-13T15:14:00Z"
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
      "date": "2025-02-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s659is.xml"
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
      "title": "GRACIE Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-13T01:23:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "GRACIE Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-13T01:23:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Generate Recordings of All Child protective Interviews Everywhere Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-13T01:23:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to establish a grant program within the Office of Juvenile Justice and Delinquency Prevention to award grants to States that require the recording of all child welfare interviews with children and adults, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-13T01:18:46Z"
    }
  ]
}
```
