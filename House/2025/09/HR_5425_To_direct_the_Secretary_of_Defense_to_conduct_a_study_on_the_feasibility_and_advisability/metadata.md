# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5425?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5425
- Title: Servicemember Retention and Education Advancement Act
- Congress: 119
- Bill type: HR
- Bill number: 5425
- Origin chamber: House
- Introduced date: 2025-09-17
- Update date: 2025-09-30T23:25:03Z
- Update date including text: 2025-09-30T23:25:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-09-17: Introduced in House
- 2025-09-17 - IntroReferral: Introduced in House
- 2025-09-17 - IntroReferral: Introduced in House
- 2025-09-17 - IntroReferral: Referred to the House Committee on Armed Services.
- Latest action: 2025-09-17: Introduced in House

## Actions

- 2025-09-17 - IntroReferral: Introduced in House
- 2025-09-17 - IntroReferral: Introduced in House
- 2025-09-17 - IntroReferral: Referred to the House Committee on Armed Services.

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
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5425",
    "number": "5425",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "C001123",
        "district": "31",
        "firstName": "Gilbert",
        "fullName": "Rep. Cisneros, Gilbert Ray [D-CA-31]",
        "lastName": "Cisneros",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Servicemember Retention and Education Advancement Act",
    "type": "HR",
    "updateDate": "2025-09-30T23:25:03Z",
    "updateDateIncludingText": "2025-09-30T23:25:03Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-17",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "hsas00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Armed Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-17",
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
          "date": "2025-09-17T14:04:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Armed Services Committee",
      "systemCode": "hsas00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5425ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5425\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 17, 2025 Mr. Cisneros introduced the following bill; which was referred to the Committee on Armed Services\nA BILL\nTo direct the Secretary of Defense to conduct a study on the feasibility and advisability of establishing a uniform policy to provide tuition assistance after on year of active duty service.\n#### 1. Short title\nThis Act may be cited as the Servicemember Retention and Education Advancement Act .\n#### 2. Study on policy to provide tuition assistance to members of the Armed Forces after one year of active duty service\n##### (a) Study\nThe Secretary of Defense shall conduct a study on the feasibility and advisability of establishing a uniform policy to provide tuition assistance to all members of the Armed Forces who complete one year of service on active duty.\n##### (b) Report\nNot later than one year after the date of the enactment of this Act, the Secretary shall submit to the congressional defense committees (as defined in section 101(a) of title 10, United States Code) a report containing the results of the study required by subsection (a), including an identification of any barriers to implementing the policy described in such subsection.",
      "versionDate": "2025-09-17",
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
        "updateDate": "2025-09-30T23:25:03Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5425ih.xml"
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
      "title": "Servicemember Retention and Education Advancement Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-30T04:38:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Servicemember Retention and Education Advancement Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-30T04:38:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Defense to conduct a study on the feasibility and advisability of establishing a uniform policy to provide tuition assistance after on year of active duty service.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-30T04:33:12Z"
    }
  ]
}
```
