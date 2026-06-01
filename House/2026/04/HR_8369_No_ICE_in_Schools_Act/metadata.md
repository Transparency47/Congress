# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8369?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8369
- Title: No ICE in Schools Act
- Congress: 119
- Bill type: HR
- Bill number: 8369
- Origin chamber: House
- Introduced date: 2026-04-20
- Update date: 2026-04-29T15:39:01Z
- Update date including text: 2026-04-29T15:39:01Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-04-20: Introduced in House
- 2026-04-20 - IntroReferral: Introduced in House
- 2026-04-20 - IntroReferral: Introduced in House
- 2026-04-20 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2026-04-20: Introduced in House

## Actions

- 2026-04-20 - IntroReferral: Introduced in House
- 2026-04-20 - IntroReferral: Introduced in House
- 2026-04-20 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-20",
    "latestAction": {
      "actionDate": "2026-04-20",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8369",
    "number": "8369",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "C001127",
        "district": "20",
        "firstName": "Sheila",
        "fullName": "Rep. Cherfilus-McCormick, Sheila [D-FL-20]",
        "lastName": "Cherfilus-McCormick",
        "party": "D",
        "state": "FL"
      }
    ],
    "title": "No ICE in Schools Act",
    "type": "HR",
    "updateDate": "2026-04-29T15:39:01Z",
    "updateDateIncludingText": "2026-04-29T15:39:01Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-20",
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
      "actionDate": "2026-04-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-20",
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
          "date": "2026-04-20T16:05:15Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8369ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8369\nIN THE HOUSE OF REPRESENTATIVES\nApril 20, 2026 Mrs. Cherfilus-McCormick introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo prohibit Federal education funds from being made available to any educational agency or institution that releases any education records or other student information for purposes of immigration enforcement.\n#### 1. Short title\nThis Act may be cited as the Keep Immigration Enforcement Out of Schools Act or the No ICE in Schools Act .\n#### 2. Prohibition of release of education records or other student information for immigration enforcement purposes\nSection 444 of the General Education Provisions Act ( 20 U.S.C. 1232g ) is amended by adding at the end the following:\n(k) Notwithstanding any other provision of this section, no funds shall be made available under any applicable program to any educational agency or institution which, for purposes of immigration enforcement, has a policy or practice of releasing, or providing access to\u2014 (1) any education records; or (2) any other information with respect to a student, including personally identifiable information or directory information, unless there is written consent from the student\u2019s parents specifying the records or information to be released, the reasons for such release, and to whom, and with a copy of the records or information to be released to the student\u2019s parents and the student if desired by the parents. .",
      "versionDate": "2026-04-20",
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
        "updateDate": "2026-04-29T15:39:01Z"
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
      "date": "2026-04-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8369ih.xml"
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
      "title": "No ICE in Schools Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-23T09:38:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "No ICE in Schools Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-23T09:38:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Keep Immigration Enforcement Out of Schools Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-23T09:38:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit Federal education funds from being made available to any educational agency or institution that releases any education records or other student information for purposes of immigration enforcement.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-23T09:33:30Z"
    }
  ]
}
```
