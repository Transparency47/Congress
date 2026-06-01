# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/997?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/997
- Title: Enabling the House of Representatives to be responsive to its membership.
- Congress: 119
- Bill type: HRES
- Bill number: 997
- Origin chamber: House
- Introduced date: 2026-01-14
- Update date: 2026-01-16T12:56:43Z
- Update date including text: 2026-01-16T12:56:43Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-01-14: Introduced in House
- 2026-01-14 - IntroReferral: Referred to the Committee on House Administration, and in addition to the Committees on Rules, and Ethics, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-01-14 - IntroReferral: Referred to the Committee on House Administration, and in addition to the Committees on Rules, and Ethics, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-01-14 - IntroReferral: Referred to the Committee on House Administration, and in addition to the Committees on Rules, and Ethics, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-01-14 - IntroReferral: Submitted in House
- 2026-01-14 - IntroReferral: Submitted in House
- Latest action: 2026-01-14: Submitted in House

## Actions

- 2026-01-14 - IntroReferral: Referred to the Committee on House Administration, and in addition to the Committees on Rules, and Ethics, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-01-14 - IntroReferral: Referred to the Committee on House Administration, and in addition to the Committees on Rules, and Ethics, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-01-14 - IntroReferral: Referred to the Committee on House Administration, and in addition to the Committees on Rules, and Ethics, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-01-14 - IntroReferral: Submitted in House
- 2026-01-14 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-14",
    "latestAction": {
      "actionDate": "2026-01-14",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/997",
    "number": "997",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "M000312",
        "district": "2",
        "firstName": "James",
        "fullName": "Rep. McGovern, James P. [D-MA-2]",
        "lastName": "McGovern",
        "party": "D",
        "state": "MA"
      }
    ],
    "title": "Enabling the House of Representatives to be responsive to its membership.",
    "type": "HRES",
    "updateDate": "2026-01-16T12:56:43Z",
    "updateDateIncludingText": "2026-01-16T12:56:43Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-14",
      "committees": {
        "item": {
          "name": "Ethics Committee",
          "systemCode": "hsso00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on House Administration, and in addition to the Committees on Rules, and Ethics, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-14",
      "committees": {
        "item": {
          "name": "Rules Committee",
          "systemCode": "hsru00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on House Administration, and in addition to the Committees on Rules, and Ethics, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-14",
      "committees": {
        "item": {
          "name": "Committee on House Administration",
          "systemCode": "hsha00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on House Administration, and in addition to the Committees on Rules, and Ethics, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2026-01-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
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
          "date": "2026-01-14T15:01:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ethics Committee",
      "systemCode": "hsso00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2026-01-14T15:01:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Rules Committee",
      "systemCode": "hsru00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2026-01-14T15:01:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Committee on House Administration",
      "systemCode": "hsha00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres997ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 997\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 14, 2026 Mr. McGovern submitted the following resolution; which was referred to the Committee on House Administration , and in addition to the Committees on Rules , and Ethics , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nRESOLUTION\nEnabling the House of Representatives to be responsive to its membership.\nI\n#### 101. Code of Official Conduct\nIn rule XXIII of the Rules of the House of Representatives, strike clause 2 and insert the following:\n2. A Member, Delegate, Resident Commissioner, officer, or employee of the House shall adhere to the spirit and the letter of the Rules of the House and to the rules of duly constituted committees thereof. .\n#### 102. Suspension of the rules\nIn rule XV of the Rules of the House of Representatives, strike clause 1 and insert the following:\n1. (a) A rule may not be suspended except by a vote of two-thirds of the Members voting, a quorum being present. The Speaker may not entertain a motion that the House suspend the rules except on Mondays, Tuesdays, and Wednesdays and during the last six days of a session of Congress. (b) Pending a motion that the House suspend the rules, the Speaker may entertain one motion that the House adjourn but may not entertain any other motion until the vote is taken on the suspension. (c) A motion that the House suspend the rules is debatable for 40 minutes, one-half in favor of the motion and one-half in opposition thereto. .\nII\n#### 201. Placement of U.S. time zone clocks in House chamber\n##### (a) Responsibilities of Clerk\nThe Clerk of the House of Representatives shall place clocks displaying each United States time zone in real time in the House Chamber in clear view of the Members.\n##### (b) Regulations\nThe Clerk shall carry out this resolution in accordance with regulations promulgated by the Committee on House Administration.",
      "versionDate": "2026-01-14",
      "versionType": "IH"
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
        "name": "Congress",
        "updateDate": "2026-01-16T12:56:43Z"
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
      "date": "2026-01-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres997ih.xml"
        }
      ],
      "type": "IH"
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
      "title": "Enabling the House of Representatives to be responsive to its membership.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-15T10:48:21Z"
    },
    {
      "title": "Enabling the House of Representatives to be responsive to its membership.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-15T09:06:34Z"
    }
  ]
}
```
