# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8190?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8190
- Title: Social Security Customer Service Act
- Congress: 119
- Bill type: HR
- Bill number: 8190
- Origin chamber: House
- Introduced date: 2026-04-02
- Update date: 2026-04-13T14:40:14Z
- Update date including text: 2026-04-13T14:40:14Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-04-02: Introduced in House
- 2026-04-02 - IntroReferral: Introduced in House
- 2026-04-02 - IntroReferral: Introduced in House
- 2026-04-02 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2026-04-02: Introduced in House

## Actions

- 2026-04-02 - IntroReferral: Introduced in House
- 2026-04-02 - IntroReferral: Introduced in House
- 2026-04-02 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-02",
    "latestAction": {
      "actionDate": "2026-04-02",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8190",
    "number": "8190",
    "originChamber": "House",
    "policyArea": {
      "name": "Social Welfare"
    },
    "sponsors": [
      {
        "bioguideId": "S001215",
        "district": "11",
        "firstName": "Haley",
        "fullName": "Rep. Stevens, Haley M. [D-MI-11]",
        "lastName": "Stevens",
        "party": "D",
        "state": "MI"
      }
    ],
    "title": "Social Security Customer Service Act",
    "type": "HR",
    "updateDate": "2026-04-13T14:40:14Z",
    "updateDateIncludingText": "2026-04-13T14:40:14Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-02",
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
      "actionDate": "2026-04-02",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-02",
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
          "date": "2026-04-02T12:30:25Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8190ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8190\nIN THE HOUSE OF REPRESENTATIVES\nApril 2, 2026 Ms. Stevens introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo require the Commissioner of Social Security to ensure that the Social Security Administration has a certain number of staff.\n#### 1. Short title\nThis Act may be cited as the Social Security Customer Service Act .\n#### 2. SSA staffing requirement\n##### (a) Staffing requirement\nNot later than 6 months after the date of enactment of this Act, the Commissioner of Social Security shall take such actions as are necessary to ensure that the number of full-time employees employed by the Social Security Administration is greater than or equal to the number of full-time employees employed by the Administration on January 19, 2025.\n##### (b) Prioritization of hiring at the Social Security Administration\nThe Commissioner of Social Security shall ensure that 75 percent of the individuals hired to reach the number of full-time employees outlined in section (a) are employees\u2014\n**(1)**\nin a position at a social security field office;\n**(2)**\nin a center responding to telephone inquiries from social security beneficiaries;\n**(3)**\nin a position at a program service center;\n**(4)**\nin a position processing or facilitating payments to beneficiaries;\n**(5)**\nin a position at a regional field office; or\n**(6)**\nin a position resolving or adjudicating disability benefits claims or disputes.\n##### (c) Nature of remaining hiring at the Social Security Administration\nThe Commissioner of Social Security shall ensure that 25 percent of the hires made to reach the number of full-time employees outlined in section (a) are employees providing managerial or administrative support to the full-time employees outlined in section (b).",
      "versionDate": "2026-04-02",
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
        "updateDate": "2026-04-13T14:40:13Z"
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
      "date": "2026-04-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8190ih.xml"
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
      "title": "Social Security Customer Service Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-08T12:23:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Social Security Customer Service Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-08T12:23:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Commissioner of Social Security to ensure that the Social Security Administration has a certain number of staff.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-08T12:18:25Z"
    }
  ]
}
```
