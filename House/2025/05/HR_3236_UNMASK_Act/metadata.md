# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3236?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/3236
- Title: UNMASK Act
- Congress: 119
- Bill type: HR
- Bill number: 3236
- Origin chamber: House
- Introduced date: 2025-05-07
- Update date: 2025-06-11T14:47:24Z
- Update date including text: 2025-06-11T14:47:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-05-07: Introduced in House
- 2025-05-07 - IntroReferral: Introduced in House
- 2025-05-07 - IntroReferral: Introduced in House
- 2025-05-07 - IntroReferral: Referred to the House Committee on Armed Services.
- Latest action: 2025-05-07: Introduced in House

## Actions

- 2025-05-07 - IntroReferral: Introduced in House
- 2025-05-07 - IntroReferral: Introduced in House
- 2025-05-07 - IntroReferral: Referred to the House Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-07",
    "latestAction": {
      "actionDate": "2025-05-07",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/3236",
    "number": "3236",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "G000594",
        "district": "23",
        "firstName": "Tony",
        "fullName": "Rep. Gonzales, Tony [R-TX-23]",
        "lastName": "Gonzales",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "UNMASK Act",
    "type": "HR",
    "updateDate": "2025-06-11T14:47:24Z",
    "updateDateIncludingText": "2025-06-11T14:47:24Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-07",
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
      "actionDate": "2025-05-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-07",
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
          "date": "2025-05-07T14:05:30Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3236ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3236\nIN THE HOUSE OF REPRESENTATIVES\nMay 7, 2025 Mr. Tony Gonzales of Texas introduced the following bill; which was referred to the Committee on Armed Services\nA BILL\nTo prohibit the Federal Government from establishing, implementing, or enforcing any Federal requirement for members of the Armed Forces to wear a face mask while in uniform when not directly related to their duties.\n#### 1. Short title\nThis Act may be cited as the Undoing and Nullifying Mandates so our Armed Services Keep Succeeding Act or the UNMASK Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nOn May 5, 2023, the World Health Organization officially declared an end to the global Public Health Emergency for COVID\u201319, which led to the Centers for Disease Control and Prevention and other public health agencies shifting guidance away from universal mask usage.\n**(2)**\nWith the widespread availability of vaccines and other therapeutic treatments, and the reduction in severe outcomes from COVID\u201319, masks are no longer justified for members of the Armed Forces.\n**(3)**\nMaintaining face coverings in the Department of Defense absent a declared national emergency risks undermining the professionalism and integrity of the uniform, adversely impacts servicemember morale, and detracts from the core mission of the Armed Forces: to fight and win the Nation\u2019s wars.\n#### 3. Prohibition on establishment of requirements for members of the Armed Forces to wear masks\n##### (a) Prohibition\nSubject to subsection (b) and notwithstanding any other provision of law, no officer or employee of the Federal Government may establish, implement, or enforce any requirement for members of the Armed Forces to wear a face mask while serving on active duty.\n##### (b) Exception\nThe Secretary of Defense may require members of the Armed Forces whose duties include activities that traditionally involve wearing personal protective equipment or other face masks for operational or safety reasons to wear such equipment, including an appropriate face mask, while performing such duties.",
      "versionDate": "2025-05-07",
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
        "updateDate": "2025-06-11T14:47:24Z"
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
      "date": "2025-05-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3236ih.xml"
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
      "title": "To prohibit the Federal Government from establishing, implementing, or enforcing any Federal requirement for members of the Armed Forces to wear a face mask while in uniform when not directly related to their duties.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-15T03:59:26Z"
    },
    {
      "title": "UNMASK Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-15T03:39:37Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "UNMASK Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-15T03:38:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Undoing and Nullifying Mandates so our Armed Services Keep Succeeding Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-15T03:38:24Z"
    }
  ]
}
```
