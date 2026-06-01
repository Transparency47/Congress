# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8478?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8478
- Title: RECON Act
- Congress: 119
- Bill type: HR
- Bill number: 8478
- Origin chamber: House
- Introduced date: 2026-04-23
- Update date: 2026-05-18T16:17:32Z
- Update date including text: 2026-05-18T16:17:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-04-23: Introduced in House
- 2026-04-23 - IntroReferral: Introduced in House
- 2026-04-23 - IntroReferral: Introduced in House
- 2026-04-23 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2026-04-23: Introduced in House

## Actions

- 2026-04-23 - IntroReferral: Introduced in House
- 2026-04-23 - IntroReferral: Introduced in House
- 2026-04-23 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-23",
    "latestAction": {
      "actionDate": "2026-04-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8478",
    "number": "8478",
    "originChamber": "House",
    "policyArea": {
      "name": "Social Welfare"
    },
    "sponsors": [
      {
        "bioguideId": "F000477",
        "district": "4",
        "firstName": "Valerie",
        "fullName": "Rep. Foushee, Valerie P. [D-NC-4]",
        "lastName": "Foushee",
        "party": "D",
        "state": "NC"
      }
    ],
    "title": "RECON Act",
    "type": "HR",
    "updateDate": "2026-05-18T16:17:32Z",
    "updateDateIncludingText": "2026-05-18T16:17:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-23",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-04-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-23",
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
          "date": "2026-04-23T13:03:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8478ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8478\nIN THE HOUSE OF REPRESENTATIVES\nApril 23, 2026 Mrs. Foushee introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend titles II and XVI of the Social Security Act to make the reconsideration review process optional.\n#### 1. Short title\nThis Act may be cited as the Respecting Every Claimant\u2019s appeal Options Now Act or the RECON Act .\n#### 2. Elimination of mandatory reconsideration review\n##### (a) Title II amendment\nSection 205(b)(1) of the Social Security Act ( 42 U.S.C. 405(b)(1) ) is amended by adding at the end the following: The Commissioner shall provide opportunity for a hearing in accordance with this subsection with respect to any initial decision or determination under this title upon the request of such applicant or such other individual. The Commissioner may not require reconsideration of the initial decision or determination prior to the hearing. .\n##### (b) Title XVI amendment\nSection 1631(c)(1)(A) of the Social Security Act ( 42 U.S.C. 1383(c)(1)(A) ) is amended by adding at the end the following: The Commissioner shall provide opportunity for a hearing in accordance with this subsection with respect to any initial decision or determination under this title upon the request of such individual. The Commissioner may not require reconsideration of the initial decision or determination prior to the hearing. .\n##### (c) Effective date\nThe amendments made by this section shall apply with respect to any initial decision or determination relating to entitlement to a benefit under title II or XVI of the Social Security Act made on or after the date that is 1 year after the date of enactment of this Act.",
      "versionDate": "2026-04-23",
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
        "name": "Social Welfare",
        "updateDate": "2026-05-18T16:17:31Z"
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
      "date": "2026-04-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8478ih.xml"
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
      "title": "RECON Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-05T13:08:30Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "RECON Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-05T13:08:29Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Respecting Every Claimant\u2019s appeal Options Now Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-05T13:08:29Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend titles II and XVI of the Social Security Act to make the reconsideration review process optional.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-05T13:03:32Z"
    }
  ]
}
```
