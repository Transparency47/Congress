# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6588?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6588
- Title: PROVIDE Act
- Congress: 119
- Bill type: HR
- Bill number: 6588
- Origin chamber: House
- Introduced date: 2025-12-10
- Update date: 2026-01-09T09:06:44Z
- Update date including text: 2026-01-09T09:06:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-10: Introduced in House
- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2026-01-05 - Committee: Referred to the Subcommittee on Disability Assistance and Memorial Affairs.
- Latest action: 2025-12-10: Introduced in House

## Actions

- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2026-01-05 - Committee: Referred to the Subcommittee on Disability Assistance and Memorial Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-10",
    "latestAction": {
      "actionDate": "2025-12-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6588",
    "number": "6588",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "P000613",
        "district": "19",
        "firstName": "Jimmy",
        "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
        "lastName": "Panetta",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "PROVIDE Act",
    "type": "HR",
    "updateDate": "2026-01-09T09:06:44Z",
    "updateDateIncludingText": "2026-01-09T09:06:44Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-05",
      "committees": {
        "item": {
          "name": "Disability Assistance and Memorial Affairs Subcommittee",
          "systemCode": "hsvr09"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Disability Assistance and Memorial Affairs.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-10",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-10",
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
          "date": "2025-12-10T15:02:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-01-05T14:13:19Z",
              "name": "Referred to"
            }
          },
          "name": "Disability Assistance and Memorial Affairs Subcommittee",
          "systemCode": "hsvr09"
        }
      },
      "systemCode": "hsvr00",
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
      "bioguideId": "H001077",
      "district": "3",
      "firstName": "Clay",
      "fullName": "Rep. Higgins, Clay [R-LA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Higgins",
      "party": "R",
      "sponsorshipDate": "2025-12-10",
      "state": "LA"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "True",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2025-12-10",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6588ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6588\nIN THE HOUSE OF REPRESENTATIVES\nDecember 10, 2025 Mr. Panetta (for himself, Mr. Higgins of Louisiana , and Mr. Lieu ) introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo direct the Secretary of Veterans Affairs to expedite the processing of claims for disability compensation by veterans affected by major disasters.\n#### 1. Short title\nThis Act may be cited as the Priority Response for Veterans Impacted by Disasters and Emergencies Act or the PROVIDE Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nThe Department of Veterans Affairs sets forth criteria for priority processing of veterans\u2019 disability claims by the Department.\n**(2)**\nSuch criteria include veterans affected by extreme financial hardship, homelessness, terminal illness, and participants in the Department\u2019s Fully Developed Claim program.\n**(3)**\nCurrently there is no process in place to prioritize the disability claims of veterans affected by major disasters such as fires and floods.\n**(4)**\nPriority claims processing for veterans affected by major disasters will significantly help such veterans begin rebuilding their lives.\n#### 3. Priority Claims Processing in the Event of a Major Disaster\n##### (a) In general\nThe Secretary shall prescribe regulations setting forth criteria for priority processing of a claim for compensation under chapter 11 of title 38, United States Code. Individuals whose claim shall be eligible for such priority processing shall include\u2014\n**(1)**\nveterans affected by extreme financial hardship;\n**(2)**\nveterans affected by homelessness;\n**(3)**\nveterans diagnosed with a terminal illness;\n**(4)**\nparticipants in the Department of Veterans Affairs Fully Developed Claim program; and\n**(5)**\nveterans who live in an area for which the President has declared a major disaster under section 401 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5170 ).\n##### (b) Special considerations for claims processing in the event of a major disaster\nThe Secretary shall prescribe additional regulations relating only to subsection (a)(5). Such additional regulations include\u2014\n**(1)**\nestablishing flexible evidence requirements for veterans unable to meet the ordinary evidence requirements for such a claim due to a major disaster; and\n**(2)**\nestablishing a flexible filing deadline for such a claim.\n##### (c) Notice to veterans of eligibility for priority claims processing\nNot later than 60 days after the date of enactment of this Act, the Secretary shall post a permanent notice to veterans on the Department of Veterans Affairs website of the categories of eligibility for priority processing of such claims, including the changes to such categories made pursuant to subsection (a).",
      "versionDate": "2025-12-10",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2026-01-07T23:24:49Z"
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
      "date": "2025-12-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6588ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Veterans Affairs to expedite the processing of claims for disability compensation by veterans affected by major disasters.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-29T14:18:24Z"
    },
    {
      "title": "PROVIDE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-29T14:08:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "PROVIDE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-29T14:08:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Priority Response for Veterans Impacted by Disasters and Emergencies Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-29T14:08:21Z"
    }
  ]
}
```
