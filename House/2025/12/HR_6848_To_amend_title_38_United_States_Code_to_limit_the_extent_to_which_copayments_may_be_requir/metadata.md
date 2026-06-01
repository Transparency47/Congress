# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6848?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6848
- Title: Whole Health for Veterans Act
- Congress: 119
- Bill type: HR
- Bill number: 6848
- Origin chamber: House
- Introduced date: 2025-12-18
- Update date: 2026-05-12T18:18:05Z
- Update date including text: 2026-05-12T18:18:05Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-12-18: Introduced in House
- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2026-01-29 - Committee: Referred to the Subcommittee on Health.
- 2026-04-16 - Committee: Forwarded by Subcommittee to Full Committee by Voice Vote.
- 2026-04-16 - Committee: Subcommittee Consideration and Mark-up Session Held
- Latest action: 2025-12-18: Introduced in House

## Actions

- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2026-01-29 - Committee: Referred to the Subcommittee on Health.
- 2026-04-16 - Committee: Forwarded by Subcommittee to Full Committee by Voice Vote.
- 2026-04-16 - Committee: Subcommittee Consideration and Mark-up Session Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-18",
    "latestAction": {
      "actionDate": "2025-12-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6848",
    "number": "6848",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "D000530",
        "district": "17",
        "firstName": "Christopher",
        "fullName": "Rep. Deluzio, Christopher R. [D-PA-17]",
        "lastName": "Deluzio",
        "party": "D",
        "state": "PA"
      }
    ],
    "title": "Whole Health for Veterans Act",
    "type": "HR",
    "updateDate": "2026-05-12T18:18:05Z",
    "updateDateIncludingText": "2026-05-12T18:18:05Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-16",
      "committees": {
        "item": {
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Forwarded by Subcommittee to Full Committee by Voice Vote.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-04-16",
      "committees": {
        "item": {
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Subcommittee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionDate": "2026-01-29",
      "committees": {
        "item": {
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Health.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-18",
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
      "actionDate": "2025-12-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-18",
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
          "date": "2025-12-18T14:03:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2026-04-16T20:32:17Z",
                "name": "Reported by"
              },
              {
                "date": "2026-04-16T13:37:52Z",
                "name": "Markup by"
              },
              {
                "date": "2026-01-29T16:38:32Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "systemCode": "hsvr00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6848ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6848\nIN THE HOUSE OF REPRESENTATIVES\nDecember 18, 2025 Mr. Deluzio introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to limit the extent to which copayments may be required for veterans receiving Whole Health well-being services, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Whole Health for Veterans Act .\n#### 2. Copayments for Whole Health well-being services\n##### (a) Sense of Congress\nCongress encourages further development of the Whole Health program of the Department of Veterans Affairs, which encourages veterans to proactively improve their health and wellness. Under the Department\u2019s current policy, veterans in priority groups (1) through (5) are exempted from making copayments under this program. It is the sense of Congress that the Department should provide all veterans with affordable access to Whole Health well-being services.\n##### (b) Copayments\nSubchapter III of chapter 17 of title 38, United States Code, is amended by adding at the end the following new section:\n1730D. Copayments for Whole Health well-being services (a) In general Notwithstanding subsections (f) and (g) of section 1710 and section 1722A(a) of this title or any other provision of law, the Secretary may not require a veteran to make any copayment for the receipt by that veteran of Whole Health well-being services, except as provided in this section. (b) Monthly copayments authorized (1) In general Except as provided in paragraphs (2) and (3), the Secretary may require a veteran to make a monthly copayment for the Whole Health well-being services received by that veteran for that month. (2) Monthly limit The monthly copayment may not exceed $30. (3) Exemption for certain priority groups The Secretary may not require a veteran within priority group (1), (2), (3), (4), or (5) in the system of enrollment under section 1705(a) of this title to make any copayment for the services received by that veteran. (c) Definition In this section, the term Whole Health well-being services means\u2014 (1) educational and skill-building services that educate, instruct, and empower veterans to understand and implement the principles and practices of Whole Health, such as Whole Health coaching, Whole Health partner sessions, and Whole Health education and skill-building courses; and (2) complementary and integrative health well-being services that promote health, well-being, and self-care independent of treatment of a specific medical condition or diagnosis, such as guided imagery, meditation, Tai Chi/Qigong, and yoga for well-being. .\n##### (c) Clerical amendment\nThe table of sections at the beginning of chapter 17 of such title is amended by inserting after the item relating to section 1730C the following new item:\n1730D. Copayments for Whole Health well-being services. .",
      "versionDate": "2025-12-18",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Health care costs and insurance",
            "updateDate": "2026-05-12T18:12:19Z"
          },
          {
            "name": "Health promotion and preventive care",
            "updateDate": "2026-05-12T18:18:04Z"
          },
          {
            "name": "Veterans' medical care",
            "updateDate": "2026-05-12T18:09:39Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2026-01-20T15:43:25Z"
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
      "date": "2025-12-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6848ih.xml"
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
      "title": "Whole Health for Veterans Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-17T06:23:43Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Whole Health for Veterans Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-17T06:23:41Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, to limit the extent to which copayments may be required for veterans receiving Whole Health well-being services, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-17T06:18:45Z"
    }
  ]
}
```
